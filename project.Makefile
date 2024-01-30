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

# 		--selected-collections extraction_set \

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

local/nmdc-schema-v7.8.0.yaml:
	curl -o $@ https://raw.githubusercontent.com/microbiomedata/nmdc-schema/v7.8.0/nmdc_schema/nmdc_materialized_patterns.yaml
	# need to remove lines like this (see_alsos whose values aren't legitimate URIs)
	#     see_also:
	#       - MIxS:experimental_factor|additional_info
	yq eval-all -i 'del(select(fileIndex == 0) | .. | select(has("see_also")) | .see_also)' $@
	yq -i 'del(.classes.DataObject.slot_usage.id.pattern)' $@ # kludge modify schema to match data
	yq -i 'del(.classes.DataObject.slot_usage.id.pattern)' $@ # kludge modify schema to match data
	rm -rf $@.bak

local/nmdc-schema-v8.0.0.owl.ttl: local/nmdc-schema-v8.0.0.yaml
	$(RUN) gen-owl $< > $@


local/nmdc-schema-v7.8.0.owl.ttl: local/nmdc-schema-v7.8.0.yaml
	$(RUN) gen-owl $< > $@

local/nmdc-sty-11-aygzgv51.yaml:
	$(RUN) get-study-related-records \
		--api-base-url https://api-napa.microbiomedata.org \
		extract-study \
		--study-id $(subst nmdc-,nmdc:,$(basename $(notdir $@))) \
		--search-orphaned-data-objects \
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
	poetry install # it's best if there isn't already a ./.venv, especially if it's not for Linux
	make squeaky-clean all test

.PHONY: create-nmdc-tdb2-from-app
create-nmdc-tdb2-from-app: # Fuseki will get it's data from this TDB2 database. It starts out empty.
	curl \
		--user 'admin:password' \
		--data 'dbType=tdb&dbName=nmdc-tdb2' \
		'http://fuseki:3030/$$/datasets'

## does this with work in both the datasets offline and active states?
#local/nmdc-tdb2-graph-list.tsv:
#	tdb2.tdbquery \
#		--loc=$(FD_ROOT)/nmdc-tdb2 \
#		--query=assets/sparql/tdb-graph-list.rq \
#		--results=TSV > $@

# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?default

# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?graph=https://w3id.org/nmdc/nmdc


.PHONY: docker-compose-down-from-host
docker-compose-down-from-host:
	docker compose down

# ----

.PHONY: print-prefixed-study-ids print-file-list

STUDY_IDS := nmdc:sty-11-34xj1150 nmdc:sty-11-5bgrvr62 nmdc:sty-11-5tgfr349 nmdc:sty-11-r2h77870 \
nmdc:sty-11-db67n062 nmdc:sty-11-8xdqsn54 nmdc:sty-11-28tm5d36 nmdc:sty-11-33fbta56 nmdc:sty-11-076c9980 \
nmdc:sty-11-t91cwb40 nmdc:sty-11-aygzgv51 nmdc:sty-11-547rwq94 nmdc:sty-11-zs2syx06 nmdc:sty-11-dcqce727 \
nmdc:sty-11-1t150432 nmdc:sty-11-8fb6t785

#print-prefixed-study-ids:
#	@echo $(STUDY_IDS)

# Replace colons with hyphens in study IDs
STUDY_FILES := $(addsuffix .yaml,$(addprefix local/study-files/,$(subst :,-,$(STUDY_IDS))))

#print-file-list:
#	@echo $(STUDY_FILES)

# Napa nmdc:sty-11-aygzgv51 = "production" gold:Gs0114663

  # [('nmdc:sty-11-34xj1150', 4443),
  # ('nmdc:sty-11-5bgrvr62', 471),
  # ('nmdc:sty-11-5tgfr349', 430),
  # ('nmdc:sty-11-r2h77870', 416),
  # ('nmdc:sty-11-db67n062', 241),
  # ('nmdc:sty-11-8xdqsn54', 207),
  # ('nmdc:sty-11-28tm5d36', 134),
  # ('nmdc:sty-11-33fbta56', 124),
  # ('nmdc:sty-11-076c9980', 105),
  # ('nmdc:sty-11-t91cwb40', 95),
  # ('nmdc:sty-11-aygzgv51', 85),
  # ('nmdc:sty-11-547rwq94', 80),
  # ('nmdc:sty-11-zs2syx06', 60), # Extracted study nmdc:sty-11-zs2syx06 from the NMDC database in 0:00:01.475736.
  # ('nmdc:sty-11-dcqce727', 53), # Extracted study nmdc:sty-11-dcqce727 from the NMDC database in 0:36:39.633116.
  # ('nmdc:sty-11-1t150432', 30), # Extracted study nmdc:sty-11-8fb6t785 from the NMDC database in 0:01:04.012420, 0:01:17.337886.
  # ('nmdc:sty-11-8fb6t785', 23)] # Extracted study nmdc:sty-11-8fb6t785 from the NMDC database in 0:01:01.963206.

# local/study-files/nmdc-sty-11-34xj1150.yaml
local/study-files/%.yaml: local/nmdc-schema-v8.0.0.yaml
	mkdir -p $(@D)
	rm -rf study-file-name.txt study-id.txt
	echo $@ > study-file-name.txt
	echo $(shell poetry run get-study-id-from-filename $$(<study-file-name.txt)) > study-id.txt
	# cumbersome! using python script because can't replace just first hyphen with colon with make text function
	# then, can't use $@ inside of a make shell call
	# we just want to transform $@, like local/study-files/nmdc-sty-11-8fb6t785.yaml to nmdc:sty-11-8fb6t785
	date
	time $(RUN) get-study-related-records \
		--api-base-url https://api-napa.microbiomedata.org \
		extract-study \
		--study-id $$(<study-id.txt) \
		--output-file $@
	$(RUN) linkml-validate --schema $< $@ > $@.validation.log.txt
	rm -rf study-file-name.txt study-id.txt

create-study-yaml-files: local/study-files/nmdc-sty-11-8fb6t785.yaml \
local/study-files/nmdc-sty-11-1t150432.yaml \
local/study-files/nmdc-sty-11-zs2syx06.yaml

# includes load into fuseki
# not doing any migration here yet
local/study-files/%.ttl: local/nmdc-schema-v8.0.0.yaml create-nmdc-tdb2-from-app create-study-yaml-files
	$(RUN) linkml-convert --output $@ --schema $< $(subst .ttl,.yaml,$@)
	curl -X \
		POST -H "Content-Type: text/turtle" \
		--user 'admin:password' \
		--data-binary @$@ http://fuseki:3030/nmdc-tdb2/data?graph=https://api-napa.microbiomedata.org

create-load-study-ttl-files: local/study-files/nmdc-sty-11-8fb6t785.ttl \
local/study-files/nmdc-sty-11-1t150432.ttl \
local/study-files/nmdc-sty-11-zs2syx06.ttl


# seems to work in both the datasets offline and active states
# could also show how to submit to fuseki via curl
# or could run interactively in Fuseki web UI, localhost:3030
# but that may only load in a private browser window
local/subjects-lacking-rdf-types.tsv:
	tdb2.tdbquery \
		--loc=$(FD_ROOT)/nmdc-tdb2 \
		--query=assets/sparql/subjects-lacking-rdf-types.rq \
		--results=TSV > $@ # this doesn't take into consideration that some entities have nmdc:type string values, which should be migrated


# retreive, validate, convert, repair, load and query selected colelctiosn form the Napa squad's MongoDB

local/some_napa_collections.yaml: local/nmdc-schema-v7.8.0.yaml
	date
	time $(RUN) pure-export \
		--client-base-url https://api-napa.microbiomedata.org \
		--endpoint-prefix nmdcschema \
		--env-file local/.env \
		--max-docs-per-coll 200000 \
		--mongo-db-name nmdc \
		--mongo-host localhost \
		--mongo-port 27777 \
		--output-yaml $@.tmp \
		--page-size 200000 \
		--schema-file $< \
		--selected-collections biosample_set \
		--selected-collections data_object_set \
		--selected-collections extraction_set \
		--selected-collections field_research_site_set \
		--selected-collections library_preparation_set \
		--selected-collections omics_processing_set \
		--selected-collections pooling_set \
		--selected-collections processed_sample_set \
		--selected-collections study_set \
		--skip-collection-check
	sed -i.bak 's/gold:/GOLD:/' $@.tmp # kludge modify data to match (old!) schema
	rm -rf $@.tmp.bak
	time $(RUN) migration-recursion \
		--schema-path $< \
		--input-path $@.tmp \
		--salvage-prefix generic \
		--output-path $@ # kludge masks ids that contain whitespace
	rm -rf $@.tmp

.PRECIOUS: local/some_napa_collections.validation.log
local/some_napa_collections.validation.log: local/nmdc-schema-v7.8.0.yaml local/some_napa_collections.yaml
	- $(RUN) linkml-validate --schema $^ > $@

local/some_napa_collections.ttl: local/nmdc-schema-v7.8.0.yaml local/some_napa_collections.yaml local/some_napa_collections.validation.log
	$(RUN) linkml-convert --output $@.tmp.ttl --schema $(word 1, $^) $(word 2, $^)
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $@.tmp.ttl \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@
	rm -rf $@.tmp.ttl

load-from-some-napa-collections: local/some_napa_collections.ttl
	curl -X \
		POST -H "Content-Type: text/turtle" \
		--user 'admin:password' \
		--data-binary @$< http://fuseki:3030/nmdc-tdb2/data?graph=https://api-napa.microbiomedata.org

.PHONY: load-non-native-uri-schema
# from linkml/linkml branch issue-1842
# poetry run gen-owl --no-use-native-uris ../nmdc-schema/src/schema/nmdc.yaml > ../nmdc-schema/local/nmdc_with_non_native_uris.owl.ttl
load-non-native-uri-schema: local/nmdc_with_non_native_uris.owl.ttl create-nmdc-tdb2-from-app
	curl -X \
		POST -H "Content-Type: text/turtle" \
		--user 'admin:password' \
		--data-binary @$< http://fuseki:3030/nmdc-tdb2/data?graph=https://w3id.org/nmdc/nmdc

local/sparql-results/objects-that-are-never-subjects.tsv:
	mkdir -p $(@D)
	echo $@
	echo $(notdir $(basename $@))
	curl \
		-H "Accept: text/tab-separated-values" \
		  --data-urlencode "query@assets/sparql/$(notdir $(basename $@)).rq" \
		  --output $@ 'http://fuseki:3030/nmdc-tdb2/query'

some-napa-collections-cleanup:
	rm -rf local/some_napa_collections*
	rm -rf local/nmdc-schema*
	# rm -rf local/sparql-results/*

.PHONY: clear-data-graph some-napa-collections-cleanup
clear-data-graph:
	curl -X \
		POST -H "Content-Type: application/sparql-update" \
		--user 'admin:password' \
		--data "CLEAR GRAPH <https://api-napa.microbiomedata.org>" \
		http://fuseki:3030/nmdc-tdb2/update