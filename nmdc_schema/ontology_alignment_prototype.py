"""Helpers for comparing semantic alignment hits against lexical strength.

This module is intentionally lightweight so it can run in the base nmdc-schema
environment while supporting an oaklib-backed metadata path and leaving room
for additional LinkML ecosystem backends.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import curies
import requests
from linkml_runtime.linkml_model.meta import PermissibleValue
from linkml_runtime.utils.schemaview import SchemaView


SEMANTIC_JUSTIFICATION = "semapv:SemanticSimilarityThresholdMatching"
OLS4_SEARCH_URL = "https://www.ebi.ac.uk/ols4/api/search"
BIOPORTAL_CLASSES_URL_TEMPLATE = "https://data.bioontology.org/ontologies/{acronym}/classes"
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
    subject_synonyms: tuple[str, ...]
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


@dataclass(frozen=True)
class MetadataResolution:
    """Resolved metadata plus provenance about how it was obtained."""

    metadata: OlsEntityMetadata
    requested_backend: str
    resolved_backend: str


@dataclass(frozen=True)
class SubjectQueryRecord:
    """Minimal representation of an NMDC subject used for retrieval."""

    subject_id: str
    subject_label: str
    subject_category: str
    subject_description: str
    subject_synonyms: tuple[str, ...] = tuple()


@dataclass(frozen=True)
class OntologyTermRecord:
    """Minimal local ontology record used for LinkML-side semantic search."""

    object_id: str
    object_label: str
    object_source: str
    object_kind: str
    object_description: str = ""
    object_synonyms: tuple[str, ...] = tuple()


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


def _string_values(*candidates: Any) -> tuple[str, ...]:
    values: list[str] = []
    for candidate in candidates:
        if not candidate:
            continue
        if isinstance(candidate, str):
            if candidate.strip():
                values.append(candidate.strip())
            continue
        if isinstance(candidate, dict):
            for key, value in candidate.items():
                values.extend(_string_values(key, value))
            continue
        if isinstance(candidate, (list, tuple, set)):
            for item in candidate:
                values.extend(_string_values(item))
            continue
    unique: list[str] = []
    seen: set[str] = set()
    for value in values:
        normalized = normalize_text(value)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique.append(value)
    return tuple(unique)


def _schema_aliases(element: Any) -> tuple[str, ...]:
    return _string_values(
        getattr(element, "aliases", None),
        getattr(element, "structured_aliases", None),
    )


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
    subject_id = getattr(class_def, "class_uri", None) or f"nmdc:{class_name}"
    return SchemaElementRecord(
        subject_id=subject_id,
        subject_label=class_def.title or class_name,
        subject_category="class",
        subject_description=class_def.description or "",
        subject_synonyms=_schema_aliases(class_def),
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
    subject_id = getattr(slot_def, "slot_uri", None) or f"nmdc:{slot_name}"
    return SchemaElementRecord(
        subject_id=subject_id,
        subject_label=slot_def.title or slot_name,
        subject_category="slot",
        subject_description=slot_def.description or "",
        subject_synonyms=_schema_aliases(slot_def),
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
        subject_synonyms=_schema_aliases(enum_def),
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
        subject_id=f"nmdc:{enum_name}#{re.sub(r'[^A-Za-z0-9._-]', '_', pv_name)}",
        subject_label=pv.text or pv_name,
        subject_category="permissible_value",
        subject_description=pv.description or "",
        subject_synonyms=_schema_aliases(pv),
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


def parse_quota_option(value: str | None) -> dict[str, int]:
    """Parse a comma-separated quota option like 'slot->class=10,pv->class=15'."""
    quotas: dict[str, int] = {}
    if not value:
        return quotas
    for item in value.split(","):
        item = item.strip()
        if not item or "=" not in item:
            continue
        key, raw_limit = item.split("=", 1)
        key = key.strip()
        raw_limit = raw_limit.strip()
        if not key or not raw_limit:
            continue
        try:
            limit = int(raw_limit)
        except ValueError:
            continue
        if limit >= 0:
            quotas[key] = limit
    return quotas


def oaklib_available() -> bool:
    """Return True when oaklib is importable in the current environment."""
    return importlib.util.find_spec("oaklib") is not None


def linkml_store_available() -> bool:
    """Return True when linkml-store is importable in the current environment."""
    return importlib.util.find_spec("linkml_store") is not None


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


def oaklib_entity_metadata(
    object_id: str,
    object_source: str,
    cache: dict[tuple[str, str], OlsEntityMetadata],
) -> OlsEntityMetadata:
    """Resolve minimal metadata through oaklib when available in the environment.

    This is intentionally conservative for the first integration step:
    - if oaklib is not installed in the current environment, return empty metadata
    - if oaklib is available, try label/definition/synonym access without
      forcing a specific backend configuration
    """
    cache_key = (object_id, object_source)
    if cache_key in cache:
        return cache[cache_key]

    metadata = OlsEntityMetadata(
        object_id=object_id,
        object_source=object_source,
        object_kind="class",
        label="",
        iri="",
        description="",
    )
    if not oaklib_available():
        cache[cache_key] = metadata
        return metadata

    try:
        from oaklib import get_adapter
    except Exception:
        cache[cache_key] = metadata
        return metadata

    try:
        # get_adapter expects a handle like "sqlite:obo:obi", not a CURIE
        adapter_handle = f"sqlite:obo:{object_source.lower()}"
        adapter = get_adapter(adapter_handle)
        label = adapter.label(object_id) or ""
        definition = ""
        if hasattr(adapter, "definition"):
            definition = adapter.definition(object_id) or ""
        synonyms: tuple[str, ...] = tuple()
        if hasattr(adapter, "entity_aliases"):
            aliases = adapter.entity_aliases(object_id) or []
            synonyms = tuple(str(alias) for alias in aliases if alias)
        metadata = OlsEntityMetadata(
            object_id=object_id,
            object_source=object_source,
            object_kind="class",
            label=label,
            iri="",
            description=definition,
            synonyms=synonyms,
        )
    except Exception:
        pass

    cache[cache_key] = metadata
    return metadata


def resolve_entity_metadata(
    object_id: str,
    object_source: str,
    backend: str,
    ols_cache: dict[tuple[str, str], OlsEntityMetadata] | None = None,
    oaklib_cache: dict[tuple[str, str], OlsEntityMetadata] | None = None,
) -> MetadataResolution:
    """Resolve metadata from the requested backend with graceful fallback."""
    requested_backend = (backend or "none").lower()
    ols_cache = ols_cache or {}
    oaklib_cache = oaklib_cache or {}

    if requested_backend == "none":
        metadata = OlsEntityMetadata(
            object_id=object_id,
            object_source=object_source,
            object_kind="class",
            label="",
            iri="",
            description="",
        )
        return MetadataResolution(metadata=metadata, requested_backend=requested_backend, resolved_backend="none")

    if requested_backend == "oaklib":
        if oaklib_available():
            metadata = oaklib_entity_metadata(object_id, object_source, oaklib_cache)
            return MetadataResolution(metadata=metadata, requested_backend=requested_backend, resolved_backend="oaklib")
        metadata = ols_entity_metadata(object_id, object_source, ols_cache)
        return MetadataResolution(metadata=metadata, requested_backend=requested_backend, resolved_backend="ols4_fallback")

    metadata = ols_entity_metadata(object_id, object_source, ols_cache)
    return MetadataResolution(metadata=metadata, requested_backend=requested_backend, resolved_backend="ols4")


def read_unique_subjects(
    alignment_results_path: str | Path,
    allowed_subject_categories: set[str] | None = None,
    max_subjects: int | None = None,
    schema_index: dict[str, SchemaElementRecord] | None = None,
) -> list[SubjectQueryRecord]:
    """Read distinct NMDC subjects from an alignment TSV while preserving first-seen order."""
    allowed_subject_categories = {item.lower() for item in (allowed_subject_categories or set())}
    schema_index = schema_index or {}
    unique: dict[str, SubjectQueryRecord] = {}
    for row in read_alignment_rows(alignment_results_path):
        subject_category = (row.get("subject_category") or "").lower()
        if allowed_subject_categories and subject_category not in allowed_subject_categories:
            continue
        subject_id = row.get("subject_id", "")
        if not subject_id or subject_id in unique:
            continue
        schema_record = schema_index.get(subject_id)
        unique[subject_id] = SubjectQueryRecord(
            subject_id=subject_id,
            subject_label=schema_record.subject_label if schema_record else row.get("subject_label", ""),
            subject_category=subject_category,
            subject_description=schema_record.subject_description if schema_record else row.get("subject_description", ""),
            subject_synonyms=schema_record.subject_synonyms if schema_record else tuple(),
        )
        if max_subjects is not None and len(unique) >= max_subjects:
            break
    return list(unique.values())


def compose_subject_query_text(subject: SubjectQueryRecord) -> str:
    """Compose a stable semantic-search query for an NMDC schema subject."""
    label = (subject.subject_label or "").strip()
    synonyms = "; ".join(item for item in subject.subject_synonyms if item).strip()
    description = (subject.subject_description or "").strip()
    parts = [part for part in (label, synonyms, description) if part]
    return " :: ".join(parts)


def compose_ontology_term_search_text(term: OntologyTermRecord) -> str:
    """Compose the text payload indexed for a local ontology term."""
    parts = [part for part in (term.object_label, "; ".join(term.object_synonyms), term.object_description) if part]
    return " :: ".join(parts)


def harvest_oaklib_ontology_terms(
    adapter_handle: str,
    ontology_prefix: str,
    max_terms: int | None = None,
) -> list[OntologyTermRecord]:
    """Harvest local ontology terms through oaklib for LinkML-side retrieval."""
    if not oaklib_available():
        raise RuntimeError("oaklib is required to harvest ontology terms")

    from oaklib import get_adapter

    adapter = get_adapter(adapter_handle)
    prefix = ontology_prefix.upper()
    harvested: list[OntologyTermRecord] = []
    for curie in adapter.entities(filter_obsoletes=True):
        if not curie.startswith(f"{prefix}:"):
            continue
        label = adapter.label(curie) or ""
        if not label:
            continue
        description = adapter.definition(curie) if hasattr(adapter, "definition") else ""
        aliases = adapter.entity_aliases(curie) if hasattr(adapter, "entity_aliases") else []
        harvested.append(
            OntologyTermRecord(
                object_id=curie,
                object_label=label,
                object_source=prefix,
                object_kind="class",
                object_description=description or "",
                object_synonyms=tuple(str(alias) for alias in (aliases or []) if alias),
            )
        )
        if max_terms is not None and len(harvested) >= max_terms:
            break
    return harvested


def _extract_bioportal_class_rows(payload: Any) -> list[dict[str, Any]]:
    """Normalize BioPortal class responses into a list of row dicts."""
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        collection = payload.get("collection")
        if isinstance(collection, list):
            return [item for item in collection if isinstance(item, dict)]
    return []


def _normalize_bioportal_object_id(raw_object_id: str, ontology_acronym: str) -> str:
    """Convert BioPortal IDs to CURIEs with LinkML-adjacent registry tooling first."""
    if not raw_object_id:
        return ""
    if ":" in raw_object_id and not raw_object_id.startswith("http"):
        return raw_object_id

    compact_match = re.search(r"/obo/([A-Za-z][A-Za-z0-9]*)[_:]([A-Za-z0-9_\\-]+)$", raw_object_id)
    if compact_match:
        return f"{compact_match.group(1).upper()}:{compact_match.group(2)}"

    fragment = raw_object_id.rsplit("/", 1)[-1].rsplit("#", 1)[-1]
    if fragment.startswith(f"{ontology_acronym.upper()}_"):
        return f"{ontology_acronym.upper()}:{fragment.split('_', 1)[1]}"

    compacted = curies.get_bioregistry_converter().compress(raw_object_id)
    if compacted:
        return normalize_curie_prefix_case(compacted)
    return normalize_curie_prefix_case(raw_object_id)


def normalize_curie_prefix_case(curie_or_iri: str) -> str:
    """Uppercase the CURIE prefix while leaving the local ID untouched."""
    if ":" not in curie_or_iri or curie_or_iri.startswith("http"):
        return curie_or_iri
    prefix, local_id = curie_or_iri.split(":", 1)
    return f"{prefix.upper()}:{local_id}"


def harvest_bioportal_ontology_terms(
    ontology_acronyms: list[str],
    api_key: str | None = None,
    max_terms: int | None = None,
    page_size: int = 250,
    include_views: bool = False,
    include_imported_terms: bool = False,
) -> list[OntologyTermRecord]:
    """Harvest ontology terms directly from BioPortal for local semantic retrieval.

    This keeps BioPortal as a corpus source only. Embeddings and retrieval still
    run locally through linkml-store.
    """
    resolved_api_key = api_key or os.environ.get("BIOPORTAL_API_KEY", "")
    if not resolved_api_key:
        raise RuntimeError("BIOPORTAL_API_KEY is required to harvest BioPortal terms")

    harvested: list[OntologyTermRecord] = []
    per_ontology_cap = max_terms if max_terms is not None and len(ontology_acronyms) == 1 else None

    for ontology_acronym in ontology_acronyms:
        acronym = ontology_acronym.strip().upper()
        if not acronym:
            continue
        page = 1
        harvested_for_acronym = 0
        while True:
            params = {
                "apikey": resolved_api_key,
                "include": "prefLabel,synonym,definition,obsolete,@id",
                "display_context": "false",
                "display_links": "false",
                "include_views": "true" if include_views else "false",
                "page": page,
                "pagesize": page_size,
            }
            response = requests.get(
                BIOPORTAL_CLASSES_URL_TEMPLATE.format(acronym=acronym),
                params=params,
                timeout=60,
            )
            response.raise_for_status()
            rows = _extract_bioportal_class_rows(response.json())
            if not rows:
                break

            for row in rows:
                raw_object_id = extract_first(row.get("@id")) or extract_first(row.get("id"))
                object_id = _normalize_bioportal_object_id(raw_object_id, acronym)
                object_label = extract_first(row.get("prefLabel")) or extract_first(row.get("label"))
                if not object_id or not object_label:
                    continue
                if not include_imported_terms and ":" in object_id:
                    object_prefix = object_id.split(":", 1)[0].upper()
                    if object_prefix != acronym:
                        continue
                definitions = row.get("definition") or []
                synonyms = row.get("synonym") or row.get("synonyms") or []
                if isinstance(definitions, str):
                    description = definitions
                else:
                    description = " ".join(str(item) for item in definitions if item)
                if isinstance(synonyms, str):
                    synonyms_tuple = (synonyms,) if synonyms else tuple()
                else:
                    synonyms_tuple = tuple(str(item) for item in synonyms if item)

                harvested.append(
                    OntologyTermRecord(
                        object_id=object_id,
                        object_label=object_label,
                        object_source=acronym,
                        object_kind="class",
                        object_description=description,
                        object_synonyms=synonyms_tuple,
                    )
                )
                harvested_for_acronym += 1
                if per_ontology_cap is not None and harvested_for_acronym >= per_ontology_cap:
                    break
                if max_terms is not None and per_ontology_cap is None and len(harvested) >= max_terms:
                    return harvested

            if per_ontology_cap is not None and harvested_for_acronym >= per_ontology_cap:
                break
            if len(rows) < page_size:
                break
            page += 1

    return harvested


def _linkml_store_similarity_search(
    query_text: str,
    vectors: list[tuple[str, Any]],
    indexer: Any,
    limit: int,
    cache_queries: bool = True,
) -> list[tuple[float, str]]:
    """Search precomputed vectors with a cached linkml-store query embedding."""
    if not vectors:
        return []

    if cache_queries:
        query_vector = indexer.text_to_vector(query_text, cache=True)
    else:
        query_vector = indexer.text_to_vector(query_text, cache=False)

    from linkml_store.utils.vector_utils import pairwise_cosine_similarity

    distances = [(float(pairwise_cosine_similarity(query_vector, item_vector)), item_id) for item_id, item_vector in vectors]
    distances.sort(key=lambda item: -item[0])
    return distances[:limit]


def run_linkml_store_semantic_search(
    subjects: list[SubjectQueryRecord],
    ontology_terms: list[OntologyTermRecord],
    top_k: int,
    embedding_model_name: str,
    cache_db_path: str | Path,
    cache_collection_name: str,
    corpus_batch_size: int = 250,
) -> list[dict[str, Any]]:
    """Run semantic retrieval with linkml-store embeddings over a locally harvested ontology corpus."""
    if not linkml_store_available():
        raise RuntimeError("linkml-store is required for LinkML-side semantic retrieval")

    from linkml_store.index.implementations.llm_indexer import LLMIndexer

    cache_db_path = str(cache_db_path)
    indexed_terms = [
        {
            "id": term.object_id,
            "search_text": compose_ontology_term_search_text(term),
        }
        for term in ontology_terms
    ]
    term_by_id = {term.object_id: term for term in ontology_terms}
    indexer = LLMIndexer(
        embedding_model_name=embedding_model_name,
        cached_embeddings_database=cache_db_path,
        cached_embeddings_collection=cache_collection_name,
        index_attributes=["search_text"],
    )
    vectors: list[Any] = []
    for start in range(0, len(indexed_terms), corpus_batch_size):
        chunk = indexed_terms[start : start + corpus_batch_size]
        vectors.extend(indexer.objects_to_vectors(chunk))
    indexed_vectors = list(zip([term["id"] for term in indexed_terms], vectors))

    rows: list[dict[str, Any]] = []
    for subject in subjects:
        query_text = compose_subject_query_text(subject)
        hits = _linkml_store_similarity_search(query_text, indexed_vectors, indexer, limit=top_k)
        for score, object_id in hits:
            term = term_by_id[object_id]
            rows.append(
                {
                    "subject_id": subject.subject_id,
                    "subject_label": subject.subject_label,
                    "subject_category": subject.subject_category,
                    "subject_description": subject.subject_description,
                    "object_id": term.object_id,
                    "object_label": term.object_label,
                    "object_source": term.object_source,
                    "predicate_id": "skos:closeMatch",
                    "mapping_justification": SEMANTIC_JUSTIFICATION,
                    "confidence": round(score, 4),
                    "comment": (
                        f"retrieval_backend=linkml_store_llm;"
                        f"embedding_model={embedding_model_name};"
                        f"cache_collection={cache_collection_name};"
                        f"query_text={query_text}"
                    ),
                }
            )
    return rows


def summarize_backend_overlap(
    reference_rows: list[dict[str, Any]],
    candidate_rows: list[dict[str, Any]],
    object_source: str,
    top_k: int,
) -> dict[str, Any]:
    """Compare top-k object overlap between two retrieval backends for one ontology source."""
    source = object_source.upper()
    reference_by_subject: dict[str, list[dict[str, Any]]] = {}
    candidate_by_subject: dict[str, list[dict[str, Any]]] = {}

    for row in reference_rows:
        if (row.get("object_source") or "").upper() != source:
            continue
        reference_by_subject.setdefault(row.get("subject_id", ""), []).append(row)
    for row in candidate_rows:
        if (row.get("object_source") or "").upper() != source:
            continue
        candidate_by_subject.setdefault(row.get("subject_id", ""), []).append(row)

    overlapping_subjects = sorted(set(reference_by_subject) & set(candidate_by_subject))
    subjects_with_any_overlap = 0
    subjects_with_top1_overlap = 0
    cumulative_overlap = 0
    for subject_id in overlapping_subjects:
        ref_rows = sorted(reference_by_subject[subject_id], key=lambda row: -float(row.get("confidence", 0.0) or 0.0))[:top_k]
        cand_rows = sorted(candidate_by_subject[subject_id], key=lambda row: -float(row.get("confidence", 0.0) or 0.0))[:top_k]
        ref_ids = {row.get("object_id", "") for row in ref_rows}
        cand_ids = {row.get("object_id", "") for row in cand_rows}
        overlap = len(ref_ids & cand_ids)
        cumulative_overlap += overlap
        if overlap:
            subjects_with_any_overlap += 1
        if ref_rows and cand_rows and ref_rows[0].get("object_id") == cand_rows[0].get("object_id"):
            subjects_with_top1_overlap += 1

    return {
        "reference_subjects": len(reference_by_subject),
        "candidate_subjects": len(candidate_by_subject),
        "subjects_compared": len(overlapping_subjects),
        "subjects_with_any_top_k_overlap": subjects_with_any_overlap,
        "subjects_with_top1_overlap": subjects_with_top1_overlap,
        "mean_exact_overlap_per_subject": round(cumulative_overlap / len(overlapping_subjects), 4) if overlapping_subjects else 0.0,
        "top_k": top_k,
        "object_source": source,
    }


def summarize_source_distribution(
    rows: list[dict[str, Any]],
    top_n: int = 20,
) -> dict[str, Any]:
    """Summarize ontology-source concentration in a retrieval result set."""
    counts: dict[str, int] = {}
    subjects_by_source: dict[str, set[str]] = {}
    for row in rows:
        source = (row.get("object_source") or "").upper()
        subject_id = row.get("subject_id", "")
        counts[source] = counts.get(source, 0) + 1
        subjects_by_source.setdefault(source, set()).add(subject_id)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return {
        "total_rows": len(rows),
        "distinct_sources": len(counts),
        "top_sources": [
            {
                "object_source": source,
                "row_count": row_count,
                "subject_count": len(subjects_by_source.get(source, set())),
            }
            for source, row_count in ranked[:top_n]
        ],
    }


def summarize_property_like_gap(
    schema_index: dict[str, SchemaElementRecord],
    baseline_rows: list[dict[str, Any]],
    ontology_prefix: str | None = None,
) -> dict[str, Any]:
    """Summarize the gap between property-like NMDC slots and class-oriented retrieval baselines."""
    property_like_slots = {
        record.subject_id
        for record in schema_index.values()
        if record.subject_category == "slot" and record.expected_alignment_type == "property_like"
    }
    class_filler_slots = {
        record.subject_id
        for record in schema_index.values()
        if record.subject_category == "slot" and record.expected_alignment_type == "class_filler"
    }
    filtered_rows = baseline_rows
    if ontology_prefix:
        prefix = ontology_prefix.upper()
        filtered_rows = [row for row in baseline_rows if (row.get("object_source") or "").upper() == prefix]
    slot_subjects_with_hits = {row.get("subject_id", "") for row in filtered_rows if (row.get("subject_category") or "").lower() == "slot"}
    property_like_with_hits = property_like_slots & slot_subjects_with_hits
    class_filler_with_hits = class_filler_slots & slot_subjects_with_hits
    return {
        "ontology_prefix": ontology_prefix.upper() if ontology_prefix else "ALL",
        "total_slot_subjects": sum(1 for record in schema_index.values() if record.subject_category == "slot"),
        "property_like_slot_subjects": len(property_like_slots),
        "class_filler_slot_subjects": len(class_filler_slots),
        "slot_subjects_with_retrieval_hits": len(slot_subjects_with_hits),
        "property_like_slots_with_retrieval_hits": len(property_like_with_hits),
        "class_filler_slots_with_retrieval_hits": len(class_filler_with_hits),
        "property_like_hit_fraction": round(len(property_like_with_hits) / len(property_like_slots), 4) if property_like_slots else 0.0,
        "class_filler_hit_fraction": round(len(class_filler_with_hits) / len(class_filler_slots), 4) if class_filler_slots else 0.0,
        "current_baseline_bias": (
            "current comparison inputs are class-oriented; property_like slots may need property retrieval or "
            "relationship-neighborhood expansion rather than class-only semantic search"
        ),
    }


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
    match_type_quotas: dict[str, int] | None = None,
) -> list[dict[str, Any]]:
    """Return a small review-focused shortlist from enriched rows."""
    preferred = {bucket: idx for idx, bucket in enumerate(preferred_buckets)}
    match_type_quotas = match_type_quotas or {}

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
    counts_by_match_type: dict[str, int] = {}
    for row in sorted(rows, key=sort_key):
        subject_id = row.get("subject_id", "")
        match_type_value = row.get("match_type", "")
        if counts_by_subject.get(subject_id, 0) >= max_per_subject:
            continue
        quota = match_type_quotas.get(match_type_value)
        if quota is not None and counts_by_match_type.get(match_type_value, 0) >= quota:
            continue
        selected.append(row)
        counts_by_subject[subject_id] = counts_by_subject.get(subject_id, 0) + 1
        counts_by_match_type[match_type_value] = counts_by_match_type.get(match_type_value, 0) + 1
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
    metadata_backend: str = "ols4",
) -> list[dict[str, Any]]:
    """Enrich a small review shortlist with more term metadata."""
    if (metadata_backend or "none").lower() == "none":
        return rows

    ols_cache: dict[tuple[str, str], OlsEntityMetadata] = {}
    oaklib_cache: dict[tuple[str, str], OlsEntityMetadata] = {}
    enriched_rows: list[dict[str, Any]] = []
    for rank, row in enumerate(rows, start=1):
        source = (row.get("object_source") or "").upper()
        resolution = resolve_entity_metadata(
            row.get("object_id", ""),
            source,
            backend=metadata_backend,
            ols_cache=ols_cache,
            oaklib_cache=oaklib_cache,
        )
        metadata = resolution.metadata
        updated = {
            **row,
            "review_rank": rank,
            "object_kind": metadata.object_kind,
            "object_label_resolved": metadata.label or row.get("object_label", ""),
            "object_iri": metadata.iri,
            "object_description": metadata.description[:500],
            "object_is_obsolete": metadata.is_obsolete,
            "object_synonyms": "|".join(metadata.synonyms[:20]),
            "metadata_backend_requested": resolution.requested_backend,
            "metadata_backend_resolved": resolution.resolved_backend,
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
        "by_metadata_backend": {},
        "by_review_flag": {},
    }
    for row in rows:
        bucket = row.get("structural_bucket", "")
        source = row.get("object_source", "")
        match_type_value = row.get("match_type", "")
        resolved_backend = row.get("metadata_backend_resolved", "")
        summary["by_structural_bucket"][bucket] = summary["by_structural_bucket"].get(bucket, 0) + 1
        summary["by_object_source"][source] = summary["by_object_source"].get(source, 0) + 1
        summary["by_match_type"][match_type_value] = summary["by_match_type"].get(match_type_value, 0) + 1
        if resolved_backend:
            summary["by_metadata_backend"][resolved_backend] = summary["by_metadata_backend"].get(resolved_backend, 0) + 1
        for flag in (row.get("review_flags", "") or "").split("|"):
            if flag:
                summary["by_review_flag"][flag] = summary["by_review_flag"].get(flag, 0) + 1
    return summary


def available_tooling() -> dict[str, bool]:
    """Report whether ecosystem backends are importable in the current environment."""
    return {
        "oaklib": oaklib_available(),
        "schema_automator": importlib.util.find_spec("schema_automator") is not None,
        "linkml_store": linkml_store_available(),
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
