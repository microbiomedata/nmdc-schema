
# project.Makefile — Project-specific targets
#
# MIxS pipeline targets are in makefiles/mixs.Makefile
# Migrator targets are in makefiles/migrators.Makefile

SCHEMA_NAME = nmdc_schema
SOURCE_SCHEMA_PATH = src/schema/nmdc.yaml
LATEST_RELEASE_TAG_FILE := local/latest_release_tag.txt

PLANTUML_JAR = local/plantuml-lgpl-1.2024.3.jar


##### Ontology registry counts #####
# On-demand target — fetches from external APIs (OLS, OBO Foundry, semantic-sql).
# BioPortal requires BIOPORTAL_API_KEY in the environment; skipped by default.
# Outputs go to local/ (gitignored).

ONTOLOGY_REGISTRY_JSON := local/ontology_registry_counts.json
ONTOLOGY_REGISTRY_TSV := local/ontology_registry_prefixes.tsv

.PHONY: ontology-registry-counts
ontology-registry-counts: $(ONTOLOGY_REGISTRY_JSON)

$(ONTOLOGY_REGISTRY_JSON):
	$(RUN) python src/scripts/ontology_registry_counts.py \
		--skip-bioportal \
		--output-json $(ONTOLOGY_REGISTRY_JSON) \
		--output-prefixes-tsv $(ONTOLOGY_REGISTRY_TSV)


##### Rules related to grabbing the current schema release from Github #####

REPO  := microbiomedata/nmdc-schema
FILE  := nmdc_schema/nmdc_materialized_patterns.yaml
LATEST_TAG_SCHEMA_FILE   := local/nmdc_schema_last_release.yaml
# -------------------------------------------------

# Get the tag that belongs to the latest (non-prerelease) GitHub release.
#  - ‘!=’ executes the shell command only once, when the Makefile is read.
LATEST_TAG = $(shell curl -fsSL https://api.github.com/repos/$(REPO)/releases/latest | jq -r '.tag_name')

# Build the raw.githubusercontent.com URL
LATEST_TAG_SCHEMA_URL := https://raw.githubusercontent.com/$(REPO)/$(LATEST_TAG)/$(FILE)

.PHONY: $(LATEST_TAG_SCHEMA_FILE)

# Rule to fetch the schema file if local/nmdc_schema_last_release.yaml does not exist OR if there is a new release 
$(LATEST_TAG_SCHEMA_FILE): $(LATEST_RELEASE_TAG_FILE)
	@echo "Checking for schema updates..."
	@if [ ! -f $@ ]; then \
		echo "Schema file does not exist. Creating it..."; \
		curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $@; \
		echo "$(LATEST_TAG)" > $(LATEST_RELEASE_TAG_FILE); \
	elif [ "$$(cat $(LATEST_RELEASE_TAG_FILE))" != "$(LATEST_TAG)" ]; then \
		echo "New release detected ($(LATEST_TAG)). Downloading schema..."; \
		curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $@; \
		echo "$(LATEST_TAG)" > $(LATEST_RELEASE_TAG_FILE); \
	else \
		echo "Local copy of schema is already up to date with release $(LATEST_TAG)."; \
	fi

# Rule to store the latest release tag locally
$(LATEST_RELEASE_TAG_FILE):
	@if [ -f $(LATEST_TAG_SCHEMA_FILE) ]; then \
	echo "ERROR: Tag file is missing. Recreating release tag and removing local schema file..."; \
		rm -f $(LATEST_TAG_SCHEMA_FILE); \
	fi
	@echo "Creating release tag file..."
	@curl -fsSL $(LATEST_TAG_SCHEMA_URL) -o $(LATEST_TAG_SCHEMA_FILE)
	@echo "$(LATEST_TAG)" > $@
	@echo "Release tag file created with tag: $(LATEST_TAG)"


.PHONY: examples-clean

examples-clean:
	rm -rf examples/output

examples/output: nmdc_schema/nmdc_materialized_patterns.yaml
	mkdir -p $@
	$(RUN) linkml examples \
		--schema $< \
		--input-directory src/data/valid \
		--counter-example-input-directory src/data/invalid \
		--output-directory $@ > $@/README.md

local/usage_template.tsv: nmdc_schema/nmdc_materialized_patterns.yaml # replaces local/usage_template.tsv target
	mkdir -p $(@D) # create parent directory
	$(RUN) linkml2schemasheets-template \
		--source-path $< \
		--output-path $@ \
		--debug-report-path $@.debug.txt \
		--log-file $@.log.txt \
		--report-style exhaustive


examples/output/Biosample-exhaustive-pretty-sorted.yaml: src/data/valid/Database-interleaved.yaml
	$(RUN) pretty-sort-yaml \
		-i $< \
		-o $@

# this setup is required if you want to retreive any content or statistics from PyMongo
# pure-export doesn't require a PyMongo connection when run in the --skip-collection-check mode
#   1. . ~/sshproxy.sh -u {YOUR_NERSC_USERNAME}
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

pure-export-and-validate: local/mongo_as_nmdc_database_validation.log

local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date
	time $(RUN) migration-recursion \
		--input-path $(word 2,$^) \
		--schema-path $(word 1,$^) \
		--output-path $@

.PRECIOUS: local/mongo_as_nmdc_database_validation.log
local/mongo_as_nmdc_database_validation.log: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	date
	time $(RUN) linkml validate --schema $^ > $@

###########################################################
#
# MIGRATOR TEST COMMANDS VIA THE API. COMMANDS ARE IN ORDER
#
###########################################################

# Define API URLs for different environments
API_PROD_URL = https://api.microbiomedata.org
API_DEV_URL = https://api-dev.microbiomedata.org

# Dynamically set the API url based on the ENV variable
API_URL = $(if $(filter dev,$(ENV)),$(API_DEV_URL),$(API_PROD_URL))

#### Target 1: Run selected collections with local/mongo_via_api_as_unvalidated_nmdc_database.yaml ####
DEFAULT_COLLECTIONS = biosample_set \
	calibration_set \
	collecting_biosamples_from_site_set \
	configuration_set \
	data_generation_set \
	data_object_set \
	field_research_site_set \
	functional_annotation_set \
	genome_feature_set \
	instrument_set \
	manifest_set \
	material_processing_set \
	processed_sample_set \
	storage_process_set \
	study_set \
	workflow_execution_set
local/mongo_via_api_as_unvalidated_nmdc_database.yaml: SELECTED_COLLECTIONS=
local/mongo_via_api_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--output-yaml $@ \
		--schema-source nmdc_schema/nmdc_materialized_patterns.yaml \
		$(if $(SELECTED_COLLECTIONS),$(foreach coll,$(SELECTED_COLLECTIONS),--selected-collections $(coll)),\
			$(foreach coll,$(DEFAULT_COLLECTIONS),--selected-collections $(coll))) \
        dump-from-api \
		--client-base-url "$(API_URL)" \
		--endpoint-prefix nmdcschema \
		--page-size 200000

#### Target 2: Run migrator with local/mongo_via_api_as_nmdc_database_after_migrator.yaml ####
local/mongo_via_api_as_nmdc_database_after_migrator.yaml: MIGRATOR=
local/mongo_via_api_as_nmdc_database_after_migrator.yaml: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_via_api_as_unvalidated_nmdc_database.yaml
	date
	time $(RUN) migration-recursion \
		--input-path $(word 2,$^) \
		--schema-path $(word 1,$^) \
		--output-path $@ \
		$(if $(MIGRATOR),--migrator-name $(MIGRATOR),)


#### Target 3: Validation with local/mongo_via_api_as_nmdc_database_validation.log ####
.PRECIOUS: local/mongo_via_api_as_nmdc_database_validation.log
local/mongo_via_api_as_nmdc_database_validation.log: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_via_api_as_nmdc_database_after_migrator.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml validate --schema $^ > $@

#### Combined Command ####
.PHONY: test-migrator-on-database
test-migrator-on-database: SELECTED_COLLECTIONS=  # Default empty, user can override
test-migrator-on-database: MIGRATOR=             # Default empty, user can override
test-migrator-on-database: ENV=prod              # Default to prod if not specified
test-migrator-on-database: local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
		local/mongo_via_api_as_nmdc_database_after_migrator.yaml \
		local/mongo_via_api_as_nmdc_database_validation.log
	@echo "Combined workflow executed successfully."

###########################################################
#
# END MIGRATOR TEST COMMANDS VIA THE API
#
###########################################################

## ALTERNATIVELY TO TEST WITH THE MONGODB:
local/mongo_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--output-yaml $@ \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections biosample_set \
		--selected-collections study_set \
		dump-from-database \
		--admin-db "admin" \
		--auth-mechanism "DEFAULT" \
		--env-file local/.env \
		--mongo-db-name nmdc \
		--mongo-host localhost \
		--mongo-port 27777 \
		--direct-connection


.PHONY: filtered-status
filtered-status:
	git status | grep -v 'project/' | grep -v 'nmdc_schema/.*yaml' | grep -v 'nmdc_schema/.*json' | \
		grep -v 'nmdc.py' | grep -v 'examples/output/' # | grep -v 'nmdc_materialized_patterns.py' |

local/biosample-slot-range-type-report.tsv: src/schema/nmdc.yaml
	$(RUN) python src/scripts/slot_range_type_reporter.py \
		--schema $< \
		--output $@ \
		--schema-class Biosample

## we can get a report of biosamples per study with the following
## may help predict how long it will take to run study-id-from-filename on a particular study
## will become unnecessary once aggregation queries are available in the napa nmdc-runtime API
local/biosamples-per-study.txt:
	$(RUN) python src/scripts/report_biosamples_per_study.py \
		--api-server api \
		--max-page-size 10000 > $@

## getting a report of GOLD study identifiers, which might have been used a Study ids in legacy (pre-Napa) data
local/gold-study-ids.json:
	curl -X 'GET' \
		--output $@ \
		'https://api.microbiomedata.org/nmdcschema/study_set?max_page_size=999&projection=id%2Cgold_study_identifiers' \
		-H 'accept: application/json'

local/nmdc-no-use-native-uris.owl.ttl: src/schema/nmdc.yaml
	$(RUN) linkml generate owl --no-use-native-uris $< > $@


local/nmdc_materialized.ttl: src/schema/nmdc.yaml
	$(RUN) python src/scripts/schema_view_relation_graph.py \
		--schema $< \
		--output $@

###

diagrams-clean:
	rm -rf assets/mermaid-erd* \
		assets/plantuml*

# requires java and the plantuml jar https://plantuml.com/download
#   https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-lgpl-1.2024.3.jar
# requires npm and https://www.npmjs.com/package/@mermaid-js/mermaid-cli
# requires inkscape
diagrams-all: diagrams-clean assets/plantuml.png assets/plantuml.pdf assets/mermaid-erd.pdf assets/mermaid-erd.png

#		--classes ChemicalConversionProcess \
#		--classes ChemicalEntity \
#		--classes ChromatographicSeparationProcess \
#		--classes DissolvingProcess \
#		--classes Extraction \
#		--classes FluidHandling \
#		--classes MassSpectrometry \
#		--classes MaterialProcessing \
#		--classes MetaboliteQuantification \
#		--classes PlannedProcess \
#		--classes PortionOfSubstance \
#		--classes Solution \
#		--classes SubstanceEntity

assets/plantuml.puml: src/schema/nmdc.yaml
	$(RUN) linkml generate plantuml \
		--classes ChemicalConversionProcess \
		--classes ChemicalEntity \
		--classes ChromatographicSeparationProcess \
		--classes DissolvingProcess \
		--classes Extraction \
		--classes MobilePhaseSegment \
		--classes PortionOfSubstance \
		$< > $@

assets/plantuml.svg: assets/plantuml.puml # https://plantuml.com/download
	java -jar $(PLANTUML_JAR) $< -tsvg

assets/plantuml.png: assets/plantuml.puml # https://plantuml.com/download
#	docker run \
#		-v plantuml_diagrams:/plantuml/in \
#		-v plantuml_images:/plantuml/out \
#		plantuml/plantuml render /plantuml/in/chemistry.puml -f png -o /plantuml/out/chemistry.png
	java -jar $(PLANTUML_JAR) $< -tpng

assets/plantuml.pdf: assets/plantuml.svg
	inkscape --export-filename=$@ $<

assets/mermaid-erd.mmd: src/schema/nmdc.yaml
	$(RUN) linkml generate erdiagram \
		--format mermaid \
		--classes ChemicalConversionProcess \
		--classes ChemicalEntity \
		--classes ChromatographicSeparationProcess \
		--classes DissolvingProcess \
		--classes Extraction \
		--classes MobilePhaseSegment \
		--classes PortionOfSubstance \
		$< > $@.tmp
	sed 's/language code/language_code/g' $@.tmp > $@
	rm -rf $@.tmp

assets/mermaid-erd.svg: assets/mermaid-erd.mmd
	mmdc -i $< -o $@

assets/mermaid-erd.pdf: assets/mermaid-erd.mmd
	mmdc -i $< -o $@

assets/mermaid-erd.png: assets/mermaid-erd.mmd
	mmdc -i $< -o $@

#assets/mermaid-erd.pdf: assets/mermaid-erd.svg # illegible
#	inkscape --export-filename=$@ $<

assets/check_examples_class_coverage.txt:
	$(RUN) python src/scripts/check_examples_class_coverage.py \
		--source_directory src/data/valid \
		--schema_file src/schema/nmdc.yaml > $@

assets/schema_pattern_linting.txt:
	$(RUN) python src/scripts/schema_pattern_linting.py \
 		--schema-file src/schema/nmdc.yaml > $@

assets/enum_pv_result.tsv: src/schema/nmdc.yaml assets/enum_pv_template.tsv
	$(RUN) linkml2sheets \
		--output $@ \
		--schema $< $(word 2,$^)

local/Database-interleaved-class-count.tsv: src/data/valid/Database-interleaved.yaml
	cat $< | grep ' type: ' | sed 's/.*type: //' | sort | uniq -c | awk '{ OFS="\t"; $$1=$$1; print $$0 }' > $@


local/class_instantiation_counts.tsv: local/usage_template.tsv local/Database-interleaved-class-count.tsv
	$(RUN) python src/scripts/class_instantiation_counts.py \
		--schemasheets-input $(word 1,$^) \
		--counts-input $(word 2,$^) \
		--output $@

.PHONY: generate-json-collections
generate-json-collections: src/data/valid/Database-interleaved.yaml
	$(RUN) python src/scripts/database_to_json_list_files.py \
		--yaml-input $< \
		--output-dir assets/jsons-for-mongodb

.PHONY: populate-mongodb-form-json-collections
populate-mongodb-form-json-collections: generate-json-collections
	src/scripts/json-dir-to-mongodb.sh # requires that the script's permissions have been set like: chmod +x src/scripts/json-dir-to-mongodb.sh

# ----	NMDC NCBI mapping process ---- #
assets/ncbi_mappings/ncbi_attribute_mappings.tsv:
	$(RUN) python src/scripts/ncbi_nmdc_exact_term_matching.py create-unmapped-ncbi-mapping-file \
		--tsv-output $@

assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv: assets/ncbi_mappings/ncbi_attribute_mappings.tsv
	$(RUN) python src/scripts/ncbi_nmdc_exact_term_matching.py exact-term-matching \
		--tsv-input $< \
		--tsv-output $@

	$(RUN) python src/scripts/ncbi_nmdc_exact_term_matching.py ignore-import-schema-slots $@
	

src/data/valid/Database-interleaved.yaml: src/schema/nmdc.yaml
	rm -f $@
	$(RUN) python src/scripts/interleave_yaml.py \
		--directory-path src/data/valid \
		--output-file $@ \
		--schema-file $<

.PHONY: interleave-yaml
interleave-yaml: src/data/valid/Database-interleaved.yaml

.PHONY: check-references
check-references:
	$(RUN) python src/scripts/check_references.py \
		--schema-file $(SOURCE_SCHEMA_PATH)

assets/mentions-of-ids-analysis.txt: src/schema/nmdc.yaml
	$(RUN) python src/scripts/analyze_mentions_of_ids.py \
		--schema-file $< 1> $@ 2> $@.log

assets/usages-report.txt: src/schema/nmdc.yaml
	$(RUN) python src/scripts/report_usages.py \
		--schema-file $< > $@


assets/element-scrutiny.tsv: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) python src/scripts/scrutinize_elements.py \
		--schema-file $< \
		--output-file assets/element-scrutiny.tsv
