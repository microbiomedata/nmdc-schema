# Unit Analysis Makefile
# 
# This Makefile demonstrates the complete schema-only workflow for generating
# storage_units annotations without needing MongoDB data.

.PHONY: all clean rebuild help mongodb-analysis

# Default target - complete workflow
all: schema.tsv input.tsv detailed.tsv single.txt multi.txt

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


# Legacy MongoDB workflow (requires external production data)
mongodb-slots-to-units_analyzed.csv: mongodb-slots-to-units.csv analyze_units.py
	python analyze_units.py --input $< --output $@

mongodb-analysis: mongodb-slots-to-units_analyzed.csv
	@echo "MongoDB unit validation analysis complete"
	@echo "Note: This requires mongodb-slots-to-units.csv from production SPARQL query"


# Clean generated files
clean:
	rm -f schema.tsv
	rm -f input.tsv
	rm -f detailed.tsv
	rm -f single.txt
	rm -f multi.txt
	rm -f mongodb-slots-to-units_analyzed.csv


# Help target
help:
	@echo "Unit Analysis Makefile - Schema-Only Workflow"
	@echo ""
	@echo "Targets:"
	@echo "  all                    - Run complete workflow (default)"
	@echo "  rebuild               - Clean then build everything"
	@echo "  mongodb-analysis      - Legacy MongoDB unit validation (requires external data)"
	@echo "  clean                 - Remove generated files"
	@echo "  help                  - Show this help"