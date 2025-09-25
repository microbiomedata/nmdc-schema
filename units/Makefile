# Unit Analysis Makefile
# 
# This Makefile demonstrates the complete schema-only workflow for generating
# storage_units annotations without needing MongoDB data.

.PHONY: all clean rebuild help fast

# Default target - alias for fast (comprehensive analysis)
all: fast

# Clean generated files
clean:
	rm -rf output/*

# Clean and rebuild everything
rebuild: clean all

# Extract preferred_unit annotations from schema (fast: ~1-2 seconds)
output/schema_preferred_units.tsv: ../nmdc_schema/nmdc_materialized_patterns.yaml
	@mkdir -p output
	poetry run units-schema-extract --schema-file $< --output $@

# Convert preferred units to UCUM notation (fast: ~1-2 seconds)
output/schema_ucum_input.tsv output/schema_ucum_detailed.tsv: output/schema_preferred_units.tsv
	poetry run units-schema-convert --input $< --output output/schema_ucum_input.tsv --detailed output/schema_ucum_detailed.tsv

# Generate yq commands for storage_units annotations (fast: ~1-2 seconds)
output/yq_commands_single_unit.txt output/yq_commands_multi_unit.txt: output/schema_ucum_input.tsv
	poetry run units-schema-generate --input $< --output-dir output


# Production data validation (uses MongoDB YAML dump)
# ⚠️  SLOWEST TARGET: Processes 32,000+ QuantityValue instances from GB-sized MongoDB dump
# Expected time: Minutes to hours depending on dump size
# Set SCHEMA_FILE to control which schema version to validate against:
# ENV=dev (default): ../nmdc_schema/nmdc_materialized_patterns.yaml (current development schema)
# ENV=prod: ../local/nmdc_schema_last_release.yaml (latest release schema)
SCHEMA_FILE ?= $(if $(filter prod,$(ENV)),../local/nmdc_schema_last_release.yaml,../nmdc_schema/nmdc_materialized_patterns.yaml)

slow-outputs/production_validation_results.tsv: ../local/mongo_via_api_as_unvalidated_nmdc_database.yaml
	@mkdir -p slow-outputs
	poetry run units-production-validate --input $< --output $@ --schema-file $(SCHEMA_FILE)
	@echo "Note: Requires MongoDB dump from: make local/mongo_via_api_as_unvalidated_nmdc_database.yaml"


# Report slots with units excuses (very fast: <1 second)
output/schema_units_excuses.tsv: $(SCHEMA_FILE)
	@mkdir -p output
	yq eval '(.slots // {}) | to_entries[] | select(.value.annotations.units_alignment_excuse) | .key + "	" + (.value.annotations.units_alignment_excuse.value // .value.annotations.units_alignment_excuse)' $< | sort > $@

# Extract user-friendly unit titles (very fast: <1 second)
output/user_friendly_units.tsv: $(SCHEMA_FILE)
	@mkdir -p output
	yq eval '.enums.UnitEnum.permissible_values | to_entries | map(select(.value | has("title"))) | .[] | .key + "	" + .value.title' $< > $@

# Extract slot-to-storage-unit pairs (expands pipe-separated values)
output/schema_storage_units_expanded.tsv: $(SCHEMA_FILE)
	poetry run units-schema-extract-slot-unit-pairs --schema-file $< --output $@

# Legacy MongoDB workflow (requires external production data) (moderate: ~30 seconds)
output/mongodb_analysis_results.csv: semi-static-inputs/mongodb-slots-to-units.csv
	@mkdir -p output
	poetry run units-mongodb-analyze --input $< --output $@

# Legacy MongoDB unit validation analysis (uses production SPARQL query results)
# Note: Analyzes semi-static-inputs/mongodb-slots-to-units.csv from production RDF/SPARQL queries


# Python script targets - newly consolidated units analysis tools
# Validate UCUM compliance of units from test data (moderate: ~10-30 seconds)
output/ucum_validation_results.csv: output/testdata_quantity_values.tsv
	poetry run units-ucum-validate --input $< --output $@

# Check QuantityValue has_unit completeness (very fast: ~1-2 seconds)
output/testdata_has_unit_check.tsv: ../src/data/valid/Biosample-possibly-exhaustive.yaml
	poetry run units-testdata-check --file-path $< --output $@

# Extract QuantityValue structures from test data (very fast: ~1-2 seconds)
output/testdata_quantity_values.tsv: ../src/data/valid/Biosample-possibly-exhaustive.yaml
	@mkdir -p output
	poetry run units-testdata-extract --input $< --output $@

# yq query targets from STORAGE_UNITS_STATUS.md analysis (all fast: 1-3 seconds each)

# List QuantityValue slots WITH storage_units annotations
output/schema_qv_with_storage.txt: $(SCHEMA_FILE)
	@mkdir -p output
	yq '.slots | to_entries | map(select(.value.range == "QuantityValue" and .value.annotations.storage_units)) | .[].key' $< > $@

# List QuantityValue slots WITHOUT storage_units annotations  
output/schema_qv_without_storage.txt: $(SCHEMA_FILE)
	@mkdir -p output
	yq '.slots | to_entries | map(select(.value.range == "QuantityValue")) | .[] | .key + " | " + (.value.annotations.storage_units.value // "MISSING")' $< | grep "MISSING" > $@

# Complete table of all QuantityValue slots with storage_units status
output/schema_qv_complete_table.txt: $(SCHEMA_FILE)
	@mkdir -p output
	yq '.slots | to_entries | map(select(.value.range == "QuantityValue")) | .[] | .key + " | " + (.value.annotations.storage_units.value // "MISSING")' $< | sort > $@

# Count QuantityValue slots with storage_units (very fast: <1 second)
output/schema_qv_storage_counts.tsv: $(SCHEMA_FILE)
	@mkdir -p output
	@echo "metric	count" > $@
	@echo "qv_slots_with_storage_units	$$(yq '.slots | to_entries | map(select(.value.range == "QuantityValue" and .value.annotations.storage_units)) | length' $<)" >> $@
	@echo "qv_slots_without_storage_units	$$(yq '.slots | to_entries | map(select(.value.range == "QuantityValue")) | .[] | .key + " | " + (.value.annotations.storage_units.value // "MISSING")' $< | grep -c "MISSING")" >> $@
	@echo "qv_slots_total	$$(yq '.slots | to_entries | map(select(.value.range == "QuantityValue")) | length' $<)" >> $@

# Fast target - comprehensive analysis pipeline
fast: output/schema_preferred_units.tsv output/schema_ucum_input.tsv output/schema_ucum_detailed.tsv output/yq_commands_single_unit.txt output/yq_commands_multi_unit.txt output/testdata_quantity_values.tsv output/ucum_validation_results.csv output/schema_qv_with_storage.txt output/schema_qv_without_storage.txt output/schema_qv_complete_table.txt output/schema_qv_storage_counts.tsv output/testdata_has_unit_check.tsv output/schema_units_excuses.tsv output/user_friendly_units.tsv output/schema_storage_units_expanded.tsv

# Clean all output files (preserves slow-outputs/ directory)
clean-fast:
	find output -name '*.tsv' -delete
	find output -name '*.txt' -delete
	find output -name '*.csv' -delete

# Help target  
help:
	@echo "Unit Analysis Makefile"
	@echo ""
	@echo "Key Targets:"
	@echo "  all      - Alias for fast (comprehensive analysis)"
	@echo "  fast     - Comprehensive analysis except slow production validation"  
	@echo "  clean    - Remove all generated files"
	@echo "  clean-fast - Clean output/ (preserves slow-outputs/)"
	@echo ""
	@echo "Slow Targets:"
	@echo "  slow-outputs/production_validation_results.tsv - Production data validation"
	@echo ""
	@echo "Environment: ENV=dev|prod (controls schema version for production validation)"