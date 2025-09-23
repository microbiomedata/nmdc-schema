# Unit Analysis Makefile
# 
# This Makefile demonstrates the complete schema-only workflow for generating
# storage_units annotations without needing MongoDB data.

.PHONY: all clean rebuild help validate-production mongodb-analysis

# Default target - complete workflow
all: schema.tsv input.tsv detailed.tsv single.txt multi.txt

# Clean generated files
clean:
	rm -f schema.tsv
	rm -f input.tsv
	rm -f detailed.tsv
	rm -f single.txt
	rm -f multi.txt
	rm -f mongodb-slots-to-units_analyzed.csv

# Clean and rebuild everything
rebuild: clean all

# Extract preferred_unit annotations from schema
schema.tsv: ../nmdc_schema/nmdc_materialized_patterns.yaml analyze.py
	python analyze.py --schema-file $< --output $@

# Generate input for process.py from schema data only
input.tsv detailed.tsv: schema.tsv extract.py
	python extract.py --input $< --output input.tsv --detailed detailed.tsv

# Process the schema input to generate yq commands
single.txt multi.txt: input.tsv process.py
	python process.py --input $< --output-dir .


# Production data validation (uses MongoDB YAML dump)
# Set SCHEMA_FILE to control which schema version to validate against:
# ENV=dev (default): ../nmdc_schema/nmdc_materialized_patterns.yaml (current development schema)
# ENV=prod: ../local/nmdc_schema_last_release.yaml (latest release schema)
SCHEMA_FILE ?= $(if $(filter prod,$(ENV)),../local/nmdc_schema_last_release.yaml,../nmdc_schema/nmdc_materialized_patterns.yaml)

production_units_validation.tsv: ../local/mongo_via_api_as_unvalidated_nmdc_database.yaml validate_production_units.py
	python validate_production_units.py --input $< --output $@ --schema-file $(SCHEMA_FILE)

validate-production: production_units_validation.tsv
	@echo "Production units validation complete"
	@echo "Note: Requires MongoDB dump from: make local/mongo_via_api_as_unvalidated_nmdc_database.yaml"

# Legacy MongoDB workflow (requires external production data)
mongodb-slots-to-units_analyzed.csv: mongodb-slots-to-units.csv analyze_units.py
	python analyze_units.py --input $< --output $@

mongodb-analysis: mongodb-slots-to-units_analyzed.csv
	@echo "MongoDB unit validation analysis complete"
	@echo "Note: This requires mongodb-slots-to-units.csv from production SPARQL query"


# Help target
help:
	@echo "Unit Analysis Makefile - Schema-Only Workflow"
	@echo ""
	@echo "Targets:"
	@echo "  all                    - Run complete workflow (default)"
	@echo "  rebuild               - Clean then build everything"
	@echo "  validate-production   - Validate production data against storage_units constraints"
	@echo "  mongodb-analysis      - Legacy MongoDB unit validation (requires external data)"
	@echo "  clean                 - Remove generated files"
	@echo "  help                  - Show this help"
	@echo ""
	@echo "Environment Variables:"
	@echo "  ENV=dev (default)     - Use current development schema"
	@echo "  ENV=prod              - Use latest release schema"
	@echo ""
	@echo "Examples:"
	@echo "  make validate-production                    # Use dev schema"
	@echo "  make validate-production ENV=prod           # Use release schema"