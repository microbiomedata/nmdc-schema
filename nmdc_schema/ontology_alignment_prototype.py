"""Helpers for comparing semantic alignment hits against lexical strength.

This module is intentionally lightweight so it can run in the base nmdc-schema
environment while exposing optional hooks for oaklib, schema-automator, and
linkml-store when those packages are available.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import requests
from linkml_runtime.linkml_model.meta import PermissibleValue
from linkml_runtime.utils.schemaview import SchemaView


SEMANTIC_JUSTIFICATION = "semapv:SemanticSimilarityThresholdMatching"
OLS4_SEARCH_URL = "https://www.ebi.ac.uk/ols4/api/search"
SCALAR_TYPES = {
    "string",
    "integer",
    "float",
    "double",
    "decimal",
    "boolean",
    "date",
    "datetime",
    "time",
    "uri",
    "uriorcurie",
    "ncname",
    "objectidentifier",
}
CONTROLLED_TERM_RANGES = {
    "OntologyClass",
    "ControlledTermValue",
    "ControlledIdentifiedTermValue",
}


@dataclass(frozen=True)
class SchemaElementRecord:
    """Minimal schema-side context for alignment review."""

    subject_id: str
    subject_label: str
    subject_category: str
    subject_description: str
    element_name: str
    range_name: str
    range_kind: str
    owners: tuple[str, ...]
    owner_mapping_sources: tuple[str, ...]
    range_mapping_sources: tuple[str, ...]
    existing_mappings: tuple[str, ...]
    existing_mapping_sources: tuple[str, ...]
    expected_alignment_type: str


@dataclass(frozen=True)
class LexicalProfile:
    """Simple local lexical similarity features."""

    exact_label_match: bool
    normalized_label_match: bool
    token_jaccard: float
    sequence_ratio: float
    containment: float
    lexical_score: float


@dataclass(frozen=True)
class OlsEntityMetadata:
    """Minimal OLS-side metadata used for structural review."""

    object_id: str
    object_source: str
    object_kind: str
    label: str = ""
    iri: str = ""
    description: str = ""
    is_obsolete: bool = False
    synonyms: tuple[str, ...] = tuple()


def normalize_text(text: str) -> str:
    """Normalize text for rough lexical comparison."""
    text = text or ""
    text = text.replace("_", " ")
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def token_set(text: str) -> set[str]:
    """Convert text to a normalized token set."""
    normalized = normalize_text(text)
    return set(normalized.split()) if normalized else set()


def mapping_source(curie: str) -> str:
    """Extract the prefix/source from a CURIE-like value."""
    if not curie:
        return ""
    if ":" in curie:
        return curie.split(":", 1)[0].upper()
    return curie.upper()


def lexical_profile(subject_label: str, object_label: str) -> LexicalProfile:
    """Compute local lexical features for a candidate mapping."""
    raw_subject = (subject_label or "").strip()
    raw_object = (object_label or "").strip()
    norm_subject = normalize_text(raw_subject)
    norm_object = normalize_text(raw_object)

    subject_tokens = token_set(raw_subject)
    object_tokens = token_set(raw_object)
    if subject_tokens or object_tokens:
        token_jaccard = len(subject_tokens & object_tokens) / len(subject_tokens | object_tokens)
    else:
        token_jaccard = 0.0

    sequence_ratio = SequenceMatcher(None, norm_subject, norm_object).ratio() if norm_subject or norm_object else 0.0

    containment = 0.0
    if subject_tokens and object_tokens:
        containment = max(
            len(subject_tokens & object_tokens) / len(subject_tokens),
            len(subject_tokens & object_tokens) / len(object_tokens),
        )

    exact_label_match = raw_subject == raw_object and bool(raw_subject)
    normalized_label_match = norm_subject == norm_object and bool(norm_subject)
    lexical_score = max(
        1.0 if exact_label_match else 0.0,
        0.98 if normalized_label_match else 0.0,
        token_jaccard,
        sequence_ratio,
        containment,
    )
    return LexicalProfile(
        exact_label_match=exact_label_match,
        normalized_label_match=normalized_label_match,
        token_jaccard=token_jaccard,
        sequence_ratio=sequence_ratio,
        containment=containment,
        lexical_score=lexical_score,
    )


def _sorted_mappings(mappings: list[str] | None) -> tuple[str, ...]:
    values = mappings or []
    return tuple(sorted({value for value in values if value}))


def _sources_from_mappings(mappings: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(sorted({mapping_source(value) for value in mappings if mapping_source(value)}))


def _range_kind(sv: SchemaView, range_name: str) -> str:
    if not range_name:
        return "none"
    lowered = range_name.lower()
    if lowered in SCALAR_TYPES:
        return "scalar"
    if range_name in CONTROLLED_TERM_RANGES:
        return "class_filler"
    if range_name in sv.all_enums():
        return "enum"
    if range_name in sv.all_classes():
        return "class"
    if range_name in sv.all_types():
        return "scalar"
    return "unknown"


def _expected_alignment_type(subject_category: str, range_kind: str) -> str:
    if subject_category == "slot":
        if range_kind in {"scalar"}:
            return "property_like"
        if range_kind in {"enum", "class", "class_filler"}:
            return "class_filler"
        return "ambiguous"
    if subject_category in {"class", "permissible_value", "enum"}:
        return "class_like"
    return "ambiguous"


def _class_record(sv: SchemaView, class_name: str) -> SchemaElementRecord:
    class_def = sv.get_class(class_name)
    mappings = []
    for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
        mappings.extend(getattr(class_def, field_name, []) or [])
    existing_mappings = _sorted_mappings(mappings)
    return SchemaElementRecord(
        subject_id=f"nmdc:{class_name}",
        subject_label=class_def.title or class_name,
        subject_category="class",
        subject_description=class_def.description or "",
        element_name=class_name,
        range_name="",
        range_kind="none",
        owners=tuple(),
        owner_mapping_sources=tuple(),
        range_mapping_sources=tuple(),
        existing_mappings=existing_mappings,
        existing_mapping_sources=_sources_from_mappings(existing_mappings),
        expected_alignment_type="class_like",
    )


def _slot_record(sv: SchemaView, slot_name: str) -> SchemaElementRecord:
    slot_def = sv.induced_slot(slot_name)
    mappings = []
    for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
        mappings.extend(getattr(slot_def, field_name, []) or [])
    owners = tuple(sorted(slot_def.domain_of or []))
    owner_mapping_sources: set[str] = set()
    for owner_name in owners:
        owner_def = sv.get_class(owner_name)
        for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
            owner_mapping_sources.update(mapping_source(value) for value in (getattr(owner_def, field_name, []) or []))
    range_name = slot_def.range or ""
    range_kind = _range_kind(sv, range_name)
    range_mapping_sources: set[str] = set()
    if range_kind == "enum":
        enum_def = sv.get_enum(range_name)
        for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
            range_mapping_sources.update(mapping_source(value) for value in (getattr(enum_def, field_name, []) or []))
    elif range_kind == "class":
        class_def = sv.get_class(range_name)
        for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
            range_mapping_sources.update(mapping_source(value) for value in (getattr(class_def, field_name, []) or []))
    existing_mappings = _sorted_mappings(mappings)
    return SchemaElementRecord(
        subject_id=f"nmdc:{slot_name}",
        subject_label=slot_def.title or slot_name,
        subject_category="slot",
        subject_description=slot_def.description or "",
        element_name=slot_name,
        range_name=range_name,
        range_kind=range_kind,
        owners=owners,
        owner_mapping_sources=tuple(sorted(filter(None, owner_mapping_sources))),
        range_mapping_sources=tuple(sorted(filter(None, range_mapping_sources))),
        existing_mappings=existing_mappings,
        existing_mapping_sources=_sources_from_mappings(existing_mappings),
        expected_alignment_type=_expected_alignment_type("slot", range_kind),
    )


def _enum_record(sv: SchemaView, enum_name: str) -> SchemaElementRecord:
    enum_def = sv.get_enum(enum_name)
    mappings = []
    for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
        mappings.extend(getattr(enum_def, field_name, []) or [])
    existing_mappings = _sorted_mappings(mappings)
    return SchemaElementRecord(
        subject_id=f"nmdc:{enum_name}",
        subject_label=enum_def.title or enum_name,
        subject_category="enum",
        subject_description=enum_def.description or "",
        element_name=enum_name,
        range_name="",
        range_kind="none",
        owners=tuple(),
        owner_mapping_sources=tuple(),
        range_mapping_sources=tuple(),
        existing_mappings=existing_mappings,
        existing_mapping_sources=_sources_from_mappings(existing_mappings),
        expected_alignment_type="class_like",
    )


def _pv_record(enum_name: str, pv_name: str, pv: PermissibleValue) -> SchemaElementRecord:
    mappings = []
    for field_name in ("exact_mappings", "close_mappings", "related_mappings", "narrow_mappings", "broad_mappings"):
        mappings.extend(getattr(pv, field_name, []) or [])
    if pv.meaning:
        mappings.append(str(pv.meaning))
    existing_mappings = _sorted_mappings(mappings)
    owner_mapping_sources = tuple(sorted({mapping_source(value) for value in existing_mappings if mapping_source(value)}))
    return SchemaElementRecord(
        subject_id=f"nmdc:{enum_name}#{pv_name}",
        subject_label=pv.text or pv_name,
        subject_category="permissible_value",
        subject_description=pv.description or "",
        element_name=pv_name,
        range_name="",
        range_kind="none",
        owners=(enum_name,),
        owner_mapping_sources=owner_mapping_sources,
        range_mapping_sources=tuple(),
        existing_mappings=existing_mappings,
        existing_mapping_sources=_sources_from_mappings(existing_mappings),
        expected_alignment_type="class_like",
    )


def build_schema_index(schema_path: str | Path) -> dict[str, SchemaElementRecord]:
    """Index nmdc schema elements by subject_id."""
    sv = SchemaView(str(schema_path))
    records: dict[str, SchemaElementRecord] = {}

    for class_name in sv.all_classes().keys():
        record = _class_record(sv, class_name)
        records[record.subject_id] = record

    for slot_name in sv.all_slots().keys():
        record = _slot_record(sv, slot_name)
        records[record.subject_id] = record

    for enum_name, enum_def in sv.all_enums().items():
        record = _enum_record(sv, enum_name)
        records[record.subject_id] = record
        for pv_name, pv in (enum_def.permissible_values or {}).items():
            pv_record = _pv_record(enum_name, pv_name, pv)
            records[pv_record.subject_id] = pv_record

    return records


def read_alignment_rows(path: str | Path) -> list[dict[str, str]]:
    """Read a TSV of alignment rows."""
    with Path(path).open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def classify_alignment(
    semantic_confidence: float,
    lexical_score_value: float,
    semantic_threshold: float,
    lexical_threshold: float,
) -> str:
    """Classify the semantic/lexical relationship for one hit."""
    if semantic_confidence >= semantic_threshold and lexical_score_value < lexical_threshold:
        return "strong_semantic_weak_lexical"
    if semantic_confidence >= semantic_threshold and lexical_score_value >= lexical_threshold:
        return "strong_semantic_strong_lexical"
    if semantic_confidence < semantic_threshold and lexical_score_value >= lexical_threshold:
        return "weak_semantic_strong_lexical"
    return "weak_semantic_weak_lexical"


def parse_csv_option(value: str | None) -> set[str]:
    """Parse a comma-separated CLI option into an uppercase set."""
    if not value:
        return set()
    return {item.strip().upper() for item in value.split(",") if item.strip()}


def ols_entity_metadata(
    object_id: str,
    object_source: str,
    cache: dict[tuple[str, str], OlsEntityMetadata],
) -> OlsEntityMetadata:
    """Resolve minimal OLS metadata for a hit using exact CURIE search."""
    cache_key = (object_id, object_source)
    if cache_key in cache:
        return cache[cache_key]

    params = {"q": object_id, "queryFields": "obo_id", "exact": "true"}
    metadata = OlsEntityMetadata(
        object_id=object_id,
        object_source=object_source,
        object_kind="class",
        label="",
        iri="",
        description="",
    )
    try:
        response = requests.get(OLS4_SEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        docs = response.json().get("response", {}).get("docs", [])
        for doc in docs:
            prefix = (doc.get("ontology_prefix") or "").upper()
            if prefix == object_source.upper() and doc.get("obo_id") == object_id:
                metadata = OlsEntityMetadata(
                    object_id=object_id,
                    object_source=object_source,
                    object_kind=(doc.get("type") or "class").lower(),
                    label=extract_first(doc.get("label")),
                    iri=doc.get("iri") or "",
                    description=" ".join(doc.get("description") or []),
                    is_obsolete=bool(doc.get("is_obsolete") or doc.get("isObsolete") or False),
                    synonyms=tuple(doc.get("synonym") or doc.get("synonyms") or []),
                )
                break
    except requests.RequestException:
        pass

    cache[cache_key] = metadata
    return metadata


def match_type(subject_category: str, object_kind: str) -> str:
    """Derive a coarse match type."""
    normalized_object_kind = object_kind or "class"
    if subject_category == "class":
        return f"class->{normalized_object_kind}"
    if subject_category == "slot":
        return f"slot->{normalized_object_kind}"
    if subject_category == "permissible_value":
        return f"pv->{normalized_object_kind}"
    if subject_category == "enum":
        return f"enum->{normalized_object_kind}"
    return f"{subject_category}->{normalized_object_kind}"


def structural_support(record: SchemaElementRecord | None, metadata: OlsEntityMetadata) -> tuple[bool, str]:
    """Estimate whether a candidate is structurally plausible from the NMDC side."""
    if record is None:
        return (False, "missing_schema_record")

    if record.subject_category == "class":
        return (metadata.object_kind == "class", "class_to_class" if metadata.object_kind == "class" else "class_to_nonclass")

    if record.subject_category == "permissible_value":
        source_overlap = metadata.object_source in set(record.existing_mapping_sources) | set(record.owner_mapping_sources)
        if metadata.object_kind != "class":
            return (False, "pv_to_nonclass")
        return (source_overlap, "pv_source_overlap" if source_overlap else "pv_source_mismatch")

    if record.subject_category == "enum":
        source_overlap = metadata.object_source in set(record.existing_mapping_sources)
        if metadata.object_kind != "class":
            return (False, "enum_to_nonclass")
        return (source_overlap, "enum_source_overlap" if source_overlap else "enum_source_mismatch")

    if record.subject_category == "slot":
        source_overlap = metadata.object_source in set(record.existing_mapping_sources) | set(record.owner_mapping_sources) | set(
            record.range_mapping_sources
        )
        if metadata.object_kind == "property":
            if record.expected_alignment_type == "property_like":
                return (True, "slot_property_scalar_fit")
            return (source_overlap, "slot_property_source_overlap" if source_overlap else "slot_property_mismatch")
        if metadata.object_kind == "class":
            if record.expected_alignment_type == "class_filler":
                return (True, "slot_class_range_fit")
            if source_overlap:
                return (True, "slot_class_source_overlap")
            return (False, "slot_class_scalar_mismatch")
        return (False, "slot_unknown_object_kind")

    return (False, "unsupported_subject_category")


def enrich_alignment_rows(
    rows: list[dict[str, str]],
    schema_index: dict[str, SchemaElementRecord],
    semantic_threshold: float,
    lexical_threshold: float,
    allowed_ontologies: set[str] | None = None,
    excluded_ontologies: set[str] | None = None,
    allowed_subject_categories: set[str] | None = None,
    resolve_ols_metadata: bool = False,
) -> list[dict[str, Any]]:
    """Join semantic hits to schema metadata, lexical features, and structural support."""
    enriched: list[dict[str, Any]] = []
    metadata_cache: dict[tuple[str, str], OlsEntityMetadata] = {}
    allowed_ontologies = allowed_ontologies or set()
    excluded_ontologies = excluded_ontologies or set()
    allowed_subject_categories = {item.lower() for item in (allowed_subject_categories or set())}

    for row in rows:
        record = schema_index.get(row["subject_id"])
        source = (row.get("object_source") or "").upper()
        subject_category = (row.get("subject_category") or "").lower()

        if allowed_ontologies and source not in allowed_ontologies:
            continue
        if excluded_ontologies and source in excluded_ontologies:
            continue
        if allowed_subject_categories and subject_category not in allowed_subject_categories:
            continue

        profile = lexical_profile(row.get("subject_label", ""), row.get("object_label", ""))
        semantic_confidence = float(row.get("confidence", 0.0) or 0.0)
        classification = classify_alignment(
            semantic_confidence=semantic_confidence,
            lexical_score_value=profile.lexical_score,
            semantic_threshold=semantic_threshold,
            lexical_threshold=lexical_threshold,
        )
        metadata = (
            ols_entity_metadata(row.get("object_id", ""), source, metadata_cache)
            if resolve_ols_metadata
            else OlsEntityMetadata(
                object_id=row.get("object_id", ""),
                object_source=source,
                object_kind="class",
                label=row.get("object_label", ""),
                iri="",
                description="",
            )
        )
        structural_fit, structural_reason = structural_support(record, metadata)
        match_type_value = match_type(subject_category, metadata.object_kind)
        enriched.append(
            {
                **row,
                "semantic_confidence": semantic_confidence,
                "lexical_score": round(profile.lexical_score, 4),
                "token_jaccard": round(profile.token_jaccard, 4),
                "sequence_ratio": round(profile.sequence_ratio, 4),
                "containment": round(profile.containment, 4),
                "exact_label_match": profile.exact_label_match,
                "normalized_label_match": profile.normalized_label_match,
                "semantic_vs_lexical": classification,
                "match_type": match_type_value,
                "object_kind": metadata.object_kind,
                "object_label_resolved": metadata.label or row.get("object_label", ""),
                "object_iri": metadata.iri,
                "object_description": metadata.description[:200],
                "object_is_obsolete": metadata.is_obsolete,
                "object_synonyms": "|".join(metadata.synonyms[:10]),
                "schema_range": record.range_name if record else "",
                "schema_range_kind": record.range_kind if record else "",
                "schema_expected_alignment_type": record.expected_alignment_type if record else "",
                "schema_owners": "|".join(record.owners) if record else "",
                "existing_mappings": "|".join(record.existing_mappings) if record else "",
                "existing_mapping_sources": "|".join(record.existing_mapping_sources) if record else "",
                "owner_mapping_sources": "|".join(record.owner_mapping_sources) if record else "",
                "range_mapping_sources": "|".join(record.range_mapping_sources) if record else "",
                "structural_fit": structural_fit,
                "structural_reason": structural_reason,
                "structural_bucket": (
                    "strong_semantic_weak_lexical_structurally_supported"
                    if classification == "strong_semantic_weak_lexical" and structural_fit
                    else classification
                ),
            }
        )
    return enriched


def summarize_alignment_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a compact summary for reporting."""
    summary: dict[str, Any] = {
        "total_rows": len(rows),
        "by_semantic_vs_lexical": {},
        "by_structural_bucket": {},
        "by_match_type": {},
        "by_object_kind": {},
        "by_object_source": {},
        "strong_semantic_weak_lexical_by_source": {},
        "structurally_supported_semantic_weak_lexical_by_source": {},
    }
    for row in rows:
        classification = row["semantic_vs_lexical"]
        structural_bucket = row["structural_bucket"]
        source = row.get("object_source", "")
        match_type_value = row.get("match_type", "")
        object_kind = row.get("object_kind", "")
        summary["by_semantic_vs_lexical"][classification] = summary["by_semantic_vs_lexical"].get(classification, 0) + 1
        summary["by_structural_bucket"][structural_bucket] = summary["by_structural_bucket"].get(structural_bucket, 0) + 1
        summary["by_match_type"][match_type_value] = summary["by_match_type"].get(match_type_value, 0) + 1
        summary["by_object_kind"][object_kind] = summary["by_object_kind"].get(object_kind, 0) + 1
        summary["by_object_source"][source] = summary["by_object_source"].get(source, 0) + 1
        if classification == "strong_semantic_weak_lexical":
            bucket = summary["strong_semantic_weak_lexical_by_source"]
            bucket[source] = bucket.get(source, 0) + 1
        if structural_bucket == "strong_semantic_weak_lexical_structurally_supported":
            bucket = summary["structurally_supported_semantic_weak_lexical_by_source"]
            bucket[source] = bucket.get(source, 0) + 1
    return summary


def shortlist_alignment_rows(
    rows: list[dict[str, Any]],
    top_n: int = 50,
    preferred_buckets: tuple[str, ...] = ("strong_semantic_weak_lexical_structurally_supported",),
    max_per_subject: int = 3,
) -> list[dict[str, Any]]:
    """Return a small review-focused shortlist from enriched rows."""
    preferred = {bucket: idx for idx, bucket in enumerate(preferred_buckets)}

    def sort_key(row: dict[str, Any]) -> tuple[Any, ...]:
        bucket = row.get("structural_bucket", "")
        preferred_rank = preferred.get(bucket, len(preferred) + 1)
        semantic_confidence = float(row.get("semantic_confidence", 0.0) or 0.0)
        lexical_score_value = float(row.get("lexical_score", 0.0) or 0.0)
        return (
            preferred_rank,
            -semantic_confidence,
            lexical_score_value,
            row.get("subject_id", ""),
            row.get("object_id", ""),
        )

    selected: list[dict[str, Any]] = []
    counts_by_subject: dict[str, int] = {}
    for row in sorted(rows, key=sort_key):
        subject_id = row.get("subject_id", "")
        if counts_by_subject.get(subject_id, 0) >= max_per_subject:
            continue
        selected.append(row)
        counts_by_subject[subject_id] = counts_by_subject.get(subject_id, 0) + 1
        if len(selected) >= top_n:
            break
    return selected


def extract_first(value: Any) -> str:
    """Extract a displayable first string value."""
    if isinstance(value, list):
        return str(value[0]) if value else ""
    return str(value or "")


def review_flags(row: dict[str, Any]) -> tuple[str, ...]:
    """Derive concise review flags for a shortlisted row."""
    flags: list[str] = []
    if str(row.get("object_is_obsolete", "")).lower() in {"true", "1"}:
        flags.append("obsolete_term")
    if row.get("structural_bucket") == "strong_semantic_weak_lexical_structurally_supported":
        flags.append("semantic_rescue")
    if row.get("match_type") == "slot->class":
        flags.append("slot_to_class")
    if row.get("match_type") == "pv->class":
        flags.append("pv_to_class")
    if row.get("schema_expected_alignment_type") == "property_like":
        flags.append("property_like_slot")
    if float(row.get("lexical_score", 0.0) or 0.0) < 0.2:
        flags.append("very_weak_lexical")
    if row.get("object_description"):
        flags.append("has_definition")
    if row.get("object_synonyms"):
        flags.append("has_synonyms")
    return tuple(flags)


def enrich_review_rows(
    rows: list[dict[str, Any]],
    resolve_ols_metadata: bool = True,
) -> list[dict[str, Any]]:
    """Enrich a small review shortlist with more term metadata."""
    if not resolve_ols_metadata:
        return rows

    metadata_cache: dict[tuple[str, str], OlsEntityMetadata] = {}
    enriched_rows: list[dict[str, Any]] = []
    for rank, row in enumerate(rows, start=1):
        source = (row.get("object_source") or "").upper()
        metadata = ols_entity_metadata(row.get("object_id", ""), source, metadata_cache)
        updated = {
            **row,
            "review_rank": rank,
            "object_kind": metadata.object_kind,
            "object_label_resolved": metadata.label or row.get("object_label", ""),
            "object_iri": metadata.iri,
            "object_description": metadata.description[:500],
            "object_is_obsolete": metadata.is_obsolete,
            "object_synonyms": "|".join(metadata.synonyms[:20]),
            "review_flags": "",
        }
        updated["review_flags"] = "|".join(review_flags(updated))
        enriched_rows.append(updated)
    return enriched_rows


def summarize_review_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize a review shortlist."""
    summary: dict[str, Any] = {
        "total_rows": len(rows),
        "by_structural_bucket": {},
        "by_object_source": {},
        "by_match_type": {},
        "by_review_flag": {},
    }
    for row in rows:
        bucket = row.get("structural_bucket", "")
        source = row.get("object_source", "")
        match_type_value = row.get("match_type", "")
        summary["by_structural_bucket"][bucket] = summary["by_structural_bucket"].get(bucket, 0) + 1
        summary["by_object_source"][source] = summary["by_object_source"].get(source, 0) + 1
        summary["by_match_type"][match_type_value] = summary["by_match_type"].get(match_type_value, 0) + 1
        for flag in (row.get("review_flags", "") or "").split("|"):
            if flag:
                summary["by_review_flag"][flag] = summary["by_review_flag"].get(flag, 0) + 1
    return summary


def available_tooling() -> dict[str, bool]:
    """Report whether optional ecosystem tools are importable."""
    return {
        "oaklib": importlib.util.find_spec("oaklib") is not None,
        "schema_automator": importlib.util.find_spec("schema_automator") is not None,
        "linkml_store": importlib.util.find_spec("linkml_store") is not None,
    }


def write_tsv(rows: list[dict[str, Any]], output_path: str | Path) -> None:
    """Write rows as TSV."""
    if not rows:
        Path(output_path).write_text("")
        return
    fieldnames = list(rows[0].keys())
    with Path(output_path).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_json(data: dict[str, Any], output_path: str | Path) -> None:
    """Write summary JSON."""
    Path(output_path).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
