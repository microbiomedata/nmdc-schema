## Add your own custom Makefile targets here
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: OmicsProcessing-clean accepting-legacy-ids-all accepting-legacy-ids-clean \
dump-validate-report-convert-mongodb examples-clean linkml-validate-mongodb mixs-yaml-clean mixs-deepdiff \
mongodb-clean rdf-clean shuttle-clean squeaky-clean

OmicsProcessing-clean:
	rm -rf OmicsProcessing.tsv

accepting-legacy-ids-clean:
	rm -rf nmdc_schema/nmdc_schema_accepting_legacy_ids*

examples-clean:
	rm -rf examples/output

mixs-yaml-clean:
	rm -rf src/schema/mixs.yaml
	rm -rf local/mixs_regen/mixs_subset_modified.yaml

mongodb-clean:
	date
	rm -rf local/mongo_as_nmdc_database*
	rm -rf local/mongo_as_unvalidated_nmdc_database.yaml

rdf-clean:
	rm -rf \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_validation.log \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_unvalidated_nmdc_database.yaml

shuttle-clean:
	rm -rf local/mixs_regen/import_slots_regardless_gen.tsv
	rm -rf local/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv
	rm -rf local/mixs_regen/mixs_slots_associated_with_biosample_omics_processing_augmented.tsv
	rm -rf local/mixs_regen/mixs_slots_used_in_schema.tsv
	rm -rf local/mixs_regen/mixs_subset.yaml
	#rm -rf local/mixs_regen/mixs_subset_modified.yaml # triggers complete regeneration
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak
	rm -rf local/mixs_regen/mixs_subset_repaired.yaml
	rm -rf local/mixs_regen/mixs_subset_repaired.yaml.bak
	rm -rf local/mixs_regen/slots_associated_with_biosample.tsv
	rm -rf local/mixs_regen/slots_associated_with_biosample_omics_processing.tsv
	rm -rf local/mixs_regen/slots_associated_with_omics_processing.tsv
	mkdir -p local/mixs_regen
	touch local/mixs_regen/.gitkeep


src/schema/mixs.yaml: shuttle-clean local/mixs_regen/mixs_subset_modified_inj_land_use.yaml
	mv $(word 2,$^) $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak

local/mixs_regen/slots_associated_with_biosample.tsv:
	yq '.classes.Biosample.slots.[]' src/schema/nmdc.yaml | sort | cat > $@

local/mixs_regen/slots_associated_with_omics_processing.tsv:
	yq '.classes.OmicsProcessing.slots.[]' src/schema/nmdc.yaml | sort | cat > $@

local/mixs_regen/slots_associated_with_biosample_omics_processing.tsv: \
local/mixs_regen/slots_associated_with_biosample.tsv \
local/mixs_regen/slots_associated_with_omics_processing.tsv
	cat $^ > $@

local/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv: \
local/mixs_regen/slots_associated_with_biosample_omics_processing.tsv
	$(RUN) get-mixs-slots-matching-slot-list \
		--slot_list_file $< \
		--output_file $@

local/mixs_regen/import_slots_regardless_gen.tsv: \
local/mixs_regen/mixs_slots_associated_with_biosample_omics_processing.tsv
	$(RUN) generate-import-slots-regardless --input_file $< --output_file $@

local/mixs_regen/mixs_subset.yaml: local/mixs_regen/import_slots_regardless_gen.tsv
	$(RUN) do_shuttle \
		--recipient_model assets/other_mixs_yaml_files/mixs_template.yaml \
		--config_tsv $< \
		--yaml_output $@

local/mixs_regen/mixs_subset_modified.yaml: local/mixs_regen/mixs_subset.yaml
	# the majority of operations
	# change the https://github.com/GenomicsStandardsConsortium/mixs/blob/main/model/schema/mixs.yaml ranges
	# to match https://github.com/microbiomedata/nmdc-schema/blame/e681592b20f98dab0cf89278b2b3c2f5e0754adf/src/schema/mixs.yaml
	#   from Apr 2022 ?
	sed 's/quantity value/QuantityValue/' $< > $@
	sed -i.bak 's/range: string/range: TextValue/' $@
	sed -i.bak 's/range: text value/range: TextValue/' $@

	yq -i '.slots.agrochem_addition.range |= "TextValue"' $@
	yq -i '.slots.air_temp_regm.range |= "TextValue"' $@
	yq -i '.slots.antibiotic_regm.range |= "TextValue"' $@
	yq -i '.slots.aromatics_pc.range |= "TextValue"' $@
	yq -i '.slots.asphaltenes_pc.range |= "TextValue"' $@
	yq -i '.slots.atmospheric_data.range |= "TextValue"' $@
	yq -i '.slots.avg_occup.range |= "TextValue"' $@
	yq -i '.slots.bathroom_count.range |= "TextValue"' $@
	yq -i '.slots.bedroom_count.range |= "TextValue"' $@
	yq -i '.slots.biocide_admin_method.range |= "TextValue"' $@
	yq -i '.slots.biomass.range |= "TextValue"' $@
	yq -i '.slots.chem_administration.range |= "ControlledTermValue"' $@
	yq -i '.slots.chem_mutagen.range |= "TextValue"' $@
	yq -i '.slots.chem_treat_method.range |= "string"' $@
	yq -i '.slots.collection_date.range |= "TimestampValue"' $@
	yq -i '.slots.cool_syst_id.range |= "TextValue"' $@
	yq -i '.slots.date_last_rain.range |= "TimestampValue"' $@
	yq -i '.slots.diether_lipids.range |= "TextValue"' $@
	yq -i '.slots.elevator.range |= "TextValue"' $@
	yq -i '.slots.emulsions.range |= "TextValue"' $@
	yq -i '.slots.env_broad_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_local_scale.range |= "ControlledIdentifiedTermValue"' $@
	yq -i '.slots.env_medium.range |= "ControlledIdentifiedTermValue"'  $@
	yq -i '.slots.escalator.range |= "TextValue"' $@
	yq -i '.slots.exp_pipe.range |= "QuantityValue"' $@
	yq -i '.slots.experimental_factor.range |= "ControlledTermValue"' $@
	yq -i '.slots.ext_door.range |= "TextValue"' $@
	yq -i '.slots.extreme_event.range |= "TimestampValue"' $@
	yq -i '.slots.fertilizer_regm.range |= "TextValue"' $@
	yq -i '.slots.fire.range |= "TimestampValue"' $@
	yq -i '.slots.flooding.range |= "TimestampValue"' $@
	yq -i '.slots.floor_count.range |= "TextValue"' $@
	yq -i '.slots.freq_clean.range |= "QuantityValue"' $@
	yq -i '.slots.freq_cook.range |= "QuantityValue"' $@
	yq -i '.slots.fungicide_regm.range |= "TextValue"' $@
	yq -i '.slots.gaseous_environment.range |= "TextValue"' $@
	yq -i '.slots.gaseous_substances.range |= "TextValue"' $@
	yq -i '.slots.gravity.range |= "TextValue"' $@
	yq -i '.slots.growth_facil.range |= "ControlledTermValue"' $@
	yq -i '.slots.growth_hormone_regm.range |= "TextValue"' $@
	yq -i '.slots.hall_count.range |= "TextValue"' $@
	yq -i '.slots.hall_count.range |= "TextValue"' $@
	yq -i '.slots.hcr_pressure.range |= "TextValue"' $@
	yq -i '.slots.hcr_temp.range |= "TextValue"' $@
	yq -i '.slots.heat_sys_deliv_meth.range |= "string"' $@
	yq -i '.slots.heat_system_id.range |= "TextValue"' $@
	yq -i '.slots.heavy_metals.range |= "TextValue"' $@
	yq -i '.slots.herbicide_regm.range |= "TextValue"' $@
	yq -i '.slots.host_body_product.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_body_site.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_family_relation.range |= "string"' $@
	yq -i '.slots.host_phenotype.range |= "ControlledTermValue"' $@
	yq -i '.slots.host_subspecf_genlin.range |= "string"' $@
	yq -i '.slots.host_symbiont.range |= "string"' $@
	yq -i '.slots.humidity_regm.range |= "TextValue"' $@
	yq -i '.slots.inorg_particles.range |= "TextValue"' $@
	yq -i '.slots.iw_bt_date_well.range |= "TimestampValue"' $@
	yq -i '.slots.last_clean.range |= "TimestampValue"' $@
	yq -i '.slots.lat_lon.range |= "GeolocationValue"' $@
	yq -i '.slots.light_regm.range |= "TextValue"' $@
	yq -i '.slots.max_occup.range |= "QuantityValue"' $@
	yq -i '.slots.micro_biomass_meth.range |= "string"' $@
	yq -i '.slots.mineral_nutr_regm.range |= "TextValue"' $@
	yq -i '.slots.misc_param.range |= "TextValue"' $@
	yq -i '.slots.n_alkanes.range |= "TextValue"' $@
	yq -i '.slots.non_min_nutr_regm.range |= "string"' $@
	yq -i '.slots.number_pets.range |= "QuantityValue"' $@
	yq -i '.slots.number_plants.range |= "QuantityValue"' $@
	yq -i '.slots.number_resident.range |= "QuantityValue"' $@
	yq -i '.slots.occup_density_samp.range |= "QuantityValue"' $@
	yq -i '.slots.occup_samp.range |= "QuantityValue"' $@
	yq -i '.slots.org_count_qpcr_info.range |= "string"' $@
	yq -i '.slots.org_particles.range |= "TextValue"' $@
	yq -i '.slots.organism_count.range |= "QuantityValue"' $@
	yq -i '.slots.particle_class.range |= "TextValue"' $@
	yq -i '.slots.permeability.range |= "TextValue"' $@
	yq -i '.slots.pesticide_regm.range |= "TextValue"' $@
	yq -i '.slots.phaeopigments.range |= "TextValue"' $@
	yq -i '.slots.phosplipid_fatt_acid.range |= "TextValue"' $@
	yq -i '.slots.plant_growth_med.range |= "ControlledTermValue"' $@
	yq -i '.slots.plant_struc.range |= "ControlledTermValue"' $@
	yq -i '.slots.pollutants.range |= "TextValue"' $@
	yq -i '.slots.porosity.range |= "TextValue"' $@
	yq -i '.slots.pres_animal_insect.range |= "string"' $@
	yq -i '.slots.prev_land_use_meth.range |= "string"' $@
	yq -i '.slots.prod_start_date.range |= "TimestampValue"' $@
	yq -i '.slots.radiation_regm.range |= "TextValue"' $@
	yq -i '.slots.rainfall_regm.range |= "TextValue"' $@
	yq -i '.slots.resins_pc.range |= "TextValue"' $@
	yq -i '.slots.room_architec_elem.range |= "string"' $@
	yq -i '.slots.room_count.range |= "TextValue"' $@
	yq -i '.slots.room_dim.range |= "TextValue"' $@
	yq -i '.slots.room_door_dist.range |= "TextValue"' $@
	yq -i '.slots.room_net_area.range |= "TextValue"' $@
	yq -i '.slots.room_occup.range |= "QuantityValue"' $@
	yq -i '.slots.room_vol.range |= "TextValue"' $@
	yq -i '.slots.root_med_carbon.range |= "TextValue"' $@
	yq -i '.slots.root_med_macronutr.range |= "TextValue"' $@
	yq -i '.slots.root_med_micronutr.range |= "TextValue"' $@
	yq -i '.slots.root_med_ph.range |= "QuantityValue"' $@
	yq -i '.slots.root_med_regl.range |= "TextValue"' $@
	yq -i '.slots.root_med_suppl.range |= "TextValue"' $@
	yq -i '.slots.salt_regm.range |= "TextValue"' $@
	yq -i '.slots.samp_collec_device.range |= "string"' $@
	yq -i '.slots.samp_collec_method.range |= "string"' $@
	yq -i '.slots.samp_loc_corr_rate.range |= "TextValue"' $@
	yq -i '.slots.samp_mat_process.range |= "ControlledTermValue"' $@
	yq -i '.slots.samp_md.range |= "QuantityValue"' $@
	yq -i '.slots.samp_name.range |= "string"' $@
	yq -i '.slots.samp_preserv.range |= "TextValue"' $@
	yq -i '.slots.samp_room_id.range |= "TextValue"' $@
	yq -i '.slots.samp_time_out.range |= "TextValue"' $@
	yq -i '.slots.samp_transport_cond.range |= "TextValue"' $@
	yq -i '.slots.samp_tvdss.range |= "TextValue"' $@
	yq -i '.slots.saturates_pc.range |= "TextValue"' $@
	yq -i '.slots.shad_dev_water_mold.range |= "string"' $@
	yq -i '.slots.sieving.range |= "TextValue"' $@
	yq -i '.slots.size_frac.range |= "TextValue"' $@
	yq -i '.slots.soil_texture_meth.range |= "string"' $@
	yq -i '.slots.soluble_inorg_mat.range |= "TextValue"' $@
	yq -i '.slots.soluble_org_mat.range |= "TextValue"' $@
	yq -i '.slots.suspend_solids.range |= "TextValue"' $@
	yq -i '.slots.tot_nitro_cont_meth.range |= "string"' $@
	yq -i '.slots.viscosity.range |= "TextValue"' $@
	yq -i '.slots.volatile_org_comp.range |= "TextValue"' $@
	yq -i '.slots.water_cont_soil_meth.range |= "string"' $@
	yq -i '.slots.water_temp_regm.range |= "TextValue"' $@
	yq -i '.slots.watering_regm.range |= "TextValue"' $@
	yq -i '.slots.window_open_freq.range |= "TextValue"' $@
	yq -i '.slots.window_size.range |= "TextValue"' $@

	yq -i 'del(.classes)' $@
	yq -i 'del(.enums.[].name)'  $@
	yq -i 'del(.enums.[].permissible_values.[].text)'  $@
	yq -i 'del(.slots.[].name)'  $@
	yq -i 'del(.slots.add_recov_method.pattern)'  $@
	yq -i 'del(.subsets.[].name)'  $@

	yq -i '.id |= "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/mixs.yaml"' $@

#	# update host_taxid and samp_taxon_id. may want to flatten to a string or URIORCURIE eventually
	yq -i 'del(.slots.host_taxid.examples)'  $@
	yq -i 'del(.slots.host_taxid.string_serialization)'  $@
	yq -i 'del(.slots.samp_taxon_id.examples)'  $@
	yq -i 'del(.slots.samp_taxon_id.string_serialization)'  $@

	yq -i '.slots.host_taxid.comments |= ["Homo sapiens [NCBITaxon:9606] would be a reasonable has_raw_value"]'  $@
	yq -i '.slots.host_taxid.range = "ControlledIdentifiedTermValue"'  $@
	yq -i '.slots.samp_taxon_id.comments |= ["coal metagenome [NCBITaxon:1260732] would be a reasonable has_raw_value"]'  $@
	yq -i '.slots.samp_taxon_id.range = "ControlledIdentifiedTermValue"'  $@


	# add "M horizon" to soil_horizon_enum
	yq -i '.enums.soil_horizon_enum.permissible_values.["M horizon"] = {}'  $@
	rm -rf local/mixs_regen/mixs_subset_modified.yaml.bak


local/mixs_regen/mixs_subset_modified_inj_land_use.yaml: assets/other_mixs_yaml_files/cur_land_use_enum.yaml local/mixs_regen/mixs_subset_modified.yaml
	# inject re-structured cur_land_use_enum
	#   using '| cat > ' because yq doesn't seem to like redirecting out to a file
	yq eval-all \
		'select(fileIndex==1).enums.cur_land_use_enum = select(fileIndex==0).enums.cur_land_use_enum | select(fileIndex==1)' \
		$^ | cat > $@

mixs-deepdiff: src/schema/mixs.yaml
	mv src/schema/mixs.yaml.bak src/schema/mixs.bak.yaml
	$(RUN) deep diff src/schema/mixs.bak.yaml $^
	mv src/schema/mixs.bak.yaml src/schema/mixs.yaml.bak

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


#assets/MIxS_6_term_updates_MIxS6_Core-_Final_clean.tsv:
#	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=178015749&format=tsv" > $@
#
#assets/MIxS_6_term_updates_MIxS6_packages_-_Final_clean.tsv:
#	curl -L "https://docs.google.com/spreadsheets/d/1QDeeUcDqXes69Y2RjU2aWgOpCVWo5OVsBX9MKmMqi_o/export?gid=750683809&format=tsv" > $@
#
#assets/sheets-for-nmdc-submission-schema_import_slots_regardless.tsv:
#	curl -L "https://docs.google.com/spreadsheets/d/1_TSuvEUX68g_o3r1d9wvOYMMbZ3vO4eluvAd2wNJoSU/export?gid=1742830620&format=tsv" > $@

MIXS_YAML_FROM_SHEETS_AND_FRIENDS = src/schema/mixs.yaml

SCHEMA_FILE = $(MIXS_YAML_FROM_SHEETS_AND_FRIENDS)

# Define a variable for the directory containing the YAML data files
YAML_DIR_VALID := src/data/valid/

# Define a variable for the list of YAML data files
YAML_DATABASE_FILES_VALID := $(wildcard $(YAML_DIR_VALID)Database*.yaml)

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

examples/output/Biosample-exhasutive_report.yaml: src/data/valid/Biosample-exhasutive.yaml
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

examples/output/Biosample-exhasutive-pretty-sorted.yaml: src/data/valid/Biosample-exhasutive.yaml
	poetry run pretty-sort-yaml \
		-i $< \
		-o $@

# # # #

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

# recommended setup:
#   1. . ~/sshproxy.sh -u <NERSC USER NAME>
#   2. ssh -i ~/.ssh/nersc -L27777:mongo-loadbalancer.nmdc.production.svc.spin.nersc.org:27017 -o ServerAliveInterval=60 {YOUR_NERSC_USERNAME}@dtn01.nersc.gov

# todo mongodb collection stats vs Database slots report
# todo convert to json
# todo compress large files

make-rdf: rdf-clean local/mongo_as_nmdc_database_validation.log local/mongo_as_nmdc_database_cuire_repaired.ttl

#   		--selected-collections functional_annotation_agg \ # huge, no publically avaiaible reference data (kegg)
#   		--selected-collections metaproteomics_analysis_activity_set \ # next slowest

local/mongo_as_unvalidated_nmdc_database.yaml:
	date  # 276.50 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) pure-export \
		--max-docs-per-coll 10000000 \
		--output-yaml $@ \
		--page-size 10000 \
		--selected-collections biosample_set \
  		--selected-collections data_object_set \
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
  		--selected-collections study_set

local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date # 449.56 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) migration-recursion \
		--schema-path $(word 1,$^) \
		--input-path $(word 2,$^) \
		--output-path $@

local/mongo_as_nmdc_database_validation.log: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	# nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml or nmdc_schema/nmdc_materialized_patterns.yaml
	date # 5m57.559s without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-validate --schema $^ > $@

local/mongo_as_nmdc_database.ttl: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_nmdc_database_rdf_safe.yaml
	# todo what reference ontologies do we want to include? kegg, but from where?
	#   nmdc schema, envo, mixs, chebi
	#   selected branches of NCBI taxonomy? protein ontology?
	#   kegg :-(
	date # 681.99 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) linkml-convert --output $@ --schema $^
	time riot --validate $@ # < 1 minute

local/mongo_as_nmdc_database_cuire_repaired.ttl: local/mongo_as_nmdc_database.ttl
	date # 287.91 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) anyuri-strings-to-iris \
		--input-ttl $< \
		--prefixes-yaml assets/misc/extra_prefix_expansions.yaml \
		--output-ttl $@

# todo: add start time reporting
# todo: allow different api base addresses
# todo: skip migration of some collections?
# todo: still getting anyurl typed string statement objects in RDF ? I added a fix in anyuri-strings-to-iris
# todo: switch to API method for getting collection names and stats: https://api.microbiomedata.org/nmdcschema/collection_stats # partially implemented

# ----

# todo: graphdb visual graph for including blank nodes
# todo: remove funding_sources char limit

# ----

#project/prefixmap/nmdc.json: gen-project

OmicsProcessing-to-catted-Biosamples.tsv: assets/sparql/OmicsProcessing-to-catted-Biosamples.rq nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) class-sparql \
		--query-file $<

OmicsProcessing-all: OmicsProcessing-clean OmicsProcessing.tsv

OmicsProcessing.tsv: project/prefixmap/nmdc.json nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
	$(RUN) class-sparql  \
		--concatenation-suffix s \
		--do-group-concat \
		--graph-name "mongodb://mongo-loadbalancer.nmdc.production.svc.spin.nersc.gov:27017" \
		--prefix-maps-json $(word 1,$^) \
		--schema-file  $(word 2,$^) \
		--target-class-name $(firstword $(subst ., ,$(lastword $(subst /, ,$@)))) \
		--target-p-o-constraint "dcterms:isPartOf nmdc:sty-11-34xj1150"

# ----

doi_report.tsv:
	$(RUN) get-study-doi-report

