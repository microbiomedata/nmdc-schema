###########################################################
# Production Data Validation with RDF/SPARQL
###########################################################
#
# Purpose: Validate production MongoDB data against the schema using
#          semantic web tools (RDF, Jena, SPARQL) and migration workflows
#
# Requirements:
#   - 32GB+ RAM (MongoDB dumps are large)
#   - Java runtime (for Jena tools)
#   - Apache Jena TDB2 installed
#   - SSH tunnel to NERSC MongoDB (for MongoDB-based targets)
#   - Dev dependencies: pymongo, python-dotenv, sparql-*, pandas
#
# Who needs this: Maintainers validating production data dumps
# Who doesn't: Contributors working on schema definitions
#
# Documentation: See DATA-VALIDATION.md for detailed setup instructions
#
# Main workflows:
#   1. API-based validation with migrations: test-migrator-on-database
#   2. MongoDB-based RDF conversion: make-rdf, pure-export-and-validate
#
# Note: For migration development tools (migration-doctests, migrator,
#       run-migrator), see makefiles/migrators.Makefile
#
###########################################################

RUN=poetry run

JENA_DIR=~/apache-jena/bin/

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: rdf-clean

rdf-clean:
	rm -rf \
		OmicsProcessing.rq \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_cuire_repaired.ttl \
		local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_nmdc_database_validation.log \
		local/mongo_as_unvalidated_nmdc_database.yaml

###########################################################
# MongoDB Export and RDF Conversion
###########################################################
#
# This setup is required if you want to retrieve any content or
# statistics from PyMongo. pure-export doesn't require a PyMongo
# connection when run in the --skip-collection-check mode.
#
# SSH tunnel setup:
#   1. . ~/sshproxy.sh -u {YOUR_NERSC_USERNAME}
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 \
#      -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov
#
###########################################################

pure-export-and-validate: local/mongo_as_nmdc_database_validation.log

make-rdf: rdf-clean \
	local/mongo_as_nmdc_database_validation.log \
	local/mongo_as_nmdc_database_cuire_repaired.ttl \
	local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl

# MongoDB collection statistics as of 2024-05-17:
# ns                           size         count      avgObjSize  storageSize  totalIndexSize  totalSize
# nmdc.functional_annotation_agg  2194573252  16167688   135         567922688    1772920832      2340843520
# nmdc.data_object_set            81218633    179620     452         24301568     29847552        54149120
# nmdc.biosample_set              10184792    8158       1248        2887680      1753088         4640768

###########################################################
# Migrator Testing via API
###########################################################
#
# Test migrators against production or dev API data
#
# Usage:
#   make test-migrator-on-database ENV=dev MIGRATOR=migrator_from_X_to_Y
#   make test-migrator-on-database SELECTED_COLLECTIONS="biosample_set study_set"
#
###########################################################

# Define API URLs for different environments
API_PROD_URL = https://api.microbiomedata.org
API_DEV_URL = https://api-dev.microbiomedata.org

# Dynamically set the API url based on the ENV variable
API_URL = $(if $(filter dev,$(ENV)),$(API_DEV_URL),$(API_PROD_URL))

# Target 1: Export collections from API
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

# Target 2: Run migrator
local/mongo_via_api_as_nmdc_database_after_migrator.yaml: MIGRATOR=
local/mongo_via_api_as_nmdc_database_after_migrator.yaml: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_via_api_as_unvalidated_nmdc_database.yaml
	date
	time $(RUN) migration-recursion \
		--input-path $(word 2,$^) \
		--schema-path $(word 1,$^) \
		--output-path $@ \
		$(if $(MIGRATOR),--migrator-name $(MIGRATOR),)

# Target 3: Validation
.PRECIOUS: local/mongo_via_api_as_nmdc_database_validation.log
local/mongo_via_api_as_nmdc_database_validation.log: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_via_api_as_nmdc_database_after_migrator.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml validate --schema $^ > $@

# Combined workflow
.PHONY: test-migrator-on-database
test-migrator-on-database: SELECTED_COLLECTIONS=  # Default empty, user can override
test-migrator-on-database: MIGRATOR=             # Default empty, user can override
test-migrator-on-database: ENV=prod              # Default to prod if not specified
test-migrator-on-database: local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
		local/mongo_via_api_as_nmdc_database_after_migrator.yaml \
		local/mongo_via_api_as_nmdc_database_validation.log
	@echo "Combined workflow executed successfully."

###########################################################
# MongoDB Direct Export (Alternative to API)
###########################################################
#
# Requires SSH tunnel to NERSC MongoDB
#
###########################################################

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

# Note: still getting anyurl typed string statement objects in RDF. Added workaround in anyuri-strings-to-iris
local/mongo_as_nmdc_database_cuire_repaired.ttl: local/mongo_as_nmdc_database.ttl
	date
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@
	- export _JAVA_OPTIONS=-Djava.io.tmpdir=local && $(JENA_DIR)/riot --validate $@ # < 1 minute
	date

local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl: local/mongo_as_nmdc_database_cuire_repaired.ttl
	$(RUN) date-created-blank-node > local/date_created_blank_node.ttl
	cat $^ local/date_created_blank_node.ttl > $@
	rm local/date_created_blank_node.ttl

###########################################################
# Utility Targets
###########################################################

.PHONY: populate-mongodb-form-json-collections

populate-mongodb-form-json-collections: generate-json-collections
	src/scripts/json-dir-to-mongodb.sh # requires that the script's permissions have been set like: chmod +x src/scripts/json-dir-to-mongodb.sh
