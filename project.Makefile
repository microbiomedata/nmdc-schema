## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

assets/mixs_slots_used_in_schema.tsv:
	$(RUN) get_mixs_slots_used_in_schema --output_file $@

assets/import_slots_regardless_gen.tsv: assets/mixs_slots_used_in_schema.tsv
	$(RUN) generate_import_slots_regardless --input_file $< --output_file $@

assets/mixs_subset.yaml: assets/import_slots_regardless_gen.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

assets/mixs_subset_repaired.yaml: assets/mixs_subset.yaml
	sed 's/quantity value/QuantityValue/' $< > $@
	sed -i.bak 's/range: string/range: TextValue/' $@
	sed -i.bak 's/slot_uri: MIXS:/slot_uri: mixs:/' $@
	yq -i '.slots.env_broad_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_local_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_medium.range |= "ControlledIdentifiedTermValue"'  $@
#	yq -i 'del(.classes.Biosample)' $(word 2,$^)
#	yq -i 'del(.classes.OmicsProcesing)' $(word 2,$^)
	yq -i 'del(.enums.[].name)'  $@
	yq -i 'del(.slots.[].name)'  $@

mixs_diff_cleanup:
	rm -rf assets/import_slots_regardless_gen.tsv
	rm -rf assets/mixs_slots_used_in_schema.tsv
	rm -rf assets/mixs_subset.yaml
	rm -rf assets/mixs_subset_repaired.yaml
	rm -rf assets/mixs_subset_repaired.yaml.bak

.PHONY: deepdiff

deepdiff: assets/mixs_subset_repaired.yaml
	$(RUN) deep diff src/schema/mixs.yaml $<

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