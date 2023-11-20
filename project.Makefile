## Add your own custom Makefile targets here

JENA_PATH=~/apache-jena/bin/
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: OmicsProcessing-clean accepting-legacy-ids-all accepting-legacy-ids-clean \
dump-validate-report-convert-mongodb examples-clean linkml-validate-mongodb mixs-yaml-clean \
rdf-clean shuttle-clean squeaky-clean

OmicsProcessing-clean:
	rm -rf OmicsProcessing.tsv
	rm -rf OmicsProcessing-to-catted-Biosamples.tsv

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
		local/mongo_as_*

shuttle-clean:
	rm -rf local/mixs_regen/mixs_subset.yaml
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_subset_modified_inj_land_use.yaml
	mv $(word 2,$^) $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak

local/mixs_regen/mixs_subset.yaml: assets/other_mixs_yaml_files/mixs_slots_import_sheet.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

local/mixs_regen/mixs_subset_modified.yaml: local/mixs_regen/mixs_subset.yaml
	cp $< $@
	yq -i '.enums.SOIL_HORIZON_ENUM.permissible_values.["M horizon"] = {}'  $@
	yq -i '.id |= "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/mixs.yaml"' $@
	yq -i '.slots.biomass.range |= "TextValue"' $@
	yq -i '.slots.calcium.range |= "QuantityValue"' $@
	yq -i '.slots.carb_nitro_ratio.range |= "QuantityValue"' $@
	yq -i '.slots.chem_administration.range |= "ControlledTermValue"' $@
	yq -i '.slots.collection_date.range |= "TimestampValue"' $@
	yq -i '.slots.cur_vegetation.range |= "ControlledTermValue"' $@
	yq -i '.slots.depth.range |= "QuantityValue"' $@
	yq -i '.slots.env_broad_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_local_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_medium.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i '.slots.experimental_factor.multivalued |= "false"' $@
	yq -i '.slots.experimental_factor.range |= "ControlledTermValue"' $@
	yq -i '.slots.experimental_factor.range |= "ControlledTermValue"' $@
	yq -i '.slots.geo_loc_name.range |= "TextValue"' $@
	yq -i '.slots.gravidity.range |= "TextValue"' $@
	yq -i '.slots.growth_facil.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_age.range |= "QuantityValue"' $@
	yq -i '.slots.host_body_habitat.range |= "TextValue"' $@
	yq -i '.slots.host_body_product.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_body_site.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_common_name.range |= "TextValue"' $@
	yq -i '.slots.host_diet.multivalued |= "true"' $@
	yq -i '.slots.host_diet.range |= "TextValue"' $@
	yq -i '.slots.host_genotype.range |= "TextValue"' $@
	yq -i '.slots.host_life_stage.range |= "TextValue"' $@
	yq -i '.slots.host_taxid.range |= "ControlledTermValue"' $@
	yq -i '.slots.lat_lon.range |= "GeolocationValue"' $@
	yq -i '.slots.magnesium.range |= "QuantityValue"' $@
	yq -i '.slots.micro_biomass_meth.pattern |= ".*"' $@ # todo too liberal
	yq -i '.slots.micro_biomass_meth.structured_pattern.syntax |= ".*"' $@ # todo too liberal
	yq -i '.slots.nitrate.range |= "QuantityValue"' $@
	yq -i '.slots.nitro.range |= "QuantityValue"' $@
	yq -i '.slots.org_carb.range |= "QuantityValue"' $@
	yq -i '.slots.perturbation.multivalued |= "true"' $@
	yq -i '.slots.perturbation.range |= "TextValue"' $@
	yq -i '.slots.potassium.range |= "QuantityValue"' $@
	yq -i '.slots.salinity.range |= "QuantityValue"' $@
	yq -i '.slots.samp_size.range |= "QuantityValue"' $@
	yq -i '.slots.samp_store_temp.range |= "QuantityValue"' $@
	yq -i '.slots.samp_taxon_id.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.sieving.range |= "TextValue"' $@
	yq -i '.slots.source_mat_id.multivalued |= "false"' $@
	yq -i '.slots.source_mat_id.range |= "TextValue"' $@
	yq -i '.slots.store_cond.range |= "TextValue"' $@
	yq -i '.slots.temp.range |= "QuantityValue"' $@
	yq -i '.slots.tot_nitro.range |= "QuantityValue"' $@
	yq -i '.slots.tot_nitro.range |= "QuantityValue"' $@
	yq -i '.slots.tot_nitro_content.range |= "QuantityValue"' $@
	yq -i '.slots.tot_org_carb.range |= "QuantityValue"' $@
	yq -i '.slots.tot_phosp.range |= "QuantityValue"' $@
	yq -i '.slots.water_content.pattern |= ".*"' $@ # todo too liberal
	yq -i '.slots.water_content.structured_pattern.syntax |= ".*"' $@ # todo too liberal
	yq -i 'del(.classes)'  $@
	yq -i 'del(.enums.[].name)'  $@
	yq -i 'del(.enums.[].permissible_values.[].text)'  $@
	yq -i 'del(.slots.[].name)'  $@
	yq -i 'del(.slots.[].required)' $@
	yq -i 'del(.subsets.[].name)'  $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: assets/other_mixs_yaml_files/cur_land_use_enum.yaml local/mixs_regen/mixs_subset_modified.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all \
		'select(fileIndex==1).enums.cur_land_use_enum = select(fileIndex==0).enums.cur_land_use_enum | select(fileIndex==1)' \
		$^ | cat > $@

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

local/usage_template.tsv: src/schema/nmdc.yaml
	mkdir -p $(@D)
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --destination-template $@ \
		 --meta-model-excel-file local/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
 		 --columns-to-insert slot \
		 --source-schema-path $<

examples/output/Biosample-exhasutive_report.yaml: src/data/Biosample-exhasutive.yaml
	poetry run exhaustion-check \
		--class-name Biosample \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path src/schema/nmdc.yaml


examples/output/Pooling-minimal-report.yaml: src/data/valid/Pooling-minimal.yaml
	poetry run exhaustion-check \
		--class-name Pooling \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path src/schema/nmdc.yaml

examples/output/Biosample-exhasutive-pretty-sorted.yaml: src/data/Biosample-exhasutive.yaml
	poetry run pretty-sort-yaml \
		-i $< \
		-o $@

# # # #

local/envo.db:
	$(RUN) semsql download envo -o $@

# # # #

#local/nlcd_2019_land_cover_l48_20210604.xml:
#	curl -o $@ https://www.mrlc.gov/downloads/sciweb1/shared/mrlc/metadata/nlcd_2019_land_cover_l48_20210604.xml
#
#
#local/nlcd_2019_land_cover_l48_20210604.yaml: local/nlcd_2019_land_cover_l48_20210604.xml
#	yq -p=xml -oy '.' $< > $@
#
#
#local/neon-nlcd-envo-mappings.tsv: local/nlcd_2019_land_cover_l48_20210604.yaml local/envo.db
#	$(RUN)  get_neon-nlcd-envo-mapping \
#		--nlcd-yaml $(word 1, $^) \
#		--envo-sqlite $(word 2, $^) \
#		--neon-nlcd-envo-mappings-tsv $@
#
#local/neon-soil-order-envo-mapping.tsv:
#	$(RUN) python nmdc_schema/neon-soil-order-envo-mapping.py

# # # #

accepting-legacy-ids-all: accepting-legacy-ids-clean \
nmdc_schema/nmdc_schema_accepting_legacy_ids.schema.json nmdc_schema/nmdc_schema_accepting_legacy_ids.py

# --useuris / --metauris
nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml: src/schema/nmdc.yaml
	$(RUN) gen-linkml \
		--format yaml \
		--mergeimports \
		--metadata \
		--no-materialize-attributes \
		--no-materialize-patterns \
		--useuris \
		--output $@ $<
	# probably should have made a list of classes and then looped over a parameterized version of this
	# could also assert that the range is string
	yq -i '(.classes[] | select(.name == "Biosample") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "Biosample") | .slot_usage.part_of.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "Biosample") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "DataObject") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "DataObject") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MagsAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MagsAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetabolomicsAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetabolomicsAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeAnnotationActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeAnnotationActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeAssembly") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeAssembly") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeSequencingActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetagenomeSequencingActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetaproteomicsAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetaproteomicsAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeAnnotationActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeAnnotationActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeAssembly") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "MetatranscriptomeAssembly") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "NomAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "NomAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "OmicsProcessing") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "OmicsProcessing") | .slot_usage.part_of.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "OmicsProcessing") | .slot_usage.has_input.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "OmicsProcessing") | .slot_usage.has_output.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "OmicsProcessing") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "ReadBasedTaxonomyAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "ReadBasedTaxonomyAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "ReadQcAnalysisActivity") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "ReadQcAnalysisActivity") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@
	yq -i '(.classes[] | select(.name == "Study") | .slot_usage.id.pattern) = ".*"' $@
	yq -i '(.classes[] | select(.name == "Study") | .slot_usage.id.structured_pattern.syntax) = ".*"' $@


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

make-rdf: rdf-clean local/mongo_as_nmdc_database_validation.log local/mongo_as_nmdc_database_cuire_repaired.ttl

# could also check --client-base-url https://api-napa.microbiomedata.org
# but separate validate-filtered-request-all is available for that now

# todo also notes about large collections: functional_annotation_agg and metaproteomics_analysis_activity_set



local/mongo_as_unvalidated_nmdc_database.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) pure-export \
		--client-base-url https://api.microbiomedata.org \
		--endpoint-prefix nmdcschema \
		--env-file local/.env \
		--max-docs-per-coll 1000000000 \
		--mongo-db-name nmdc \
		--mongo-host localhost \
		--mongo-port 27777 \
		--output-yaml $@ \
		--page-size 200000 \
		--schema-file src/schema/nmdc.yaml \
		--selected-collections data_object_set \
		--selected-collections biosample_set \
		--selected-collections extraction_set \
		--selected-collections field_research_site_set \
		--selected-collections library_preparation_set \
		--selected-collections mags_activity_set \
		--selected-collections metabolomics_analysis_activity_set \
		--selected-collections metagenome_annotation_activity_set \
		--selected-collections metagenome_assembly_set \
		--selected-collections metagenome_sequencing_activity_set  \
		--selected-collections metatranscriptome_activity_set \
		--selected-collections nom_analysis_activity_set \
		--selected-collections omics_processing_set \
		--selected-collections pooling_set \
		--selected-collections processed_sample_set \
		--selected-collections read_based_taxonomy_analysis_activity_set \
		--selected-collections read_qc_analysis_activity_set \
		--selected-collections study_set \
		--skip-collection-check

local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date # 449.56 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) migration-recursion \
		--schema-path $(word 1,$^) \
		--input-path $(word 2,$^) \
		--salvage-prefix generic \
		--output-path $@

.PRECIOUS: local/mongo_as_nmdc_database_validation.log

# make local/mongo_as_nmdc_database_rdf_safe.yaml ; linkml-validate \
#	--schema nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml \
#	local/mongo_as_nmdc_database_rdf_safe.yaml > local/mongo_as_nmdc_database_validation.log

local/mongo_as_nmdc_database_validation.log: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml mongo_as_nmdc_database_rdf_safe.yaml
	# nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml or nmdc_schema/nmdc_materialized_patterns.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-validate --schema $^ > $@

local/mongo_as_nmdc_database.ttl: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml mongo_as_nmdc_database_rdf_safe.yaml
	date # 681.99 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-convert --output $@ --schema $^
	export _JAVA_OPTIONS=-Djava.io.tmpdir=local
	- $(JENA_PATH)/riot --validate $@ # < 1 minute

# todo: still getting anyurl typed string statement objects in RDF. I added a workarround in anyuri-strings-to-iris
local/mongo_as_nmdc_database_cuire_repaired.ttl: local/mongo_as_nmdc_database.ttl
	date
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--emsl-uuid-replacement emsl_uuid_like \
		--output-ttl $@
	export _JAVA_OPTIONS=-Djava.io.tmpdir=local
	- $(JENA_PATH)/riot --validate $@ # < 1 minute
	date

# ----

OmicsProcessing-to-catted-Biosamples.tsv: assets/sparql/OmicsProcessing-to-catted-Biosamples.rq nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) class-sparql \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--query-file $<

assets/sparql/undesc-ununsed-slots.tsv: assets/sparql/undesc-ununsed-slots.rq nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) class-sparql \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--query-file $<

OmicsProcessing-all: OmicsProcessing-clean OmicsProcessing.tsv OmicsProcessing-to-catted-Biosamples.tsv

OmicsProcessing.tsv: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) class-sparql  \
		--concatenation-suffix s \
		--do-group-concat \
		--graph-name "mongodb://mongo-loadbalancer.nmdc.production.svc.spin.nersc.gov:27017" \
		--jsonld-context-jsons project/jsonld/nmdc.context.jsonld \
		--schema-file  $< \
		--target-class-name $(firstword $(subst ., ,$(lastword $(subst /, ,$@)))) \
		--target-p-o-constraint "dcterms:isPartOf nmdc:sty-11-34xj1150"

validate-filtered-request-all: validate-filtered-request-clean assets/filtered-api-requests/filtered-request-validation-log.txt

.PHONY: validate-filtered-request-all validate-filtered-request-clean

validate-filtered-request-clean:
	rm -rf assets/filtered-api-requests/*

# user is responsible for providing pre-tested, properly escaped, filtered https://api-napa.microbiomedata.org/docs#/metadata requests
# todo: explicitly running this through the python interpreter emits less logging
assets/filtered-api-requests/filtered-request-result.yaml:
	$(RUN) build-datafile-from-api-requests \
		--output-file $@ \
		--api-url "https://api-napa.microbiomedata.org/nmdcschema/study_set?filter=%7B%22id%22%3A%22nmdc%3Asty-11-aygzgv51%22%7D&max_page_size=999999" \
		--api-url "https://api-napa.microbiomedata.org/nmdcschema/biosample_set?filter=%7B%22part_of%22%3A%22nmdc%3Asty-11-aygzgv51%22%7D&max_page_size=999999" \
		--api-url "https://api-napa.microbiomedata.org/nmdcschema/omics_processing_set?filter=%7B%22part_of%22%3A%22nmdc%3Asty-11-aygzgv51%22%7D&max_page_size=999999"

assets/filtered-api-requests/filtered-request-validation-log.txt: nmdc_schema/nmdc_materialized_patterns.yaml \
assets/filtered-api-requests/filtered-request-result.yaml
	- $(RUN) linkml-validate --schema $^ > $@

.PHONY: validate-polymorphic

validate-polymorphic:
	$(RUN) linkml-validate \
		--include-range-class-descendants \
		--schema src/schema/nmdc.yaml src/data/polymorphic-valid/Database-polymorphic-planned-process-set.yaml

.PHONY: migration-doctests
migration-doctests:
	$(RUN) python -m doctest -v nmdc_schema/migrators/migrator_from_A_B_C_to_X_Y_Z.py