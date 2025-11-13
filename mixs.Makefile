###########################################################
# MIxS Schema Import and Regeneration
###########################################################
#
# Purpose: Import and regenerate the MIxS (Minimum Information
#          about any (x) Sequence) schema components
#
# Main workflow:
#   1. Extract MIxS slots from upstream source (do_shuttle)
#   2. Apply transformations and modifications
#   3. Inject NMDC-specific enums and annotations
#   4. Generate final src/schema/mixs.yaml
#
# Key targets:
#   mixs-yaml-clean: Remove generated MIxS files (forces regeneration)
#   src/schema/mixs.yaml: Main target - generates MIxS schema module
#
# Dependencies:
#   - sheets_and_friends (for do_shuttle)
#   - yq (YAML processor)
#   - Various asset files in assets/
#
###########################################################

RUN=poetry run

.PHONY: mixs-yaml-clean shuttle-clean

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified*yaml

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
	yq eval '(.. | select(. == "quantity value")) |= "QuantityValue" | (.. | select(tag == "!!str" and . == "string")) |= "TextValue" | (.. | select(tag == "!!str" and . == "text value")) |= "TextValue"' $(word 1, $^) > $@

	# Then apply all slot-specific transformations from config file
	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: local/mixs_regen/mixs_subset_modified.yaml \
assets/other_mixs_yaml_files/cur_land_use_enum.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all 'select(fileIndex==0).enums.cur_land_use_enum = select(fileIndex==1).enums.cur_land_use_enum | select(fileIndex==0)' $^ | cat > $@

local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml: local/mixs_regen/mixs_subset_modified_inj_land_use.yaml \
assets/other_mixs_yaml_files/TargetGeneEnum.yaml
	yq eval-all 'select(fileIndex==0).enums.TargetGeneEnum = select(fileIndex==1).enums.TargetGeneEnum | select(fileIndex==0)' $^ | cat > $@
	yq -i '.slots.target_gene.range = "TargetGeneEnum"' $@


local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml: local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	# Inject all three environment triad tooltips in a single step
	yq eval-all 'select(fileIndex==0).slots.env_broad_scale.annotations.tooltip = select(fileIndex==1).slots.env_broad_scale.annotations.tooltip | select(fileIndex==0).slots.env_local_scale.annotations.tooltip = select(fileIndex==1).slots.env_local_scale.annotations.tooltip | select(fileIndex==0).slots.env_medium.annotations.tooltip = select(fileIndex==1).slots.env_medium.annotations.tooltip | select(fileIndex==0)' $^ | cat > $@

local/mixs_regen/mixs_minus_1.yaml: local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml \
assets/other_mixs_yaml_files/mixs_env_triad_field_slot.yaml
	yq eval-all 'select(fileIndex==0).slots.mixs_env_triad_field = select(fileIndex==1).slots.mixs_env_triad_field | select(fileIndex==0)' $^ | cat > $@
