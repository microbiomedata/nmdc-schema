# Ontology alignment via OLS4 embeddings + LinkML-side comparison
#
# Prerequisites:
#   poetry install --with dev,deps
#
# For OLS4 targets: no API key needed (public endpoint)
# For linkml-store targets: OPENAI_API_KEY and optionally BIOPORTAL_API_KEY (loaded from local/.env)
#
# Quick start:
#   make ols4-embeddings-postprocess   # enrich committed baseline (no API calls)
#   make ols4-embeddings-smoke         # small OBI-only test (~30 queries)
#   make ols4-embeddings-search        # full exhaustive run (~19 min)
#   make alignment-enrich              # schema-aware enrichment (no API calls)
#   make alignment-review              # review shortlist from enriched results
#   make alignment-gap-report          # property-like and source coverage gaps
#   make alignment-linkml-store-smoke  # small OBI test via linkml-store (needs OPENAI_API_KEY)
#   make alignment-clean               # remove all generated output from local/

# Committed baseline results (regenerate with ols4-embeddings-search, then copy)
OLS4_BASELINE = assets/ontology_alignment/ols4_embeddings_results.tsv
# Fresh search results go to local/ (gitignored)
OLS4_RESULTS = local/ols4_embeddings_results.tsv
OLS4_ENRICHED = local/ols4_embeddings_enriched.tsv
OLS4_SUMMARY = local/ols4_embeddings_summary.json

ALIGNMENT_ENRICHED = local/linkml_embeddings_alignment_enriched.tsv
ALIGNMENT_SUMMARY = local/linkml_embeddings_alignment_summary.json
ALIGNMENT_REVIEW = local/linkml_alignment_review.tsv
ALIGNMENT_GAP = local/linkml_alignment_gap_report.json

.PHONY: ols4-embeddings-search ols4-embeddings-smoke ols4-embeddings-postprocess
.PHONY: ols4-embeddings-postprocess-obi ols4-embeddings-postprocess-slots
.PHONY: ols4-embeddings-clean ols4-embeddings-update-baseline
.PHONY: alignment-enrich alignment-enrich-obi alignment-enrich-slots
.PHONY: alignment-review alignment-gap-report alignment-clean
.PHONY: alignment-linkml-store-smoke alignment-linkml-store-obi alignment-linkml-store-bioportal

# ---------- OLS4 retrieval ----------

# Full exhaustive search: all element types, full OLS4 corpus
# ~2,300 queries x 0.5s = ~19 min. Writes to local/ (gitignored).
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

# Update the committed baseline from a fresh search run
ols4-embeddings-update-baseline: $(OLS4_RESULTS)
	cp $(OLS4_RESULTS) $(OLS4_BASELINE)
	@echo "Baseline updated. Review the diff and commit if appropriate."

# ---------- OLS4 post-processing ----------

# Enrich results with schema context and lexical diagnostics (no API calls).
# Uses local results if available, falls back to committed baseline.
ols4-embeddings-postprocess:
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		-o $(OLS4_ENRICHED) \
		--summary-json $(OLS4_SUMMARY)

# Post-process filtered to OBI only
ols4-embeddings-postprocess-obi:
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--allowed-ontologies OBI \
		-o local/ols4_embeddings_obi_enriched.tsv \
		--summary-json local/ols4_embeddings_obi_summary.json

# Post-process filtered to slots only (useful for property alignment analysis)
ols4-embeddings-postprocess-slots:
	$(RUN) python src/scripts/ols4_embeddings_postprocess.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--subject-categories slot \
		-o local/ols4_embeddings_slots_enriched.tsv \
		--summary-json local/ols4_embeddings_slots_summary.json

# ---------- Schema-aware enrichment (uses linkml_embeddings_alignment_prototype.py) ----------

alignment-enrich:
	$(RUN) python src/scripts/linkml_embeddings_alignment_prototype.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		-o $(ALIGNMENT_ENRICHED) \
		--summary-json $(ALIGNMENT_SUMMARY)

alignment-enrich-obi:
	$(RUN) python src/scripts/linkml_embeddings_alignment_prototype.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--allowed-ontologies OBI \
		-o local/linkml_embeddings_alignment_obi.tsv \
		--summary-json local/linkml_embeddings_alignment_obi_summary.json

alignment-enrich-slots:
	$(RUN) python src/scripts/linkml_embeddings_alignment_prototype.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--semantic-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--subject-categories slot \
		-o local/linkml_embeddings_alignment_slots.tsv \
		--summary-json local/linkml_embeddings_alignment_slots_summary.json

# ---------- Review shortlist ----------

# Runs alignment-enrich first if the enriched file doesn't exist.
alignment-review:
	@test -f $(ALIGNMENT_ENRICHED) || $(MAKE) alignment-enrich
	$(RUN) python src/scripts/linkml_alignment_review.py \
		--enriched-results $(ALIGNMENT_ENRICHED) \
		-o $(ALIGNMENT_REVIEW) \
		--summary-json local/linkml_alignment_review_summary.json

# ---------- Gap report ----------

alignment-gap-report:
	$(RUN) python src/scripts/linkml_alignment_gap_report.py \
		--schema $(SOURCE_SCHEMA_PATH) \
		--baseline-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--summary-json $(ALIGNMENT_GAP)

# ---------- LinkML-store local retrieval ----------

# Smoke test: OBI via oaklib, 5 subjects (needs OPENAI_API_KEY)
alignment-linkml-store-smoke:
	$(RUN) python src/scripts/linkml_store_embeddings_search.py \
		--ols4-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--ontology-prefix OBI \
		--max-subjects 5 \
		--max-ontology-terms 500 \
		--top-k 10 \
		-o local/linkml_store_smoke.tsv \
		--summary-json local/linkml_store_smoke_summary.json

# Full OBI comparison via oaklib (all baseline subjects with OBI hits)
alignment-linkml-store-obi:
	$(RUN) python src/scripts/linkml_store_embeddings_search.py \
		--ols4-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--ontology-prefix OBI \
		--all-baseline-subjects \
		--top-k 20 \
		-o local/linkml_store_embeddings_obi.tsv \
		--summary-json local/linkml_store_embeddings_obi_summary.json \
		--enriched-output local/linkml_store_embeddings_obi_enriched.tsv \
		--enriched-summary-json local/linkml_store_embeddings_obi_enriched_summary.json

# BioPortal-backed retrieval (needs OPENAI_API_KEY + BIOPORTAL_API_KEY)
alignment-linkml-store-bioportal:
	$(RUN) python src/scripts/linkml_store_embeddings_search.py \
		--ols4-results $(if $(wildcard $(OLS4_RESULTS)),$(OLS4_RESULTS),$(OLS4_BASELINE)) \
		--corpus-source bioportal \
		--bioportal-acronyms OBI \
		--bioportal-exclude-imports \
		--all-baseline-subjects \
		--top-k 20 \
		-o local/linkml_store_bioportal_obi.tsv \
		--summary-json local/linkml_store_bioportal_obi_summary.json \
		--enriched-output local/linkml_store_bioportal_obi_enriched.tsv \
		--enriched-summary-json local/linkml_store_bioportal_obi_enriched_summary.json

# ---------- Cleanup ----------

ols4-embeddings-clean:
	rm -f local/ols4_embeddings_*.tsv local/ols4_embeddings_*.json

alignment-clean: ols4-embeddings-clean
	rm -f local/linkml_embeddings_alignment_*.tsv local/linkml_embeddings_alignment_*.json
	rm -f local/linkml_alignment_*.tsv local/linkml_alignment_*.json
	rm -f local/linkml_store_*.tsv local/linkml_store_*.json
