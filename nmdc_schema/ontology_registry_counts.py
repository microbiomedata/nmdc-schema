"""Helpers for counting ontology registries and extracting prefixes."""

from __future__ import annotations

import csv
import os
from collections import Counter
from pathlib import Path
from typing import Any

import requests
import yaml


OLS4_ONTOLOGIES_URL = "https://www.ebi.ac.uk/ols4/api/ontologies"
BIOPORTAL_ONTOLOGIES_URL = "https://data.bioontology.org/ontologies"
OBO_FOUNDRY_CONTENTS_URL = "https://api.github.com/repos/OBOFoundry/OBOFoundry.github.io/contents/ontology"
SEMSQL_REGISTRY_RAW_URL = (
    "https://raw.githubusercontent.com/INCATools/semantic-sql/main/src/semsql/builder/registry/ontologies.yaml"
)


def read_ols_embeddings_corpus(semantic_results_path: str | Path) -> dict[str, Any]:
    """Count and summarize the ontology prefixes present in an OLS-derived embeddings TSV."""
    rows = list(csv.DictReader(Path(semantic_results_path).open(), delimiter="\t"))
    counts = Counter((row.get("object_source") or "").upper() for row in rows if row.get("object_source"))
    return {
        "source_name": "ols_embeddings_corpus",
        "count": len(counts),
        "prefixes": sorted(counts),
        "top_prefixes_by_row_count": [
            {"prefix": prefix, "row_count": row_count} for prefix, row_count in counts.most_common(50)
        ],
    }


def fetch_ols_overall_registry(timeout: int = 120) -> dict[str, Any]:
    """Fetch the OLS4 ontology registry count and preferred prefixes from the public API."""
    response = requests.get(f"{OLS4_ONTOLOGIES_URL}?page=0&size=500", timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    ontologies = payload.get("_embedded", {}).get("ontologies", [])
    prefixes = sorted(
        {
            (
                ontology.get("config", {}).get("preferredPrefix")
                or ontology.get("ontologyId")
                or ontology.get("config", {}).get("id")
                or ""
            ).upper()
            for ontology in ontologies
            if (
                ontology.get("config", {}).get("preferredPrefix")
                or ontology.get("ontologyId")
                or ontology.get("config", {}).get("id")
            )
        }
    )
    return {
        "source_name": "ols_overall",
        "count": int(payload.get("page", {}).get("totalElements", len(ontologies))),
        "prefixes": prefixes,
        "sample": [
            {
                "ontologyId": ontology.get("ontologyId"),
                "preferredPrefix": ontology.get("config", {}).get("preferredPrefix"),
                "numberOfTerms": ontology.get("numberOfTerms"),
                "loaded": ontology.get("loaded"),
            }
            for ontology in ontologies[:20]
        ],
    }


def fetch_bioportal_registry(api_key: str | None = None, timeout: int = 120) -> dict[str, Any]:
    """Fetch the BioPortal ontology count and acronyms with a minimal response payload."""
    api_key = api_key or os.environ.get("BIOPORTAL_API_KEY")
    if not api_key:
        raise RuntimeError("BIOPORTAL_API_KEY is required for BioPortal registry access")
    response = requests.get(
        BIOPORTAL_ONTOLOGIES_URL,
        params={
            "include": "acronym,name",
            "display_context": "false",
            "display_links": "false",
            "include_views": "false",
        },
        headers={"Authorization": f"apikey token={api_key}"},
        timeout=timeout,
    )
    response.raise_for_status()
    ontologies = response.json()
    acronyms = sorted({ontology.get("acronym", "").upper() for ontology in ontologies if ontology.get("acronym")})
    return {
        "source_name": "bioportal",
        "count": len(ontologies),
        "prefixes": acronyms,
        "sample": ontologies[:20],
    }


def fetch_obo_foundry_registry(timeout: int = 120) -> dict[str, Any]:
    """Fetch the OBO Foundry registry prefix list from the official GitHub contents API."""
    response = requests.get(OBO_FOUNDRY_CONTENTS_URL, timeout=timeout)
    response.raise_for_status()
    entries = response.json()
    stems = sorted({entry["name"][:-3].upper() for entry in entries if entry.get("name", "").endswith(".md")})
    return {
        "source_name": "obo_foundry_registry",
        "count": len(stems),
        "prefixes": stems,
    }


def fetch_semsql_registry(timeout: int = 120) -> dict[str, Any]:
    """Fetch the semantic-sql ontology registry prefix list from the maintained YAML."""
    response = requests.get(SEMSQL_REGISTRY_RAW_URL, timeout=timeout)
    response.raise_for_status()
    payload = yaml.safe_load(response.text)
    ontologies = payload.get("ontologies", {})
    prefixes = sorted(ontologies)
    return {
        "source_name": "semantic_sql_registry",
        "count": len(prefixes),
        "prefixes": prefixes,
    }


def summarize_registry_differences(
    ols_overall: dict[str, Any],
    ols_embeddings_corpus: dict[str, Any],
    obo_foundry_registry: dict[str, Any],
    bioportal_registry: dict[str, Any] | None = None,
    semsql_registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a compact comparison summary across registry sources."""
    summary: dict[str, Any] = {
        "ols_overall_count": ols_overall["count"],
        "ols_embeddings_corpus_count": ols_embeddings_corpus["count"],
        "ols_overall_not_in_embeddings": sorted(set(ols_overall["prefixes"]) - set(ols_embeddings_corpus["prefixes"])),
        "ols_embeddings_not_in_ols_overall": sorted(set(ols_embeddings_corpus["prefixes"]) - set(ols_overall["prefixes"])),
        "obo_missing_from_ols_embeddings": sorted(
            set(obo_foundry_registry["prefixes"]) - set(ols_embeddings_corpus["prefixes"])
        ),
    }
    if bioportal_registry:
        summary["bioportal_count"] = bioportal_registry["count"]
    if semsql_registry:
        summary["semantic_sql_count"] = semsql_registry["count"]
    return summary
