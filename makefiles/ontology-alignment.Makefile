# Ontology alignment via OLS4 embeddings search and post-processing
#
# Prerequisites:
#   poetry install --with dev,deps
#
# No API key needed — the OLS4 embeddings endpoint is public.
#
# Quick start:
#   make ols4-embeddings-postprocess   # enrich committed baseline (no API calls)
#   make ols4-embeddings-smoke         # small OBI-only test (~30 queries)
#   make ols4-embeddings-search        # full exhaustive run (~19 min)

OLS4_RESULTS = src/scripts/ols4_embeddings_results.tsv
OLS4_ENRICHED = local/ols4_embeddings_enriched.tsv
OLS4_SUMMARY = local/ols4_embeddings_summary.json

.PHONY: ols4-embeddings-search ols4-embeddings-smoke ols4-embeddings-postprocess
.PHONY: ols4-embeddings-postprocess-obi ols4-embeddings-postprocess-slots

# ---------- OLS4 retrieval ----------

# Full exhaustive search: all element types, full OLS4 corpus
# ~2,300 queries x 0.5s = ~19 min. Overwrites committed results TSV.
ols4-embeddings-search:
	$(RUN) python src/scripts/ols4_embeddings_search.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--element-types classes,slots,enums,pvs \
		--rows 5 \
		-o $(OLS4_RESULTS)

# Smoke test: classes only, OBI only (~60 queries, ~30s)
ols4-embeddings-smoke:
	$(RUN) python src/scripts/ols4_embeddings_search.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--element-types classes \
		--ontology obi \
		--rows 3 \
		-o local/ols4_embeddings_smoke_obi.tsv -v

# ---------- OLS4 post-processing ----------

# Enrich full results with schema context and lexical diagnostics (no API calls)
ols4-embeddings-postprocess: $(OLS4_RESULTS)
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(OLS4_RESULTS) \
		-o $(OLS4_ENRICHED) \
		--summary-json $(OLS4_SUMMARY)

# Post-process filtered to OBI only
ols4-embeddings-postprocess-obi: $(OLS4_RESULTS)
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(OLS4_RESULTS) \
		--allowed-ontologies OBI \
		-o local/ols4_embeddings_obi_enriched.tsv \
		--summary-json local/ols4_embeddings_obi_summary.json

# Post-process filtered to slots only (useful for property alignment analysis)
ols4-embeddings-postprocess-slots: $(OLS4_RESULTS)
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(OLS4_RESULTS) \
		--subject-categories slot \
		-o local/ols4_embeddings_slots_enriched.tsv \
		--summary-json local/ols4_embeddings_slots_summary.json
