# LinkML-Store Embeddings Comparison for nmdc-schema

This document describes the LinkML-side retrieval pipeline that compares
local embeddings search (via oaklib + linkml-store) against the OLS4
embeddings baseline from [PR #2909](https://github.com/microbiomedata/nmdc-schema/pull/2909).

For the OLS4 baseline docs, see [ontology-alignment-ols4.md](ontology-alignment-ols4.md).

## Purpose

The OLS4 embeddings API searches against ~210 ontologies using a specific
embedding model (`llama-embed-nemotron-8b_pca512`). This pipeline provides
an **alternative retrieval path** that:

- Uses a different embedding model (`text-embedding-3-small` via OpenAI)
- Can search ontologies **not in OLS4** (e.g. METPO, or any BioPortal ontology)
- Lets you control which ontology corpus is searched
- Produces comparable SSSOM-style output for direct comparison with OLS4

## Prerequisites

```bash
poetry install --with dev,deps
```

**API keys** (set as environment variables):
- `OPENAI_API_KEY` — required for all linkml-store targets
- `BIOPORTAL_API_KEY` — required only for BioPortal corpus harvesting

Both can be sourced from `~/gitrepos/metpo/.env`.

**OLS4 baseline results:** This pipeline uses the OLS4 results TSV as its
query set (the list of NMDC schema elements to search). On the `2907` branch
this file is committed at `src/scripts/ols4_embeddings_results.tsv`. On the
`2908` branch, copy or symlink it:

```bash
cp path/to/ols4_embeddings_results.tsv local/ols4_embeddings_results.tsv
```

## Quick start

```bash
# Smoke test: OBI, 5 subjects (~30s, needs OPENAI_API_KEY)
make alignment-linkml-store-smoke

# Enrich OLS4 baseline with schema context (no API calls, no key needed)
make alignment-enrich

# Generate review shortlist from enriched results
make alignment-review

# Gap report: property-like slots and source coverage
make alignment-gap-report

# Full OBI comparison (all baseline subjects with OBI hits)
make alignment-linkml-store-obi

# BioPortal-backed OBI (needs both API keys)
make alignment-linkml-store-bioportal
```

## Scripts

### `linkml_store_embeddings_search.py` — local semantic retrieval

Harvests ontology terms via oaklib or BioPortal, embeds them locally with
linkml-store's `LLMIndexer`, and searches for NMDC schema elements.

```bash
poetry run python src/scripts/linkml_store_embeddings_search.py --help
```

Key options:

| Option | Default | Description |
|--------|---------|-------------|
| `--ols4-results` | `/tmp/ols4_embeddings_results.tsv` | OLS4 baseline TSV (used to derive query set) |
| `--corpus-source` | `oaklib` | `oaklib` or `bioportal` |
| `--ontology-prefix` | `OBI` | Ontology prefix for oaklib harvests |
| `--adapter-handle` | `sqlite:obo:obi` | oaklib adapter handle |
| `--bioportal-acronyms` | | Comma-separated BioPortal acronyms (e.g. `OBI,CHEMINF`) |
| `--bioportal-exclude-imports` | off | Drop imported classes from BioPortal harvest |
| `--restrict-to-baseline-source-hits` | on | Only query subjects that had OLS4 hits in the target ontology |
| `--all-baseline-subjects` | off | Query all subjects regardless of OLS4 hits |
| `--max-subjects` | (all) | Limit number of subjects queried |
| `--max-ontology-terms` | (all) | Limit ontology corpus size |
| `--top-k` | 20 | Results per query |
| `--embedding-model-name` | `text-embedding-3-small` | OpenAI embedding model |
| `--cache-db` | `local/linkml-store-embeddings.db` | DuckDB cache path |
| `--enriched-output` | | Optional: also write enriched TSV |
| `--enriched-summary-json` | | Optional: also write enriched summary |

**Cache behavior:** The DuckDB cache stores embeddings by collection name
(auto-derived from ontology prefix + model). Subsequent runs reuse cached
embeddings, so only the first run for a given ontology slice is slow.

### `linkml_embeddings_alignment_prototype.py` — schema-aware enrichment

Same enrichment logic as the OLS4 postprocessor, but with additional
`available_tooling()` reporting. Can enrich either OLS4 or linkml-store
results.

### `linkml_alignment_review.py` — review shortlist

Selects top-N rows with quotas per match type (`slot->class=15`,
`class->class=10`, `pv->class=15`, `enum->class=10`), max 3 per subject.
Prioritizes `strong_semantic_weak_lexical_structurally_supported` bucket.

### `linkml_alignment_gap_report.py` — coverage gap analysis

Quantifies:
- How many NMDC slots are `property_like` (302/851) vs `class_filler`
- Source concentration in the OLS4 baseline (SNOMED, NCIT, NCBITaxon dominate)
- Which subjects got no retrieval hits at all

## Comparing OLS4 vs linkml-store

The `linkml_store_embeddings_search.py` script includes built-in overlap
analysis. When `--ols4-results` is provided, the summary JSON includes an
`overlap_vs_ols4_by_source` section reporting per ontology:

- Subjects compared
- Subjects with any top-k overlap
- Subjects with top-1 overlap
- Mean exact overlap per subject

**Important:** Early comparison results (3/25 top-1 overlap for OBI)
predate the symmetric textualization fix (commit `98aabfab6`). Rerun before
drawing conclusions.

### Why results differ between backends

Even for the same ontology (e.g. OBI), results will differ because:

1. **Different embedding models** — `llama-embed-nemotron-8b_pca512` (OLS4) vs `text-embedding-3-small` (OpenAI)
2. **Different corpus content** — OLS4 indexes its own curated corpus; oaklib uses semsql SQLite; BioPortal has different term coverage and may include imported classes
3. **Different text representations** — OLS4 constructs its own embeddings from label+definition; linkml-store uses `compose_ontology_term_search_text()` which formats as `"label :: synonyms :: definition"`

Low overlap between backends is expected and does not indicate a bug.

## Current limitations

- **No property-oriented retrieval.** 302/851 NMDC slots are `property_like`
  (scalar range), but both backends only search for classes. Slots like
  `depth`, `latitude`, `pH` get structurally mismatched class hits.
  This is the most important gap.
- **Comparison results need rerun** after the symmetric textualization fix.
- **No METPO coverage.** METPO is not in OLS4 or BioPortal (stale build).
  This is the primary motivator for the local retrieval path long-term.

## Related issues

- [#2908](https://github.com/microbiomedata/nmdc-schema/issues/2908) — Evaluate LinkML ecosystem tools for embeddings-based ontology grounding
- [#2907](https://github.com/microbiomedata/nmdc-schema/issues/2907) — OLS4 embeddings search (baseline)
- [#2912](https://github.com/microbiomedata/nmdc-schema/issues/2912) — Ground MS/chromatography enums in OBI
- [#2913](https://github.com/microbiomedata/nmdc-schema/issues/2913) — OWL axiom decomposition for refinement
- [berkeleybop/metpo#364](https://github.com/berkeleybop/metpo/issues/364) — Evaluate OLS4+linkml-store for METPO
