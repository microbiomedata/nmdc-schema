# Ontology Registry Counts

This note documents how to count ontologies and extract prefixes across the sources currently relevant to NMDC ontology-alignment work.

The important distinction is:

- `OLS overall`: the complete OLS4 ontology registry exposed by the public OLS4 API
- `OLS embeddings corpus`: the ontology prefixes actually represented in the current embeddings workflow output TSV

Those are not the same thing.

## Sources

- OLS overall: `https://www.ebi.ac.uk/ols4/api/ontologies?page=0&size=500`
- OLS embeddings corpus: `/tmp/ols4_embeddings_results.tsv` or another checked results TSV from the current workflow
- BioPortal: `https://data.bioontology.org/ontologies` with:
  - `include=acronym,name`
  - `display_context=false`
  - `display_links=false`
  - `include_views=false`
- OBO Foundry registry: `https://api.github.com/repos/OBOFoundry/OBOFoundry.github.io/contents/ontology`
- semantic-sql registry: `https://raw.githubusercontent.com/INCATools/semantic-sql/main/src/semsql/builder/registry/ontologies.yaml`

## Reproducible script

Run:

```bash
cd ~/gitrepos/nmdc-schema
export BIOPORTAL_API_KEY=your-key-here  # or load from your preferred secrets manager
poetry run python src/scripts/ontology_registry_counts.py \
  --ols-embeddings-results /tmp/ols4_embeddings_results.tsv \
  --output-json local/ontology_registry_counts.json \
  --output-prefixes-tsv local/ontology_registry_prefixes.tsv
```

This writes:

- `local/ontology_registry_counts.json`
- `local/ontology_registry_prefixes.tsv`

## Current observed counts

These values are expected to drift over time and should be regenerated:

- OLS overall: `276`
- OLS embeddings corpus: derived from the current TSV, not the OLS API
- BioPortal: `1476`
- OBO Foundry registry: `264`
- semantic-sql registry: `150`

## Caveats

- OBO Foundry registry presence is not the same thing as asserting full Foundry compliance.
- BioPortal counts depend on `include_views=false` if you want ontology counts rather than ontology-plus-view counts.
- OLS overall includes ontologies not represented in the current embeddings workflow.
- The current OLS embeddings corpus reflects the actual search space used by the current workflow, which is the more relevant denominator for retrieval comparisons.
