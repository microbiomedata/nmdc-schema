# LinkML Embeddings Alignment Roadmap

This roadmap turns `#2910` into a layered prototype rather than a single retrieval experiment.

## Goals

- compare multiple retrieval surfaces instead of binding the workflow to OLS4
- use LinkML schema structure to rerank and prune candidates after retrieval
- make review artifacts small enough for manual curation
- preserve SSSOM-friendly outputs

## Architecture

### 1. Retrieval

- OLS4 embeddings search as the baseline candidate generator
- local vectorized ontology corpora as the non-OLS alternative
- possible future BioPortal-backed retrieval for broader non-OBO coverage
- explicit gap reporting so we do not confuse current backend coverage with actual semantic recall

### 2. Ontology access

- `oaklib` as the abstraction layer across backends
- semsql/SQLite backends when local graph-style querying is needed
- optional ROBOT extracts when we want smaller ontology slices

### 3. Schema-aware reranking

- split by NMDC subject type before review:
  - `class -> class`
  - `slot -> class`
  - `slot -> property`
  - `pv -> class`
- use schema-side signals for reranking:
  - slot range kind
  - slot owner context
  - mapping-source overlap
  - lexical strength

### 4. Review outputs

- enriched candidate TSV for bulk diagnostics
- shortlist review TSV for manual inspection
- summary JSON for counts by bucket, ontology, and match type

## Immediate implementation steps

1. Keep the existing OLS4 TSV as the baseline input.
2. Enrich it with schema-aware diagnostics and structural buckets.
3. Shortlist a small review set and fetch richer term metadata only for that subset.
4. Add `oaklib` and test local ontology access independently of OLS4.
5. Add a local embedding/index path so OLS4 is no longer the only retrieval backend.
6. Add explicit gap reporting for backend coverage and property-like slots.
7. Evaluate whether semsql-backed local databases improve closure and property inspection.
8. Add BioPortal or other non-OLS repository coverage when we want broader ontology families.

## What this patch adds

- schema-aware enrichment and structural bucketing
- a review-shortlist script that can fetch richer metadata only for shortlisted rows
- a cleaner separation between candidate generation, reranking, and review
- a local `oaklib + linkml-store` retrieval path so OLS4 is no longer the only semantic backend
- a gap-report script that makes class-only and backend-coverage limitations explicit

## Current gaps made explicit

- The current OLS4 baseline is class-oriented and does not cover `slot -> property` retrieval.
- In the current schema snapshot, `302 / 851` NMDC slots are `property_like`, so class-only retrieval is structurally incomplete.
- The current OLS4 baseline is heavily concentrated in sources such as `SNOMED`, `NCIT`, and `NCBITaxon`, which means OLS4-driven review is not the same thing as repository-complete review.
- The LinkML-side retrieval experiment uses `oaklib + linkml-store` over local ontology corpora, with BioPortal-backed corpus harvesting available (`make alignment-linkml-store-bioportal`).
- `semsql` is most likely to help after retrieval by expanding property, relationship, and neighborhood context around candidate classes.

## Open questions

- Which ontology families should be first-class allowlists for NMDC review?
- Do we want BioPortal runtime queries or locally mirrored non-OBO corpora?
- When should `slot -> property` become a first-class path rather than an optional extension?
