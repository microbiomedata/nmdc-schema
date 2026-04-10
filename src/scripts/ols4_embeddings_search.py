"""Search OLS4 embeddings API for ontology term candidates matching nmdc-schema elements.

Iterates classes, slots, enums, and permissible values from the schema,
sends name + description to the OLS4 LLM search endpoint, and writes
results as SSSOM-style TSV.

Usage:
    poetry run python src/scripts/ols4_embeddings_search.py [OPTIONS]

See --help for options.
"""

import csv
import logging
import re
import time
from pathlib import Path
from typing import Optional

import click
import requests
from linkml_runtime.utils.schemaview import SchemaView

logger = logging.getLogger(__name__)

OLS4_BASE = "https://www.ebi.ac.uk/ols4/api/v2"
DEFAULT_MODEL = "llama-embed-nemotron-8b_pca512"
DEFAULT_SCHEMA = "src/schema/nmdc.yaml"
DEFAULT_ROWS = 5
DEFAULT_DELAY = 0.5  # seconds between requests

SSSOM_HEADER = [
    "subject_id",
    "subject_label",
    "subject_category",
    "subject_description",
    "object_id",
    "object_label",
    "object_source",
    "predicate_id",
    "mapping_justification",
    "confidence",
    "comment",
]


def ols4_llm_search(
    query: str,
    model: str = DEFAULT_MODEL,
    rows: int = DEFAULT_ROWS,
    ontology: Optional[str] = None,
    endpoint: str = "classes",
) -> list[dict]:
    """Call OLS4 embeddings search and return parsed results."""
    if ontology:
        url = f"{OLS4_BASE}/ontologies/{ontology}/{endpoint}/llm_search"
    else:
        url = f"{OLS4_BASE}/{endpoint}/llm_search"

    params = {"q": query, "model": model, "rows": rows}

    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data.get("elements", [])
    except requests.RequestException as e:
        logger.warning("OLS4 request failed for %r: %s", query[:60], e)
        return []


def extract_curie(element: dict) -> Optional[str]:
    """Extract a CURIE from an OLS4 search result element."""
    # OLS4 v2 uses camelCase field names
    curie = element.get("curie")
    if curie:
        return curie
    short_form = element.get("shortForm")
    if short_form:
        return short_form
    # Fall back to full IRI prefixed with "iri:" so downstream consumers
    # can distinguish it from a real CURIE (intentional for traceability).
    iri = element.get("iri")
    if iri:
        return f"iri:{iri}"
    return None


def extract_label(element: dict) -> str:
    """Extract label from an OLS4 result (may be a list)."""
    label = element.get("label")
    if isinstance(label, list):
        return label[0] if label else ""
    return label or ""


def extract_ontology(element: dict) -> str:
    """Extract the source ontology from an OLS4 result."""
    ontology_id = element.get("ontologyId") or ""
    if not ontology_id:
        appears_in = element.get("appearsIn", [])
        if appears_in:
            ontology_id = appears_in[0]
    return ontology_id.upper()


def extract_score(element: dict) -> str:
    """Extract the similarity score from an OLS4 result."""
    score = element.get("score")
    if score is not None:
        return f"{score:.4f}"
    return ""


def build_query(name: str, description: Optional[str]) -> str:
    """Build a search query from element name and description."""
    # Expand CamelCase
    expanded = ""
    for i, ch in enumerate(name):
        if ch.isupper() and i > 0 and name[i - 1].islower():
            expanded += " "
        expanded += ch
    # Replace underscores
    expanded = expanded.replace("_", " ")

    if description:
        # Truncate long descriptions to keep queries focused
        desc = description[:200].strip()
        return f"{expanded}: {desc}"
    return expanded


def search_element(
    subject_id: str,
    subject_label: str,
    subject_category: str,
    description: Optional[str],
    model: str,
    rows: int,
    delay: float,
    ontology: Optional[str],
) -> list[dict]:
    """Search OLS4 for one schema element and return SSSOM rows."""
    query = build_query(subject_label, description)
    results = ols4_llm_search(query, model=model, rows=rows, ontology=ontology)
    time.sleep(delay)

    sssom_rows = []
    for hit in results:
        curie = extract_curie(hit)
        if not curie:
            continue
        label = extract_label(hit)
        source = extract_ontology(hit)
        score = extract_score(hit)
        sssom_rows.append(
            {
                "subject_id": subject_id,
                "subject_label": subject_label,
                "subject_category": subject_category,
                "subject_description": (description or "")[:200],
                "object_id": curie,
                "object_label": label,
                "object_source": source,
                "predicate_id": "skos:closeMatch",
                "mapping_justification": "semapv:SemanticSimilarityThresholdMatching",
                "confidence": score,
                "comment": "",
            }
        )
    return sssom_rows


@click.command()
@click.option(
    "--schema",
    default=DEFAULT_SCHEMA,
    show_default=True,
    help="Path to LinkML schema YAML",
)
@click.option(
    "--output",
    "-o",
    default="ols4_embeddings_results.tsv",
    show_default=True,
    help="Output TSV file",
)
@click.option(
    "--model",
    default=DEFAULT_MODEL,
    show_default=True,
    help="OLS4 embedding model name",
)
@click.option(
    "--rows",
    default=DEFAULT_ROWS,
    show_default=True,
    help="Number of OLS4 results per query",
)
@click.option(
    "--delay",
    default=DEFAULT_DELAY,
    show_default=True,
    help="Seconds between API requests",
)
@click.option(
    "--ontology",
    default=None,
    help="Restrict search to a specific ontology (e.g. 'obi', 'envo')",
)
@click.option(
    "--element-types",
    default="classes,slots,enums,pvs",
    show_default=True,
    help="Comma-separated element types to search",
)
@click.option(
    "--skip-mapped/--include-mapped",
    default=False,
    show_default=True,
    help="Skip elements that already have mappings",
)
@click.option("--verbose", "-v", is_flag=True, help="Verbose logging")
def main(
    schema: str,
    output: str,
    model: str,
    rows: int,
    delay: float,
    ontology: Optional[str],
    element_types: str,
    skip_mapped: bool,
    verbose: bool,
):
    """Search OLS4 embeddings for ontology terms matching nmdc-schema elements."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(message)s",
    )

    types = set(element_types.split(","))
    sv = SchemaView(schema)
    all_rows: list[dict] = []
    total_queries = 0
    skipped = 0

    def has_mappings(element) -> bool:
        return bool(
            getattr(element, "exact_mappings", None)
            or getattr(element, "close_mappings", None)
            or getattr(element, "broad_mappings", None)
            or getattr(element, "related_mappings", None)
            or getattr(element, "narrow_mappings", None)
        )

    # Classes
    if "classes" in types:
        classes = sv.all_classes()
        logger.info("Searching %d classes...", len(classes))
        for name, cls in classes.items():
            if skip_mapped and has_mappings(cls):
                skipped += 1
                continue
            curie = cls.class_uri or f"nmdc:{name}"
            results = search_element(
                curie, name, "class", cls.description, model, rows, delay, ontology
            )
            all_rows.extend(results)
            total_queries += 1
            if total_queries % 50 == 0:
                logger.info("  ...%d queries done, %d results so far", total_queries, len(all_rows))

    # Slots
    if "slots" in types:
        all_slots = sv.all_slots()
        logger.info("Searching %d slots...", len(all_slots))
        for name, slot in all_slots.items():
            if skip_mapped and has_mappings(slot):
                skipped += 1
                continue
            curie = slot.slot_uri or f"nmdc:{name}"
            results = search_element(
                curie, name, "slot", slot.description, model, rows, delay, ontology
            )
            all_rows.extend(results)
            total_queries += 1
            if total_queries % 50 == 0:
                logger.info("  ...%d queries done, %d results so far", total_queries, len(all_rows))

    # Enums
    if "enums" in types:
        all_enums = sv.all_enums()
        logger.info("Searching %d enums...", len(all_enums))
        for name, enum in all_enums.items():
            if skip_mapped and has_mappings(enum):
                skipped += 1
                continue
            curie = f"nmdc:{name}"
            results = search_element(
                curie, name, "enum", enum.description, model, rows, delay, ontology
            )
            all_rows.extend(results)
            total_queries += 1
            if total_queries % 50 == 0:
                logger.info("  ...%d queries done, %d results so far", total_queries, len(all_rows))

    # Permissible values
    if "pvs" in types:
        all_enums = sv.all_enums()
        pv_count = sum(
            len(e.permissible_values) for e in all_enums.values() if e.permissible_values
        )
        logger.info("Searching %d permissible values...", pv_count)
        for enum_name, enum in all_enums.items():
            if not enum.permissible_values:
                continue
            for pv_text, pv in enum.permissible_values.items():
                if skip_mapped and pv.meaning:
                    skipped += 1
                    continue
                sanitized_pv = re.sub(r"[^A-Za-z0-9._-]", "_", pv_text)
                subject_id = f"nmdc:{enum_name}.{sanitized_pv}"
                results = search_element(
                    subject_id,
                    pv_text,
                    "permissible_value",
                    pv.description,
                    model,
                    rows,
                    delay,
                    ontology,
                )
                all_rows.extend(results)
                total_queries += 1
                if total_queries % 50 == 0:
                    logger.info(
                        "  ...%d queries done, %d results so far",
                        total_queries,
                        len(all_rows),
                    )

    # Write output
    output_path = Path(output)
    with output_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SSSOM_HEADER, delimiter="\t")
        writer.writeheader()
        writer.writerows(all_rows)

    logger.info(
        "Done. %d queries, %d results written to %s (skipped %d already-mapped)",
        total_queries,
        len(all_rows),
        output_path,
        skipped,
    )


if __name__ == "__main__":
    main()
