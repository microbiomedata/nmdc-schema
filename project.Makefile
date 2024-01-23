## Add your own custom Makefile targets here

RUN=poetry run

FD_ROOT=local/fuseki-data/databases

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: accepting-legacy-ids-all accepting-legacy-ids-clean \
dump-validate-report-convert-mongodb examples-clean linkml-validate-mongodb mixs-yaml-clean mixs-deepdiff \
rdf-clean shuttle-clean

accepting-legacy-ids-clean:
	rm -rf nmdc_schema/nmdc_schema_accepting_legacy_ids*

examples-clean:
	rm -rf examples/output

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified.yaml

rdf-clean:
	rm -rf \
		OmicsProcessing.rq \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_cuire_repaired.ttl \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_nmdc_database_validation.log \
		local/mongo_as_unvalidated_nmdc_database.yaml

shuttle-clean:
	#rm -rf local/mixs_regen/mixs_subset_modified.yaml # triggers complete regeneration
	rm -rf local/mixs_regen/mixs_subset.yaml
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_subset_modified_inj_land_use.yaml
	mv $(word 2,$^) $@
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
	sed 's/quantity value/QuantityValue/' $(word 1, $^) > $@
	sed -i.bak 's/range: string/range: TextValue/' $@
	sed -i.bak 's/range: text value/range: TextValue/' $@

	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done
	# eval yq -i $$line $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: assets/other_mixs_yaml_files/cur_land_use_enum.yaml local/mixs_regen/mixs_subset_modified.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all \
		'select(fileIndex==1).enums.cur_land_use_enum = select(fileIndex==0).enums.cur_land_use_enum | select(fileIndex==1)' \
		$^ | cat > $@

# will we ever want to use deepdiff to compare the MIxS schema between two verisons or forms?

project/nmdc_schema_generated.yaml: $(SOURCE_SCHEMA_PATH)
	# the need for this may be eliminated by adding mandatory pattern materialization to gen-json-schema
	$(RUN) gen-linkml \
		--output $@ \
		--materialize-patterns \
		--no-materialize-attributes \
		--format yaml $<

examples/output: project/nmdc_schema_generated.yaml
	mkdir -p $@
	$(RUN) linkml-run-examples \
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

examples/output/Biosample-exhaustive_report.yaml: src/data/valid/Biosample-exhasutive.yaml # replaces misspelled Biosample-exhasutive_report target
	poetry run exhaustion-check \
		--class-name Biosample \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path src/schema/nmdc.yaml

examples/output/Biosample-exhasutive-pretty-sorted.yaml: src/data/valid/Biosample-exhasutive.yaml
	poetry run pretty-sort-yaml \
		-i $< \
		-o $@

accepting-legacy-ids-all: accepting-legacy-ids-clean \
nmdc_schema/nmdc_schema_accepting_legacy_ids.schema.json nmdc_schema/nmdc_schema_accepting_legacy_ids.py

nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml: src/schema/nmdc.yaml assets/yq-for-nmdc_schema_accepting_legacy_ids.txt
	$(RUN) gen-linkml \
		--format yaml \
		--mergeimports \
		--metadata \
		--no-materialize-attributes \
		--no-materialize-patterns \
		--useuris \
		--output $@ $(word 1, $^)

	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done

	$(RUN) gen-linkml \
		--format yaml \
		--mergeimports \
		--metadata \
		--no-materialize-attributes \
		--materialize-patterns \
		--useuris \
		--output $@.temp $@

	mv $@.temp $@

nmdc_schema/nmdc_schema_accepting_legacy_ids.schema.json: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) gen-json-schema \
		--closed $< > $@

nmdc_schema/nmdc_schema_accepting_legacy_ids.py: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) gen-python --log_level ERROR --validate $< > $@ # todo doesn't honor --log_level
	$(RUN) test-more-tolerant-schema

# ----

# this setup is required if you want to retreive any content or statistics from PyMongo
# pure-export doesn't require a PyMongo connection when run in the --skip-collection-check mode
#   1. . ~/sshproxy.sh -u {YOUR_NERSC_USERNAME}
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

# todo mongodb collection stats vs Database slots report
# todo convert to json
# todo compress large files
# todo: switch to API method for getting collection names and stats: https://api.microbiomedata.org/nmdcschema/collection_stats # partially implemented

pure-export-and-validate: local/mongo_as_nmdc_database_validation.log
make-rdf: rdf-clean local/mongo_as_nmdc_database_cuire_repaired.ttl

# functional_annotation_agg is enormous. metaproteomics_analysis_activity_set is large. metap_gene_function_aggregation?

## to ensure API only access: --skip-collection-check

local/mongo_as_unvalidated_nmdc_database.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) pure-export \
		--client-base-url https://api.microbiomedata.org \
		--endpoint-prefix nmdcschema \
		--env-file local/.env \
		--max-docs-per-coll 200000 \
		--mongo-db-name nmdc \
		--mongo-host localhost \
		--mongo-port 27777 \
		--output-yaml $@ \
		--page-size 200000 \
		--schema-file src/schema/nmdc.yaml \
		--selected-collections activity_set \
		--selected-collections biosample_set \
		--selected-collections collecting_biosamples_from_site_set \
		--selected-collections data_object_set \
		--selected-collections extraction_set \
		--selected-collections field_research_site_set \
		--selected-collections functional_annotation_agg \
		--selected-collections genome_feature_set \
		--selected-collections library_preparation_set \
		--selected-collections mags_activity_set \
		--selected-collections material_sample_set \
		--selected-collections metabolomics_analysis_activity_set \
		--selected-collections metagenome_annotation_activity_set \
		--selected-collections metagenome_assembly_set \
		--selected-collections metagenome_sequencing_activity_set \
		--selected-collections metap_gene_function_aggregation \
		--selected-collections metatranscriptome_activity_set \
		--selected-collections nom_analysis_activity_set \
		--selected-collections omics_processing_set \
		--selected-collections planned_process_set \
		--selected-collections pooling_set \
		--selected-collections processed_sample_set \
		--selected-collections read_based_taxonomy_analysis_activity_set \
		--selected-collections read_qc_analysis_activity_set \
		--selected-collections study_set \
		--skip-collection-check

local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date # 449.56 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) migration-recursion \
		--migrator-name migrator_from_9_3_to_10_0 \
		--schema-path $(word 1,$^) \
		--input-path $(word 2,$^) \
		--salvage-prefix generic \
		--output-path $@

.PRECIOUS: local/mongo_as_nmdc_database_validation.log

local/mongo_as_nmdc_database_validation.log: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	# nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml or nmdc_schema/nmdc_materialized_patterns.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-validate --schema $^ > $@

local/mongo_as_nmdc_database.ttl: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	date # 681.99 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-convert --output $@ --schema $^
	export _JAVA_OPTIONS=-Djava.io.tmpdir=local
	- riot --validate $@ # < 1 minute

# todo: still getting anyurl typed string statement objects in RDF. I added a workarround in anyuri-strings-to-iris
local/mongo_as_nmdc_database_cuire_repaired.ttl: local/mongo_as_nmdc_database.ttl
	date
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@
	export _JAVA_OPTIONS=-Djava.io.tmpdir=local
	- riot --validate $@ # < 1 minute
	date

.PHONY: migration-doctests migrator

# Runs all doctests defined within the migrator modules, adapters, and CLI scripts.
migration-doctests:
	$(RUN) python -m doctest -v nmdc_schema/migrators/*.py
	$(RUN) python -m doctest -v nmdc_schema/migrators/adapters/*.py
	$(RUN) python -m doctest -v nmdc_schema/migrators/cli/*.py

# Generates a migrator skeleton for the specified schema versions.
# Note: `create-migrator` is a Poetry script registered in `pyproject.toml`.
migrator:
	$(RUN) create-migrator

.PHONY: filtered-status
filtered-status:
	git status | grep -v 'project/' | grep -v 'nmdc_schema/.*yaml' | grep -v 'nmdc_schema/.*json' | \
		grep -v 'nmdc.py' | grep -v 'nmdc_schema_accepting_legacy_ids.py'

local/biosample-slot-range-type-report.tsv: src/schema/nmdc.yaml
	$(RUN) slot-range-type-reporter \
		--schema $< \
		--output $@ \
		--schema-class Biosample

### example of preparing to validate napa squad data
local/nmdc-schema-v8.0.0.yaml:
	curl -o $@ https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v8.0.0/nmdc_schema/nmdc_materialized_patterns.yaml
	# need to remove lines like this (see_alsos whose values aren't legitimate URIs)
	#     see_also:
	#       - MIxS:experimental_factor|additional_info
	yq eval-all -i 'del(select(fileIndex == 0) | .. | select(has("see_also")) | .see_also)' $@

local/nmdc-schema-v8.0.0.owl.ttl: local/nmdc-schema-v8.0.0.yaml
	$(RUN) gen-owl $< > $@

local/nmdc-sty-11-aygzgv51.yaml:
	$(RUN) get-study-related-records \
		--api-base-url https://api-napa.microbiomedata.org \
		extract-study \
		--study-id $(subst nmdc-,nmdc:,$(basename $(notdir $@))) \
		--output-file $@

### FUSEKI, DOCKER, ETC
# we use Apache's Jena RDF/SPARQL framework
# Jena provides command line tools for accessing RDF *files*
# or you can use a TDB as the data backend
# Fuseki is a web interface for submitting SPARQL queries
# we are foing all of this in docker so you don't have to install any of this software

.PHONY: thorough-docker-fuseki-cleanup-from-host # this level of cleanup may not be needed ona regular basis
thorough-docker-fuseki-cleanup-from-host:
	- docker compose down
	rm -rf local/fuseki-data
	rm -rf local/nmdc-data*
	rm -rf local/nmdc-tdb2*
	docker system prune --force # very aggressive. may delete containers etc that you want but are not currently running

.PHONY: docker-startup-from-host
docker-startup-from-host:
	docker compose up --build  --detach # --build is only necessary if changes have been made to the Dockerfile

# manually: `docker compose exec app bash`
# then you can do any nmdc-schem makefile commands in the 'app' environment

.PHONY: build-schema-in-app
build-schema-in-app:
	# Warning: 'get-study-related-records' is an entry point defined in pyproject.toml, but it's not installed as a script. You may get improper `sys.argv[0]`.
	# The support to run uninstalled scripts will be removed in a future release.
	# Run `poetry install` to resolve and get rid of this message.
	poetry install
	make squeaky-clean all test

.PHONY: comprehensive-fuseki-in-app
comprehensive-fuseki-in-app: create-nmdc-tdb2-from-app populate-nmdc-tdb2-in-app # run simultaneously with tests above in new `docker compose exec app bash`

.PHONY: create-nmdc-tdb2-from-app
create-nmdc-tdb2-from-app: # Fuseki will get it's data from this TDB2 database. It starts out empty.
	curl \
		--user 'admin:password' \
		--data 'dbType=tdb&dbName=nmdc-tdb2' \
		'http://fuseki:3030/$$/datasets'

.PHONY: populate-nmdc-tdb2-in-app
populate-nmdc-tdb2-in-app: local/nmdc-data.ttl populate-nmdc-tdb2 # can be run concurrently with tests, in its own "docker compose exec app bash"

# Napa nmdc:sty-11-aygzgv51 = gold:Gs0114663
local/nmdc-data.yaml:
	# this does not traverse every possible path from a Study to all related records
	# --quick-test \
	# 40 minutes?
	date
	time $(RUN) get-study-related-records \
		--api-base-url https://api.microbiomedata.org \
		extract-study \
		--study-id gold:Gs0114663 \
		--output-file $@ # this is a CLI that bundles several API calls to get data from MongoDB

local/nmdc-data-validation-log.txt: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/nmdc-data.yaml
	$(RUN) linkml-validate --schema $^ > $@

local/nmdc-data-raw.ttl: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/nmdc-data.yaml local/nmdc-data-validation-log.txt
	$(RUN) linkml-convert --output $@ --schema $(word 1, $^) $(word 2, $^) # remember, TTL is one serialization of RDF data

local/nmdc-data.ttl: local/nmdc-data-raw.ttl
	$(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@ # this converts some string values from linkml-convert to object relationships
	riot --validate $@

# Populates a Jena TDB2 database that will be accessible to Fuseki.
#
# Note: Manually stop the `fuseki` container before running this target,
#       in order to release a lock on a file that this target writes to.
#
# Note: We expect people to run this make target from within the `app` container.
#
.PHONY: populate-nmdc-tdb2
populate-nmdc-tdb2: project/owl/nmdc.owl.ttl local/nmdc-data.ttl
	curl -X \
		POST -H "Content-Type: text/turtle" \
		--user 'admin:password' \
		--data-binary @$(word 1, $^) http://fuseki:3030/nmdc-tdb2/data?graph=https://w3id.org/nmdc/nmdc
	curl -X \
		POST -H "Content-Type: text/turtle" \
		--user 'admin:password' \
		--data-binary @$(word 2, $^) http://fuseki:3030/nmdc-tdb2/data

# does this with work in both the datasets offline and active states?
local/nmdc-tdb2-graph-list.tsv:
	tdb2.tdbquery \
		--loc=$(FD_ROOT)/nmdc-tdb2 \
		--query=assets/sparql/tdb-graph-list.rq \
		--results=TSV > $@

# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?default

# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?graph=https://w3id.org/nmdc/nmdc


.PHONY: docker-compose-down-from-host
docker-compose-down-from-host:
	docker compose down

