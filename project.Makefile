## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: mixs-deepdiff shuttle_cleanup

## these get_slots_from_class operations aren't very useful
##  they only get class/slot assignments from the last nmdc_schema/nmdc_schema_merged.yaml
#assets/mixs_regen/slots_associated_with_biosample.tsv:
#	$(RUN) get_slots_from_class --class_name Biosample --output_file $@
#
#assets/mixs_regen/slots_associated_with_omics_processing.tsv:
#	$(RUN) get_slots_from_class --class_name OmicsProcessing --output_file $@

assets/MIxS_6_term_updates_MIxS6_Core-_Final_clean.tsv:
	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=178015749&format=tsv" > $@

assets/MIxS_6_term_updates_MIxS6_packages_-_Final_clean.tsv:
	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=750683809&format=tsv" > $@

assets/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv:
	curl -L "https://docs.google.com/spreadsheets/d/1_TSuvEUX68g_o3r1d9wvOYMMbZ3vO4eluvAd2wNJoSU/export?gid=1742830620&format=tsv" > $@

assets/slot_annotations_diffs.tsv: assets/other_mixs_yaml_files/mixs_new.yaml assets/other_mixs_yaml_files/mixs_legacy.yaml
	$(RUN) mixs_deep_diff \
		--include_descriptions True \
		--shingle_size 2 \
		--current_mixs_module_in $< \
		--legacy_mixs_module_in $(word 2,$^)  \
		--anno_diff_tsv_out $@ \
		--slot_diff_yaml_out $(patsubst %.tsv,%.yaml,$@)

assets/slot_roster.tsv:
	$(RUN) slot_roster \
		--input_paths "https://raw.githubusercontent.com/microbiomedata/sheets_and_friends/main/artifacts/nmdc_submission_schema.yaml" \
		--input_paths "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/main/model/schema/mixs.yaml" \
		--input_paths "src/schema/nmdc.yaml" \
		--output_tsv $@

assets/MIxS_6_term_updates_dtm.tsv: \
assets/MIxS_6_term_updates_MIxS6_Core-_Final_clean.tsv \
assets/MIxS_6_term_updates_MIxS6_packages_-_Final_clean.tsv
	$(RUN) mixs_slot_text_mining \
		--core_file $< \
		--packages_file $(word 2,$^) \
		--output_file $@

assets/mixs_slots_by_submission_class.tsv: assets/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv
	$(RUN) mixs_coverage \
  		--in_file $< \
  		--out_file $@

assets/boolean_usages.tsv:
	$(RUN) boolean_usages \
		--out_file $@

MIXS_YAML_FROM_SHEETS_AND_FRIENDS = src/schema/mixs.yaml
MIXS_YAML_MARK_OLDER_PYTHON = src/schema/mixs_new.yaml
MIXS_YAML_PERL_CURATED_Q = src/schema/other_mixs_yaml_files/mixs_legacy.yaml

SCHEMA_FILE = $(MIXS_YAML_FROM_SHEETS_AND_FRIENDS)

schemasheets/populated_tsv/slots.tsv:
	$(RUN) linkml2sheets \
		--output-directory $(dir $@) \
		--schema $(SCHEMA_FILE) schemasheets/schemasheets_templates/slots.tsv

missing_slots_from_exhaustive_data::
	$(RUN) python nmdc_schema/still_not_exhasutive.py


####################################################################################################

.PHONY: nmdc-mixs-update

nmdc-mixs-update: mixs-module-all nmdc-schema-usages-all

####################################################################################################

.PHONY: mixs-cleanup

mixs-module-all: mixs-module-cleanup src/schema/mixs.yaml

mixs-module-cleanup:
	rm -rf assets/mixs_regen/import_slots_regardless_gen.tsv
	rm -rf assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv
	rm -rf assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing_augmented.tsv
	rm -rf assets/mixs_regen/mixs_slots_used_in_schema.tsv
	rm -rf assets/mixs_regen/mixs_subset.yaml
	rm -rf assets/mixs_regen/mixs_subset_repaired.yaml
	rm -rf assets/mixs_regen/mixs_subset_repaired.yaml.bak
	rm -rf assets/mixs_regen/slots_associated_with_biosample.tsv
	rm -rf assets/mixs_regen/slots_associated_with_biosample_omics_processing.tsv
	rm -rf assets/mixs_regen/slots_associated_with_omics_processing.tsv
	mkdir -p assets/mixs_regen
	echo "do not delete this placeholder file" > assets/mixs_regen/placeholder.txt
	rm -rf src/schema/mixs.yaml
	rm -rf src/schema/mixs.yaml.bak

# the next several targets get slot lists from the Google sheets
# switch to GSC's mixs.ysml from XXX or the released Excel file
assets/mixs_regen/slots_associated_with_biosample.tsv: src/schema/nmdc.yaml
	yq '.classes.Biosample.slots.[]' $< > $@

assets/mixs_regen/slots_associated_with_omics_processing.tsv: src/schema/nmdc.yaml
	yq '.classes.OmicsProcessing.slots.[]' $< > $@

assets/mixs_regen/slots_associated_with_biosample_omics_processing.tsv: \
assets/mixs_regen/slots_associated_with_biosample.tsv \
assets/mixs_regen/slots_associated_with_omics_processing.tsv
	cat $^ > $@

assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv: \
assets/mixs_regen/slots_associated_with_biosample_omics_processing.tsv
	$(RUN) get_mixs_slots_matching_slot_list \
		--slot_list_file $< \
		--output_file $@

assets/mixs_regen/import_slots_regardless_gen.tsv: \
assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv
	$(RUN) generate_import_slots_regardless --input_file $< --output_file $@

# this gets slot contents from the GSC mixs.yaml, not the Google sheets
assets/mixs_regen/mixs_subset.yaml: assets/mixs_regen/import_slots_regardless_gen.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

src/schema/mixs.yaml: assets/mixs_regen/mixs_subset.yaml
	sed 's/quantity value/QuantityValue/' $< > $@
	sed -i.bak 's/range: text value/range: TextValue/' $@
	yq -i 'del(.classes)' $@
	yq -i 'del(.enums.[].name)'  $@
	yq -i 'del(.enums.[].permissible_values.[].text)'  $@
	yq -i 'del(.slots.[].name)'  $@
	yq -i 'del(.subsets.[].name)'  $@
	rm -rf assets/mixs_subset_repaired.yaml.bak
	rm -rf src/schema/mixs.yaml.bak

####################################################################################################


mixs-deepdiff: src/schema/mixs.yaml
	mv src/schema/mixs.yaml.bak src/schema/mixs.bak.yaml
	$(RUN) deep diff src/schema/mixs.bak.yaml $^
	mv src/schema/mixs.bak.yaml src/schema/mixs.yaml.bak

####################################################################################################

.PHONY: nmdc-schema-usages-all nmdc-schema-cleanup

nmdc-schema-usages-all: nmdc-usages-cleanup src/schema/nmdc_with_bs_usages.yaml
	mv src/schema/nmdc_with_bs_usages.yaml src/schema/nmdc.yaml

nmdc-usages-cleanup:
	rm -rf src/schema/nmdc.yaml.bak
	rm -rf src/schema/nmdc_with_bs_usages.yaml
	rm -rf src/schema/nmdc_with_usages.yaml
	cp src/schema/nmdc.yaml src/schema/nmdc.yaml.bak
	$(RUN) python nmdc_schema/remove_usages_keep_comments.py
	mv src/schema/nmdc_no_bs_usage.yaml src/schema/nmdc.yaml
	rm -rf src/schema/nmdc_no_bs_usage.yaml

src/schema/nmdc_with_bs_usages.yaml: src/schema/nmdc.yaml
	$(RUN) modifications_and_validation \
		--yaml_input $< \
		--modifications_config_tsv assets/other_mixs_yaml_files/sheets-for-nmdc-submission-schema-modifications_long.tsv \
		--validation_config_tsv assets/other_mixs_yaml_files/blank_validation_converter.tsv \
		--yaml_output $@

####################################################################################################

examples-all: examples-clean src/data/output

examples-clean:
	@echo running examples-clean
	rm -rf src/data/output project/nmdc_*.yaml

project/nmdc_schema_merged.yaml:
	$(RUN) gen-linkml \
		--format yaml \
		--no-materialize-attributes \
		--no-materialize-patterns \
		--output $@ $(SOURCE_SCHEMA_PATH)

project/nmdc_materialized_patterns.yaml:
	$(RUN) gen-linkml \
		--format yaml \
		--materialize-patterns \
		--no-materialize-attributes \
		--output $@ $(SOURCE_SCHEMA_PATH)

project/nmdc_materialized_patterns.schema.json: project/nmdc_materialized_patterns.yaml
	$(RUN) gen-json-schema \
		--closed \
		--top-class Database $< > $@

src/data/output: project/nmdc_materialized_patterns.yaml
	@echo making src/data/output
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--counter-example-input-directory src/data/invalid \
		--input-directory src/data/valid \
		--output-directory $@ \
		--schema $< > $@/README.md


