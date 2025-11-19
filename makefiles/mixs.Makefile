###########################################################
# MIxS Schema Import and Regeneration
###########################################################
#
# Purpose: Import and regenerate the MIxS (Minimum Information
#          about any (x) Sequence) schema components
#
# Main workflow (7-step transformation pipeline):
#   1. Extract MIxS slots from upstream source (do_shuttle)
#   2. Apply global string replacements and slot-specific transformations
#   3. Inject NMDC-specific enums (cur_land_use_enum, TargetGeneEnum)
#   4. Inject NMDC-specific annotations (environmental context triad tooltips)
#   5. Inject NMDC-specific slots (mixs_env_triad_field)
#   6. Dematerialize schema (remove redundant metadata)
#   7. Generate final src/schema/mixs.yaml
#
# Key targets:
#   src/schema/mixs.yaml: Main target - generates MIxS schema module
#   mixs-yaml-clean: Remove generated MIxS files (forces regeneration)
#   shuttle-clean: Remove all intermediate files (forces complete regeneration)
#
# Typical workflow for complete rebuild (only when expecting MIxS changes):
#   make squeaky-clean mixs-yaml-clean  # Clean all generated files
#   make src/schema/mixs.yaml           # Regenerate MIxS schema from upstream
#   make squeaky-clean all test         # Rebuild everything and run tests
#
# Dependencies:
#   - sheets_and_friends (for do_shuttle command)
#   - yq (YAML processor - system tool)
#   - Asset files:
#     - assets/import_mixs_slots_regardless.tsv (do_shuttle config)
#     - assets/yq-for-mixs_subset_modified.txt (slot transformations)
#     - assets/other_mixs_yaml_files/*.yaml (NMDC customizations)
#
###########################################################

RUN=poetry run

.PHONY: mixs-yaml-clean shuttle-clean

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified*yaml

shuttle-clean:
	# Remove all intermediate YAML files to force complete regeneration from source
	# Note: This removes the initial do_shuttle output, forcing re-extraction from upstream MIxS
	rm -rf local/mixs_regen/*.yaml
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


# Step 7: Dematerialize and generate final MIxS schema
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
	yq eval 'del(.source_file, .definition_uri, .imported_from, .metamodel_version, .source_file_date, .source_file_size, .generation_date) | del(.. | select(has("from_schema")).from_schema) | del(.. | select(has("owner")).owner) | del(.. | select(has("domain_of")).domain_of) | del(.. | select(has("is_usage_slot")).is_usage_slot) | del(.. | select(has("usage_slot_name")).usage_slot_name) | (.classes[] | select(has("annotations")).annotations) |= map_values(.value) | .prefixes |= map_values(.prefix_reference) | (.settings // {}) |= map_values(.setting_value) | (.slots[] | select(has("annotations")).annotations) |= map_values(.value) | del(.classes.[].name) | del(.classes.[].slot_usage.[].name) | del(.enums.[].name) | del(.enums.[].permissible_values.[].text) | del(.slots[] | select(.domain != "MixsCompliantData") | .domain) | del(.slots.[].name) | del(.subsets.[].name) | del(.slots[] | select(.aliases and .title and (.aliases | length == 1) and .aliases[0] == .title) | .aliases)' $(word 2,$^) > $@

# Step 1: Extract MIxS slots from upstream using do_shuttle
local/mixs_regen/mixs_subset.yaml: assets/import_mixs_slots_regardless.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

# Step 2: Apply global replacements and slot-specific transformations
local/mixs_regen/mixs_subset_modified.yaml: local/mixs_regen/mixs_subset.yaml assets/yq-for-mixs_subset_modified.txt
	# switching to TextValue may not add any value. the other range changes do improve the structure of the data.
	# ironically changing back to strings for the submission-schema, data harmonizer, submission portal etc.
	# may switch source of truth to the MIxS 6.2.2 release candidate

	# First, apply global string replacements using yq (replacing sed)
	yq eval '(.. | select(. == "quantity value")) |= "QuantityValue" | (.. | select(tag == "!!str" and . == "string")) |= "TextValue" | (.. | select(tag == "!!str" and . == "text value")) |= "TextValue"' $(word 1, $^) > $@

	# Then apply all slot-specific transformations from config file
	grep "^'" $(word 2, $^) | while IFS= read -r line ; do echo $$line ; eval yq -i $$line $@ ; done

# Step 3: Inject NMDC-specific cur_land_use_enum
local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: local/mixs_regen/mixs_subset_modified.yaml \
assets/other_mixs_yaml_files/cur_land_use_enum.yaml
	# Inject re-structured cur_land_use_enum to replace upstream version
	# Using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all 'select(fileIndex==0).enums.cur_land_use_enum = select(fileIndex==1).enums.cur_land_use_enum | select(fileIndex==0)' $^ | cat > $@

# Step 4: Inject NMDC-specific TargetGeneEnum
local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml: local/mixs_regen/mixs_subset_modified_inj_land_use.yaml \
assets/other_mixs_yaml_files/TargetGeneEnum.yaml
	# Inject TargetGeneEnum and set it as the range for target_gene slot
	yq eval-all 'select(fileIndex==0).enums.TargetGeneEnum = select(fileIndex==1).enums.TargetGeneEnum | select(fileIndex==0)' $^ | cat > $@
	yq -i '.slots.target_gene.range = "TargetGeneEnum"' $@

# Step 5: Inject NMDC-specific environmental context triad (env_triad) annotations
local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml: local/mixs_regen/mixs_subset_modified_inj_TargetGeneEnum.yaml \
assets/other_mixs_yaml_files/nmdc_mixs_env_triad_tooltips.yaml
	# Inject tooltip annotations for the MIxS environmental triad slots (env_broad_scale, env_local_scale, env_medium)
	yq eval-all 'select(fileIndex==0).slots.env_broad_scale.annotations.tooltip = select(fileIndex==1).slots.env_broad_scale.annotations.tooltip | select(fileIndex==0).slots.env_local_scale.annotations.tooltip = select(fileIndex==1).slots.env_local_scale.annotations.tooltip | select(fileIndex==0).slots.env_medium.annotations.tooltip = select(fileIndex==1).slots.env_medium.annotations.tooltip | select(fileIndex==0)' $^ | cat > $@

# Step 6: Inject NMDC-specific mixs_env_triad_field slot (environmental context triad)
local/mixs_regen/mixs_minus_1.yaml: local/mixs_regen/mixs_subset_modified_inj_env_triad.yaml \
assets/other_mixs_yaml_files/mixs_env_triad_field_slot.yaml
	# Inject custom slot for MIxS environmental context triad field handling
	yq eval-all 'select(fileIndex==0).slots.mixs_env_triad_field = select(fileIndex==1).slots.mixs_env_triad_field | select(fileIndex==0)' $^ | cat > $@
