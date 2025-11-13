
# ⚠️ WARNING: Do NOT commit any local edits to `project.Makefile`!
# The `project.Makefile` is a shared build and automation file for the entire project. 
# Any changes made for local testing or experimentation should **never** be committed to version control. 
# Committing edits may break CI/CD pipelines or disrupt other developers' workflows.
# If you want to make contributions or add commands that would be helpful for wider use, create an issue and PR. 


### Rules and variables used in different places in the makefile ###

RUN=poetry run

JENA_DIR=~/apache-jena/bin/

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)
LATEST_RELEASE_TAG_FILE := local/latest_release_tag.txt

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


.PHONY: examples-clean mixs-yaml-clean rdf-clean shuttle-clean

examples-clean:
	rm -rf examples/output

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified*yaml

rdf-clean:
	rm -rf \
		OmicsProcessing.rq \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_cuire_repaired.ttl \
		local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_nmdc_database_validation.log \
		local/mongo_as_unvalidated_nmdc_database.yaml

shuttle-clean:
	#rm -rf local/mixs_regen/mixs_subset_modified.yaml # triggers complete regeneration
	rm -rf local/mixs_regen/*.yaml
	rm -rf $@.bak
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_minus_1.yaml
	# Remove all readonly metaslot assertions (these should only be set by schema loader)
	# Schema-level: definition_uri, from_schema, imported_from, metamodel_version, source_file, source_file_date, source_file_size, generation_date
	# Element-level: owner, domain_of, is_usage_slot, usage_slot_name
	# Then apply ALL dematerialization transformations from SCHEMA_MATERIALIZATION_GUIDE.md:
	# Step 2: Simplify annotations in classes
	# Step 3: Simplify prefixes (ExpandedDict -> SimpleDict)
	# Step 4: Simplify settings (ExpandedDict -> SimpleDict)
	# Step 5: Simplify annotations in slots
	# Step 6: Remove redundant class names
	# Step 7: Remove redundant slot_usage names
	# Step 8: Remove redundant enum names
	# Step 9: Remove redundant permissible_values text
	# Step 10: Remove domain (except MixsCompliantData)
	# Step 11: Remove redundant slot names
	# Step 13: Remove redundant subset names
	# Additional: Remove redundant aliases when they duplicate title
	yq eval 'del(.source_file, .definition_uri, .imported_from, .metamodel_version, .source_file_date, .source_file_size, .generation_date) | \
		del(.. | select(has("from_schema")).from_schema) | \
		del(.. | select(has("owner")).owner) | \
		del(.. | select(has("domain_of")).domain_of) | \
		del(.. | select(has("is_usage_slot")).is_usage_slot) | \
		del(.. | select(has("usage_slot_name")).usage_slot_name) | \
		(.classes[] | select(has("annotations")).annotations) |= map_values(.value) | \
		.prefixes |= map_values(.prefix_reference) | \
		(.settings // {}) |= map_values(.setting_value) | \
		(.slots[] | select(has("annotations")).annotations) |= map_values(.value) | \
		del(.classes.[].name) | \
		del(.classes.[].slot_usage.[].name) | \
		del(.enums.[].name) | \
		del(.enums.[].permissible_values.[].text) | \
		del(.slots[] | select(.domain != "MixsCompliantData") | .domain) | \
		del(.slots.[].name) | \
		del(.subsets.[].name) | \
		del(.slots[] | select(.aliases and .title and (.aliases | length == 1) and .aliases[0] == .title) | .aliases)' \
		$(word 2,$^) > $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak

local/mixs_regen/mixs_subset.yaml: assets/import_mixs_slots_regardless.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

local/mixs_regen/mixs_subset_modified.yaml: local/mixs_regen/mixs_subset.yaml assets/yq-for-mixs_subset_modified.txt
	# switching to TextValue may not add any value. the other range changes do improve the structure of the data.
	# ironically changing back to strings for the submission-schema, data harmonizer, submission portal etc.
	# may switch source of truth to the MIxS 6.2.2 release candidate

	# First, apply global string replacements using yq (replacing sed)
	yq eval '(.. | select(. == "quantity value")) |= "QuantityValue" | \
		(.. | select(tag == "!!str" and . == "string")) |= "TextValue" | \
		(.. | select(tag == "!!str" and . == "text value")) |= "TextValue"' \
		$(word 1, $^) > $@

	# Then apply all slot-specific transformations from config file
	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: local/mixs_regen/mixs_subset_modified.yaml \
assets/other_mixs_yaml_files/cur_land_use_enum.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all \
		'select(fileIndex==0).enums.cur_land_use_enum = select(fileIndex==1).enums.cur_land_use_enum | select(fileIndex==0)' \
		$^ | cat > $@

local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml: local/mixs_regen/mixs_subset_modified_inj_land_use.yaml \
assets/other_mixs_yaml_files/TargetGeneEnum.yaml
	yq eval-all \
		'select(fileIndex==0).enums.TargetGeneEnum = select(fileIndex==1).enums.TargetGeneEnum | select(fileIndex==0)' \
		$^ | cat > $@
	yq -i '.slots.target_gene.range = "TargetGeneEnum"' $@


local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml: local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	# Inject all three environment triad tooltips in a single step
	yq eval-all '\
		select(fileIndex==0).slots.env_broad_scale.annotations.tooltip = select(fileIndex==1).slots.env_broad_scale.annotations.tooltip | \
		select(fileIndex==0).slots.env_local_scale.annotations.tooltip = select(fileIndex==1).slots.env_local_scale.annotations.tooltip | \
		select(fileIndex==0).slots.env_medium.annotations.tooltip = select(fileIndex==1).slots.env_medium.annotations.tooltip | \
		select(fileIndex==0)' \
		$^ | cat > $@

local/mixs_regen/mixs_minus_1.yaml: local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml \
assets/other_mixs_yaml_files/mixs_env_triad_field_slot.yaml
	yq eval-all \
		'select(fileIndex==0).slots.mixs_env_triad_field = select(fileIndex==1).slots.mixs_env_triad_field | select(fileIndex==0)' \
		$^ | cat > $@

examples/output: nmdc_schema/nmdc_materialized_patterns.yaml
	mkdir -p $@
	$(RUN) linkml run-examples \
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

###########################################################
# ADVANCED: Production Data Validation with RDF/SPARQL
###########################################################
#
# Purpose: Validate production MongoDB data against the schema using
#          semantic web tools (RDF, Jena, SPARQL)
#
# Requirements:
#   - 32GB+ RAM (MongoDB dumps are large)
#   - Java runtime (for Jena tools)
#   - Apache Jena TDB2 installed
#   - SSH tunnel to NERSC MongoDB
#
# Who needs this: Maintainers validating production data dumps
# Who doesn't: Contributors working on schema definitions
#
# Documentation: See docs/data-validation.md for detailed instructions
#
# Main targets:
#   make-rdf: Full RDF conversion and validation pipeline
#   pure-export-and-validate: Export and validate MongoDB data
#
###########################################################

# this setup is required if you want to retreive any content or statistics from PyMongo
# pure-export doesn't require a PyMongo connection when run in the --skip-collection-check mode
#   1. . ~/sshproxy.sh -u {YOUR_NERSC_USERNAME}
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

pure-export-and-validate: local/mongo_as_nmdc_database_validation.log

make-rdf: rdf-clean \
	local/mongo_as_nmdc_database_validation.log \
	local/mongo_as_nmdc_database_cuire_repaired.ttl \
	local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl # could omit rdf-clean. then this could build incrementally on top of pure-export-and-validate

# statistics of large collections as of 2024-05-17
#ns	size	count	avgObjSize	storageSize	totalIndexSize	totalSize	scaleFactor
#nmdc.functional_annotation_agg	2194573252	16167688	135	567922688	1772920832	2340843520	1
#nmdc.data_object_set	81218633	179620	452	24301568	29847552	54149120	1
#nmdc.biosample_set	10184792	8158	1248	2887680	1753088	4640768	1

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

local/mongo_as_nmdc_database.ttl: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	date # 681.99 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml convert --output $@ --schema $^
	mv $@ $@.tmp
	cat  assets/my_emsl_prefix.ttl $@.tmp  > $@
	rm -rf $@.tmp
	- export _JAVA_OPTIONS=-Djava.io.tmpdir=local ; $(JENA_DIR)/riot --validate $@ # < 1 minute
	date


# todo: still getting anyurl typed string statement objects in RDF. I added a workaround in anyuri-strings-to-iris
local/mongo_as_nmdc_database_cuire_repaired.ttl: local/mongo_as_nmdc_database.ttl
	date
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@
	- export _JAVA_OPTIONS=-Djava.io.tmpdir=local && $(JENA_DIR)/riot --validate $@ # < 1 minute
	date

.PHONY: migration-doctests migrator

# Runs all doctests defined within the migrator modules, adapters, and CLI scripts.
#
# To run in non-verbose mode:
# ```
# $ make migration-doctests DOCTEST_OPT=''
# ```
DOCTEST_OPT ?= -v
migration-doctests: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/partials/**/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/adapters/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/cli/*.py

# Generates a migrator skeleton for the specified schema versions.
# Note: `create-migrator` is a Poetry script registered in `pyproject.toml`.
migrator:
	$(RUN) create-migrator

# Runs a specific migrator against MongoDB
# Usage: make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 [ACTION=rollback|commit]
# The migrator now resides in: nmdc_schema/migrators/partials/migrator_from_11_9_1_to_11_10_0/
# MongoDB connection details are read from .env file or environment variables
MIGRATOR ?= migrator_from_11_9_1_to_11_10_0
ACTION ?=
.PHONY: run-migrator
run-migrator:
	@if [ -z "$(MIGRATOR)" ]; then \
		echo "Error: MIGRATOR parameter is required"; \
		echo "Usage: make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 [ACTION=rollback|commit]"; \
		echo "MongoDB connection details are read from .env file or environment variables"; \
		exit 1; \
	fi
	$(RUN) run-migrator $(MIGRATOR) $(if $(ACTION),$(ACTION))

.PHONY: filtered-status
filtered-status:
	git status | grep -v 'project/' | grep -v 'nmdc_schema/.*yaml' | grep -v 'nmdc_schema/.*json' | \
		grep -v 'nmdc.py' | grep -v 'examples/output/' # | grep -v 'nmdc_materialized_patterns.py' |

local/biosample-slot-range-type-report.tsv: src/schema/nmdc.yaml
	$(RUN) slot-range-type-reporter \
		--schema $< \
		--output $@ \
		--schema-class Biosample

## we can get a report of biosamples per study with the following
## may help predict how long it will take to run study-id-from-filename on a particular study
## will become unnecessary once aggregation queries are available in the napa nmdc-runtime API
local/biosamples-per-study.txt:
	$(RUN) report-biosamples-per-study \
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
	$(RUN) schema-view-relation-graph \
		--schema $< \
		--output $@

local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl: local/mongo_as_nmdc_database_cuire_repaired.ttl
	$(RUN) date-created-blank-node > local/date_created_blank_node.ttl
	cat $^ local/date_created_blank_node.ttl > $@
	rm local/date_created_blank_node.ttl

###

assets/check_examples_class_coverage.txt:
	$(RUN) check-examples-class-coverage \
		--source_directory src/data/valid \
		--schema_file src/schema/nmdc.yaml > $@

assets/schema_pattern_linting.txt:
	$(RUN) schema-pattern-linting \
 		--schema-file src/schema/nmdc.yaml > $@

assets/enum_pv_result.tsv: src/schema/nmdc.yaml assets/enum_pv_template.tsv
	$(RUN) linkml2sheets \
		--output $@ \
		--schema $< $(word 2,$^)

local/Database-interleaved-class-count.tsv: src/data/valid/Database-interleaved.yaml
	cat $< | grep ' type: ' | sed 's/.*type: //' | sort | uniq -c | awk '{ OFS="\t"; $$1=$$1; print $$0 }' > $@


local/class_instantiation_counts.tsv: local/usage_template.tsv local/Database-interleaved-class-count.tsv
	$(RUN) class-instantiation-counts \
		--schemasheets-input $(word 1,$^) \
		--counts-input $(word 2,$^) \
		--output $@

.PHONY: generate-json-collections
generate-json-collections: src/data/valid/Database-interleaved.yaml
	$(RUN) database-to-json-list-files \
		--yaml-input $< \
		--output-dir assets/jsons-for-mongodb

.PHONY: populate-mongodb-form-json-collections
populate-mongodb-form-json-collections: generate-json-collections
	src/scripts/json-dir-to-mongodb.sh # requires that the script's permissions have been set like: chmod +x src/scripts/json-dir-to-mongodb.sh

# ----	NMDC NCBI mapping process ---- #
assets/ncbi_mappings/ncbi_attribute_mappings.tsv:
	$(RUN) nmdc-ncbi-mapping create-unmapped-ncbi-mapping-file \
		--tsv-output $@

assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv: assets/ncbi_mappings/ncbi_attribute_mappings.tsv
	$(RUN) nmdc-ncbi-mapping exact-term-matching \
		--tsv-input $< \
		--tsv-output $@

	$(RUN) nmdc-ncbi-mapping ignore-import-schema-slots $@
	

src/data/valid/Database-interleaved-new.yaml: src/schema/nmdc.yaml
	$(RUN) interleave-yaml \
		--directory-path src/data/valid \
		--output-file $@ \
		--schema-file $<

assets/mentions-of-ids-analysis.txt: src/schema/nmdc.yaml
	$(RUN) analyze-mentions-of-ids \
		--schema-file $< 1> $@ 2> $@.log

assets/usages-report.txt: src/schema/nmdc.yaml
	$(RUN) report-usages \
		--schema-file $< > $@


assets/element-scrutiny.tsv: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN)  scrutinize-elements \
		--schema-file $< \
		--output-file assets/element-scrutiny.tsv

# EXPERIMENTAL
assets/partial-imports-graph.pdf: src/schema/nmdc.yaml
	$(RUN) python src/scripts/experimental/partial_imports_graph.py # needs networkx and plotly
