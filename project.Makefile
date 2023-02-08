## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: mixs_deepdiff shuttle_cleanup

shuttle_cleanup:
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

assets/mixs_regen/mixs_slots_used_in_schema.tsv:
	$(RUN) get_mixs_slots_used_in_schema --output_file $@

assets/mixs_regen/slots_associated_with_biosample.tsv:
	$(RUN) get_slots_from_class --class_name Biosample --output_file $@

assets/mixs_regen/slots_associated_with_omics_processing.tsv:
	$(RUN) get_slots_from_class --class_name OmicsProcessing --output_file $@

assets/mixs_regen/slots_associated_with_biosample_omics_processing.tsv: \
assets/mixs_regen/slots_associated_with_biosample.tsv \
assets/mixs_regen/slots_associated_with_omics_processing.tsv
	cat $^ > $@

assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv: \
assets/mixs_regen/slots_associated_with_biosample_omics_processing.tsv
	$(RUN) get_mixs_slots_matching_slot_list \
		--slot_list_file $< \
		--output_file $@

assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing_augmented.tsv: \
assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv
	cp $< $@
	echo "rel_to_oxygen" >> $@
	echo "abs_air_humidity" >> $@


assets/mixs_regen/import_slots_regardless_gen.tsv: \
assets/mixs_regen/mixs_slots_associated_with_biosample_omics_processing_augmented.tsv
	$(RUN) generate_import_slots_regardless --input_file $< --output_file $@

assets/mixs_regen/mixs_subset.yaml: assets/mixs_regen/import_slots_regardless_gen.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

src/schema/mixs.yaml: assets/mixs_regen/mixs_subset.yaml
	mv src/schema/mixs.yaml src/schema/mixs.yaml.bak
	sed 's/quantity value/QuantityValue/' $< > $@
	sed -i.bak 's/range: string/range: TextValue/' $@
	#sed -i.bak 's/slot_uri: MIXS:/slot_uri: mixs:/' $@
	#sed -i.bak 's/slot_uri: mixs:/slot_uri: MIXS:/' $@
	yq -i '.slots.env_broad_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_local_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_medium.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i 'del(.classes)' $@
	yq -i 'del(.enums.[].name)'  $@
	yq -i 'del(.slots.[].name)'  $@
	rm -rf assets/mixs_subset_repaired.yaml.bak

mixs_deepdiff: src/schema/mixs.yaml
	mv src/schema/mixs.yaml.bak src/schema/mixs.bak.yaml
	$(RUN) deep diff src/schema/mixs.bak.yaml $^
	mv src/schema/mixs.bak.yaml src/schema/mixs.yaml.bak

#examples-all: examples-clean src/data/output
#
#examples-clean:
#	rm -rf src/data/output project/nmdc_schema_generated.yaml
#
#project/nmdc_schema_generated.yaml: $(SOURCE_SCHEMA_PATH)
#	# the need for this may be eliminated by adding mandatory pattern materialization to gen-json-schema
#	$(RUN) gen-linkml \
#		--output $@ \
#		--materialize-patterns \
#		--no-materialize-attributes \
#		--format yaml $<
#
#src/data/output: project/nmdc_schema_generated.yaml
#	mkdir -p $@
#	$(RUN) linkml-run-examples \
#		--schema $< \
#		--input-directory src/data/valid \
#		--counter-example-input-directory src/data/invalid \
#		--output-directory $@ > $@/README.md
#

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