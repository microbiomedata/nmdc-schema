# OLS4 Embeddings Search for nmdc-schema Ontology Alignment

This document describes how to use the OLS4 embeddings search pipeline to
discover ontology term candidates for nmdc-schema elements (classes, slots,
enums, and permissible values).

## Background

[OLS4](https://www.ebi.ac.uk/ols4/) hosts ~276 ontologies and provides an
LLM embeddings search endpoint (`/api/v2/classes/llm_search`) using the
`llama-embed-nemotron-8b_pca512` model. This pipeline queries that endpoint
for every schema element and produces SSSOM-style TSV output, then enriches
results with schema-aware diagnostics.

**No API key is needed.** The OLS4 embeddings API is public. The only
constraint is courtesy rate-limiting (0.5s delay between requests by default).

## Quick start

```bash
# Enrich the committed baseline results (instant, no API calls)
make ols4-embeddings-postprocess

# Run a smoke test against OBI only (~30s)
make ols4-embeddings-smoke

# Re-run the full exhaustive search (~19 min)
make ols4-embeddings-search
```

## Scripts

### `src/scripts/ols4_embeddings_search.py`

Iterates schema elements, queries OLS4, writes raw SSSOM-style TSV.

```bash
poetry run python src/scripts/ols4_embeddings_search.py --help
```

Key options:

| Option | Default | Description |
|--------|---------|-------------|
| `--schema` | `src/schema/nmdc.yaml` | Schema to iterate |
| `--element-types` | `classes,slots,enums,pvs` | Which element types to search |
| `--ontology` | (all) | Restrict to one ontology (e.g. `obi`, `envo`) |
| `--rows` | 5 | Results per query |
| `--delay` | 0.5 | Seconds between API requests |
| `--skip-mapped` | off | Skip elements that already have mappings |
| `-o` | `ols4_embeddings_results.tsv` | Output file |

**Query construction:** CamelCase names are expanded to spaces, underscores
replaced. If the element has a description, it's truncated to 200 chars and
appended after a colon: `"Biosample: A material sample..."`.

### `src/scripts/ols4_embeddings_postprocess.py`

Enriches raw search results with schema context and lexical diagnostics.

```bash
poetry run python src/scripts/ols4_embeddings_postprocess.py \
  --semantic-results src/scripts/ols4_embeddings_results.tsv
```

Key options:

| Option | Default | Description |
|--------|---------|-------------|
| `--semantic-threshold` | 0.90 | Confidence threshold for "strong semantic" |
| `--lexical-threshold` | 0.45 | Score below which lexical similarity is "weak" |
| `--allowed-ontologies` | (all) | Comma-separated prefixes to keep (e.g. `OBI,ENVO`) |
| `--excluded-ontologies` | (none) | Comma-separated prefixes to exclude |
| `--subject-categories` | (all) | Filter to specific categories: `class,slot,enum,permissible_value` |
| `--resolve-ols-metadata` | off | Make additional OLS4 API calls to distinguish classes from properties |

**Outputs** (in `local/`, gitignored):
- Enriched TSV with 34 columns including lexical profile, structural analysis, and bucket classification
- Summary JSON with counts by bucket, source, match type

## Interpreting results

### Semantic vs. lexical classification

Each result row is classified into a 2x2 matrix:

| | Strong lexical (>= 0.45) | Weak lexical (< 0.45) |
|---|---|---|
| **Strong semantic (>= 0.90)** | `strong_semantic_strong_lexical` — expected matches | `strong_semantic_weak_lexical` — novel candidates |
| **Weak semantic (< 0.90)** | `weak_semantic_strong_lexical` — name overlap, low confidence | `weak_semantic_weak_lexical` — unlikely matches |

The `strong_semantic_weak_lexical` bucket is the most interesting for
discovery — these are cases where the embedding model sees semantic
similarity despite different labels. However, **many of these are noise**
for short/generic PV labels (e.g. "east" matching species names, "wood"
matching tree species). See [#2917](https://github.com/microbiomedata/nmdc-schema/issues/2917) for filtering improvements.

### Structural support

The post-processor checks whether a match is structurally plausible given
the NMDC element type:

- **class -> class**: always supported
- **slot -> property**: supported if the slot has a scalar range
  (`property_like`), or if there's ontology source overlap
- **slot -> class**: supported if the slot's range is an enum or class
  (`class_filler`), or if there's ontology source overlap. Scalar-range
  slots with no source overlap get `slot_class_scalar_mismatch`.
- **PV -> class**: supported if there's ontology source overlap with
  existing mappings or owner mappings
- **enum -> class**: supported if source overlap with existing mappings

### Key columns in the enriched TSV

| Column | Description |
|--------|-------------|
| `confidence` | OLS4 embedding similarity score (0-1) |
| `lexical_score` | Max of token Jaccard, SequenceMatcher ratio, containment, exact/normalized match |
| `semantic_vs_lexical` | 2x2 bucket classification |
| `structural_bucket` | Refined classification incorporating structural plausibility |
| `structural_fit` | Boolean: is this match structurally plausible? |
| `structural_reason` | Why (or why not): `slot_class_range_fit`, `slot_class_scalar_mismatch`, etc. |
| `schema_expected_alignment_type` | `class_filler` or `property_like` |
| `existing_mappings` | Mappings already declared in the schema for this element |

## OLS4 API reference

The OLS4 LLM search endpoint is:

```
GET https://www.ebi.ac.uk/ols4/api/v2/classes/llm_search
    ?q=<query text>
    &model=llama-embed-nemotron-8b_pca512
    &rows=<number of results>
```

Scoped to a specific ontology:

```
GET https://www.ebi.ac.uk/ols4/api/v2/ontologies/{ontology_id}/classes/llm_search
    ?q=<query text>
    &model=llama-embed-nemotron-8b_pca512
    &rows=<number of results>
```

- **No authentication** required
- Returns JSON with an `elements` array, each element having `curie`, `label`,
  `ontologyId`, `score`, `iri`, etc.
- The embeddings corpus covers **210 of 276** OLS4 ontologies
- Dominant sources in results: SNOMED, NCIT, NCBITaxon, EFO, ENVO

### Coverage relative to nmdc-schema

Of the ~31 ontology prefixes used in nmdc-schema, only 3 are missing from the
OLS4 embeddings corpus:

- **MISO** (1 reference in schema) — BioPortal-only
- **FMA** (declared but unused) — see [#2920](https://github.com/microbiomedata/nmdc-schema/issues/2920)
- **gtpo** (placeholder with `example.org` URI)

All heavily-used prefixes (OBI, CHEBI, MS, NCIT, ENVO, GO, NCBITaxon) are covered.

## Current results summary

The committed baseline (`src/scripts/ols4_embeddings_results.tsv`) contains:
- **45,940 rows** from **2,298 schema elements** across 210 ontologies
- **2,284 rows** with confidence > 0.90
- **1,959** strong semantic + strong lexical
- **325** strong semantic + weak lexical (novel candidates)
- Only **2** of those 325 are structurally supported (both for the `model` slot)

## Related issues

- [#2907](https://github.com/microbiomedata/nmdc-schema/issues/2907) — Use OLS4 embeddings search to discover ontology mappings
- [#2906](https://github.com/microbiomedata/nmdc-schema/issues/2906) — Audit direct PROV and OBI usage
- [#2912](https://github.com/microbiomedata/nmdc-schema/issues/2912) — Ground MS/chromatography enums in OBI
- [#2913](https://github.com/microbiomedata/nmdc-schema/issues/2913) — Use OWL axiom decomposition to refine matches
- [#2917](https://github.com/microbiomedata/nmdc-schema/issues/2917) — Filter short/generic PV labels
- [#2918](https://github.com/microbiomedata/nmdc-schema/issues/2918) — Add property-oriented retrieval
