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

SCHEMA_FILE ?= $(if $(filter prod,$(ENV)),../local/nmdc_schema_last_release.yaml,../nmdc_schema/nmdc_materialized_patterns.yaml)

# Report slots with units excuses (very fast: <1 second)
output/schema_units_excuses.tsv: $(SCHEMA_FILE)
	@mkdir -p output
	yq eval '(.slots // {}) | to_entries[] | select(.value.annotations.units_alignment_excuse) | .key + "	" + (.value.annotations.units_alignment_excuse.value // .value.annotations.units_alignment_excuse)' $< | sort > $@

# Extract user-friendly unit titles (very fast: <1 second)
output/user_friendly_units.tsv: $(SCHEMA_FILE)
	@mkdir -p output
	yq eval '.enums.UnitEnum.permissible_values | to_entries | map(select(.value | has("title"))) | .[] | .key + "	" + .value.title' $< > $@

# yq query targets (all fast: 1-3 seconds each)

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

# Fast target - comprehensive analysis pipeline (yq queries only)
fast: output/schema_qv_with_storage.txt output/schema_qv_without_storage.txt output/schema_qv_complete_table.txt output/schema_qv_storage_counts.tsv output/schema_units_excuses.tsv output/user_friendly_units.tsv

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
	@echo "  fast     - All fast targets (schema + testdata analysis)"
	@echo "  clean    - Remove all generated files"
	@echo "  clean-fast - Clean output/ (preserves slow-outputs/)"