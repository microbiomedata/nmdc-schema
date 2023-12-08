## Add your own custom Makefile targets here

JENA_PATH=~/apache-jena/bin/
RUN=poetry run

SCHEMA_NAME = $(shell bash ./utils/get-value.sh name)
SOURCE_SCHEMA_PATH = $(shell bash ./utils/get-value.sh source_schema_path)

.PHONY: OmicsProcessing-clean accepting-legacy-ids-all accepting-legacy-ids-clean \
dump-validate-report-convert-mongodb examples-clean linkml-validate-mongodb mixs-yaml-clean mixs-deepdiff \
mongodb-clean rdf-clean shuttle-clean squeaky-clean

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

mongodb-clean:
	date
	rm -rf local/mongo_as_nmdc_database*
	rm -rf local/mongo_as_unvalidated_nmdc_database.yaml

rdf-clean:
	rm -rf \
		OmicsProcessing.rq \
		local/mongo_as_nmdc_database.ttl \
		local/mongo_as_nmdc_database_cuire_repaired.ttl \
		local/mongo_as_nmdc_database_rdf_safe.yaml \
		local/mongo_as_nmdc_database_validation.log \
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
	# switching to TextValue may not add any value. the other range changes do improve the structure of the data.
	# ironically changing back to strings for the submission-schema, data harmonizer, submission portal etc.
	# may switch source of truth to the MIxS 6.2.2 release candidate
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

#mixs-deepdiff: src/schema/mixs.yaml
#	mv src/schema/mixs.yaml.bak src/schema/mixs.bak.yaml
#	$(RUN) deep diff src/schema/mixs.bak.yaml $^
#	mv src/schema/mixs.bak.yaml src/schema/mixs.yaml.bak

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

#local/usage_template.tsv: src/schema/nmdc.yaml # rewrite to use schemasheets linkml2schemasheets-template
#	mkdir -p $(@D)
#	$(RUN) generate_and_populate_template \
#		 --base-class slot_definition \
#		 --columns-to-insert class \
#		 --destination-template $@ \
#		 --meta-model-excel-file local/meta.xlsx \
#		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
# 		 --columns-to-insert slot \
#		 --source-schema-path $<

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

# 		--selected-collections data_object_set \
# 		--selected-collections extraction_set \
# 		--selected-collections field_research_site_set \
# 		--selected-collections library_preparation_set \
# 		--selected-collections mags_activity_set \
# 		--selected-collections metabolomics_analysis_activity_set \
# 		--selected-collections metagenome_annotation_activity_set \
# 		--selected-collections metagenome_assembly_set \
# 		--selected-collections metagenome_sequencing_activity_set  \
# 		--selected-collections metaproteomics_analysis_activity_set \
# 		--selected-collections metatranscriptome_activity_set \
# 		--selected-collections nom_analysis_activity_set \
# 		--selected-collections omics_processing_set \
# 		--selected-collections pooling_set \
# 		--selected-collections processed_sample_set \
# 		--selected-collections read_based_taxonomy_analysis_activity_set \
# 		--selected-collections read_qc_analysis_activity_set \

## can't handle empty selected-collections yet
## https://github.com/microbiomedata/nmdc-schema/issues/1485
 #		--selected-collections activity_set \
 #		--selected-collections collecting_biosamples_from_site_set \
 #		--selected-collections material_sample_set \
 #		--selected-collections planned_process_set \

#  		--selected-collections metap_gene_function_aggregation \

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
		--selected-collections biosample_set \
		--selected-collections data_object_set \
		--selected-collections functional_annotation_agg \
		--selected-collections study_set \
 		--selected-collections extraction_set \
 		--selected-collections field_research_site_set \
 		--selected-collections library_preparation_set \
 		--selected-collections mags_activity_set \
 		--selected-collections metabolomics_analysis_activity_set \
 		--selected-collections metagenome_annotation_activity_set \
 		--selected-collections metagenome_assembly_set \
 		--selected-collections metagenome_sequencing_activity_set  \
 		--selected-collections metaproteomics_analysis_activity_set \
 		--selected-collections metatranscriptome_activity_set \
 		--selected-collections nom_analysis_activity_set \
 		--selected-collections omics_processing_set \
 		--selected-collections pooling_set \
 		--selected-collections processed_sample_set \
 		--selected-collections read_based_taxonomy_analysis_activity_set \
 		--selected-collections read_qc_analysis_activity_set

#		--skip-collection-check


local/mongo_as_nmdc_database_rdf_safe.yaml: nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml local/mongo_as_unvalidated_nmdc_database.yaml
	date # 449.56 seconds on 2023-08-30 without functional_annotation_agg or metaproteomics_analysis_activity_set
	time $(RUN) migration-recursion \
		--migrator-name Migrator_from_9_1_to_9_2 \
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

.PHONY: migration-doctests

# Runs all doctests defined within the migrator modules.
migration-doctests:
	$(RUN) python -m doctest -v nmdc_schema/migrators/*.py