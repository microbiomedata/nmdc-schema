## Add your own custom Makefile targets here

RUN=poetry run

JENA_DIR=~/apache-jena/bin/

FD_ROOT=local/fuseki-data/databases

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: examples-clean \
mixs-yaml-clean \
rdf-clean \
shuttle-clean \
squeaky-clean

examples-clean:
	rm -rf examples/output

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified*yaml

rdf-clean:
	rm -rf \
		OmicsProcessing.rq \
		local/mongo_as_*

shuttle-clean:
	rm -rf \
		local/mixs_regen/mixs_subset.yaml \
		local/mixs_regen/mixs_subset_modified.yaml.bak \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_cuire_repaired.ttl \
		local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_nmdc_database_validation.log \
		local/mongo_as_unvalidated_nmdc_database.yaml
	rm -rf local/mixs_regen/*.yaml
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_subset_modified_inj_env_medium_alt_description.yaml
	mv $(word 2,$^) $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak

local/mixs_regen/mixs_subset.yaml: assets/other_mixs_yaml_files/mixs_slots_import_sheet.tsv
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


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: local/mixs_regen/mixs_subset_modified.yaml \
assets/other_mixs_yaml_files/cur_land_use_enum.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all \
		'select(fileIndex==0).enums.cur_land_use_enum = select(fileIndex==1).enums.cur_land_use_enum | select(fileIndex==0)' \
		$^ | cat > $@

local/mixs_regen/mixs_subset_modified_inj_env_broad_scale_alt_description.yaml: local/mixs_regen/mixs_subset_modified_inj_land_use.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	yq eval-all \
		'select(fileIndex==0).slots.env_broad_scale.annotations.tooltip = select(fileIndex==1).slots.env_broad_scale.annotations.tooltip | select(fileIndex==0)' \
		$^ | cat > $@

local/mixs_regen/mixs_subset_modified_inj_env_local_scale_alt_description.yaml: local/mixs_regen/mixs_subset_modified_inj_env_broad_scale_alt_description.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	yq eval-all \
		'select(fileIndex==0).slots.env_local_scale.annotations.tooltip = select(fileIndex==1).slots.env_local_scale.annotations.tooltip | select(fileIndex==0)' \
		$^ | cat > $@

local/mixs_regen/mixs_subset_modified_inj_env_medium_alt_description.yaml: local/mixs_regen/mixs_subset_modified_inj_env_local_scale_alt_description.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	yq eval-all \
		'select(fileIndex==0).slots.env_medium.annotations.tooltip = select(fileIndex==1).slots.env_medium.annotations.tooltip | select(fileIndex==0)' \
		$^ | cat > $@

examples/output: nmdc_schema/nmdc_materialized_patterns.yaml
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

examples/output/Biosample-exhaustive_report.yaml: src/data/valid/Biosample-exhasutive.yaml
	$(RUN) exhaustion-check \
		--class-name Biosample \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path src/schema/nmdc.yaml

examples/output/Pooling-minimal-report.yaml: src/data/valid/Pooling-minimal.yaml
	mkdir -p $(@D) # create parent directory
	poetry run exhaustion-check \
		--class-name Pooling \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path src/schema/nmdc.yaml

examples/output/Biosample-exhasutive-pretty-sorted.yaml: src/data/valid/Biosample-exhasutive.yaml
	$(RUN) pretty-sort-yaml \
		-i $< \
		-o $@

# this setup is required if you want to retreive any content or statistics from PyMongo
# pure-export doesn't require a PyMongo connection when run in the --skip-collection-check mode
#   1. . ~/sshproxy.sh -u {YOUR_NERSC_USERNAME}
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

# todo mongodb collection stats vs Database slots report
# todo convert to json
# todo compress large files
# todo: switch to API method for getting collection names and stats: https://api.microbiomedata.org/nmdcschema/collection_stats # partially implemented

pure-export-and-validate: local/mongo_as_nmdc_database_validation.log.txt

make-rdf: rdf-clean \
	local/mongo_as_nmdc_database_validation.log.txt \
	local/mongo_as_nmdc_database_cuire_repaired.ttl \
	local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl # could omit rdf-clean. then this could build incrementally on top of pure-export-and-validate

# statistics of large collections as of 2024-05-17
#ns	size	count	avgObjSize	storageSize	totalIndexSize	totalSize	scaleFactor
#nmdc.functional_annotation_agg	2194573252	16167688	135	567922688	1772920832	2340843520	1
#nmdc.metaproteomics_analysis_activity_set	133268047	52	2562847	37380096	40960	37421056	1
#nmdc.data_object_set	81218633	179620	452	24301568	29847552	54149120	1
#nmdc.biosample_set	10184792	8158	1248	2887680	1753088	4640768	1

# todo: metagenome_sequencing_set and metagenome_sequencing_activity_set are degenerate
#   and can't be validated, migrated or converted to RDF

local/mongo_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--output-yaml $@ \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections activity_set \
		--selected-collections biosample_set \
		--selected-collections collecting_biosamples_from_site_set \
		--selected-collections data_object_set \
		--selected-collections extraction_set \
		--selected-collections field_research_site_set \
		--selected-collections functional_annotation_set \
		--selected-collections genome_feature_set \
		--selected-collections library_preparation_set \
		--selected-collections mags_activity_set \
		--selected-collections mags_set \
		--selected-collections material_sample_set \
		--selected-collections metabolomics_analysis_activity_set \
		--selected-collections metabolomics_analysis_set \
		--selected-collections metagenome_annotation_activity_set \
		--selected-collections metagenome_annotation_set \
		--selected-collections metagenome_assembly_set \
		--selected-collections metagenome_sequencing_activity_set \
		--selected-collections metagenome_sequencing_set \
		--selected-collections metap_gene_function_aggregation \
		--selected-collections metatranscriptome_activity_set \
		--selected-collections metatranscriptome_analysis_set \
		--selected-collections nom_analysis_activity_set \
		--selected-collections omics_processing_set \
		--selected-collections planned_process_set \
		--selected-collections pooling_set \
		--selected-collections processed_sample_set \
		--selected-collections read_based_taxonomy_analysis_activity_set \
		--selected-collections read_qc_analysis_activity_set \
		--selected-collections study_set \
		--selected-collections workflow_chain_set \
		--selected-collections workflow_execution_set \
		dump-from-api \
		--client-base-url "https://api.microbiomedata.org" \
		--endpoint-prefix nmdcschema \
		--page-size 200000

## ALTERNATIVELY:
#local/mongo_as_unvalidated_nmdc_database.yaml:
#	date
#	time $(RUN) pure-export \
#		--max-docs-per-coll 200000 \
#		--output-yaml $@ \
#		--schema-source src/schema/nmdc.yaml \
#		--selected-collections biosample_set \
#		--selected-collections study_set \
#		dump-from-database \
#		--admin-db "admin" \
#		--auth-mechanism "DEFAULT" \
#		--env-file local/.env \
#		--mongo-db-name nmdc \
#		--mongo-host localhost \
#		--mongo-port 27777 \
#		--direct-connection

local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date # 449.56 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) migration-recursion \
		--input-path $(word 2,$^) \
		--schema-path $(word 1,$^) \
		--output-path $@

.PRECIOUS: local/mongo_as_nmdc_database_validation.log.txt

local/mongo_as_nmdc_database_validation.log: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-validate --schema $^ > $@

local/mongo_as_nmdc_database.ttl: nmdc_schema/nmdc_materialized_patterns.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	date # 681.99 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-convert --output $@ --schema $^
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
migration-doctests:
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/adapters/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/cli/*.py

# Generates a migrator skeleton for the specified schema versions.
# Note: `create-migrator` is a Poetry script registered in `pyproject.toml`.
migrator:
	$(RUN) create-migrator

.PHONY: filtered-status
filtered-status:
	git status | grep -v 'project/' | grep -v 'nmdc_schema/.*yaml' | grep -v 'nmdc_schema/.*json' | \
		grep -v 'nmdc.py' | grep -v 'examples/output/' # | grep -v 'nmdc_materialized_patterns.py' |

local/biosample-slot-range-type-report.tsv: src/schema/nmdc.yaml
	$(RUN) slot-range-type-reporter \
		--schema $< \
		--output $@ \
		--schema-class Biosample


## FUSEKI, DOCKER, ETC
# we use Apache's Jena RDF/SPARQL framework
# Jena provides command line tools for accessing RDF *files*
# we use a Jena TDB2 database as the backend (as opposed to operating over files)
# Fuseki is Jena's web interface for submitting SPARQL queries
# we are doing all of this in docker so you don't have to install any of this system software

.PHONY: thorough-docker-fuseki-cleanup-from-host # this level of cleanup may not be needed on a regular basis
thorough-docker-fuseki-cleanup-from-host: some-napa-collections-cleanup
	- docker compose down
	rm -rf local/fuseki-data
	rm -rf local/sparql-results/*
	rm -rf .venv
	docker system prune --force # very aggressive. may delete containers etc that you want but are not currently running

.PHONY: docker-startup-from-host
docker-startup-from-host:
	docker compose up --build  --detach # --build is only necessary if changes have been made to the Dockerfile

# from host: checkout the desired branch, fetch and pull
# from host: `docker compose exec app bash`
#   it's best if there isn't already a ./.venv, especially if the environment wasn't built for Linux
# in container: `poetry install`
# in container: `make build-schema-in-app`

# then you can do any nmdc-schema makefile commands in the 'app' environment

.PHONY: build-schema-in-app
build-schema-in-app: pre-build
	make squeaky-clean all test

.PHONY: pre-build
pre-build: local/gold-study-ids.yaml create-nmdc-tdb2-from-app

.PHONY: create-nmdc-tdb2-from-app
create-nmdc-tdb2-from-app: # Fuseki will get it's data from this TDB2 database. It starts out empty.
	curl \
		--user 'admin:password' \
		--data 'dbType=tdb&dbName=nmdc-tdb2' \
		'http://fuseki:3030/$$/datasets'


## Option 2 of 2 for getting data from MongoDB for Napa QC: get-study-id-from-filename
#
# advantage: can retreive records that have known, chacterized paths to a Study (useful scoping)
# disadvantages:
#   some paths to records form some collections aren't implemented yet
#   runs slow on Mark's computers in Philadelphia. Running pure-export can reteive more data more quickly, but without any scoping
# the core targets include wildcards in their names,
#   but an individual YAML file can be built like this: make local/study-files/nmdc-sty-11-8fb6t785.yaml
#   or an explicit subset of YAML files can be built with: make create-study-yaml-files-subset
#   or YAML files can be built from a list of study ids (STUDY_IDS) like this: make create-study-yaml-files-from-study-ids-list


# can't ever be used without generating local/gold-study-ids.yaml first
STUDY_IDS := $(shell yq '.resources.[].id' local/gold-study-ids.yaml  | awk '{printf "%s ", $$0} END {print ""}')

.PHONY: print-discovered-study-ids print-intended-yaml-files

# can't ever be used without generating local/gold-study-ids.yaml first
print-discovered-study-ids:
	@echo $(STUDY_IDS)

# Replace colons with hyphens in study IDs
# can't ever be used without generating local/gold-study-ids.yaml first
STUDY_YAML_FILES := $(addsuffix .yaml,$(addprefix local/study-files/,$(subst :,-,$(STUDY_IDS))))

.PHONY: all-study-yaml-files

# can't ever be used without generating local/gold-study-ids.yaml first
create-study-yaml-files-from-study-ids-list: $(STUDY_YAML_FILES)

# can't ever be used without generating local/gold-study-ids.yaml first
print-intended-yaml-files: local/gold-study-ids.yaml
	@echo $(STUDY_YAML_FILES)

## we can get a report of biosamples per study with the following
## may help predict how long it will take to run study-id-from-filename on a particular study
## will become unnecessary once aggregation queries are available in the napa nmdc-runtime API
local/biosamples-per-study.txt:
	$(RUN) python src/scripts/report_biosamples_per_study.py > $@

## getting a report of GOLD study identifiers, which might have been used a Study ids in legacy (pre-Napa) data
local/gold-study-ids.json:
	curl -X 'GET' \
		--output $@ \
		'https://api-napa.microbiomedata.org/nmdcschema/study_set?max_page_size=999&projection=id%2Cgold_study_identifiers' \
		-H 'accept: application/json'

local/gold-study-ids.yaml: local/gold-study-ids.json
	yq -p json -o yaml $< | cat > $@

local/study-files/%.yaml: nmdc_schema/nmdc_materialized_patterns.yaml
	mkdir -p $(@D)
	study_file_name=`echo $@` ; \
		echo $$study_file_name ; \
		study_id=`poetry run get-study-id-from-filename $$study_file_name` ; \
		echo $$study_id ; \
		date ; \
		time $(RUN) get-study-related-records \
			--api-base-url https://api-napa.microbiomedata.org \
			extract-study \
			--study-id $$study_id \
			--output-file $@.tmp.yaml
	sed -i.bak 's/gold:/GOLD:/' $@.tmp.yaml # kludge modify data to match (old!) schema
	rm -rf $@.tmp.bak
	- $(RUN) linkml-validate --schema $< $@.tmp.yaml > $@.validation.log.txt
	time $(RUN) migration-recursion \
		--schema-path $< \
		--input-path $@.tmp.yaml \
		--output-path $@ # kludge masks ids that contain whitespace
	rm -rf $@.tmp.yaml $@.tmp.yaml.bak

.PHONY: create-study-yaml-files-subset create-study-ttl-files-subset load-from-some-napa-collections

create-study-yaml-files-subset: local/study-files/nmdc-sty-11-8fb6t785.yaml \
local/study-files/nmdc-sty-11-1t150432.yaml \
local/study-files/nmdc-sty-11-dcqce727.yaml

local/study-files/%.ttl: nmdc_schema/nmdc_materialized_patterns.yaml create-nmdc-tdb2-from-app create-study-yaml-files-subset
	$(RUN) linkml-convert --output $@ --schema $< $(subst .ttl,.yaml,$@)

create-study-ttl-files-subset: local/study-files/nmdc-sty-11-8fb6t785.ttl \
local/study-files/nmdc-sty-11-1t150432.ttl \
local/study-files/nmdc-sty-11-dcqce727.ttl

## Option 2 of 2 for getting data from MongoDB for Napa QC: get-study-id-from-filename
# retrieve selected collections from the Napa squad's MongoDB and fix ids containing whitespace
local/some_napa_collections.yaml: nmdc_schema/nmdc_materialized_patterns.yaml
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
		--output-path $@ # kludge masks ids that contain whitespace
	rm -rf $@.tmp

.PRECIOUS: local/some_napa_collections.validation.log
local/some_napa_collections.validation.log: nmdc_schema/nmdc_materialized_patterns.yaml local/some_napa_collections.yaml
	- $(RUN) linkml-validate --schema $^ > $@

local/some_napa_collections.ttl: nmdc_schema/nmdc_materialized_patterns.yaml local/some_napa_collections.yaml local/some_napa_collections.validation.log
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
load-non-native-uri-schema: local/nmdc-schema-v7.8.0.owl.ttl create-nmdc-tdb2-from-app
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

.PHONY: clear-data-graph some-napa-collections-cleanup
clear-data-graph:
	curl -X \
		POST -H "Content-Type: application/sparql-update" \
		--user 'admin:password' \
		--data "CLEAR GRAPH <https://api-napa.microbiomedata.org>" \
		http://fuseki:3030/nmdc-tdb2/update

.PHONY: docker-compose-down-from-host
docker-compose-down-from-host:
	docker compose down

## Querying with Fuseki's SAPRQL API is preferred. Here's an example of querying TDB2 database directly.
##   We haven't whetehr the direct query is appropriate or preferable in any cases
# or could run interactively in Fuseki web UI, localhost:3030
# but that may only load in a private browser window

#local/nmdc-tdb2-graph-list.tsv:
#	tdb2.tdbquery \
#		--loc=$(FD_ROOT)/nmdc-tdb2 \
#		--query=assets/sparql/tdb-graph-list.rq \
#		--results=TSV > $@

#local/subjects-lacking-rdf-types.tsv:
#	tdb2.tdbquery \
#		--loc=$(FD_ROOT)/nmdc-tdb2 \
#		--query=assets/sparql/subjects-lacking-rdf-types.rq \
#		--results=TSV > $@ # this doesn't take into consideration that some entities have nmdc:type string values, which should be migrated

## when would we want to delete instead of clearing?
# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?default

# curl -X DELETE \
#   --user 'admin:password' \
#   http://fuseki:3030/nmdc-tdb2/data?graph=https://w3id.org/nmdc/nmdc

local/nmdc-no-use-native-uris.owl.ttl: src/schema/nmdc.yaml
	$(RUN) gen-owl --no-use-native-uris $< > $@


local/nmdc_materialized.ttl: src/schema/nmdc.yaml
	$(RUN) python src/scripts/schema_view_relation_graph.py \
		--schema $< \
		--output $@

local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl: local/mongo_as_nmdc_database_cuire_repaired.ttl
	$(RUN) python src/scripts/date_created_blank_node.py > local/date_created_blank_node.ttl
	cat $^ local/date_created_blank_node.ttl > $@
	rm local/date_created_blank_node.ttl

# ----	NMDC NCBI mapping process ---- #
assets/ncbi_mappings/ncbi_attribute_mappings.tsv:
	poetry run nmdc-ncbi-mapping create-unmapped-ncbi-mapping-file \
		--tsv-output $@

assets/ncbi_mappings/ncbi_attribute_mappings_filled.tsv: assets/ncbi_mappings/ncbi_attribute_mappings.tsv
	poetry run nmdc-ncbi-mapping exact-term-matching \
		--tsv-input $< \
		--tsv-output $@

	poetry run nmdc-ncbi-mapping ignore-import-schema-slots $@
	