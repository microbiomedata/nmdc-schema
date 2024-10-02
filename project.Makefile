## Add your own custom Makefile targets here

RUN=poetry run

JENA_DIR=~/apache-jena/bin/

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

PLANTUML_JAR = local/plantuml-lgpl-1.2024.3.jar

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


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_subset_modified_inj_env_medium_alt_description.yaml
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
	rm -rf $@.bak


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


examples/output/Biosample-exhasutive-pretty-sorted.yaml: src/data/problem/valid/Biosample-exhasutive.yaml
	$(RUN) pretty-sort-yaml \
		-i $< \
		-o $@

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
#nmdc.metaproteomics_analysis_activity_set	133268047	52	2562847	37380096	40960	37421056	1
#nmdc.data_object_set	81218633	179620	452	24301568	29847552	54149120	1
#nmdc.biosample_set	10184792	8158	1248	2887680	1753088	4640768	1

# todo: metagenome_sequencing_set and metagenome_sequencing_activity_set are degenerate
#   and can't be validated, migrated or converted to RDF

# --selected-collections workflow_execution_set

local/mongo_as_unvalidated_nmdc_database.yaml:
	date
	time $(RUN) pure-export \
		--max-docs-per-coll 200000 \
		--output-yaml $@ \
		--schema-source src/schema/nmdc.yaml \
		--selected-collections biosample_set \
		--selected-collections calibration_set \
		--selected-collections chemical_entity_set \
		--selected-collections collecting_biosamples_from_site_set \
		--selected-collections configuration_set \
		--selected-collections data_generation_set \
		--selected-collections data_object_set \
		--selected-collections field_research_site_set \
		--selected-collections functional_annotation_set \
		--selected-collections genome_feature_set \
		--selected-collections instrument_set \
		--selected-collections material_processing_set \
		--selected-collections processed_sample_set \
		--selected-collections protocol_execution_set \
		--selected-collections storage_process_set \
		--selected-collections study_set \
		dump-from-api \
		--client-base-url "https://api-berkeley.microbiomedata.org" \
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

.PRECIOUS: local/mongo_as_nmdc_database_validation.log

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
migration-doctests: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/partials/**/*.py
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
		'https://api-berkeley.microbiomedata.org/nmdcschema/study_set?max_page_size=999&projection=id%2Cgold_study_identifiers' \
		-H 'accept: application/json'

local/nmdc-no-use-native-uris.owl.ttl: src/schema/nmdc.yaml
	$(RUN) gen-owl --no-use-native-uris $< > $@


local/nmdc_materialized.ttl: src/schema/nmdc.yaml
	$(RUN) schema-view-relation-graph \
		--schema $< \
		--output $@

local/mongo_as_nmdc_database_cuire_repaired_stamped.ttl: local/mongo_as_nmdc_database_cuire_repaired.ttl
	$(RUN) date-created-blank-node > local/date_created_blank_node.ttl
	cat $^ local/date_created_blank_node.ttl > $@
	rm local/date_created_blank_node.ttl

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
	$(RUN) gen-plantuml \
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
	$(RUN) gen-erdiagram \
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

local/Database-interleaved-class-count.tsv: src/data/problem/valid/Database-interleaved.yaml
	cat $< | grep ' type: ' | sed 's/.*type: //' | sort | uniq -c | awk '{ OFS="\t"; $$1=$$1; print $$0 }' > $@


local/class_instantiation_counts.tsv: local/usage_template.tsv local/Database-interleaved-class-count.tsv
	$(RUN) class-instantiation-counts \
		--schemasheets-input $(word 1,$^) \
		--counts-input $(word 2,$^) \
		--output $@

.PHONY: generate-json-collections
generate-json-collections: src/data/problem/valid/Database-interleaved.yaml
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
