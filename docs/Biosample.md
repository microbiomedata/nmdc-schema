# Class: Biosample


_Biological source material which can be characterized by an experiment._





URI: [nmdc:Biosample](https://w3id.org/nmdc/Biosample)




```mermaid
 classDiagram
    class Biosample
      MaterialEntity <|-- Biosample
      
      Biosample : abs_air_humidity
        
          Biosample --|> QuantityValue : abs_air_humidity
        
      Biosample : add_date
        
      Biosample : add_recov_method
        
          Biosample --|> TextValue : add_recov_method
        
      Biosample : additional_info
        
          Biosample --|> TextValue : additional_info
        
      Biosample : address
        
          Biosample --|> TextValue : address
        
      Biosample : adj_room
        
          Biosample --|> TextValue : adj_room
        
      Biosample : aero_struc
        
          Biosample --|> TextValue : aero_struc
        
      Biosample : agrochem_addition
        
          Biosample --|> TextValue : agrochem_addition
        
      Biosample : air_PM_concen
        
          Biosample --|> TextValue : air_PM_concen
        
      Biosample : air_temp
        
          Biosample --|> QuantityValue : air_temp
        
      Biosample : air_temp_regm
        
          Biosample --|> TextValue : air_temp_regm
        
      Biosample : al_sat
        
          Biosample --|> QuantityValue : al_sat
        
      Biosample : al_sat_meth
        
          Biosample --|> TextValue : al_sat_meth
        
      Biosample : alkalinity
        
          Biosample --|> QuantityValue : alkalinity
        
      Biosample : alkalinity_method
        
          Biosample --|> TextValue : alkalinity_method
        
      Biosample : alkyl_diethers
        
          Biosample --|> QuantityValue : alkyl_diethers
        
      Biosample : alt
        
          Biosample --|> QuantityValue : alt
        
      Biosample : alternative_identifiers
        
      Biosample : aminopept_act
        
          Biosample --|> QuantityValue : aminopept_act
        
      Biosample : ammonium
        
          Biosample --|> QuantityValue : ammonium
        
      Biosample : ammonium_nitrogen
        
          Biosample --|> QuantityValue : ammonium_nitrogen
        
      Biosample : amount_light
        
          Biosample --|> QuantityValue : amount_light
        
      Biosample : analysis_type
        
          Biosample --|> analysis_type_enum : analysis_type
        
      Biosample : ances_data
        
          Biosample --|> TextValue : ances_data
        
      Biosample : annual_precpt
        
          Biosample --|> QuantityValue : annual_precpt
        
      Biosample : annual_temp
        
          Biosample --|> QuantityValue : annual_temp
        
      Biosample : antibiotic_regm
        
          Biosample --|> TextValue : antibiotic_regm
        
      Biosample : api
        
          Biosample --|> QuantityValue : api
        
      Biosample : arch_struc
        
          Biosample --|> arch_struc_enum : arch_struc
        
      Biosample : aromatics_pc
        
          Biosample --|> TextValue : aromatics_pc
        
      Biosample : asphaltenes_pc
        
          Biosample --|> TextValue : asphaltenes_pc
        
      Biosample : atmospheric_data
        
          Biosample --|> TextValue : atmospheric_data
        
      Biosample : avg_dew_point
        
          Biosample --|> QuantityValue : avg_dew_point
        
      Biosample : avg_occup
        
          Biosample --|> TextValue : avg_occup
        
      Biosample : avg_temp
        
          Biosample --|> QuantityValue : avg_temp
        
      Biosample : bac_prod
        
          Biosample --|> QuantityValue : bac_prod
        
      Biosample : bac_resp
        
          Biosample --|> QuantityValue : bac_resp
        
      Biosample : bacteria_carb_prod
        
          Biosample --|> QuantityValue : bacteria_carb_prod
        
      Biosample : barometric_press
        
          Biosample --|> QuantityValue : barometric_press
        
      Biosample : basin
        
          Biosample --|> TextValue : basin
        
      Biosample : bathroom_count
        
          Biosample --|> TextValue : bathroom_count
        
      Biosample : bedroom_count
        
          Biosample --|> TextValue : bedroom_count
        
      Biosample : benzene
        
          Biosample --|> QuantityValue : benzene
        
      Biosample : biochem_oxygen_dem
        
          Biosample --|> QuantityValue : biochem_oxygen_dem
        
      Biosample : biocide
        
          Biosample --|> TextValue : biocide
        
      Biosample : biocide_admin_method
        
          Biosample --|> TextValue : biocide_admin_method
        
      Biosample : biol_stat
        
          Biosample --|> biol_stat_enum : biol_stat
        
      Biosample : biomass
        
          Biosample --|> TextValue : biomass
        
      Biosample : biosample_categories
        
          Biosample --|> BiosampleCategoryEnum : biosample_categories
        
      Biosample : biotic_regm
        
          Biosample --|> TextValue : biotic_regm
        
      Biosample : biotic_relationship
        
          Biosample --|> biotic_relationship_enum : biotic_relationship
        
      Biosample : bishomohopanol
        
          Biosample --|> QuantityValue : bishomohopanol
        
      Biosample : blood_press_diast
        
          Biosample --|> QuantityValue : blood_press_diast
        
      Biosample : blood_press_syst
        
          Biosample --|> QuantityValue : blood_press_syst
        
      Biosample : bromide
        
          Biosample --|> QuantityValue : bromide
        
      Biosample : build_docs
        
          Biosample --|> build_docs_enum : build_docs
        
      Biosample : build_occup_type
        
          Biosample --|> build_occup_type_enum : build_occup_type
        
      Biosample : building_setting
        
          Biosample --|> building_setting_enum : building_setting
        
      Biosample : built_struc_age
        
          Biosample --|> QuantityValue : built_struc_age
        
      Biosample : built_struc_set
        
          Biosample --|> TextValue : built_struc_set
        
      Biosample : built_struc_type
        
          Biosample --|> TextValue : built_struc_type
        
      Biosample : bulk_elect_conductivity
        
          Biosample --|> QuantityValue : bulk_elect_conductivity
        
      Biosample : calcium
        
          Biosample --|> QuantityValue : calcium
        
      Biosample : carb_dioxide
        
          Biosample --|> QuantityValue : carb_dioxide
        
      Biosample : carb_monoxide
        
          Biosample --|> QuantityValue : carb_monoxide
        
      Biosample : carb_nitro_ratio
        
          Biosample --|> QuantityValue : carb_nitro_ratio
        
      Biosample : ceil_area
        
          Biosample --|> QuantityValue : ceil_area
        
      Biosample : ceil_cond
        
          Biosample --|> ceil_cond_enum : ceil_cond
        
      Biosample : ceil_finish_mat
        
          Biosample --|> ceil_finish_mat_enum : ceil_finish_mat
        
      Biosample : ceil_struc
        
          Biosample --|> TextValue : ceil_struc
        
      Biosample : ceil_texture
        
          Biosample --|> ceil_texture_enum : ceil_texture
        
      Biosample : ceil_thermal_mass
        
          Biosample --|> QuantityValue : ceil_thermal_mass
        
      Biosample : ceil_type
        
          Biosample --|> ceil_type_enum : ceil_type
        
      Biosample : ceil_water_mold
        
          Biosample --|> TextValue : ceil_water_mold
        
      Biosample : chem_administration
        
          Biosample --|> ControlledTermValue : chem_administration
        
      Biosample : chem_mutagen
        
          Biosample --|> TextValue : chem_mutagen
        
      Biosample : chem_oxygen_dem
        
          Biosample --|> QuantityValue : chem_oxygen_dem
        
      Biosample : chem_treat_method
        
      Biosample : chem_treatment
        
          Biosample --|> TextValue : chem_treatment
        
      Biosample : chimera_check
        
          Biosample --|> TextValue : chimera_check
        
      Biosample : chloride
        
          Biosample --|> QuantityValue : chloride
        
      Biosample : chlorophyll
        
          Biosample --|> QuantityValue : chlorophyll
        
      Biosample : climate_environment
        
          Biosample --|> TextValue : climate_environment
        
      Biosample : collected_from
        
          Biosample --|> FieldResearchSite : collected_from
        
      Biosample : collection_date
        
          Biosample --|> TimestampValue : collection_date
        
      Biosample : collection_date_inc
        
      Biosample : collection_time
        
      Biosample : collection_time_inc
        
      Biosample : community
        
      Biosample : conduc
        
          Biosample --|> QuantityValue : conduc
        
      Biosample : cool_syst_id
        
          Biosample --|> TextValue : cool_syst_id
        
      Biosample : core_field
        
      Biosample : crop_rotation
        
          Biosample --|> TextValue : crop_rotation
        
      Biosample : cult_root_med
        
          Biosample --|> TextValue : cult_root_med
        
      Biosample : cur_land_use
        
          Biosample --|> cur_land_use_enum : cur_land_use
        
      Biosample : cur_vegetation
        
          Biosample --|> TextValue : cur_vegetation
        
      Biosample : cur_vegetation_meth
        
          Biosample --|> TextValue : cur_vegetation_meth
        
      Biosample : date_last_rain
        
          Biosample --|> TimestampValue : date_last_rain
        
      Biosample : density
        
          Biosample --|> QuantityValue : density
        
      Biosample : depos_env
        
          Biosample --|> depos_env_enum : depos_env
        
      Biosample : depth
        
          Biosample --|> QuantityValue : depth
        
      Biosample : description
        
      Biosample : dew_point
        
          Biosample --|> QuantityValue : dew_point
        
      Biosample : diether_lipids
        
          Biosample --|> TextValue : diether_lipids
        
      Biosample : diss_carb_dioxide
        
          Biosample --|> QuantityValue : diss_carb_dioxide
        
      Biosample : diss_hydrogen
        
          Biosample --|> QuantityValue : diss_hydrogen
        
      Biosample : diss_inorg_carb
        
          Biosample --|> QuantityValue : diss_inorg_carb
        
      Biosample : diss_inorg_nitro
        
          Biosample --|> QuantityValue : diss_inorg_nitro
        
      Biosample : diss_inorg_phosp
        
          Biosample --|> QuantityValue : diss_inorg_phosp
        
      Biosample : diss_iron
        
          Biosample --|> QuantityValue : diss_iron
        
      Biosample : diss_org_carb
        
          Biosample --|> QuantityValue : diss_org_carb
        
      Biosample : diss_org_nitro
        
          Biosample --|> QuantityValue : diss_org_nitro
        
      Biosample : diss_oxygen
        
          Biosample --|> QuantityValue : diss_oxygen
        
      Biosample : diss_oxygen_fluid
        
          Biosample --|> QuantityValue : diss_oxygen_fluid
        
      Biosample : dna_absorb1
        
      Biosample : dna_absorb2
        
      Biosample : dna_collect_site
        
      Biosample : dna_concentration
        
      Biosample : dna_cont_type
        
          Biosample --|> JgiContTypeEnum : dna_cont_type
        
      Biosample : dna_cont_well
        
      Biosample : dna_container_id
        
      Biosample : dna_dnase
        
          Biosample --|> YesNoEnum : dna_dnase
        
      Biosample : dna_isolate_meth
        
      Biosample : dna_organisms
        
      Biosample : dna_project_contact
        
      Biosample : dna_samp_id
        
      Biosample : dna_sample_format
        
          Biosample --|> dna_sample_format_enum : dna_sample_format
        
      Biosample : dna_sample_name
        
      Biosample : dna_seq_project
        
      Biosample : dna_seq_project_name
        
      Biosample : dna_seq_project_pi
        
      Biosample : dna_volume
        
      Biosample : dnase_rna
        
          Biosample --|> YesNoEnum : dnase_rna
        
      Biosample : door_comp_type
        
          Biosample --|> door_comp_type_enum : door_comp_type
        
      Biosample : door_cond
        
          Biosample --|> door_cond_enum : door_cond
        
      Biosample : door_direct
        
          Biosample --|> door_direct_enum : door_direct
        
      Biosample : door_loc
        
          Biosample --|> door_loc_enum : door_loc
        
      Biosample : door_mat
        
          Biosample --|> door_mat_enum : door_mat
        
      Biosample : door_move
        
          Biosample --|> door_move_enum : door_move
        
      Biosample : door_size
        
          Biosample --|> QuantityValue : door_size
        
      Biosample : door_type
        
          Biosample --|> door_type_enum : door_type
        
      Biosample : door_type_metal
        
          Biosample --|> door_type_metal_enum : door_type_metal
        
      Biosample : door_type_wood
        
          Biosample --|> door_type_wood_enum : door_type_wood
        
      Biosample : door_water_mold
        
          Biosample --|> TextValue : door_water_mold
        
      Biosample : down_par
        
          Biosample --|> QuantityValue : down_par
        
      Biosample : drainage_class
        
          Biosample --|> drainage_class_enum : drainage_class
        
      Biosample : drawings
        
          Biosample --|> drawings_enum : drawings
        
      Biosample : ecosystem
        
      Biosample : ecosystem_category
        
      Biosample : ecosystem_subtype
        
      Biosample : ecosystem_type
        
      Biosample : efficiency_percent
        
          Biosample --|> QuantityValue : efficiency_percent
        
      Biosample : elev
        
      Biosample : elevator
        
          Biosample --|> TextValue : elevator
        
      Biosample : embargoed
        
      Biosample : emsl_biosample_identifiers
        
      Biosample : emulsions
        
          Biosample --|> TextValue : emulsions
        
      Biosample : env_broad_scale
        
          Biosample --|> ControlledIdentifiedTermValue : env_broad_scale
        
      Biosample : env_local_scale
        
          Biosample --|> ControlledIdentifiedTermValue : env_local_scale
        
      Biosample : env_medium
        
          Biosample --|> ControlledIdentifiedTermValue : env_medium
        
      Biosample : env_package
        
          Biosample --|> TextValue : env_package
        
      Biosample : environment_field
        
      Biosample : escalator
        
          Biosample --|> TextValue : escalator
        
      Biosample : ethylbenzene
        
          Biosample --|> QuantityValue : ethylbenzene
        
      Biosample : exp_duct
        
          Biosample --|> QuantityValue : exp_duct
        
      Biosample : exp_pipe
        
          Biosample --|> QuantityValue : exp_pipe
        
      Biosample : experimental_factor
        
          Biosample --|> ControlledTermValue : experimental_factor
        
      Biosample : experimental_factor_other
        
      Biosample : ext_door
        
          Biosample --|> TextValue : ext_door
        
      Biosample : ext_wall_orient
        
          Biosample --|> ext_wall_orient_enum : ext_wall_orient
        
      Biosample : ext_window_orient
        
          Biosample --|> ext_window_orient_enum : ext_window_orient
        
      Biosample : extreme_event
        
      Biosample : fao_class
        
          Biosample --|> fao_class_enum : fao_class
        
      Biosample : fertilizer_regm
        
          Biosample --|> TextValue : fertilizer_regm
        
      Biosample : field
        
          Biosample --|> TextValue : field
        
      Biosample : filter_method
        
      Biosample : filter_type
        
          Biosample --|> filter_type_enum : filter_type
        
      Biosample : fire
        
      Biosample : fireplace_type
        
          Biosample --|> TextValue : fireplace_type
        
      Biosample : flooding
        
      Biosample : floor_age
        
          Biosample --|> QuantityValue : floor_age
        
      Biosample : floor_area
        
          Biosample --|> QuantityValue : floor_area
        
      Biosample : floor_cond
        
          Biosample --|> floor_cond_enum : floor_cond
        
      Biosample : floor_count
        
          Biosample --|> TextValue : floor_count
        
      Biosample : floor_finish_mat
        
          Biosample --|> floor_finish_mat_enum : floor_finish_mat
        
      Biosample : floor_struc
        
          Biosample --|> floor_struc_enum : floor_struc
        
      Biosample : floor_thermal_mass
        
          Biosample --|> QuantityValue : floor_thermal_mass
        
      Biosample : floor_water_mold
        
          Biosample --|> floor_water_mold_enum : floor_water_mold
        
      Biosample : fluor
        
          Biosample --|> QuantityValue : fluor
        
      Biosample : freq_clean
        
          Biosample --|> QuantityValue : freq_clean
        
      Biosample : freq_cook
        
          Biosample --|> QuantityValue : freq_cook
        
      Biosample : fungicide_regm
        
          Biosample --|> TextValue : fungicide_regm
        
      Biosample : furniture
        
          Biosample --|> furniture_enum : furniture
        
      Biosample : gaseous_environment
        
          Biosample --|> TextValue : gaseous_environment
        
      Biosample : gaseous_substances
        
          Biosample --|> TextValue : gaseous_substances
        
      Biosample : gender_restroom
        
          Biosample --|> gender_restroom_enum : gender_restroom
        
      Biosample : genetic_mod
        
          Biosample --|> TextValue : genetic_mod
        
      Biosample : geo_loc_name
        
          Biosample --|> TextValue : geo_loc_name
        
      Biosample : glucosidase_act
        
          Biosample --|> QuantityValue : glucosidase_act
        
      Biosample : gold_biosample_identifiers
        
      Biosample : gravidity
        
          Biosample --|> TextValue : gravidity
        
      Biosample : gravity
        
          Biosample --|> TextValue : gravity
        
      Biosample : growth_facil
        
          Biosample --|> ControlledTermValue : growth_facil
        
      Biosample : growth_habit
        
          Biosample --|> growth_habit_enum : growth_habit
        
      Biosample : growth_hormone_regm
        
          Biosample --|> TextValue : growth_hormone_regm
        
      Biosample : habitat
        
      Biosample : hall_count
        
          Biosample --|> TextValue : hall_count
        
      Biosample : handidness
        
          Biosample --|> handidness_enum : handidness
        
      Biosample : has_numeric_value
        
      Biosample : has_raw_value
        
      Biosample : has_unit
        
      Biosample : hc_produced
        
          Biosample --|> hc_produced_enum : hc_produced
        
      Biosample : hcr
        
          Biosample --|> hcr_enum : hcr
        
      Biosample : hcr_fw_salinity
        
          Biosample --|> QuantityValue : hcr_fw_salinity
        
      Biosample : hcr_geol_age
        
          Biosample --|> hcr_geol_age_enum : hcr_geol_age
        
      Biosample : hcr_pressure
        
          Biosample --|> TextValue : hcr_pressure
        
      Biosample : hcr_temp
        
          Biosample --|> TextValue : hcr_temp
        
      Biosample : heat_cool_type
        
          Biosample --|> heat_cool_type_enum : heat_cool_type
        
      Biosample : heat_deliv_loc
        
          Biosample --|> heat_deliv_loc_enum : heat_deliv_loc
        
      Biosample : heat_sys_deliv_meth
        
      Biosample : heat_system_id
        
          Biosample --|> TextValue : heat_system_id
        
      Biosample : heavy_metals
        
          Biosample --|> TextValue : heavy_metals
        
      Biosample : heavy_metals_meth
        
          Biosample --|> TextValue : heavy_metals_meth
        
      Biosample : height_carper_fiber
        
          Biosample --|> QuantityValue : height_carper_fiber
        
      Biosample : herbicide_regm
        
          Biosample --|> TextValue : herbicide_regm
        
      Biosample : horizon_meth
        
          Biosample --|> TextValue : horizon_meth
        
      Biosample : host_age
        
          Biosample --|> QuantityValue : host_age
        
      Biosample : host_body_habitat
        
          Biosample --|> TextValue : host_body_habitat
        
      Biosample : host_body_product
        
          Biosample --|> ControlledTermValue : host_body_product
        
      Biosample : host_body_site
        
          Biosample --|> ControlledTermValue : host_body_site
        
      Biosample : host_body_temp
        
          Biosample --|> QuantityValue : host_body_temp
        
      Biosample : host_color
        
          Biosample --|> TextValue : host_color
        
      Biosample : host_common_name
        
          Biosample --|> TextValue : host_common_name
        
      Biosample : host_diet
        
          Biosample --|> TextValue : host_diet
        
      Biosample : host_disease_stat
        
          Biosample --|> TextValue : host_disease_stat
        
      Biosample : host_dry_mass
        
          Biosample --|> QuantityValue : host_dry_mass
        
      Biosample : host_family_relation
        
      Biosample : host_genotype
        
          Biosample --|> TextValue : host_genotype
        
      Biosample : host_growth_cond
        
          Biosample --|> TextValue : host_growth_cond
        
      Biosample : host_height
        
          Biosample --|> QuantityValue : host_height
        
      Biosample : host_last_meal
        
          Biosample --|> TextValue : host_last_meal
        
      Biosample : host_length
        
          Biosample --|> QuantityValue : host_length
        
      Biosample : host_life_stage
        
          Biosample --|> TextValue : host_life_stage
        
      Biosample : host_name
        
      Biosample : host_phenotype
        
          Biosample --|> ControlledTermValue : host_phenotype
        
      Biosample : host_sex
        
          Biosample --|> host_sex_enum : host_sex
        
      Biosample : host_shape
        
          Biosample --|> TextValue : host_shape
        
      Biosample : host_subject_id
        
          Biosample --|> TextValue : host_subject_id
        
      Biosample : host_subspecf_genlin
        
      Biosample : host_substrate
        
          Biosample --|> TextValue : host_substrate
        
      Biosample : host_symbiont
        
      Biosample : host_taxid
        
          Biosample --|> ControlledIdentifiedTermValue : host_taxid
        
      Biosample : host_tot_mass
        
          Biosample --|> QuantityValue : host_tot_mass
        
      Biosample : host_wet_mass
        
          Biosample --|> QuantityValue : host_wet_mass
        
      Biosample : humidity
        
          Biosample --|> QuantityValue : humidity
        
      Biosample : humidity_regm
        
          Biosample --|> TextValue : humidity_regm
        
      Biosample : id
        
      Biosample : igsn_biosample_identifiers
        
      Biosample : img_identifiers
        
      Biosample : indoor_space
        
          Biosample --|> indoor_space_enum : indoor_space
        
      Biosample : indoor_surf
        
          Biosample --|> indoor_surf_enum : indoor_surf
        
      Biosample : indust_eff_percent
        
          Biosample --|> QuantityValue : indust_eff_percent
        
      Biosample : inorg_particles
        
          Biosample --|> TextValue : inorg_particles
        
      Biosample : insdc_biosample_identifiers
        
      Biosample : inside_lux
        
          Biosample --|> QuantityValue : inside_lux
        
      Biosample : int_wall_cond
        
          Biosample --|> int_wall_cond_enum : int_wall_cond
        
      Biosample : investigation_field
        
      Biosample : isotope_exposure
        
      Biosample : iw_bt_date_well
        
          Biosample --|> TimestampValue : iw_bt_date_well
        
      Biosample : iwf
        
          Biosample --|> QuantityValue : iwf
        
      Biosample : last_clean
        
          Biosample --|> TimestampValue : last_clean
        
      Biosample : lat_lon
        
          Biosample --|> GeolocationValue : lat_lon
        
      Biosample : lbc_thirty
        
          Biosample --|> QuantityValue : lbc_thirty
        
      Biosample : lbceq
        
          Biosample --|> QuantityValue : lbceq
        
      Biosample : light_intensity
        
          Biosample --|> QuantityValue : light_intensity
        
      Biosample : light_regm
        
          Biosample --|> TextValue : light_regm
        
      Biosample : light_type
        
          Biosample --|> light_type_enum : light_type
        
      Biosample : link_addit_analys
        
          Biosample --|> TextValue : link_addit_analys
        
      Biosample : link_class_info
        
          Biosample --|> TextValue : link_class_info
        
      Biosample : link_climate_info
        
          Biosample --|> TextValue : link_climate_info
        
      Biosample : lithology
        
          Biosample --|> lithology_enum : lithology
        
      Biosample : local_class
        
          Biosample --|> TextValue : local_class
        
      Biosample : local_class_meth
        
          Biosample --|> TextValue : local_class_meth
        
      Biosample : location
        
      Biosample : magnesium
        
          Biosample --|> QuantityValue : magnesium
        
      Biosample : manganese
        
          Biosample --|> QuantityValue : manganese
        
      Biosample : max_occup
        
          Biosample --|> QuantityValue : max_occup
        
      Biosample : mean_frict_vel
        
          Biosample --|> QuantityValue : mean_frict_vel
        
      Biosample : mean_peak_frict_vel
        
          Biosample --|> QuantityValue : mean_peak_frict_vel
        
      Biosample : mech_struc
        
          Biosample --|> mech_struc_enum : mech_struc
        
      Biosample : mechanical_damage
        
          Biosample --|> TextValue : mechanical_damage
        
      Biosample : methane
        
          Biosample --|> QuantityValue : methane
        
      Biosample : micro_biomass_c_meth
        
      Biosample : micro_biomass_meth
        
      Biosample : micro_biomass_n_meth
        
      Biosample : microbial_biomass
        
          Biosample --|> QuantityValue : microbial_biomass
        
      Biosample : microbial_biomass_c
        
      Biosample : microbial_biomass_n
        
      Biosample : mineral_nutr_regm
        
          Biosample --|> TextValue : mineral_nutr_regm
        
      Biosample : misc_param
        
          Biosample --|> TextValue : misc_param
        
      Biosample : mod_date
        
      Biosample : n_alkanes
        
          Biosample --|> TextValue : n_alkanes
        
      Biosample : name
        
      Biosample : ncbi_taxonomy_name
        
      Biosample : neon_biosample_identifiers
        
      Biosample : nitrate
        
          Biosample --|> QuantityValue : nitrate
        
      Biosample : nitrate_nitrogen
        
          Biosample --|> QuantityValue : nitrate_nitrogen
        
      Biosample : nitrite
        
          Biosample --|> QuantityValue : nitrite
        
      Biosample : nitrite_nitrogen
        
          Biosample --|> QuantityValue : nitrite_nitrogen
        
      Biosample : nitro
        
          Biosample --|> QuantityValue : nitro
        
      Biosample : non_microb_biomass
        
      Biosample : non_microb_biomass_method
        
      Biosample : non_min_nutr_regm
        
      Biosample : nucl_acid_amp
        
          Biosample --|> TextValue : nucl_acid_amp
        
      Biosample : nucl_acid_ext
        
          Biosample --|> TextValue : nucl_acid_ext
        
      Biosample : nucleic_acid_sequence_source_field
        
      Biosample : number_pets
        
          Biosample --|> QuantityValue : number_pets
        
      Biosample : number_plants
        
          Biosample --|> QuantityValue : number_plants
        
      Biosample : number_resident
        
          Biosample --|> QuantityValue : number_resident
        
      Biosample : occup_density_samp
        
          Biosample --|> QuantityValue : occup_density_samp
        
      Biosample : occup_document
        
          Biosample --|> occup_document_enum : occup_document
        
      Biosample : occup_samp
        
          Biosample --|> QuantityValue : occup_samp
        
      Biosample : org_carb
        
          Biosample --|> QuantityValue : org_carb
        
      Biosample : org_count_qpcr_info
        
      Biosample : org_matter
        
          Biosample --|> QuantityValue : org_matter
        
      Biosample : org_nitro
        
          Biosample --|> QuantityValue : org_nitro
        
      Biosample : org_nitro_method
        
      Biosample : org_particles
        
          Biosample --|> TextValue : org_particles
        
      Biosample : organism_count
        
          Biosample --|> QuantityValue : organism_count
        
      Biosample : other_treatment
        
      Biosample : owc_tvdss
        
          Biosample --|> QuantityValue : owc_tvdss
        
      Biosample : oxy_stat_samp
        
          Biosample --|> oxy_stat_samp_enum : oxy_stat_samp
        
      Biosample : oxygen
        
          Biosample --|> QuantityValue : oxygen
        
      Biosample : part_of
        
          Biosample --|> Study : part_of
        
      Biosample : part_org_carb
        
          Biosample --|> QuantityValue : part_org_carb
        
      Biosample : part_org_nitro
        
          Biosample --|> QuantityValue : part_org_nitro
        
      Biosample : particle_class
        
          Biosample --|> TextValue : particle_class
        
      Biosample : pcr_cond
        
          Biosample --|> TextValue : pcr_cond
        
      Biosample : pcr_primers
        
          Biosample --|> TextValue : pcr_primers
        
      Biosample : permeability
        
          Biosample --|> TextValue : permeability
        
      Biosample : perturbation
        
          Biosample --|> TextValue : perturbation
        
      Biosample : pesticide_regm
        
          Biosample --|> TextValue : pesticide_regm
        
      Biosample : petroleum_hydrocarb
        
          Biosample --|> QuantityValue : petroleum_hydrocarb
        
      Biosample : ph
        
      Biosample : ph_meth
        
          Biosample --|> TextValue : ph_meth
        
      Biosample : ph_regm
        
          Biosample --|> TextValue : ph_regm
        
      Biosample : phaeopigments
        
          Biosample --|> TextValue : phaeopigments
        
      Biosample : phosphate
        
          Biosample --|> QuantityValue : phosphate
        
      Biosample : phosplipid_fatt_acid
        
          Biosample --|> TextValue : phosplipid_fatt_acid
        
      Biosample : photon_flux
        
          Biosample --|> QuantityValue : photon_flux
        
      Biosample : plant_growth_med
        
          Biosample --|> ControlledTermValue : plant_growth_med
        
      Biosample : plant_product
        
          Biosample --|> TextValue : plant_product
        
      Biosample : plant_sex
        
          Biosample --|> plant_sex_enum : plant_sex
        
      Biosample : plant_struc
        
          Biosample --|> ControlledTermValue : plant_struc
        
      Biosample : pollutants
        
          Biosample --|> TextValue : pollutants
        
      Biosample : pool_dna_extracts
        
          Biosample --|> TextValue : pool_dna_extracts
        
      Biosample : porosity
        
          Biosample --|> TextValue : porosity
        
      Biosample : potassium
        
          Biosample --|> QuantityValue : potassium
        
      Biosample : pour_point
        
          Biosample --|> QuantityValue : pour_point
        
      Biosample : pre_treatment
        
          Biosample --|> TextValue : pre_treatment
        
      Biosample : pres_animal_insect
        
      Biosample : pressure
        
          Biosample --|> QuantityValue : pressure
        
      Biosample : prev_land_use_meth
        
      Biosample : previous_land_use
        
          Biosample --|> TextValue : previous_land_use
        
      Biosample : primary_prod
        
          Biosample --|> QuantityValue : primary_prod
        
      Biosample : primary_treatment
        
          Biosample --|> TextValue : primary_treatment
        
      Biosample : prod_rate
        
          Biosample --|> QuantityValue : prod_rate
        
      Biosample : prod_start_date
        
          Biosample --|> TimestampValue : prod_start_date
        
      Biosample : profile_position
        
          Biosample --|> profile_position_enum : profile_position
        
      Biosample : project_id
        
      Biosample : proport_woa_temperature
        
      Biosample : proposal_dna
        
      Biosample : proposal_rna
        
      Biosample : quad_pos
        
          Biosample --|> quad_pos_enum : quad_pos
        
      Biosample : radiation_regm
        
          Biosample --|> TextValue : radiation_regm
        
      Biosample : rainfall_regm
        
          Biosample --|> TextValue : rainfall_regm
        
      Biosample : reactor_type
        
          Biosample --|> TextValue : reactor_type
        
      Biosample : redox_potential
        
          Biosample --|> QuantityValue : redox_potential
        
      Biosample : rel_air_humidity
        
          Biosample --|> QuantityValue : rel_air_humidity
        
      Biosample : rel_humidity_out
        
          Biosample --|> QuantityValue : rel_humidity_out
        
      Biosample : rel_samp_loc
        
          Biosample --|> rel_samp_loc_enum : rel_samp_loc
        
      Biosample : replicate_number
        
      Biosample : reservoir
        
          Biosample --|> TextValue : reservoir
        
      Biosample : resins_pc
        
          Biosample --|> TextValue : resins_pc
        
      Biosample : rna_absorb1
        
      Biosample : rna_absorb2
        
      Biosample : rna_collect_site
        
      Biosample : rna_concentration
        
      Biosample : rna_cont_type
        
          Biosample --|> JgiContTypeEnum : rna_cont_type
        
      Biosample : rna_cont_well
        
      Biosample : rna_container_id
        
      Biosample : rna_isolate_meth
        
      Biosample : rna_organisms
        
      Biosample : rna_project_contact
        
      Biosample : rna_samp_id
        
      Biosample : rna_sample_format
        
          Biosample --|> rna_sample_format_enum : rna_sample_format
        
      Biosample : rna_sample_name
        
      Biosample : rna_seq_project
        
      Biosample : rna_seq_project_name
        
      Biosample : rna_seq_project_pi
        
      Biosample : rna_volume
        
      Biosample : room_air_exch_rate
        
          Biosample --|> QuantityValue : room_air_exch_rate
        
      Biosample : room_architec_elem
        
      Biosample : room_condt
        
          Biosample --|> room_condt_enum : room_condt
        
      Biosample : room_connected
        
          Biosample --|> room_connected_enum : room_connected
        
      Biosample : room_count
        
          Biosample --|> TextValue : room_count
        
      Biosample : room_dim
        
          Biosample --|> TextValue : room_dim
        
      Biosample : room_door_dist
        
          Biosample --|> TextValue : room_door_dist
        
      Biosample : room_door_share
        
          Biosample --|> TextValue : room_door_share
        
      Biosample : room_hallway
        
          Biosample --|> TextValue : room_hallway
        
      Biosample : room_loc
        
          Biosample --|> room_loc_enum : room_loc
        
      Biosample : room_moist_dam_hist
        
      Biosample : room_net_area
        
          Biosample --|> TextValue : room_net_area
        
      Biosample : room_occup
        
          Biosample --|> QuantityValue : room_occup
        
      Biosample : room_samp_pos
        
          Biosample --|> room_samp_pos_enum : room_samp_pos
        
      Biosample : room_type
        
          Biosample --|> room_type_enum : room_type
        
      Biosample : room_vol
        
          Biosample --|> TextValue : room_vol
        
      Biosample : room_wall_share
        
          Biosample --|> TextValue : room_wall_share
        
      Biosample : room_window_count
        
      Biosample : root_cond
        
          Biosample --|> TextValue : root_cond
        
      Biosample : root_med_carbon
        
          Biosample --|> TextValue : root_med_carbon
        
      Biosample : root_med_macronutr
        
          Biosample --|> TextValue : root_med_macronutr
        
      Biosample : root_med_micronutr
        
          Biosample --|> TextValue : root_med_micronutr
        
      Biosample : root_med_ph
        
          Biosample --|> QuantityValue : root_med_ph
        
      Biosample : root_med_regl
        
          Biosample --|> TextValue : root_med_regl
        
      Biosample : root_med_solid
        
          Biosample --|> TextValue : root_med_solid
        
      Biosample : root_med_suppl
        
          Biosample --|> TextValue : root_med_suppl
        
      Biosample : salinity
        
          Biosample --|> QuantityValue : salinity
        
      Biosample : salinity_category
        
      Biosample : salinity_meth
        
          Biosample --|> TextValue : salinity_meth
        
      Biosample : salt_regm
        
          Biosample --|> TextValue : salt_regm
        
      Biosample : samp_capt_status
        
          Biosample --|> samp_capt_status_enum : samp_capt_status
        
      Biosample : samp_collec_device
        
      Biosample : samp_collec_method
        
      Biosample : samp_collect_point
        
          Biosample --|> samp_collect_point_enum : samp_collect_point
        
      Biosample : samp_dis_stage
        
          Biosample --|> samp_dis_stage_enum : samp_dis_stage
        
      Biosample : samp_floor
        
          Biosample --|> samp_floor_enum : samp_floor
        
      Biosample : samp_loc_corr_rate
        
          Biosample --|> TextValue : samp_loc_corr_rate
        
      Biosample : samp_mat_process
        
          Biosample --|> ControlledTermValue : samp_mat_process
        
      Biosample : samp_md
        
          Biosample --|> QuantityValue : samp_md
        
      Biosample : samp_name
        
      Biosample : samp_preserv
        
          Biosample --|> TextValue : samp_preserv
        
      Biosample : samp_room_id
        
          Biosample --|> TextValue : samp_room_id
        
      Biosample : samp_size
        
          Biosample --|> QuantityValue : samp_size
        
      Biosample : samp_sort_meth
        
          Biosample --|> TextValue : samp_sort_meth
        
      Biosample : samp_store_dur
        
          Biosample --|> TextValue : samp_store_dur
        
      Biosample : samp_store_loc
        
          Biosample --|> TextValue : samp_store_loc
        
      Biosample : samp_store_temp
        
          Biosample --|> QuantityValue : samp_store_temp
        
      Biosample : samp_subtype
        
          Biosample --|> samp_subtype_enum : samp_subtype
        
      Biosample : samp_taxon_id
        
          Biosample --|> ControlledIdentifiedTermValue : samp_taxon_id
        
      Biosample : samp_time_out
        
          Biosample --|> TextValue : samp_time_out
        
      Biosample : samp_transport_cond
        
          Biosample --|> TextValue : samp_transport_cond
        
      Biosample : samp_tvdss
        
          Biosample --|> TextValue : samp_tvdss
        
      Biosample : samp_type
        
          Biosample --|> TextValue : samp_type
        
      Biosample : samp_vol_we_dna_ext
        
          Biosample --|> QuantityValue : samp_vol_we_dna_ext
        
      Biosample : samp_weather
        
          Biosample --|> samp_weather_enum : samp_weather
        
      Biosample : samp_well_name
        
          Biosample --|> TextValue : samp_well_name
        
      Biosample : sample_collection_site
        
      Biosample : sample_link
        
      Biosample : sample_shipped
        
      Biosample : sample_type
        
          Biosample --|> sample_type_enum : sample_type
        
      Biosample : saturates_pc
        
          Biosample --|> TextValue : saturates_pc
        
      Biosample : season
        
          Biosample --|> TextValue : season
        
      Biosample : season_environment
        
          Biosample --|> TextValue : season_environment
        
      Biosample : season_precpt
        
          Biosample --|> QuantityValue : season_precpt
        
      Biosample : season_temp
        
          Biosample --|> QuantityValue : season_temp
        
      Biosample : season_use
        
          Biosample --|> season_use_enum : season_use
        
      Biosample : secondary_treatment
        
          Biosample --|> TextValue : secondary_treatment
        
      Biosample : sediment_type
        
          Biosample --|> sediment_type_enum : sediment_type
        
      Biosample : seq_meth
        
          Biosample --|> TextValue : seq_meth
        
      Biosample : seq_quality_check
        
          Biosample --|> TextValue : seq_quality_check
        
      Biosample : sequencing_field
        
      Biosample : sewage_type
        
          Biosample --|> TextValue : sewage_type
        
      Biosample : shad_dev_water_mold
        
      Biosample : shading_device_cond
        
          Biosample --|> shading_device_cond_enum : shading_device_cond
        
      Biosample : shading_device_loc
        
          Biosample --|> TextValue : shading_device_loc
        
      Biosample : shading_device_mat
        
          Biosample --|> TextValue : shading_device_mat
        
      Biosample : shading_device_type
        
          Biosample --|> shading_device_type_enum : shading_device_type
        
      Biosample : sieving
        
          Biosample --|> TextValue : sieving
        
      Biosample : silicate
        
          Biosample --|> QuantityValue : silicate
        
      Biosample : size_frac
        
          Biosample --|> TextValue : size_frac
        
      Biosample : size_frac_low
        
          Biosample --|> QuantityValue : size_frac_low
        
      Biosample : size_frac_up
        
          Biosample --|> QuantityValue : size_frac_up
        
      Biosample : slope_aspect
        
          Biosample --|> QuantityValue : slope_aspect
        
      Biosample : slope_gradient
        
          Biosample --|> QuantityValue : slope_gradient
        
      Biosample : sludge_retent_time
        
          Biosample --|> QuantityValue : sludge_retent_time
        
      Biosample : sodium
        
          Biosample --|> QuantityValue : sodium
        
      Biosample : soil_horizon
        
          Biosample --|> soil_horizon_enum : soil_horizon
        
      Biosample : soil_text_measure
        
          Biosample --|> QuantityValue : soil_text_measure
        
      Biosample : soil_texture_meth
        
      Biosample : soil_type
        
          Biosample --|> TextValue : soil_type
        
      Biosample : soil_type_meth
        
          Biosample --|> TextValue : soil_type_meth
        
      Biosample : solar_irradiance
        
          Biosample --|> QuantityValue : solar_irradiance
        
      Biosample : soluble_inorg_mat
        
          Biosample --|> TextValue : soluble_inorg_mat
        
      Biosample : soluble_iron_micromol
        
      Biosample : soluble_org_mat
        
          Biosample --|> TextValue : soluble_org_mat
        
      Biosample : soluble_react_phosp
        
          Biosample --|> QuantityValue : soluble_react_phosp
        
      Biosample : source_mat_id
        
          Biosample --|> TextValue : source_mat_id
        
      Biosample : space_typ_state
        
          Biosample --|> TextValue : space_typ_state
        
      Biosample : specific
        
          Biosample --|> specific_enum : specific
        
      Biosample : specific_ecosystem
        
      Biosample : specific_humidity
        
          Biosample --|> QuantityValue : specific_humidity
        
      Biosample : sr_dep_env
        
          Biosample --|> sr_dep_env_enum : sr_dep_env
        
      Biosample : sr_geol_age
        
          Biosample --|> sr_geol_age_enum : sr_geol_age
        
      Biosample : sr_kerog_type
        
          Biosample --|> sr_kerog_type_enum : sr_kerog_type
        
      Biosample : sr_lithology
        
          Biosample --|> sr_lithology_enum : sr_lithology
        
      Biosample : standing_water_regm
        
          Biosample --|> TextValue : standing_water_regm
        
      Biosample : start_date_inc
        
      Biosample : start_time_inc
        
      Biosample : store_cond
        
          Biosample --|> TextValue : store_cond
        
      Biosample : substructure_type
        
          Biosample --|> substructure_type_enum : substructure_type
        
      Biosample : subsurface_depth
        
          Biosample --|> QuantityValue : subsurface_depth
        
      Biosample : sulfate
        
          Biosample --|> QuantityValue : sulfate
        
      Biosample : sulfate_fw
        
          Biosample --|> QuantityValue : sulfate_fw
        
      Biosample : sulfide
        
          Biosample --|> QuantityValue : sulfide
        
      Biosample : surf_air_cont
        
          Biosample --|> surf_air_cont_enum : surf_air_cont
        
      Biosample : surf_humidity
        
          Biosample --|> QuantityValue : surf_humidity
        
      Biosample : surf_material
        
          Biosample --|> surf_material_enum : surf_material
        
      Biosample : surf_moisture
        
          Biosample --|> QuantityValue : surf_moisture
        
      Biosample : surf_moisture_ph
        
      Biosample : surf_temp
        
          Biosample --|> QuantityValue : surf_temp
        
      Biosample : suspend_part_matter
        
          Biosample --|> QuantityValue : suspend_part_matter
        
      Biosample : suspend_solids
        
          Biosample --|> TextValue : suspend_solids
        
      Biosample : tan
        
          Biosample --|> QuantityValue : tan
        
      Biosample : target_gene
        
          Biosample --|> TextValue : target_gene
        
      Biosample : target_subfragment
        
          Biosample --|> TextValue : target_subfragment
        
      Biosample : technical_reps
        
      Biosample : temp
        
          Biosample --|> QuantityValue : temp
        
      Biosample : temp_out
        
          Biosample --|> QuantityValue : temp_out
        
      Biosample : tertiary_treatment
        
          Biosample --|> TextValue : tertiary_treatment
        
      Biosample : tidal_stage
        
          Biosample --|> tidal_stage_enum : tidal_stage
        
      Biosample : tillage
        
          Biosample --|> tillage_enum : tillage
        
      Biosample : tiss_cult_growth_med
        
          Biosample --|> TextValue : tiss_cult_growth_med
        
      Biosample : toluene
        
          Biosample --|> QuantityValue : toluene
        
      Biosample : tot_carb
        
          Biosample --|> QuantityValue : tot_carb
        
      Biosample : tot_depth_water_col
        
          Biosample --|> QuantityValue : tot_depth_water_col
        
      Biosample : tot_diss_nitro
        
          Biosample --|> QuantityValue : tot_diss_nitro
        
      Biosample : tot_inorg_nitro
        
          Biosample --|> QuantityValue : tot_inorg_nitro
        
      Biosample : tot_iron
        
          Biosample --|> QuantityValue : tot_iron
        
      Biosample : tot_nitro
        
          Biosample --|> QuantityValue : tot_nitro
        
      Biosample : tot_nitro_cont_meth
        
      Biosample : tot_nitro_content
        
          Biosample --|> QuantityValue : tot_nitro_content
        
      Biosample : tot_org_c_meth
        
          Biosample --|> TextValue : tot_org_c_meth
        
      Biosample : tot_org_carb
        
          Biosample --|> QuantityValue : tot_org_carb
        
      Biosample : tot_part_carb
        
          Biosample --|> QuantityValue : tot_part_carb
        
      Biosample : tot_phosp
        
          Biosample --|> QuantityValue : tot_phosp
        
      Biosample : tot_phosphate
        
          Biosample --|> QuantityValue : tot_phosphate
        
      Biosample : tot_sulfur
        
          Biosample --|> QuantityValue : tot_sulfur
        
      Biosample : train_line
        
          Biosample --|> train_line_enum : train_line
        
      Biosample : train_stat_loc
        
          Biosample --|> train_stat_loc_enum : train_stat_loc
        
      Biosample : train_stop_loc
        
          Biosample --|> train_stop_loc_enum : train_stop_loc
        
      Biosample : turbidity
        
          Biosample --|> QuantityValue : turbidity
        
      Biosample : tvdss_of_hcr_press
        
          Biosample --|> QuantityValue : tvdss_of_hcr_press
        
      Biosample : tvdss_of_hcr_temp
        
          Biosample --|> QuantityValue : tvdss_of_hcr_temp
        
      Biosample : typ_occup_density
        
      Biosample : type
        
      Biosample : ventilation_rate
        
          Biosample --|> QuantityValue : ventilation_rate
        
      Biosample : ventilation_type
        
          Biosample --|> TextValue : ventilation_type
        
      Biosample : vfa
        
          Biosample --|> QuantityValue : vfa
        
      Biosample : vfa_fw
        
          Biosample --|> QuantityValue : vfa_fw
        
      Biosample : vis_media
        
          Biosample --|> vis_media_enum : vis_media
        
      Biosample : viscosity
        
          Biosample --|> TextValue : viscosity
        
      Biosample : volatile_org_comp
        
          Biosample --|> TextValue : volatile_org_comp
        
      Biosample : wall_area
        
          Biosample --|> QuantityValue : wall_area
        
      Biosample : wall_const_type
        
          Biosample --|> wall_const_type_enum : wall_const_type
        
      Biosample : wall_finish_mat
        
          Biosample --|> wall_finish_mat_enum : wall_finish_mat
        
      Biosample : wall_height
        
          Biosample --|> QuantityValue : wall_height
        
      Biosample : wall_loc
        
          Biosample --|> wall_loc_enum : wall_loc
        
      Biosample : wall_surf_treatment
        
          Biosample --|> wall_surf_treatment_enum : wall_surf_treatment
        
      Biosample : wall_texture
        
          Biosample --|> wall_texture_enum : wall_texture
        
      Biosample : wall_thermal_mass
        
          Biosample --|> QuantityValue : wall_thermal_mass
        
      Biosample : wall_water_mold
        
          Biosample --|> TextValue : wall_water_mold
        
      Biosample : wastewater_type
        
          Biosample --|> TextValue : wastewater_type
        
      Biosample : water_cont_soil_meth
        
      Biosample : water_content
        
      Biosample : water_current
        
          Biosample --|> QuantityValue : water_current
        
      Biosample : water_cut
        
          Biosample --|> QuantityValue : water_cut
        
      Biosample : water_feat_size
        
          Biosample --|> QuantityValue : water_feat_size
        
      Biosample : water_feat_type
        
          Biosample --|> water_feat_type_enum : water_feat_type
        
      Biosample : water_prod_rate
        
          Biosample --|> QuantityValue : water_prod_rate
        
      Biosample : water_temp_regm
        
          Biosample --|> TextValue : water_temp_regm
        
      Biosample : watering_regm
        
          Biosample --|> TextValue : watering_regm
        
      Biosample : weekday
        
          Biosample --|> weekday_enum : weekday
        
      Biosample : win
        
          Biosample --|> TextValue : win
        
      Biosample : wind_direction
        
          Biosample --|> TextValue : wind_direction
        
      Biosample : wind_speed
        
          Biosample --|> QuantityValue : wind_speed
        
      Biosample : window_cond
        
          Biosample --|> window_cond_enum : window_cond
        
      Biosample : window_cover
        
          Biosample --|> window_cover_enum : window_cover
        
      Biosample : window_horiz_pos
        
          Biosample --|> window_horiz_pos_enum : window_horiz_pos
        
      Biosample : window_loc
        
          Biosample --|> window_loc_enum : window_loc
        
      Biosample : window_mat
        
          Biosample --|> window_mat_enum : window_mat
        
      Biosample : window_open_freq
        
          Biosample --|> TextValue : window_open_freq
        
      Biosample : window_size
        
          Biosample --|> TextValue : window_size
        
      Biosample : window_status
        
          Biosample --|> TextValue : window_status
        
      Biosample : window_type
        
          Biosample --|> window_type_enum : window_type
        
      Biosample : window_vert_pos
        
          Biosample --|> window_vert_pos_enum : window_vert_pos
        
      Biosample : window_water_mold
        
          Biosample --|> TextValue : window_water_mold
        
      Biosample : xylene
        
          Biosample --|> QuantityValue : xylene
        
      Biosample : zinc
        
          Biosample --|> QuantityValue : zinc
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [MaterialEntity](MaterialEntity.md)
        * **Biosample**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [host_disease_stat](host_disease_stat.md) | 0..1 <br/> [TextValue](TextValue.md) | List of diseases with which the host has been diagnosed; can include multiple... | direct |
| [neon_biosample_identifiers](neon_biosample_identifiers.md) | 0..* <br/> [ExternalIdentifier](ExternalIdentifier.md) |  | direct |
| [host_taxid](host_taxid.md) | 0..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | NCBI taxon id of the host, e | direct |
| [embargoed](embargoed.md) | 0..1 _recommended_ <br/> [Boolean](Boolean.md) | If true, the data are embargoed and not available for public access | direct |
| [collected_from](collected_from.md) | 0..1 <br/> [FieldResearchSite](FieldResearchSite.md) | The Site from which a Biosample was collected | direct |
| [type](type.md) | 0..1 <br/> [String](String.md) | An optional string that specifies the type object | direct |
| [img_identifiers](img_identifiers.md) | 0..* <br/> [ExternalIdentifier](ExternalIdentifier.md) | A list of identifiers that relate the biosample to records in the IMG databas... | direct |
| [samp_name](samp_name.md) | 0..1 <br/> [String](String.md) | A local identifier or name that for the material sample used for extracting n... | direct |
| [biosample_categories](biosample_categories.md) | 0..* <br/> [BiosampleCategoryEnum](BiosampleCategoryEnum.md) |  | direct |
| [type](type.md) | 0..1 <br/> [String](String.md) | An optional string that specifies the type object | direct |
| [part_of](part_of.md) | 1..* <br/> [Study](Study.md) | Links a resource to another resource that either logically or physically incl... | direct |
| [id](id.md) | 1..1 <br/> [Uriorcurie](Uriorcurie.md) | An NMDC assigned unique identifier for a biosample submitted to NMDC | direct |
| [alternative_identifiers](alternative_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | Unique identifier for a biosample submitted to additional resources | direct |
| [gold_biosample_identifiers](gold_biosample_identifiers.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | Unique identifier for a biosample submitted to GOLD that matches the NMDC sub... | direct |
| [insdc_biosample_identifiers](insdc_biosample_identifiers.md) | 0..* <br/> [ExternalIdentifier](ExternalIdentifier.md) | identifiers for corresponding sample in INSDC | direct |
| [emsl_biosample_identifiers](emsl_biosample_identifiers.md) | 0..* <br/> [ExternalIdentifier](ExternalIdentifier.md) | A list of identifiers for the biosample from the EMSL database | direct |
| [igsn_biosample_identifiers](igsn_biosample_identifiers.md) | 0..* <br/> [ExternalIdentifier](ExternalIdentifier.md) | A list of identifiers for the biosample from the IGSN database | direct |
| [abs_air_humidity](abs_air_humidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Actual mass of water vapor - mh20 - present in the air water vapor mixture | direct |
| [add_recov_method](add_recov_method.md) | 0..1 <br/> [TextValue](TextValue.md) | Additional (i | direct |
| [additional_info](additional_info.md) | 0..1 <br/> [TextValue](TextValue.md) | Information that doesn't fit anywhere else | direct |
| [address](address.md) | 0..1 <br/> [TextValue](TextValue.md) | The street name and building number where the sampling occurred | direct |
| [adj_room](adj_room.md) | 0..1 <br/> [TextValue](TextValue.md) | List of rooms (room number, room name) immediately adjacent to the sampling r... | direct |
| [aero_struc](aero_struc.md) | 0..1 <br/> [TextValue](TextValue.md) | Aerospace structures typically consist of thin plates with stiffeners for the... | direct |
| [agrochem_addition](agrochem_addition.md) | 0..* <br/> [TextValue](TextValue.md) | Addition of fertilizers, pesticides, etc | direct |
| [air_PM_concen](air_PM_concen.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of substances that remain suspended in the air, and comprise mi... | direct |
| [air_temp](air_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Temperature of the air at the time of sampling | direct |
| [air_temp_regm](air_temp_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to varying temperatures; sh... | direct |
| [al_sat](al_sat.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The relative abundance of aluminum in the sample | direct |
| [al_sat_meth](al_sat_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining Aluminum saturation | direct |
| [alkalinity](alkalinity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Alkalinity, the ability of a solution to neutralize acids to the equivalence ... | direct |
| [alkalinity_method](alkalinity_method.md) | 0..1 <br/> [TextValue](TextValue.md) | Method used for alkalinity measurement | direct |
| [alkyl_diethers](alkyl_diethers.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of alkyl diethers | direct |
| [alt](alt.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Altitude is a term used to identify heights of objects such as airplanes, spa... | direct |
| [aminopept_act](aminopept_act.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of aminopeptidase activity | direct |
| [ammonium](ammonium.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of ammonium in the sample | direct |
| [ammonium_nitrogen](ammonium_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of ammonium nitrogen in the sample | direct |
| [amount_light](amount_light.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The unit of illuminance and luminous emittance, measuring luminous flux per u... | direct |
| [ances_data](ances_data.md) | 0..1 <br/> [TextValue](TextValue.md) | Information about either pedigree or other ancestral information description ... | direct |
| [annual_precpt](annual_precpt.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average of all annual precipitation values known, or an estimated equival... | direct |
| [annual_temp](annual_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Mean annual temperature | direct |
| [antibiotic_regm](antibiotic_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving antibiotic administration; should inclu... | direct |
| [api](api.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | API gravity is a measure of how heavy or light a petroleum liquid is compared... | direct |
| [arch_struc](arch_struc.md) | 0..1 <br/> [ArchStrucEnum](ArchStrucEnum.md) | An architectural structure is a human-made, free-standing, immobile outdoor c... | direct |
| [aromatics_pc](aromatics_pc.md) | 0..1 <br/> [TextValue](TextValue.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... | direct |
| [asphaltenes_pc](asphaltenes_pc.md) | 0..1 <br/> [TextValue](TextValue.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... | direct |
| [atmospheric_data](atmospheric_data.md) | 0..* <br/> [TextValue](TextValue.md) | Measurement of atmospheric data; can include multiple data | direct |
| [avg_dew_point](avg_dew_point.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average of dew point measures taken at the beginning of every hour over a... | direct |
| [avg_occup](avg_occup.md) | 0..1 <br/> [TextValue](TextValue.md) | Daily average occupancy of room | direct |
| [avg_temp](avg_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average of temperatures taken at the beginning of every hour over a 24 ho... | direct |
| [bac_prod](bac_prod.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Bacterial production in the water column measured by isotope uptake | direct |
| [bac_resp](bac_resp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of bacterial respiration in the water column | direct |
| [bacteria_carb_prod](bacteria_carb_prod.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of bacterial carbon production | direct |
| [barometric_press](barometric_press.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Force per unit area exerted against a surface by the weight of air above that... | direct |
| [basin](basin.md) | 0..1 <br/> [TextValue](TextValue.md) | Name of the basin (e | direct |
| [bathroom_count](bathroom_count.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of bathrooms in the building | direct |
| [bedroom_count](bedroom_count.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of bedrooms in the building | direct |
| [benzene](benzene.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of benzene in the sample | direct |
| [biochem_oxygen_dem](biochem_oxygen_dem.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Amount of dissolved oxygen needed by aerobic biological organisms in a body o... | direct |
| [biocide](biocide.md) | 0..1 <br/> [TextValue](TextValue.md) | List of biocides (commercial name of product and supplier) and date of admini... | direct |
| [biocide_admin_method](biocide_admin_method.md) | 0..1 <br/> [TextValue](TextValue.md) | Method of biocide administration (dose, frequency, duration, time elapsed bet... | direct |
| [biol_stat](biol_stat.md) | 0..1 <br/> [BiolStatEnum](BiolStatEnum.md) | The level of genome modification | direct |
| [biomass](biomass.md) | 0..* <br/> [TextValue](TextValue.md) | Amount of biomass; should include the name for the part of biomass measured, ... | direct |
| [biotic_regm](biotic_regm.md) | 0..1 <br/> [TextValue](TextValue.md) | Information about treatment(s) involving use of biotic factors, such as bacte... | direct |
| [biotic_relationship](biotic_relationship.md) | 0..1 <br/> [BioticRelationshipEnum](BioticRelationshipEnum.md) | Description of relationship(s) between the subject organism and other organis... | direct |
| [bishomohopanol](bishomohopanol.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of bishomohopanol | direct |
| [blood_press_diast](blood_press_diast.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Resting diastolic blood pressure, measured as mm mercury | direct |
| [blood_press_syst](blood_press_syst.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Resting systolic blood pressure, measured as mm mercury | direct |
| [bromide](bromide.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of bromide | direct |
| [build_docs](build_docs.md) | 0..1 <br/> [BuildDocsEnum](BuildDocsEnum.md) | The building design, construction and operation documents | direct |
| [build_occup_type](build_occup_type.md) | 0..* <br/> [BuildOccupTypeEnum](BuildOccupTypeEnum.md) | The primary function for which a building or discrete part of a building is i... | direct |
| [building_setting](building_setting.md) | 0..1 <br/> [BuildingSettingEnum](BuildingSettingEnum.md) | A location (geography) where a building is set | direct |
| [built_struc_age](built_struc_age.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The age of the built structure since construction | direct |
| [built_struc_set](built_struc_set.md) | 0..1 <br/> [TextValue](TextValue.md) | The characterization of the location of the built structure as high or low hu... | direct |
| [built_struc_type](built_struc_type.md) | 0..1 <br/> [TextValue](TextValue.md) | A physical structure that is a body or assemblage of bodies in space to form ... | direct |
| [calcium](calcium.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of calcium in the sample | direct |
| [carb_dioxide](carb_dioxide.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Carbon dioxide (gas) amount or concentration at the time of sampling | direct |
| [carb_monoxide](carb_monoxide.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Carbon monoxide (gas) amount or concentration at the time of sampling | direct |
| [carb_nitro_ratio](carb_nitro_ratio.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Ratio of amount or concentrations of carbon to nitrogen | direct |
| [ceil_area](ceil_area.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The area of the ceiling space within the room | direct |
| [ceil_cond](ceil_cond.md) | 0..1 <br/> [CeilCondEnum](CeilCondEnum.md) | The physical condition of the ceiling at the time of sampling; photos or vide... | direct |
| [ceil_finish_mat](ceil_finish_mat.md) | 0..1 <br/> [CeilFinishMatEnum](CeilFinishMatEnum.md) | The type of material used to finish a ceiling | direct |
| [ceil_struc](ceil_struc.md) | 0..1 <br/> [TextValue](TextValue.md) | The construction format of the ceiling | direct |
| [ceil_texture](ceil_texture.md) | 0..1 <br/> [CeilTextureEnum](CeilTextureEnum.md) | The feel, appearance, or consistency of a ceiling surface | direct |
| [ceil_thermal_mass](ceil_thermal_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The ability of the ceiling to provide inertia against temperature fluctuation... | direct |
| [ceil_type](ceil_type.md) | 0..1 <br/> [CeilTypeEnum](CeilTypeEnum.md) | The type of ceiling according to the ceiling's appearance or construction | direct |
| [ceil_water_mold](ceil_water_mold.md) | 0..1 <br/> [TextValue](TextValue.md) | Signs of the presence of mold or mildew on the ceiling | direct |
| [chem_administration](chem_administration.md) | 0..* <br/> [ControlledTermValue](ControlledTermValue.md) | List of chemical compounds administered to the host or site where sampling oc... | direct |
| [chem_mutagen](chem_mutagen.md) | 0..* <br/> [TextValue](TextValue.md) | Treatment involving use of mutagens; should include the name of mutagen, amou... | direct |
| [chem_oxygen_dem](chem_oxygen_dem.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | A measure of the capacity of water to consume oxygen during the decomposition... | direct |
| [chem_treat_method](chem_treat_method.md) | 0..1 <br/> [String](String.md) | Method of chemical administration(dose, frequency, duration, time elapsed bet... | direct |
| [chem_treatment](chem_treatment.md) | 0..1 <br/> [TextValue](TextValue.md) | List of chemical compounds administered upstream the sampling location where ... | direct |
| [chimera_check](chimera_check.md) | 0..1 <br/> [TextValue](TextValue.md) | Tool(s) used for chimera checking, including version number and parameters, t... | direct |
| [chloride](chloride.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of chloride in the sample | direct |
| [chlorophyll](chlorophyll.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of chlorophyll | direct |
| [climate_environment](climate_environment.md) | 0..* <br/> [TextValue](TextValue.md) | Treatment involving an exposure to a particular climate; treatment regimen in... | direct |
| [collection_date](collection_date.md) | 0..1 <br/> [TimestampValue](TimestampValue.md) | The time of sampling, either as an instance (single point in time) or interva... | direct |
| [conduc](conduc.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Electrical conductivity of water | direct |
| [cool_syst_id](cool_syst_id.md) | 0..1 <br/> [TextValue](TextValue.md) | The cooling system identifier | direct |
| [core_field](core_field.md) | 0..1 <br/> [String](String.md) | basic fields | direct |
| [crop_rotation](crop_rotation.md) | 0..1 <br/> [TextValue](TextValue.md) | Whether or not crop is rotated, and if yes, rotation schedule | direct |
| [cult_root_med](cult_root_med.md) | 0..1 <br/> [TextValue](TextValue.md) | Name or reference for the hydroponic or in vitro culture rooting medium; can ... | direct |
| [cur_land_use](cur_land_use.md) | 0..1 <br/> [CurLandUseEnum](CurLandUseEnum.md) | Present state of sample site | direct |
| [cur_vegetation](cur_vegetation.md) | 0..1 <br/> [TextValue](TextValue.md) | Vegetation classification from one or more standard classification systems, o... | direct |
| [cur_vegetation_meth](cur_vegetation_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in vegetation classification | direct |
| [date_last_rain](date_last_rain.md) | 0..1 <br/> [TimestampValue](TimestampValue.md) | The date of the last time it rained | direct |
| [density](density.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Density of the sample, which is its mass per unit volume (aka volumetric mass... | direct |
| [depos_env](depos_env.md) | 0..1 <br/> [DeposEnvEnum](DeposEnvEnum.md) | Main depositional environment (https://en | direct |
| [depth](depth.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The vertical distance below local surface, e | direct |
| [dew_point](dew_point.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The temperature to which a given parcel of humid air must be cooled, at const... | direct |
| [diether_lipids](diether_lipids.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of diether lipids; can include multiple types of diether lipids | direct |
| [diss_carb_dioxide](diss_carb_dioxide.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved carbon dioxide in the sample or liquid portion of ... | direct |
| [diss_hydrogen](diss_hydrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved hydrogen | direct |
| [diss_inorg_carb](diss_inorg_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Dissolved inorganic carbon concentration in the sample, typically measured af... | direct |
| [diss_inorg_nitro](diss_inorg_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved inorganic nitrogen | direct |
| [diss_inorg_phosp](diss_inorg_phosp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved inorganic phosphorus in the sample | direct |
| [diss_iron](diss_iron.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved iron in the sample | direct |
| [diss_org_carb](diss_org_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved organic carbon in the sample, liquid portion of th... | direct |
| [diss_org_nitro](diss_org_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Dissolved organic nitrogen concentration measured as; total dissolved nitroge... | direct |
| [diss_oxygen](diss_oxygen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved oxygen | direct |
| [diss_oxygen_fluid](diss_oxygen_fluid.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of dissolved oxygen in the oil field produced fluids as it cont... | direct |
| [dna_cont_well](dna_cont_well.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [door_comp_type](door_comp_type.md) | 0..1 <br/> [DoorCompTypeEnum](DoorCompTypeEnum.md) | The composite type of the door | direct |
| [door_cond](door_cond.md) | 0..1 <br/> [DoorCondEnum](DoorCondEnum.md) | The phsical condition of the door | direct |
| [door_direct](door_direct.md) | 0..1 <br/> [DoorDirectEnum](DoorDirectEnum.md) | The direction the door opens | direct |
| [door_loc](door_loc.md) | 0..1 <br/> [DoorLocEnum](DoorLocEnum.md) | The relative location of the door in the room | direct |
| [door_mat](door_mat.md) | 0..1 <br/> [DoorMatEnum](DoorMatEnum.md) | The material the door is composed of | direct |
| [door_move](door_move.md) | 0..1 <br/> [DoorMoveEnum](DoorMoveEnum.md) | The type of movement of the door | direct |
| [door_size](door_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The size of the door | direct |
| [door_type](door_type.md) | 0..1 <br/> [DoorTypeEnum](DoorTypeEnum.md) | The type of door material | direct |
| [door_type_metal](door_type_metal.md) | 0..1 <br/> [DoorTypeMetalEnum](DoorTypeMetalEnum.md) | The type of metal door | direct |
| [door_type_wood](door_type_wood.md) | 0..1 <br/> [DoorTypeWoodEnum](DoorTypeWoodEnum.md) | The type of wood door | direct |
| [door_water_mold](door_water_mold.md) | 0..1 <br/> [TextValue](TextValue.md) | Signs of the presence of mold or mildew on a door | direct |
| [down_par](down_par.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Visible waveband radiance and irradiance measurements in the water column | direct |
| [drainage_class](drainage_class.md) | 0..1 <br/> [DrainageClassEnum](DrainageClassEnum.md) | Drainage classification from a standard system such as the USDA system | direct |
| [drawings](drawings.md) | 0..1 <br/> [DrawingsEnum](DrawingsEnum.md) | The buildings architectural drawings; if design is chosen, indicate phase-con... | direct |
| [ecosystem](ecosystem.md) | 0..1 <br/> [String](String.md) | An ecosystem is a combination of a physical environment (abiotic factors) and... | direct |
| [ecosystem_category](ecosystem_category.md) | 0..1 <br/> [String](String.md) | Ecosystem categories represent divisions within the ecosystem based on specif... | direct |
| [ecosystem_subtype](ecosystem_subtype.md) | 0..1 <br/> [String](String.md) | Ecosystem subtypes represent further subdivision of Ecosystem types into more... | direct |
| [ecosystem_type](ecosystem_type.md) | 0..1 <br/> [String](String.md) | Ecosystem types represent things having common characteristics within the Eco... | direct |
| [efficiency_percent](efficiency_percent.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Percentage of volatile solids removed from the anaerobic digestor | direct |
| [elev](elev.md) | 0..1 <br/> [Float](Float.md) | Elevation of the sampling site is its height above a fixed reference point, m... | direct |
| [elevator](elevator.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of elevators within the built structure | direct |
| [emulsions](emulsions.md) | 0..* <br/> [TextValue](TextValue.md) | Amount or concentration of substances such as paints, adhesives, mayonnaise, ... | direct |
| [env_broad_scale](env_broad_scale.md) | 1..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | Report the major environmental system the sample or specimen came from | direct |
| [env_local_scale](env_local_scale.md) | 1..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | Report the entity or entities which are in the sample or specimen’s local vic... | direct |
| [env_medium](env_medium.md) | 1..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | Report the environmental material(s) immediately surrounding the sample or sp... | direct |
| [env_package](env_package.md) | 0..1 <br/> [TextValue](TextValue.md) | MIxS extension for reporting of measurements and observations obtained from o... | direct |
| [environment_field](environment_field.md) | 0..1 <br/> [String](String.md) | field describing environmental aspect of a sample | direct |
| [escalator](escalator.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of escalators within the built structure | direct |
| [ethylbenzene](ethylbenzene.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of ethylbenzene in the sample | direct |
| [exp_duct](exp_duct.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The amount of exposed ductwork in the room | direct |
| [exp_pipe](exp_pipe.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of exposed pipes in the room | direct |
| [experimental_factor](experimental_factor.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Experimental factors are essentially the variable aspects of an experiment de... | direct |
| [ext_door](ext_door.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of exterior doors in the built structure | direct |
| [ext_wall_orient](ext_wall_orient.md) | 0..1 <br/> [ExtWallOrientEnum](ExtWallOrientEnum.md) | The orientation of the exterior wall | direct |
| [ext_window_orient](ext_window_orient.md) | 0..1 <br/> [ExtWindowOrientEnum](ExtWindowOrientEnum.md) | The compass direction the exterior window of the room is facing | direct |
| [extreme_event](extreme_event.md) | 0..1 <br/> [String](String.md) | Unusual physical events that may have affected microbial populations | direct |
| [fao_class](fao_class.md) | 0..1 <br/> [FaoClassEnum](FaoClassEnum.md) | Soil classification from the FAO World Reference Database for Soil Resources | direct |
| [fertilizer_regm](fertilizer_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving the use of fertilizers; should include ... | direct |
| [field](field.md) | 0..1 <br/> [TextValue](TextValue.md) | Name of the hydrocarbon field (e | direct |
| [filter_type](filter_type.md) | 0..* <br/> [FilterTypeEnum](FilterTypeEnum.md) | A device which removes solid particulates or airborne molecular contaminants | direct |
| [fire](fire.md) | 0..1 <br/> [String](String.md) | Historical and/or physical evidence of fire | direct |
| [fireplace_type](fireplace_type.md) | 0..1 <br/> [TextValue](TextValue.md) | A firebox with chimney | direct |
| [flooding](flooding.md) | 0..1 <br/> [String](String.md) | Historical and/or physical evidence of flooding | direct |
| [floor_age](floor_age.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The time period since installment of the carpet or flooring | direct |
| [floor_area](floor_area.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The area of the floor space within the room | direct |
| [floor_cond](floor_cond.md) | 0..1 <br/> [FloorCondEnum](FloorCondEnum.md) | The physical condition of the floor at the time of sampling; photos or video ... | direct |
| [floor_count](floor_count.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of floors in the building, including basements and mechanical pent... | direct |
| [floor_finish_mat](floor_finish_mat.md) | 0..1 <br/> [FloorFinishMatEnum](FloorFinishMatEnum.md) | The floor covering type; the finished surface that is walked on | direct |
| [floor_struc](floor_struc.md) | 0..1 <br/> [FloorStrucEnum](FloorStrucEnum.md) | Refers to the structural elements and subfloor upon which the finish flooring... | direct |
| [floor_thermal_mass](floor_thermal_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The ability of the floor to provide inertia against temperature fluctuations | direct |
| [floor_water_mold](floor_water_mold.md) | 0..1 <br/> [FloorWaterMoldEnum](FloorWaterMoldEnum.md) | Signs of the presence of mold or mildew in a room | direct |
| [fluor](fluor.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Raw or converted fluorescence of water | direct |
| [freq_clean](freq_clean.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of times the sample location is cleaned | direct |
| [freq_cook](freq_cook.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of times a meal is cooked per week | direct |
| [fungicide_regm](fungicide_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of fungicides; should include the n... | direct |
| [furniture](furniture.md) | 0..1 <br/> [FurnitureEnum](FurnitureEnum.md) | The types of furniture present in the sampled room | direct |
| [gaseous_environment](gaseous_environment.md) | 0..* <br/> [TextValue](TextValue.md) | Use of conditions with differing gaseous environments; should include the nam... | direct |
| [gaseous_substances](gaseous_substances.md) | 0..* <br/> [TextValue](TextValue.md) | Amount or concentration of substances such as hydrogen sulfide, carbon dioxid... | direct |
| [gender_restroom](gender_restroom.md) | 0..1 <br/> [GenderRestroomEnum](GenderRestroomEnum.md) | The gender type of the restroom | direct |
| [genetic_mod](genetic_mod.md) | 0..1 <br/> [TextValue](TextValue.md) | Genetic modifications of the genome of an organism, which may occur naturally... | direct |
| [geo_loc_name](geo_loc_name.md) | 0..1 <br/> [TextValue](TextValue.md) | The geographical origin of the sample as defined by the country or sea name f... | direct |
| [glucosidase_act](glucosidase_act.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of glucosidase activity | direct |
| [gravidity](gravidity.md) | 0..1 <br/> [TextValue](TextValue.md) | Whether or not subject is gravid, and if yes date due or date post-conception... | direct |
| [gravity](gravity.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of gravity factor to study various ... | direct |
| [growth_facil](growth_facil.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Type of facility where the sampled plant was grown; controlled vocabulary: gr... | direct |
| [growth_habit](growth_habit.md) | 0..1 <br/> [GrowthHabitEnum](GrowthHabitEnum.md) | Characteristic shape, appearance or growth form of a plant species | direct |
| [growth_hormone_regm](growth_hormone_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of growth hormones; should include ... | direct |
| [hall_count](hall_count.md) | 0..1 <br/> [TextValue](TextValue.md) | The total count of hallways and cooridors in the built structure | direct |
| [handidness](handidness.md) | 0..1 <br/> [HandidnessEnum](HandidnessEnum.md) | The handidness of the individual sampled | direct |
| [has_numeric_value](has_numeric_value.md) | 0..1 <br/> [Double](Double.md) |  | direct |
| [has_raw_value](has_raw_value.md) | 0..1 <br/> [String](String.md) |  | direct |
| [has_unit](has_unit.md) | 0..1 <br/> [String](String.md) | Example "m" | direct |
| [hc_produced](hc_produced.md) | 0..1 <br/> [HcProducedEnum](HcProducedEnum.md) | Main hydrocarbon type produced from resource (i | direct |
| [hcr](hcr.md) | 0..1 <br/> [HcrEnum](HcrEnum.md) | Main Hydrocarbon Resource type | direct |
| [hcr_fw_salinity](hcr_fw_salinity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Original formation water salinity (prior to secondary recovery e | direct |
| [hcr_geol_age](hcr_geol_age.md) | 0..1 <br/> [HcrGeolAgeEnum](HcrGeolAgeEnum.md) | Geological age of hydrocarbon resource (Additional info: https://en | direct |
| [hcr_pressure](hcr_pressure.md) | 0..1 <br/> [TextValue](TextValue.md) | Original pressure of the hydrocarbon resource | direct |
| [hcr_temp](hcr_temp.md) | 0..1 <br/> [TextValue](TextValue.md) | Original temperature of the hydrocarbon resource | direct |
| [heat_cool_type](heat_cool_type.md) | 0..* <br/> [HeatCoolTypeEnum](HeatCoolTypeEnum.md) | Methods of conditioning or heating a room or building | direct |
| [heat_deliv_loc](heat_deliv_loc.md) | 0..1 <br/> [HeatDelivLocEnum](HeatDelivLocEnum.md) | The location of heat delivery within the room | direct |
| [heat_sys_deliv_meth](heat_sys_deliv_meth.md) | 0..1 <br/> [String](String.md) | The method by which the heat is delivered through the system | direct |
| [heat_system_id](heat_system_id.md) | 0..1 <br/> [TextValue](TextValue.md) | The heating system identifier | direct |
| [heavy_metals](heavy_metals.md) | 0..* <br/> [TextValue](TextValue.md) | Heavy metals present in the sample and their concentrations | direct |
| [heavy_metals_meth](heavy_metals_meth.md) | 0..* <br/> [TextValue](TextValue.md) | Reference or method used in determining heavy metals | direct |
| [height_carper_fiber](height_carper_fiber.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average carpet fiber height in the indoor environment | direct |
| [herbicide_regm](herbicide_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of herbicides; information about tr... | direct |
| [horizon_meth](horizon_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining the horizon | direct |
| [host_age](host_age.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Age of host at the time of sampling; relevant scale depends on species and st... | direct |
| [host_body_habitat](host_body_habitat.md) | 0..1 <br/> [TextValue](TextValue.md) | Original body habitat where the sample was obtained from | direct |
| [host_body_product](host_body_product.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Substance produced by the body, e | direct |
| [host_body_site](host_body_site.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Name of body site where the sample was obtained from, such as a specific orga... | direct |
| [host_body_temp](host_body_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Core body temperature of the host when sample was collected | direct |
| [host_color](host_color.md) | 0..1 <br/> [TextValue](TextValue.md) | The color of host | direct |
| [host_common_name](host_common_name.md) | 0..1 <br/> [TextValue](TextValue.md) | Common name of the host | direct |
| [host_diet](host_diet.md) | 0..* <br/> [TextValue](TextValue.md) | Type of diet depending on the host, for animals omnivore, herbivore etc | direct |
| [host_dry_mass](host_dry_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of dry mass | direct |
| [host_family_relation](host_family_relation.md) | 0..* <br/> [String](String.md) | Familial relationships to other hosts in the same study; can include multiple... | direct |
| [host_genotype](host_genotype.md) | 0..1 <br/> [TextValue](TextValue.md) | Observed genotype | direct |
| [host_growth_cond](host_growth_cond.md) | 0..1 <br/> [TextValue](TextValue.md) | Literature reference giving growth conditions of the host | direct |
| [host_height](host_height.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The height of subject | direct |
| [host_last_meal](host_last_meal.md) | 0..* <br/> [TextValue](TextValue.md) | Content of last meal and time since feeding; can include multiple values | direct |
| [host_length](host_length.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The length of subject | direct |
| [host_life_stage](host_life_stage.md) | 0..1 <br/> [TextValue](TextValue.md) | Description of life stage of host | direct |
| [host_phenotype](host_phenotype.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Phenotype of human or other host | direct |
| [host_sex](host_sex.md) | 0..1 <br/> [HostSexEnum](HostSexEnum.md) | Gender or physical sex of the host | direct |
| [host_shape](host_shape.md) | 0..1 <br/> [TextValue](TextValue.md) | Morphological shape of host | direct |
| [host_subject_id](host_subject_id.md) | 0..1 <br/> [TextValue](TextValue.md) | A unique identifier by which each subject can be referred to, de-identified | direct |
| [host_subspecf_genlin](host_subspecf_genlin.md) | 0..* <br/> [String](String.md) | Information about the genetic distinctness of the host organism below the sub... | direct |
| [host_substrate](host_substrate.md) | 0..1 <br/> [TextValue](TextValue.md) | The growth substrate of the host | direct |
| [host_symbiont](host_symbiont.md) | 0..* <br/> [String](String.md) | The taxonomic name of the organism(s) found living in mutualistic, commensali... | direct |
| [host_taxid](host_taxid.md) | 0..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | NCBI taxon id of the host, e | direct |
| [host_tot_mass](host_tot_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total mass of the host at collection, the unit depends on host | direct |
| [host_wet_mass](host_wet_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of wet mass | direct |
| [humidity](humidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Amount of water vapour in the air, at the time of sampling | direct |
| [humidity_regm](humidity_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to varying degree of humidi... | direct |
| [indoor_space](indoor_space.md) | 0..1 <br/> [IndoorSpaceEnum](IndoorSpaceEnum.md) | A distinguishable space within a structure, the purpose for which discrete ar... | direct |
| [indoor_surf](indoor_surf.md) | 0..1 <br/> [IndoorSurfEnum](IndoorSurfEnum.md) | Type of indoor surface | direct |
| [indust_eff_percent](indust_eff_percent.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Percentage of industrial effluents received by wastewater treatment plant | direct |
| [inorg_particles](inorg_particles.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of particles such as sand, grit, metal particles, ceramics, etc | direct |
| [inside_lux](inside_lux.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The recorded value at sampling time (power density) | direct |
| [int_wall_cond](int_wall_cond.md) | 0..1 <br/> [IntWallCondEnum](IntWallCondEnum.md) | The physical condition of the wall at the time of sampling; photos or video p... | direct |
| [investigation_field](investigation_field.md) | 0..1 <br/> [String](String.md) | field describing aspect of the investigation/study to which the sample belong... | direct |
| [iw_bt_date_well](iw_bt_date_well.md) | 0..1 <br/> [TimestampValue](TimestampValue.md) | Injection water breakthrough date per well following a secondary and/or terti... | direct |
| [iwf](iwf.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Proportion of the produced fluids derived from injected water at the time of ... | direct |
| [last_clean](last_clean.md) | 0..1 <br/> [TimestampValue](TimestampValue.md) | The last time the floor was cleaned (swept, mopped, vacuumed) | direct |
| [lat_lon](lat_lon.md) | 0..1 <br/> [GeolocationValue](GeolocationValue.md) | The geographical origin of the sample as defined by latitude and longitude | direct |
| [lbc_thirty](lbc_thirty.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | lime buffer capacity, determined after 30 minute incubation | direct |
| [lbceq](lbceq.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | lime buffer capacity, determined at equilibrium after 5 day incubation | direct |
| [light_intensity](light_intensity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of light intensity | direct |
| [light_regm](light_regm.md) | 0..1 <br/> [TextValue](TextValue.md) | Information about treatment(s) involving exposure to light, including both li... | direct |
| [light_type](light_type.md) | 0..* <br/> [LightTypeEnum](LightTypeEnum.md) | Application of light to achieve some practical or aesthetic effect | direct |
| [link_addit_analys](link_addit_analys.md) | 0..1 <br/> [TextValue](TextValue.md) | Link to additional analysis results performed on the sample | direct |
| [link_class_info](link_class_info.md) | 0..1 <br/> [TextValue](TextValue.md) | Link to digitized soil maps or other soil classification information | direct |
| [link_climate_info](link_climate_info.md) | 0..1 <br/> [TextValue](TextValue.md) | Link to climate resource | direct |
| [lithology](lithology.md) | 0..1 <br/> [LithologyEnum](LithologyEnum.md) | Hydrocarbon resource main lithology (Additional information: http://petrowiki | direct |
| [local_class](local_class.md) | 0..1 <br/> [TextValue](TextValue.md) | Soil classification based on local soil classification system | direct |
| [local_class_meth](local_class_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining the local soil classification | direct |
| [magnesium](magnesium.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of magnesium in the sample | direct |
| [manganese](manganese.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of manganese in the sample | direct |
| [max_occup](max_occup.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The maximum amount of people allowed in the indoor environment | direct |
| [mean_frict_vel](mean_frict_vel.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of mean friction velocity | direct |
| [mean_peak_frict_vel](mean_peak_frict_vel.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of mean peak friction velocity | direct |
| [mech_struc](mech_struc.md) | 0..1 <br/> [MechStrucEnum](MechStrucEnum.md) | mechanical structure: a moving structure | direct |
| [mechanical_damage](mechanical_damage.md) | 0..* <br/> [TextValue](TextValue.md) | Information about any mechanical damage exerted on the plant; can include mul... | direct |
| [methane](methane.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Methane (gas) amount or concentration at the time of sampling | direct |
| [micro_biomass_meth](micro_biomass_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining microbial biomass | direct |
| [microbial_biomass](microbial_biomass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The part of the organic matter in the soil that constitutes living microorgan... | direct |
| [mineral_nutr_regm](mineral_nutr_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving the use of mineral supplements; should ... | direct |
| [misc_param](misc_param.md) | 0..* <br/> [TextValue](TextValue.md) | Any other measurement performed or parameter collected, that is not listed he... | direct |
| [n_alkanes](n_alkanes.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of n-alkanes; can include multiple n-alkanes | direct |
| [nitrate](nitrate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrate in the sample | direct |
| [nitrate_nitrogen](nitrate_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrate nitrogen in the sample | direct |
| [nitrite](nitrite.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrite in the sample | direct |
| [nitrite_nitrogen](nitrite_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrite nitrogen in the sample | direct |
| [nitro](nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrogen (total) | direct |
| [non_min_nutr_regm](non_min_nutr_regm.md) | 0..* <br/> [String](String.md) | Information about treatment involving the exposure of plant to non-mineral nu... | direct |
| [nucl_acid_amp](nucl_acid_amp.md) | 0..1 <br/> [TextValue](TextValue.md) | A link to a literature reference, electronic resource or a standard operating... | direct |
| [nucl_acid_ext](nucl_acid_ext.md) | 0..1 <br/> [TextValue](TextValue.md) | A link to a literature reference, electronic resource or a standard operating... | direct |
| [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md) | 0..1 <br/> [String](String.md) |  | direct |
| [number_pets](number_pets.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of pets residing in the sampled space | direct |
| [number_plants](number_plants.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of plant(s) in the sampling space | direct |
| [number_resident](number_resident.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The number of individuals currently occupying in the sampling location | direct |
| [occup_density_samp](occup_density_samp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Average number of occupants at time of sampling per square footage | direct |
| [occup_document](occup_document.md) | 0..1 <br/> [OccupDocumentEnum](OccupDocumentEnum.md) | The type of documentation of occupancy | direct |
| [occup_samp](occup_samp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Number of occupants present at time of sample within the given space | direct |
| [org_carb](org_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of organic carbon | direct |
| [org_count_qpcr_info](org_count_qpcr_info.md) | 0..1 <br/> [String](String.md) | If qpcr was used for the cell count, the target gene name, the primer sequenc... | direct |
| [org_matter](org_matter.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of organic matter | direct |
| [org_nitro](org_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of organic nitrogen | direct |
| [org_particles](org_particles.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of particles such as faeces, hairs, food, vomit, paper fibers, ... | direct |
| [organism_count](organism_count.md) | 0..* <br/> [QuantityValue](QuantityValue.md) | Total cell count of any organism (or group of organisms) per gram, volume or ... | direct |
| [owc_tvdss](owc_tvdss.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Depth of the original oil water contact (OWC) zone (average) (m TVDSS) | direct |
| [oxy_stat_samp](oxy_stat_samp.md) | 0..1 <br/> [OxyStatSampEnum](OxyStatSampEnum.md) | Oxygenation status of sample | direct |
| [oxygen](oxygen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Oxygen (gas) amount or concentration at the time of sampling | direct |
| [part_org_carb](part_org_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of particulate organic carbon | direct |
| [part_org_nitro](part_org_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of particulate organic nitrogen | direct |
| [particle_class](particle_class.md) | 0..* <br/> [TextValue](TextValue.md) | Particles are classified, based on their size, into six general categories:cl... | direct |
| [pcr_cond](pcr_cond.md) | 0..1 <br/> [TextValue](TextValue.md) | Description of reaction conditions and components of PCR in the form of 'init... | direct |
| [pcr_primers](pcr_primers.md) | 0..1 <br/> [TextValue](TextValue.md) | PCR primers that were used to amplify the sequence of the targeted gene, locu... | direct |
| [permeability](permeability.md) | 0..1 <br/> [TextValue](TextValue.md) | Measure of the ability of a hydrocarbon resource to allow fluids to pass thro... | direct |
| [perturbation](perturbation.md) | 0..* <br/> [TextValue](TextValue.md) | Type of perturbation, e | direct |
| [pesticide_regm](pesticide_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of insecticides; should include the... | direct |
| [petroleum_hydrocarb](petroleum_hydrocarb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of petroleum hydrocarbon | direct |
| [ph](ph.md) | 0..1 <br/> [Double](Double.md) | Ph measurement of the sample, or liquid portion of sample, or aqueous phase o... | direct |
| [ph_meth](ph_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining ph | direct |
| [ph_regm](ph_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving exposure of plants to varying levels of... | direct |
| [phaeopigments](phaeopigments.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of phaeopigments; can include multiple phaeopigments | direct |
| [phosphate](phosphate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of phosphate | direct |
| [phosplipid_fatt_acid](phosplipid_fatt_acid.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of phospholipid fatty acids; can include multiple values | direct |
| [photon_flux](photon_flux.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of photon flux | direct |
| [plant_growth_med](plant_growth_med.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Specification of the media for growing the plants or tissue cultured samples,... | direct |
| [plant_product](plant_product.md) | 0..1 <br/> [TextValue](TextValue.md) | Substance produced by the plant, where the sample was obtained from | direct |
| [plant_sex](plant_sex.md) | 0..1 <br/> [PlantSexEnum](PlantSexEnum.md) | Sex of the reproductive parts on the whole plant, e | direct |
| [plant_struc](plant_struc.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Name of plant structure the sample was obtained from; for Plant Ontology (PO)... | direct |
| [pollutants](pollutants.md) | 0..* <br/> [TextValue](TextValue.md) | Pollutant types and, amount or concentrations measured at the time of samplin... | direct |
| [pool_dna_extracts](pool_dna_extracts.md) | 0..1 <br/> [TextValue](TextValue.md) | Indicate whether multiple DNA extractions were mixed | direct |
| [porosity](porosity.md) | 0..1 <br/> [TextValue](TextValue.md) | Porosity of deposited sediment is volume of voids divided by the total volume... | direct |
| [potassium](potassium.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of potassium in the sample | direct |
| [pour_point](pour_point.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Temperature at which a liquid becomes semi solid and loses its flow character... | direct |
| [pre_treatment](pre_treatment.md) | 0..1 <br/> [TextValue](TextValue.md) | The process of pre-treatment removes materials that can be easily collected f... | direct |
| [pres_animal_insect](pres_animal_insect.md) | 0..1 <br/> [String](String.md) | The type and number of animals or insects present in the sampling space | direct |
| [pressure](pressure.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Pressure to which the sample is subject to, in atmospheres | direct |
| [prev_land_use_meth](prev_land_use_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining previous land use and dates | direct |
| [previous_land_use](previous_land_use.md) | 0..1 <br/> [TextValue](TextValue.md) | Previous land use and dates | direct |
| [primary_prod](primary_prod.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of primary production, generally measured as isotope uptake | direct |
| [primary_treatment](primary_treatment.md) | 0..1 <br/> [TextValue](TextValue.md) | The process to produce both a generally homogeneous liquid capable of being t... | direct |
| [prod_rate](prod_rate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Oil and/or gas production rates per well (e | direct |
| [prod_start_date](prod_start_date.md) | 0..1 <br/> [TimestampValue](TimestampValue.md) | Date of field's first production | direct |
| [profile_position](profile_position.md) | 0..1 <br/> [ProfilePositionEnum](ProfilePositionEnum.md) | Cross-sectional position in the hillslope where sample was collected | direct |
| [quad_pos](quad_pos.md) | 0..1 <br/> [QuadPosEnum](QuadPosEnum.md) | The quadrant position of the sampling room within the building | direct |
| [radiation_regm](radiation_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving exposure of plant or a plant part to a ... | direct |
| [rainfall_regm](rainfall_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to a given amount of rainfa... | direct |
| [reactor_type](reactor_type.md) | 0..1 <br/> [TextValue](TextValue.md) | Anaerobic digesters can be designed and engineered to operate using a number ... | direct |
| [redox_potential](redox_potential.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Redox potential, measured relative to a hydrogen cell, indicating oxidation o... | direct |
| [rel_air_humidity](rel_air_humidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Partial vapor and air pressure, density of the vapor and air, or by the actua... | direct |
| [rel_humidity_out](rel_humidity_out.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The recorded outside relative humidity value at the time of sampling | direct |
| [rel_samp_loc](rel_samp_loc.md) | 0..1 <br/> [RelSampLocEnum](RelSampLocEnum.md) | The sampling location within the train car | direct |
| [reservoir](reservoir.md) | 0..1 <br/> [TextValue](TextValue.md) | Name of the reservoir (e | direct |
| [resins_pc](resins_pc.md) | 0..1 <br/> [TextValue](TextValue.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... | direct |
| [room_air_exch_rate](room_air_exch_rate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The rate at which outside air replaces indoor air in a given space | direct |
| [room_architec_elem](room_architec_elem.md) | 0..1 <br/> [String](String.md) | The unique details and component parts that, together, form the architecture ... | direct |
| [room_condt](room_condt.md) | 0..1 <br/> [RoomCondtEnum](RoomCondtEnum.md) | The condition of the room at the time of sampling | direct |
| [room_connected](room_connected.md) | 0..1 <br/> [RoomConnectedEnum](RoomConnectedEnum.md) | List of rooms connected to the sampling room by a doorway | direct |
| [room_count](room_count.md) | 0..1 <br/> [TextValue](TextValue.md) | The total count of rooms in the built structure including all room types | direct |
| [room_dim](room_dim.md) | 0..1 <br/> [TextValue](TextValue.md) | The length, width and height of sampling room | direct |
| [room_door_dist](room_door_dist.md) | 0..1 <br/> [TextValue](TextValue.md) | Distance between doors (meters) in the hallway between the sampling room and ... | direct |
| [room_door_share](room_door_share.md) | 0..1 <br/> [TextValue](TextValue.md) | List of room(s) (room number, room name) sharing a door with the sampling roo... | direct |
| [room_hallway](room_hallway.md) | 0..1 <br/> [TextValue](TextValue.md) | List of room(s) (room number, room name) located in the same hallway as sampl... | direct |
| [room_loc](room_loc.md) | 0..1 <br/> [RoomLocEnum](RoomLocEnum.md) | The position of the room within the building | direct |
| [room_moist_dam_hist](room_moist_dam_hist.md) | 0..1 <br/> [Integer](Integer.md) | The history of moisture damage or mold in the past 12 months | direct |
| [room_net_area](room_net_area.md) | 0..1 <br/> [TextValue](TextValue.md) | The net floor area of sampling room | direct |
| [room_occup](room_occup.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Count of room occupancy at time of sampling | direct |
| [room_samp_pos](room_samp_pos.md) | 0..1 <br/> [RoomSampPosEnum](RoomSampPosEnum.md) | The horizontal sampling position in the room relative to architectural elemen... | direct |
| [room_type](room_type.md) | 0..1 <br/> [RoomTypeEnum](RoomTypeEnum.md) | The main purpose or activity of the sampling room | direct |
| [room_vol](room_vol.md) | 0..1 <br/> [TextValue](TextValue.md) | Volume of sampling room | direct |
| [room_wall_share](room_wall_share.md) | 0..1 <br/> [TextValue](TextValue.md) | List of room(s) (room number, room name) sharing a wall with the sampling roo... | direct |
| [room_window_count](room_window_count.md) | 0..1 <br/> [Integer](Integer.md) | Number of windows in the room | direct |
| [root_cond](root_cond.md) | 0..1 <br/> [TextValue](TextValue.md) | Relevant rooting conditions such as field plot size, sowing density, containe... | direct |
| [root_med_carbon](root_med_carbon.md) | 0..1 <br/> [TextValue](TextValue.md) | Source of organic carbon in the culture rooting medium; e | direct |
| [root_med_macronutr](root_med_macronutr.md) | 0..1 <br/> [TextValue](TextValue.md) | Measurement of the culture rooting medium macronutrients (N,P, K, Ca, Mg, S);... | direct |
| [root_med_micronutr](root_med_micronutr.md) | 0..1 <br/> [TextValue](TextValue.md) | Measurement of the culture rooting medium micronutrients (Fe, Mn, Zn, B, Cu, ... | direct |
| [root_med_ph](root_med_ph.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | pH measurement of the culture rooting medium; e | direct |
| [root_med_regl](root_med_regl.md) | 0..1 <br/> [TextValue](TextValue.md) | Growth regulators in the culture rooting medium such as cytokinins, auxins, g... | direct |
| [root_med_solid](root_med_solid.md) | 0..1 <br/> [TextValue](TextValue.md) | Specification of the solidifying agent in the culture rooting medium; e | direct |
| [root_med_suppl](root_med_suppl.md) | 0..1 <br/> [TextValue](TextValue.md) | Organic supplements of the culture rooting medium, such as vitamins, amino ac... | direct |
| [salinity](salinity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The total concentration of all dissolved salts in a liquid or solid sample | direct |
| [salinity_meth](salinity_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining salinity | direct |
| [salt_regm](salt_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving use of salts as supplement to liquid an... | direct |
| [samp_capt_status](samp_capt_status.md) | 0..1 <br/> [SampCaptStatusEnum](SampCaptStatusEnum.md) | Reason for the sample | direct |
| [samp_collec_device](samp_collec_device.md) | 0..1 <br/> [String](String.md) | The device used to collect an environmental sample | direct |
| [samp_collec_method](samp_collec_method.md) | 0..1 <br/> [String](String.md) | The method employed for collecting the sample | direct |
| [samp_collect_point](samp_collect_point.md) | 0..1 <br/> [SampCollectPointEnum](SampCollectPointEnum.md) | Sampling point on the asset were sample was collected (e | direct |
| [samp_dis_stage](samp_dis_stage.md) | 0..1 <br/> [SampDisStageEnum](SampDisStageEnum.md) | Stage of the disease at the time of sample collection, e | direct |
| [samp_floor](samp_floor.md) | 0..1 <br/> [SampFloorEnum](SampFloorEnum.md) | The floor of the building, where the sampling room is located | direct |
| [samp_loc_corr_rate](samp_loc_corr_rate.md) | 0..1 <br/> [TextValue](TextValue.md) | Metal corrosion rate is the speed of metal deterioration due to environmental... | direct |
| [samp_mat_process](samp_mat_process.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | A brief description of any processing applied to the sample during or after r... | direct |
| [samp_md](samp_md.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | In non deviated well, measured depth is equal to the true vertical depth, TVD... | direct |
| [samp_name](samp_name.md) | 0..1 <br/> [String](String.md) | A local identifier or name that for the material sample used for extracting n... | direct |
| [samp_preserv](samp_preserv.md) | 0..1 <br/> [TextValue](TextValue.md) | Preservative added to the sample (e | direct |
| [samp_room_id](samp_room_id.md) | 0..1 <br/> [TextValue](TextValue.md) | Sampling room number | direct |
| [samp_size](samp_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample coll... | direct |
| [samp_sort_meth](samp_sort_meth.md) | 0..* <br/> [TextValue](TextValue.md) | Method by which samples are sorted; open face filter collecting total suspend... | direct |
| [samp_store_dur](samp_store_dur.md) | 0..1 <br/> [TextValue](TextValue.md) | Duration for which the sample was stored | direct |
| [samp_store_loc](samp_store_loc.md) | 0..1 <br/> [TextValue](TextValue.md) | Location at which sample was stored, usually name of a specific freezer/room | direct |
| [samp_store_temp](samp_store_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Temperature at which sample was stored, e | direct |
| [samp_subtype](samp_subtype.md) | 0..1 <br/> [SampSubtypeEnum](SampSubtypeEnum.md) | Name of sample sub-type | direct |
| [samp_taxon_id](samp_taxon_id.md) | 0..1 <br/> [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | NCBI taxon id of the sample | direct |
| [samp_time_out](samp_time_out.md) | 0..1 <br/> [TextValue](TextValue.md) | The recent and long term history of outside sampling | direct |
| [samp_transport_cond](samp_transport_cond.md) | 0..1 <br/> [TextValue](TextValue.md) | Sample transport duration (in days or hrs) and temperature the sample was exp... | direct |
| [samp_tvdss](samp_tvdss.md) | 0..1 <br/> [TextValue](TextValue.md) | Depth of the sample i | direct |
| [samp_type](samp_type.md) | 0..1 <br/> [TextValue](TextValue.md) | The type of material from which the sample was obtained | direct |
| [samp_vol_we_dna_ext](samp_vol_we_dna_ext.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Volume (ml) or mass (g) of total collected sample processed for DNA extractio... | direct |
| [samp_weather](samp_weather.md) | 0..1 <br/> [SampWeatherEnum](SampWeatherEnum.md) | The weather on the sampling day | direct |
| [samp_well_name](samp_well_name.md) | 0..1 <br/> [TextValue](TextValue.md) | Name of the well (e | direct |
| [saturates_pc](saturates_pc.md) | 0..1 <br/> [TextValue](TextValue.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... | direct |
| [season](season.md) | 0..1 <br/> [TextValue](TextValue.md) | The season when sampling occurred | direct |
| [season_environment](season_environment.md) | 0..* <br/> [TextValue](TextValue.md) | Treatment involving an exposure to a particular season (e | direct |
| [season_precpt](season_precpt.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average of all seasonal precipitation values known, or an estimated equiv... | direct |
| [season_temp](season_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Mean seasonal temperature | direct |
| [season_use](season_use.md) | 0..1 <br/> [SeasonUseEnum](SeasonUseEnum.md) | The seasons the space is occupied | direct |
| [secondary_treatment](secondary_treatment.md) | 0..1 <br/> [TextValue](TextValue.md) | The process for substantially degrading the biological content of the sewage | direct |
| [sediment_type](sediment_type.md) | 0..1 <br/> [SedimentTypeEnum](SedimentTypeEnum.md) | Information about the sediment type based on major constituents | direct |
| [seq_meth](seq_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Sequencing machine used | direct |
| [seq_quality_check](seq_quality_check.md) | 0..1 <br/> [TextValue](TextValue.md) | Indicate if the sequence has been called by automatic systems (none) or under... | direct |
| [sequencing_field](sequencing_field.md) | 0..1 <br/> [String](String.md) |  | direct |
| [sewage_type](sewage_type.md) | 0..1 <br/> [TextValue](TextValue.md) | Type of wastewater treatment plant as municipial or industrial | direct |
| [shad_dev_water_mold](shad_dev_water_mold.md) | 0..1 <br/> [String](String.md) | Signs of the presence of mold or mildew on the shading device | direct |
| [shading_device_cond](shading_device_cond.md) | 0..1 <br/> [ShadingDeviceCondEnum](ShadingDeviceCondEnum.md) | The physical condition of the shading device at the time of sampling | direct |
| [shading_device_loc](shading_device_loc.md) | 0..1 <br/> [TextValue](TextValue.md) | The location of the shading device in relation to the built structure | direct |
| [shading_device_mat](shading_device_mat.md) | 0..1 <br/> [TextValue](TextValue.md) | The material the shading device is composed of | direct |
| [shading_device_type](shading_device_type.md) | 0..1 <br/> [ShadingDeviceTypeEnum](ShadingDeviceTypeEnum.md) | The type of shading device | direct |
| [sieving](sieving.md) | 0..1 <br/> [TextValue](TextValue.md) | Collection design of pooled samples and/or sieve size and amount of sample si... | direct |
| [silicate](silicate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of silicate | direct |
| [size_frac](size_frac.md) | 0..1 <br/> [TextValue](TextValue.md) | Filtering pore size used in sample preparation | direct |
| [size_frac_low](size_frac_low.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Refers to the mesh/pore size used to pre-filter/pre-sort the sample | direct |
| [size_frac_up](size_frac_up.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Refers to the mesh/pore size used to retain the sample | direct |
| [slope_aspect](slope_aspect.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The direction a slope faces | direct |
| [slope_gradient](slope_gradient.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Commonly called 'slope' | direct |
| [sludge_retent_time](sludge_retent_time.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The time activated sludge remains in reactor | direct |
| [sodium](sodium.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Sodium concentration in the sample | direct |
| [soil_horizon](soil_horizon.md) | 0..1 <br/> [SoilHorizonEnum](SoilHorizonEnum.md) | Specific layer in the land area which measures parallel to the soil surface a... | direct |
| [soil_text_measure](soil_text_measure.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The relative proportion of different grain sizes of mineral particles in a so... | direct |
| [soil_texture_meth](soil_texture_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining soil texture | direct |
| [soil_type](soil_type.md) | 0..1 <br/> [TextValue](TextValue.md) | Description of the soil type or classification | direct |
| [soil_type_meth](soil_type_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining soil series name or other lower-level... | direct |
| [solar_irradiance](solar_irradiance.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The amount of solar energy that arrives at a specific area of a surface durin... | direct |
| [soluble_inorg_mat](soluble_inorg_mat.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of substances such as ammonia, road-salt, sea-salt, cyanide, hy... | direct |
| [soluble_org_mat](soluble_org_mat.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of substances such as urea, fruit sugars, soluble proteins, dru... | direct |
| [soluble_react_phosp](soluble_react_phosp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of soluble reactive phosphorus | direct |
| [source_mat_id](source_mat_id.md) | 0..1 <br/> [TextValue](TextValue.md) | A globally unique identifier assigned to the biological sample | direct |
| [space_typ_state](space_typ_state.md) | 0..1 <br/> [TextValue](TextValue.md) | Customary or normal state of the space | direct |
| [specific](specific.md) | 0..1 <br/> [SpecificEnum](SpecificEnum.md) | The building specifications | direct |
| [specific_ecosystem](specific_ecosystem.md) | 0..1 <br/> [String](String.md) | Specific ecosystems represent specific features of the environment like aphot... | direct |
| [specific_humidity](specific_humidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The mass of water vapour in a unit mass of moist air, usually expressed as gr... | direct |
| [sr_dep_env](sr_dep_env.md) | 0..1 <br/> [SrDepEnvEnum](SrDepEnvEnum.md) | Source rock depositional environment (https://en | direct |
| [sr_geol_age](sr_geol_age.md) | 0..1 <br/> [SrGeolAgeEnum](SrGeolAgeEnum.md) | Geological age of source rock (Additional info: https://en | direct |
| [sr_kerog_type](sr_kerog_type.md) | 0..1 <br/> [SrKerogTypeEnum](SrKerogTypeEnum.md) | Origin of kerogen | direct |
| [sr_lithology](sr_lithology.md) | 0..1 <br/> [SrLithologyEnum](SrLithologyEnum.md) | Lithology of source rock (https://en | direct |
| [standing_water_regm](standing_water_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Treatment involving an exposure to standing water during a plant's life span,... | direct |
| [store_cond](store_cond.md) | 0..1 <br/> [TextValue](TextValue.md) | Explain how and for how long the soil sample was stored before DNA extraction... | direct |
| [substructure_type](substructure_type.md) | 0..* <br/> [SubstructureTypeEnum](SubstructureTypeEnum.md) | The substructure or under building is that largely hidden section of the buil... | direct |
| [sulfate](sulfate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of sulfate in the sample | direct |
| [sulfate_fw](sulfate_fw.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Original sulfate concentration in the hydrocarbon resource | direct |
| [sulfide](sulfide.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of sulfide in the sample | direct |
| [surf_air_cont](surf_air_cont.md) | 0..* <br/> [SurfAirContEnum](SurfAirContEnum.md) | Contaminant identified on surface | direct |
| [surf_humidity](surf_humidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Surfaces: water activity as a function of air and material moisture | direct |
| [surf_material](surf_material.md) | 0..1 <br/> [SurfMaterialEnum](SurfMaterialEnum.md) | Surface materials at the point of sampling | direct |
| [surf_moisture](surf_moisture.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Water held on a surface | direct |
| [surf_moisture_ph](surf_moisture_ph.md) | 0..1 <br/> [Double](Double.md) | ph measurement of surface | direct |
| [surf_temp](surf_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Temperature of the surface at the time of sampling | direct |
| [suspend_part_matter](suspend_part_matter.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of suspended particulate matter | direct |
| [suspend_solids](suspend_solids.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of substances including a wide variety of material, such as sil... | direct |
| [tan](tan.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total Acid Number¬†(TAN) is a measurement of acidity that is determined by th... | direct |
| [target_gene](target_gene.md) | 0..1 <br/> [TextValue](TextValue.md) | Targeted gene or locus name for marker gene studies | direct |
| [target_subfragment](target_subfragment.md) | 0..1 <br/> [TextValue](TextValue.md) | Name of subfragment of a gene or locus | direct |
| [temp](temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Temperature of the sample at the time of sampling | direct |
| [temp_out](temp_out.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The recorded temperature value at sampling time outside | direct |
| [tertiary_treatment](tertiary_treatment.md) | 0..1 <br/> [TextValue](TextValue.md) | The process providing a final treatment stage to raise the effluent quality b... | direct |
| [tidal_stage](tidal_stage.md) | 0..1 <br/> [TidalStageEnum](TidalStageEnum.md) | Stage of tide | direct |
| [tillage](tillage.md) | 0..* <br/> [TillageEnum](TillageEnum.md) | Note method(s) used for tilling | direct |
| [tiss_cult_growth_med](tiss_cult_growth_med.md) | 0..1 <br/> [TextValue](TextValue.md) | Description of plant tissue culture growth media used | direct |
| [toluene](toluene.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of toluene in the sample | direct |
| [tot_carb](tot_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total carbon content | direct |
| [tot_depth_water_col](tot_depth_water_col.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of total depth of water column | direct |
| [tot_diss_nitro](tot_diss_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total dissolved nitrogen concentration, reported as nitrogen, measured by: to... | direct |
| [tot_inorg_nitro](tot_inorg_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total inorganic nitrogen content | direct |
| [tot_iron](tot_iron.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of total iron in the sample | direct |
| [tot_nitro](tot_nitro.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total nitrogen concentration of water samples, calculated by: total nitrogen ... | direct |
| [tot_nitro_cont_meth](tot_nitro_cont_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining the total nitrogen | direct |
| [tot_nitro_content](tot_nitro_content.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total nitrogen content of the sample | direct |
| [tot_org_c_meth](tot_org_c_meth.md) | 0..1 <br/> [TextValue](TextValue.md) | Reference or method used in determining total organic carbon | direct |
| [tot_org_carb](tot_org_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Definition for soil: total organic carbon content of the soil, definition oth... | direct |
| [tot_part_carb](tot_part_carb.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total particulate carbon content | direct |
| [tot_phosp](tot_phosp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total phosphorus concentration in the sample, calculated by: total phosphorus... | direct |
| [tot_phosphate](tot_phosphate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Total amount or concentration of phosphate | direct |
| [tot_sulfur](tot_sulfur.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of total sulfur in the sample | direct |
| [train_line](train_line.md) | 0..1 <br/> [TrainLineEnum](TrainLineEnum.md) | The subway line name | direct |
| [train_stat_loc](train_stat_loc.md) | 0..1 <br/> [TrainStatLocEnum](TrainStatLocEnum.md) | The train station collection location | direct |
| [train_stop_loc](train_stop_loc.md) | 0..1 <br/> [TrainStopLocEnum](TrainStopLocEnum.md) | The train stop collection location | direct |
| [turbidity](turbidity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measure of the amount of cloudiness or haziness in water caused by individual... | direct |
| [tvdss_of_hcr_press](tvdss_of_hcr_press.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | True vertical depth subsea (TVDSS) of the hydrocarbon resource where the orig... | direct |
| [tvdss_of_hcr_temp](tvdss_of_hcr_temp.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | True vertical depth subsea (TVDSS) of the hydrocarbon resource where the orig... | direct |
| [typ_occup_density](typ_occup_density.md) | 0..1 <br/> [Double](Double.md) | Customary or normal density of occupants | direct |
| [ventilation_rate](ventilation_rate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Ventilation rate of the system in the sampled premises | direct |
| [ventilation_type](ventilation_type.md) | 0..1 <br/> [TextValue](TextValue.md) | Ventilation system used in the sampled premises | direct |
| [vfa](vfa.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of Volatile Fatty Acids in the sample | direct |
| [vfa_fw](vfa_fw.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Original volatile fatty acid concentration in the hydrocarbon resource | direct |
| [vis_media](vis_media.md) | 0..1 <br/> [VisMediaEnum](VisMediaEnum.md) | The building visual media | direct |
| [viscosity](viscosity.md) | 0..1 <br/> [TextValue](TextValue.md) | A measure of oil's resistance¬†to gradual deformation by¬†shear stress¬†or¬†t... | direct |
| [volatile_org_comp](volatile_org_comp.md) | 0..* <br/> [TextValue](TextValue.md) | Concentration of carbon-based chemicals that easily evaporate at room tempera... | direct |
| [wall_area](wall_area.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The total area of the sampled room's walls | direct |
| [wall_const_type](wall_const_type.md) | 0..1 <br/> [WallConstTypeEnum](WallConstTypeEnum.md) | The building class of the wall defined by the composition of the building ele... | direct |
| [wall_finish_mat](wall_finish_mat.md) | 0..1 <br/> [WallFinishMatEnum](WallFinishMatEnum.md) | The material utilized to finish the outer most layer of the wall | direct |
| [wall_height](wall_height.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The average height of the walls in the sampled room | direct |
| [wall_loc](wall_loc.md) | 0..1 <br/> [WallLocEnum](WallLocEnum.md) | The relative location of the wall within the room | direct |
| [wall_surf_treatment](wall_surf_treatment.md) | 0..1 <br/> [WallSurfTreatmentEnum](WallSurfTreatmentEnum.md) | The surface treatment of interior wall | direct |
| [wall_texture](wall_texture.md) | 0..1 <br/> [WallTextureEnum](WallTextureEnum.md) | The feel, appearance, or consistency of a wall surface | direct |
| [wall_thermal_mass](wall_thermal_mass.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The ability of the wall to provide inertia against temperature fluctuations | direct |
| [wall_water_mold](wall_water_mold.md) | 0..1 <br/> [TextValue](TextValue.md) | Signs of the presence of mold or mildew on a wall | direct |
| [wastewater_type](wastewater_type.md) | 0..1 <br/> [TextValue](TextValue.md) | The origin of wastewater such as human waste, rainfall, storm drains, etc | direct |
| [water_cont_soil_meth](water_cont_soil_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining the water content of soil | direct |
| [water_content](water_content.md) | 0..* <br/> [String](String.md) | Water content measurement | direct |
| [water_current](water_current.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Measurement of magnitude and direction of flow within a fluid | direct |
| [water_cut](water_cut.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Current amount of water (%) in a produced fluid stream; or the average of the... | direct |
| [water_feat_size](water_feat_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The size of the water feature | direct |
| [water_feat_type](water_feat_type.md) | 0..1 <br/> [WaterFeatTypeEnum](WaterFeatTypeEnum.md) | The type of water feature present within the building being sampled | direct |
| [water_prod_rate](water_prod_rate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Water production rates per well (e | direct |
| [water_temp_regm](water_temp_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to water with varying degre... | direct |
| [watering_regm](watering_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to watering frequencies, tr... | direct |
| [weekday](weekday.md) | 0..1 <br/> [WeekdayEnum](WeekdayEnum.md) | The day of the week when sampling occurred | direct |
| [win](win.md) | 0..1 <br/> [TextValue](TextValue.md) | A unique identifier of a well or wellbore | direct |
| [wind_direction](wind_direction.md) | 0..1 <br/> [TextValue](TextValue.md) | Wind direction is the direction from which a wind originates | direct |
| [wind_speed](wind_speed.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Speed of wind measured at the time of sampling | direct |
| [window_cond](window_cond.md) | 0..1 <br/> [WindowCondEnum](WindowCondEnum.md) | The physical condition of the window at the time of sampling | direct |
| [window_cover](window_cover.md) | 0..1 <br/> [WindowCoverEnum](WindowCoverEnum.md) | The type of window covering | direct |
| [window_horiz_pos](window_horiz_pos.md) | 0..1 <br/> [WindowHorizPosEnum](WindowHorizPosEnum.md) | The horizontal position of the window on the wall | direct |
| [window_loc](window_loc.md) | 0..1 <br/> [WindowLocEnum](WindowLocEnum.md) | The relative location of the window within the room | direct |
| [window_mat](window_mat.md) | 0..1 <br/> [WindowMatEnum](WindowMatEnum.md) | The type of material used to finish a window | direct |
| [window_open_freq](window_open_freq.md) | 0..1 <br/> [TextValue](TextValue.md) | The number of times windows are opened per week | direct |
| [window_size](window_size.md) | 0..1 <br/> [TextValue](TextValue.md) | The window's length and width | direct |
| [window_status](window_status.md) | 0..1 <br/> [TextValue](TextValue.md) | Defines whether the windows were open or closed during environmental testing | direct |
| [window_type](window_type.md) | 0..1 <br/> [WindowTypeEnum](WindowTypeEnum.md) | The type of windows | direct |
| [window_vert_pos](window_vert_pos.md) | 0..1 <br/> [WindowVertPosEnum](WindowVertPosEnum.md) | The vertical position of the window on the wall | direct |
| [window_water_mold](window_water_mold.md) | 0..1 <br/> [TextValue](TextValue.md) | Signs of the presence of mold or mildew on the window | direct |
| [xylene](xylene.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of xylene in the sample | direct |
| [zinc](zinc.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of zinc in the sample | direct |
| [ecosystem](ecosystem.md) | 0..1 <br/> [String](String.md) | An ecosystem is a combination of a physical environment (abiotic factors) and... | direct |
| [ecosystem_category](ecosystem_category.md) | 0..1 <br/> [String](String.md) | Ecosystem categories represent divisions within the ecosystem based on specif... | direct |
| [ecosystem_type](ecosystem_type.md) | 0..1 <br/> [String](String.md) | Ecosystem types represent things having common characteristics within the Eco... | direct |
| [ecosystem_subtype](ecosystem_subtype.md) | 0..1 <br/> [String](String.md) | Ecosystem subtypes represent further subdivision of Ecosystem types into more... | direct |
| [specific_ecosystem](specific_ecosystem.md) | 0..1 <br/> [String](String.md) | Specific ecosystems represent specific features of the environment like aphot... | direct |
| [add_date](add_date.md) | 0..1 <br/> [String](String.md) | The date on which the information was added to the database | direct |
| [community](community.md) | 0..1 <br/> [String](String.md) |  | direct |
| [habitat](habitat.md) | 0..1 <br/> [String](String.md) |  | direct |
| [host_name](host_name.md) | 0..1 <br/> [String](String.md) |  | direct |
| [location](location.md) | 0..1 <br/> [String](String.md) |  | direct |
| [mod_date](mod_date.md) | 0..1 <br/> [String](String.md) | The last date on which the database information was modified | direct |
| [ncbi_taxonomy_name](ncbi_taxonomy_name.md) | 0..1 <br/> [String](String.md) |  | direct |
| [proport_woa_temperature](proport_woa_temperature.md) | 0..1 <br/> [String](String.md) |  | direct |
| [salinity_category](salinity_category.md) | 0..1 <br/> [String](String.md) | Categorical description of the sample's salinity | direct |
| [sample_collection_site](sample_collection_site.md) | 0..1 <br/> [String](String.md) |  | direct |
| [soluble_iron_micromol](soluble_iron_micromol.md) | 0..1 <br/> [String](String.md) |  | direct |
| [subsurface_depth](subsurface_depth.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) |  | direct |
| [air_temp_regm](air_temp_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to varying temperatures; sh... | direct |
| [biotic_regm](biotic_regm.md) | 0..1 <br/> [TextValue](TextValue.md) | Information about treatment(s) involving use of biotic factors, such as bacte... | direct |
| [biotic_relationship](biotic_relationship.md) | 0..1 <br/> [BioticRelationshipEnum](BioticRelationshipEnum.md) | Description of relationship(s) between the subject organism and other organis... | direct |
| [climate_environment](climate_environment.md) | 0..* <br/> [TextValue](TextValue.md) | Treatment involving an exposure to a particular climate; treatment regimen in... | direct |
| [experimental_factor](experimental_factor.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Experimental factors are essentially the variable aspects of an experiment de... | direct |
| [gaseous_environment](gaseous_environment.md) | 0..* <br/> [TextValue](TextValue.md) | Use of conditions with differing gaseous environments; should include the nam... | direct |
| [growth_facil](growth_facil.md) | 0..1 <br/> [ControlledTermValue](ControlledTermValue.md) | Type of facility where the sampled plant was grown; controlled vocabulary: gr... | direct |
| [humidity_regm](humidity_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to varying degree of humidi... | direct |
| [light_regm](light_regm.md) | 0..1 <br/> [TextValue](TextValue.md) | Information about treatment(s) involving exposure to light, including both li... | direct |
| [phosphate](phosphate.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of phosphate | direct |
| [samp_collec_method](samp_collec_method.md) | 0..1 <br/> [String](String.md) | The method employed for collecting the sample | direct |
| [samp_size](samp_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample coll... | direct |
| [source_mat_id](source_mat_id.md) | 0..1 <br/> [TextValue](TextValue.md) | A globally unique identifier assigned to the biological sample | direct |
| [watering_regm](watering_regm.md) | 0..* <br/> [TextValue](TextValue.md) | Information about treatment involving an exposure to watering frequencies, tr... | direct |
| [dna_absorb1](dna_absorb1.md) | 0..1 _recommended_ <br/> [Float](Float.md) | 260/280 measurement of DNA sample purity | direct |
| [dna_absorb2](dna_absorb2.md) | 0..1 _recommended_ <br/> [Float](Float.md) | 260/230 measurement of DNA sample purity | direct |
| [dna_collect_site](dna_collect_site.md) | 0..1 _recommended_ <br/> [String](String.md) | Provide information on the site your DNA sample was collected from | direct |
| [dna_concentration](dna_concentration.md) | 0..1 _recommended_ <br/> [Float](Float.md) |  | direct |
| [dna_cont_type](dna_cont_type.md) | 0..1 _recommended_ <br/> [JgiContTypeEnum](JgiContTypeEnum.md) | Tube or plate (96-well) | direct |
| [dna_cont_well](dna_cont_well.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_container_id](dna_container_id.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_dnase](dna_dnase.md) | 0..1 _recommended_ <br/> [YesNoEnum](YesNoEnum.md) |  | direct |
| [dna_isolate_meth](dna_isolate_meth.md) | 0..1 _recommended_ <br/> [String](String.md) | Describe the method/protocol/kit used to extract DNA/RNA | direct |
| [dna_organisms](dna_organisms.md) | 0..1 _recommended_ <br/> [String](String.md) | List any organisms known or suspected to grow in co-culture, as well as estim... | direct |
| [dna_project_contact](dna_project_contact.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_samp_id](dna_samp_id.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_sample_format](dna_sample_format.md) | 0..1 _recommended_ <br/> [DnaSampleFormatEnum](DnaSampleFormatEnum.md) | Solution in which the DNA sample has been suspended | direct |
| [dna_sample_name](dna_sample_name.md) | 0..1 _recommended_ <br/> [String](String.md) | Give the DNA sample a name that is meaningful to you | direct |
| [dna_seq_project](dna_seq_project.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_seq_project_pi](dna_seq_project_pi.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_seq_project_name](dna_seq_project_name.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dna_volume](dna_volume.md) | 0..1 _recommended_ <br/> [Float](Float.md) |  | direct |
| [proposal_dna](proposal_dna.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [dnase_rna](dnase_rna.md) | 0..1 _recommended_ <br/> [YesNoEnum](YesNoEnum.md) |  | direct |
| [proposal_rna](proposal_rna.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_absorb1](rna_absorb1.md) | 0..1 _recommended_ <br/> [Float](Float.md) | 260/280 measurement of RNA sample purity | direct |
| [rna_absorb2](rna_absorb2.md) | 0..1 _recommended_ <br/> [Float](Float.md) | 260/230 measurement of RNA sample purity | direct |
| [rna_collect_site](rna_collect_site.md) | 0..1 _recommended_ <br/> [String](String.md) | Provide information on the site your RNA sample was collected from | direct |
| [rna_concentration](rna_concentration.md) | 0..1 _recommended_ <br/> [Float](Float.md) |  | direct |
| [rna_cont_type](rna_cont_type.md) | 0..1 _recommended_ <br/> [JgiContTypeEnum](JgiContTypeEnum.md) | Tube or plate (96-well) | direct |
| [rna_cont_well](rna_cont_well.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_container_id](rna_container_id.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_isolate_meth](rna_isolate_meth.md) | 0..1 _recommended_ <br/> [String](String.md) | Describe the method/protocol/kit used to extract DNA/RNA | direct |
| [rna_organisms](rna_organisms.md) | 0..1 _recommended_ <br/> [String](String.md) | List any organisms known or suspected to grow in co-culture, as well as estim... | direct |
| [rna_project_contact](rna_project_contact.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_samp_id](rna_samp_id.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_sample_format](rna_sample_format.md) | 0..1 _recommended_ <br/> [RnaSampleFormatEnum](RnaSampleFormatEnum.md) | Solution in which the RNA sample has been suspended | direct |
| [rna_sample_name](rna_sample_name.md) | 0..1 _recommended_ <br/> [String](String.md) | Give the RNA sample a name that is meaningful to you | direct |
| [rna_seq_project](rna_seq_project.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_seq_project_pi](rna_seq_project_pi.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_seq_project_name](rna_seq_project_name.md) | 0..1 _recommended_ <br/> [String](String.md) |  | direct |
| [rna_volume](rna_volume.md) | 0..1 _recommended_ <br/> [Float](Float.md) |  | direct |
| [collection_date_inc](collection_date_inc.md) | 0..1 _recommended_ <br/> [String](String.md) | Date the incubation was harvested/collected/ended | direct |
| [collection_time](collection_time.md) | 0..1 _recommended_ <br/> [String](String.md) | The time of sampling, either as an instance (single point) or interval | direct |
| [collection_time_inc](collection_time_inc.md) | 0..1 _recommended_ <br/> [String](String.md) | Time the incubation was harvested/collected/ended | direct |
| [experimental_factor_other](experimental_factor_other.md) | 0..1 _recommended_ <br/> [String](String.md) | Other details about your sample that you feel can't be accurately represented... | direct |
| [filter_method](filter_method.md) | 0..1 _recommended_ <br/> [String](String.md) | Type of filter used or how the sample was filtered | direct |
| [isotope_exposure](isotope_exposure.md) | 0..1 _recommended_ <br/> [String](String.md) | List isotope exposure or addition applied to your sample | direct |
| [micro_biomass_c_meth](micro_biomass_c_meth.md) | 0..1 _recommended_ <br/> [String](String.md) | Reference or method used in determining microbial biomass carbon | direct |
| [micro_biomass_n_meth](micro_biomass_n_meth.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining microbial biomass nitrogen | direct |
| [microbial_biomass_c](microbial_biomass_c.md) | 0..1 <br/> [String](String.md) | The part of the organic matter in the soil that constitutes living microorgan... | direct |
| [microbial_biomass_n](microbial_biomass_n.md) | 0..1 <br/> [String](String.md) | The part of the organic matter in the soil that constitutes living microorgan... | direct |
| [non_microb_biomass](non_microb_biomass.md) | 0..1 <br/> [String](String.md) | Amount of biomass; should include the name for the part of biomass measured, ... | direct |
| [non_microb_biomass_method](non_microb_biomass_method.md) | 0..1 <br/> [String](String.md) | Reference or method used in determining biomass | direct |
| [org_nitro_method](org_nitro_method.md) | 0..1 <br/> [String](String.md) | Method used for obtaining organic nitrogen | direct |
| [other_treatment](other_treatment.md) | 0..1 _recommended_ <br/> [String](String.md) | Other treatments applied to your samples that are not applicable to the provi... | direct |
| [start_date_inc](start_date_inc.md) | 0..1 _recommended_ <br/> [String](String.md) | Date the incubation was started | direct |
| [start_time_inc](start_time_inc.md) | 0..1 _recommended_ <br/> [String](String.md) | Time the incubation was started | direct |
| [project_id](project_id.md) | 0..1 _recommended_ <br/> [String](String.md) | Proposal IDs or names associated with dataset | direct |
| [replicate_number](replicate_number.md) | 0..1 _recommended_ <br/> [String](String.md) | If sending biological replicates, indicate the rep number here | direct |
| [sample_shipped](sample_shipped.md) | 0..1 _recommended_ <br/> [String](String.md) | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample sent... | direct |
| [sample_type](sample_type.md) | 0..1 _recommended_ <br/> [SampleTypeEnum](SampleTypeEnum.md) | Type of sample being submitted | direct |
| [technical_reps](technical_reps.md) | 0..1 _recommended_ <br/> [String](String.md) | If sending technical replicates of the same sample, indicate the replicate co... | direct |
| [analysis_type](analysis_type.md) | 0..* _recommended_ <br/> [AnalysisTypeEnum](AnalysisTypeEnum.md) | Select all the data types associated or available for this biosample | direct |
| [sample_link](sample_link.md) | 0..* _recommended_ <br/> [String](String.md) | A unique identifier to assign parent-child, subsample, or sibling samples | direct |
| [bulk_elect_conductivity](bulk_elect_conductivity.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Electrical conductivity is a measure of the ability to carry electric current... | direct |
| [zinc](zinc.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of zinc in the sample | direct |
| [manganese](manganese.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of manganese in the sample | direct |
| [ammonium_nitrogen](ammonium_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of ammonium nitrogen in the sample | direct |
| [nitrate_nitrogen](nitrate_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrate nitrogen in the sample | direct |
| [nitrite_nitrogen](nitrite_nitrogen.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Concentration of nitrite nitrogen in the sample | direct |
| [lbc_thirty](lbc_thirty.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | lime buffer capacity, determined after 30 minute incubation | direct |
| [lbceq](lbceq.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | lime buffer capacity, determined at equilibrium after 5 day incubation | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | A human readable label for an entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | a human-readable description of a thing | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Database](Database.md) | [biosample_set](biosample_set.md) | range | [Biosample](Biosample.md) |
| [Pooling](Pooling.md) | [has_input](has_input.md) | range | [Biosample](Biosample.md) |
| [LibraryPreparation](LibraryPreparation.md) | [has_input](has_input.md) | range | [Biosample](Biosample.md) |
| [CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) | [has_output](has_output.md) | range | [Biosample](Biosample.md) |
| [Biosample](Biosample.md) | [collected_from](collected_from.md) | domain | [Biosample](Biosample.md) |
| [BiosampleProcessing](BiosampleProcessing.md) | [has_input](has_input.md) | range | [Biosample](Biosample.md) |




## Aliases


* sample
* material sample
* specimen
* biospecimen



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nmdc:Biosample |
| native | nmdc:Biosample |
| exact | OBI:0000747, NCIT:C43412, http://purl.obolibrary.org/obo/FBcv_0003024 |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Biosample
description: Biological source material which can be characterized by an experiment.
alt_descriptions:
  embl.ena:
    source: embl.ena
    description: A sample contains information about the sequenced source material.
      Samples are associated with checklists, which define the fields used to annotate
      the samples. Samples are always associated with a taxon.
notes:
- could add GOLD and EBI's biosample definitions to the alt_descriptions?
in_subset:
- sample subset
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample
- material sample
- specimen
- biospecimen
exact_mappings:
- OBI:0000747
- NCIT:C43412
- http://purl.obolibrary.org/obo/FBcv_0003024
is_a: MaterialEntity
slots:
- host_disease_stat
- neon_biosample_identifiers
- host_taxid
- embargoed
- collected_from
- type
- img_identifiers
- samp_name
- biosample_categories
- type
- part_of
- id
- alternative_identifiers
- gold_biosample_identifiers
- insdc_biosample_identifiers
- emsl_biosample_identifiers
- igsn_biosample_identifiers
- abs_air_humidity
- add_recov_method
- additional_info
- address
- adj_room
- aero_struc
- agrochem_addition
- air_PM_concen
- air_temp
- air_temp_regm
- al_sat
- al_sat_meth
- alkalinity
- alkalinity_method
- alkyl_diethers
- alt
- aminopept_act
- ammonium
- ammonium_nitrogen
- amount_light
- ances_data
- annual_precpt
- annual_temp
- antibiotic_regm
- api
- arch_struc
- aromatics_pc
- asphaltenes_pc
- atmospheric_data
- avg_dew_point
- avg_occup
- avg_temp
- bac_prod
- bac_resp
- bacteria_carb_prod
- barometric_press
- basin
- bathroom_count
- bedroom_count
- benzene
- biochem_oxygen_dem
- biocide
- biocide_admin_method
- biol_stat
- biomass
- biotic_regm
- biotic_relationship
- bishomohopanol
- blood_press_diast
- blood_press_syst
- bromide
- build_docs
- build_occup_type
- building_setting
- built_struc_age
- built_struc_set
- built_struc_type
- calcium
- carb_dioxide
- carb_monoxide
- carb_nitro_ratio
- ceil_area
- ceil_cond
- ceil_finish_mat
- ceil_struc
- ceil_texture
- ceil_thermal_mass
- ceil_type
- ceil_water_mold
- chem_administration
- chem_mutagen
- chem_oxygen_dem
- chem_treat_method
- chem_treatment
- chimera_check
- chloride
- chlorophyll
- climate_environment
- collection_date
- conduc
- cool_syst_id
- core field
- crop_rotation
- cult_root_med
- cur_land_use
- cur_vegetation
- cur_vegetation_meth
- date_last_rain
- density
- depos_env
- depth
- dew_point
- diether_lipids
- diss_carb_dioxide
- diss_hydrogen
- diss_inorg_carb
- diss_inorg_nitro
- diss_inorg_phosp
- diss_iron
- diss_org_carb
- diss_org_nitro
- diss_oxygen
- diss_oxygen_fluid
- dna_cont_well
- door_comp_type
- door_cond
- door_direct
- door_loc
- door_mat
- door_move
- door_size
- door_type
- door_type_metal
- door_type_wood
- door_water_mold
- down_par
- drainage_class
- drawings
- ecosystem
- ecosystem_category
- ecosystem_subtype
- ecosystem_type
- efficiency_percent
- elev
- elevator
- emulsions
- env_broad_scale
- env_local_scale
- env_medium
- env_package
- environment field
- escalator
- ethylbenzene
- exp_duct
- exp_pipe
- experimental_factor
- ext_door
- ext_wall_orient
- ext_window_orient
- extreme_event
- fao_class
- fertilizer_regm
- field
- filter_type
- fire
- fireplace_type
- flooding
- floor_age
- floor_area
- floor_cond
- floor_count
- floor_finish_mat
- floor_struc
- floor_thermal_mass
- floor_water_mold
- fluor
- freq_clean
- freq_cook
- fungicide_regm
- furniture
- gaseous_environment
- gaseous_substances
- gender_restroom
- genetic_mod
- geo_loc_name
- glucosidase_act
- gravidity
- gravity
- growth_facil
- growth_habit
- growth_hormone_regm
- hall_count
- handidness
- has numeric value
- has raw value
- has unit
- hc_produced
- hcr
- hcr_fw_salinity
- hcr_geol_age
- hcr_pressure
- hcr_temp
- heat_cool_type
- heat_deliv_loc
- heat_sys_deliv_meth
- heat_system_id
- heavy_metals
- heavy_metals_meth
- height_carper_fiber
- herbicide_regm
- horizon_meth
- host_age
- host_body_habitat
- host_body_product
- host_body_site
- host_body_temp
- host_color
- host_common_name
- host_diet
- host_dry_mass
- host_family_relation
- host_genotype
- host_growth_cond
- host_height
- host_last_meal
- host_length
- host_life_stage
- host_phenotype
- host_sex
- host_shape
- host_subject_id
- host_subspecf_genlin
- host_substrate
- host_symbiont
- host_taxid
- host_tot_mass
- host_wet_mass
- humidity
- humidity_regm
- indoor_space
- indoor_surf
- indust_eff_percent
- inorg_particles
- inside_lux
- int_wall_cond
- investigation field
- iw_bt_date_well
- iwf
- last_clean
- lat_lon
- lbc_thirty
- lbceq
- light_intensity
- light_regm
- light_type
- link_addit_analys
- link_class_info
- link_climate_info
- lithology
- local_class
- local_class_meth
- magnesium
- manganese
- max_occup
- mean_frict_vel
- mean_peak_frict_vel
- mech_struc
- mechanical_damage
- methane
- micro_biomass_meth
- microbial_biomass
- mineral_nutr_regm
- misc_param
- n_alkanes
- nitrate
- nitrate_nitrogen
- nitrite
- nitrite_nitrogen
- nitro
- non_min_nutr_regm
- nucl_acid_amp
- nucl_acid_ext
- nucleic acid sequence source field
- number_pets
- number_plants
- number_resident
- occup_density_samp
- occup_document
- occup_samp
- org_carb
- org_count_qpcr_info
- org_matter
- org_nitro
- org_particles
- organism_count
- owc_tvdss
- oxy_stat_samp
- oxygen
- part_org_carb
- part_org_nitro
- particle_class
- pcr_cond
- pcr_primers
- permeability
- perturbation
- pesticide_regm
- petroleum_hydrocarb
- ph
- ph_meth
- ph_regm
- phaeopigments
- phosphate
- phosplipid_fatt_acid
- photon_flux
- plant_growth_med
- plant_product
- plant_sex
- plant_struc
- pollutants
- pool_dna_extracts
- porosity
- potassium
- pour_point
- pre_treatment
- pres_animal_insect
- pressure
- prev_land_use_meth
- previous_land_use
- primary_prod
- primary_treatment
- prod_rate
- prod_start_date
- profile_position
- quad_pos
- radiation_regm
- rainfall_regm
- reactor_type
- redox_potential
- rel_air_humidity
- rel_humidity_out
- rel_samp_loc
- reservoir
- resins_pc
- room_air_exch_rate
- room_architec_elem
- room_condt
- room_connected
- room_count
- room_dim
- room_door_dist
- room_door_share
- room_hallway
- room_loc
- room_moist_dam_hist
- room_net_area
- room_occup
- room_samp_pos
- room_type
- room_vol
- room_wall_share
- room_window_count
- root_cond
- root_med_carbon
- root_med_macronutr
- root_med_micronutr
- root_med_ph
- root_med_regl
- root_med_solid
- root_med_suppl
- salinity
- salinity_meth
- salt_regm
- samp_capt_status
- samp_collec_device
- samp_collec_method
- samp_collect_point
- samp_dis_stage
- samp_floor
- samp_loc_corr_rate
- samp_mat_process
- samp_md
- samp_name
- samp_preserv
- samp_room_id
- samp_size
- samp_sort_meth
- samp_store_dur
- samp_store_loc
- samp_store_temp
- samp_subtype
- samp_taxon_id
- samp_time_out
- samp_transport_cond
- samp_tvdss
- samp_type
- samp_vol_we_dna_ext
- samp_weather
- samp_well_name
- saturates_pc
- season
- season_environment
- season_precpt
- season_temp
- season_use
- secondary_treatment
- sediment_type
- seq_meth
- seq_quality_check
- sequencing field
- sewage_type
- shad_dev_water_mold
- shading_device_cond
- shading_device_loc
- shading_device_mat
- shading_device_type
- sieving
- silicate
- size_frac
- size_frac_low
- size_frac_up
- slope_aspect
- slope_gradient
- sludge_retent_time
- sodium
- soil_horizon
- soil_text_measure
- soil_texture_meth
- soil_type
- soil_type_meth
- solar_irradiance
- soluble_inorg_mat
- soluble_org_mat
- soluble_react_phosp
- source_mat_id
- space_typ_state
- specific
- specific_ecosystem
- specific_humidity
- sr_dep_env
- sr_geol_age
- sr_kerog_type
- sr_lithology
- standing_water_regm
- store_cond
- substructure_type
- sulfate
- sulfate_fw
- sulfide
- surf_air_cont
- surf_humidity
- surf_material
- surf_moisture
- surf_moisture_ph
- surf_temp
- suspend_part_matter
- suspend_solids
- tan
- target_gene
- target_subfragment
- temp
- temp_out
- tertiary_treatment
- tidal_stage
- tillage
- tiss_cult_growth_med
- toluene
- tot_carb
- tot_depth_water_col
- tot_diss_nitro
- tot_inorg_nitro
- tot_iron
- tot_nitro
- tot_nitro_cont_meth
- tot_nitro_content
- tot_org_c_meth
- tot_org_carb
- tot_part_carb
- tot_phosp
- tot_phosphate
- tot_sulfur
- train_line
- train_stat_loc
- train_stop_loc
- turbidity
- tvdss_of_hcr_press
- tvdss_of_hcr_temp
- typ_occup_density
- ventilation_rate
- ventilation_type
- vfa
- vfa_fw
- vis_media
- viscosity
- volatile_org_comp
- wall_area
- wall_const_type
- wall_finish_mat
- wall_height
- wall_loc
- wall_surf_treatment
- wall_texture
- wall_thermal_mass
- wall_water_mold
- wastewater_type
- water_cont_soil_meth
- water_content
- water_current
- water_cut
- water_feat_size
- water_feat_type
- water_prod_rate
- water_temp_regm
- watering_regm
- weekday
- win
- wind_direction
- wind_speed
- window_cond
- window_cover
- window_horiz_pos
- window_loc
- window_mat
- window_open_freq
- window_size
- window_status
- window_type
- window_vert_pos
- window_water_mold
- xylene
- zinc
- ecosystem
- ecosystem_category
- ecosystem_type
- ecosystem_subtype
- specific_ecosystem
- add_date
- community
- habitat
- host_name
- location
- mod_date
- ncbi_taxonomy_name
- proport_woa_temperature
- salinity_category
- sample_collection_site
- soluble_iron_micromol
- subsurface_depth
- air_temp_regm
- biotic_regm
- biotic_relationship
- climate_environment
- experimental_factor
- gaseous_environment
- growth_facil
- humidity_regm
- light_regm
- phosphate
- samp_collec_method
- samp_size
- source_mat_id
- watering_regm
- dna_absorb1
- dna_absorb2
- dna_collect_site
- dna_concentration
- dna_cont_type
- dna_cont_well
- dna_container_id
- dna_dnase
- dna_isolate_meth
- dna_organisms
- dna_project_contact
- dna_samp_id
- dna_sample_format
- dna_sample_name
- dna_seq_project
- dna_seq_project_pi
- dna_seq_project_name
- dna_volume
- proposal_dna
- dnase_rna
- proposal_rna
- rna_absorb1
- rna_absorb2
- rna_collect_site
- rna_concentration
- rna_cont_type
- rna_cont_well
- rna_container_id
- rna_isolate_meth
- rna_organisms
- rna_project_contact
- rna_samp_id
- rna_sample_format
- rna_sample_name
- rna_seq_project
- rna_seq_project_pi
- rna_seq_project_name
- rna_volume
- collection_date_inc
- collection_time
- collection_time_inc
- experimental_factor_other
- filter_method
- isotope_exposure
- micro_biomass_c_meth
- micro_biomass_n_meth
- microbial_biomass_c
- microbial_biomass_n
- non_microb_biomass
- non_microb_biomass_method
- org_nitro_method
- other_treatment
- start_date_inc
- start_time_inc
- project_id
- replicate_number
- sample_shipped
- sample_type
- technical_reps
- analysis_type
- sample_link
- bulk_elect_conductivity
- zinc
- manganese
- ammonium_nitrogen
- nitrate_nitrogen
- nitrite_nitrogen
- lbc_thirty
- lbceq
slot_usage:
  elev:
    name: elev
    title: elevation, meters
    comments:
    - All elevations must be reported in meters. Provide the numerical portion only.
    - Please use https://www.advancedconverter.com/map-tools/find-altitude-by-coordinates,
      if needed, to help estimate the elevation based on latitude and longitude coordinates.
    examples:
    - value: '100'
    domain_of:
    - FieldResearchSite
    - Biosample
    range: float
  oxy_stat_samp:
    name: oxy_stat_samp
    domain_of:
    - Biosample
    range: oxy_stat_samp_enum
  id:
    name: id
    description: An NMDC assigned unique identifier for a biosample submitted to NMDC.
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    required: true
    structured_pattern:
      syntax: '{id_nmdc_prefix}:bsm-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true
  gold_biosample_identifiers:
    name: gold_biosample_identifiers
    annotations:
      display_hint:
        tag: display_hint
        value: Provide the GOLD biosample IDs associated with this biosample.
    description: Unique identifier for a biosample submitted to GOLD that matches
      the NMDC submitted biosample
    comments:
    - This is the ID provided by GOLD that starts with 'GB'
    domain_of:
    - Biosample
    range: uriorcurie
  alternative_identifiers:
    name: alternative_identifiers
    description: Unique identifier for a biosample submitted to additional resources.
      Matches the entity that has been submitted to NMDC
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
  lat_lon:
    name: lat_lon
    notes:
    - This is currently a required field but it's not clear if this should be required
      for human hosts
    domain_of:
    - FieldResearchSite
    - Biosample
  env_broad_scale:
    name: env_broad_scale
    domain_of:
    - Biosample
    required: true
  env_local_scale:
    name: env_local_scale
    domain_of:
    - Biosample
    required: true
  env_medium:
    name: env_medium
    domain_of:
    - Biosample
    required: true
  part_of:
    name: part_of
    domain_of:
    - FieldResearchSite
    - Biosample
    - Study
    - OmicsProcessing
    - WorkflowExecutionActivity
    range: Study
    required: true
    pattern: ^nmdc:sty-[0-9][a-z]{0,6}[0-9]-[A-Za-z0-9]{1,}(\.[A-Za-z0-9]{1,})*(_[A-Za-z0-9_\.-]+)?$
  fire:
    name: fire
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    comments:
    - Provide the date the fire occurred. If extended burning occurred provide the
      date range.
    examples:
    - value: '1871-10-10'
    - value: 1871-10-01 to 1871-10-31
    domain_of:
    - Biosample
    range: string
    pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?(\s+to\s+[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?)?$
  flooding:
    name: flooding
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    - What about if the "day" isn't known? Is this ok?
    comments:
    - Provide the date the flood occurred. If extended flooding occurred provide the
      date range.
    examples:
    - value: '1927-04-15'
    - value: 1927-04 to 1927-05
    domain_of:
    - Biosample
    range: string
  extreme_event:
    name: extreme_event
    annotations:
      expected_value:
        tag: expected_value
        value: date, string
    examples:
    - value: 1980-05-18, volcanic eruption
    domain_of:
    - Biosample
    range: string
  slope_aspect:
    name: slope_aspect
    description: The direction a slope faces. While looking down a slope use a compass
      to record the direction you are facing (direction or degrees). This measure
      provides an indication of sun and wind exposure that will influence soil temperature
      and evapotranspiration.
    comments:
    - Aspect is the orientation of slope, measured clockwise in degrees from 0 to
      360, where 0 is north-facing, 90 is east-facing, 180 is south-facing, and 270
      is west-facing.
    examples:
    - value: '35'
    domain_of:
    - Biosample
  slope_gradient:
    name: slope_gradient
    todos:
    - Slope is a percent. How does the validation work? Check to correct examples
    examples:
    - value: 10%
    - value: 10 %
    - value: '0.10'
    domain_of:
    - Biosample
  al_sat:
    name: al_sat
    description: The relative abundance of aluminum in the sample
    title: aluminum saturation/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    notes:
    - Aluminum saturation is the percentage of the CEC occupies by aluminum. Like
      all cations, aluminum held by the cation exchange complex is in equilibrium
      with aluminum in the soil solution.
    examples:
    - value: 27%
    domain_of:
    - Biosample
  al_sat_meth:
    name: al_sat_meth
    description: Reference or method used in determining Aluminum saturation
    title: aluminum saturation method/ extreme unusual properties
    todos:
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
    comments:
    - Required when aluminum saturation is provided.
    examples:
    - value: https://doi.org/10.1371/journal.pone.0176357
    domain_of:
    - Biosample
  annual_precpt:
    name: annual_precpt
    examples:
    - value: 8.94 inch
    domain_of:
    - Biosample
  cur_vegetation:
    name: cur_vegetation
    description: Vegetation classification from one or more standard classification
      systems, or agricultural crop
    todos:
    - Recommend changing this from text value to some king of ontology?
    comments:
    - Values provided here can be specific species of vegetation or vegetation regions
    - See for vegetation regions- https://education.nationalgeographic.org/resource/vegetation-region
    examples:
    - value: deciduous forest
    - value: forest
    - value: Bauhinia variegata
    domain_of:
    - FieldResearchSite
    - Biosample
  cur_vegetation_meth:
    name: cur_vegetation_meth
    todos:
    - I'm not sure this is a DOI, PMID, or URI. Should pool the community and find
      out how they accomplish this if provided.
    comments:
    - Required when current vegetation is provided.
    examples:
    - value: https://doi.org/10.1111/j.1654-109X.2011.01154.x
    domain_of:
    - Biosample
  heavy_metals:
    name: heavy_metals
    description: Heavy metals present in the sample and their concentrations.
    title: heavy metals/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    comments:
    - For multiple heavy metals and concentrations, separate by ;
    examples:
    - value: mercury 0.09 micrograms per gram
    - value: mercury 0.09 ug/g; chromium 0.03 ug/g
    domain_of:
    - Biosample
  heavy_metals_meth:
    name: heavy_metals_meth
    title: heavy metals method/ extreme unusual properties
    comments:
    - Required when heavy metals are provided
    - If different methods are used for multiple metals, indicate the metal and method.
      Separate metals by ;
    examples:
    - value: https://doi.org/10.3390/ijms9040434
    - value: mercury https://doi.org/10.1007/BF01056090; chromium https://doi.org/10.1007/s00216-006-0322-8
    multivalued: true
    domain_of:
    - Biosample
  season_precpt:
    name: season_precpt
    title: average seasonal precipitation
    todos:
    - check validation & examples. always mm? so value only? Or value + unit
    notes:
    - mean and average are the same thing, but it seems like bad practice to not be
      consistent. Changed mean to average
    comments:
    - Seasons are defined as spring (March, April, May), summer (June, July, August),
      autumn (September, October, November) and winter (December, January, February).
    examples:
    - value: 0.4 inch
    - value: 10.16 mm
    domain_of:
    - Biosample
  water_cont_soil_meth:
    name: water_cont_soil_meth
    todos:
    - Why is it soil water content method in the name but not the title? Is this slot
      used in other samples?
    - Soil water content can be measure MANY ways and often, multiple ways are used
      in one experiment (gravimetric water content and water holding capacity and
      water filled pore space, to name a few).
    - Should this be multi valued? How to we manage and validate this?
    comments:
    - Required if providing water content
    examples:
    - value: J. Nat. Prod. Plant Resour., 2012, 2 (4):500-503
    - value: https://dec.alaska.gov/applications/spar/webcalc/definitions.htm
    domain_of:
    - Biosample
  water_content:
    name: water_content
    annotations:
      expected_value:
        tag: expected_value
        value: string
      preferred_unit:
        tag: preferred_unit
        value: gram per gram or cubic centimeter per cubic centimeter
    todos:
    - value in preferred unit is too limiting. need to change this
    - check and correct validation so examples are accepted
    - how to manage multiple water content methods?
    examples:
    - value: 0.75 g water/g dry soil
    - value: 75% water holding capacity
    - value: 1.1 g fresh weight/ dry weight
    - value: 10% water filled pore space
    multivalued: true
    domain_of:
    - Biosample
    range: string
  ph_meth:
    name: ph_meth
    comments:
    - This can include a link to the instrument used or a citation for the method.
    examples:
    - value: https://www.southernlabware.com/pc9500-benchtop-ph-conductivity-meter-kit-ph-accuracy-2000mv-ph-range-2-000-to-20-000.html?gclid=Cj0KCQiAwJWdBhCYARIsAJc4idCO5vtvbVMf545fcvdROFqa6zjzNSoywNx6K4k9Coo9cCc2pybtvGsaAiR0EALw_wcB
    - value: https://doi.org/10.2136/sssabookser5.3.c16
    domain_of:
    - Biosample
  tot_carb:
    name: tot_carb
    todos:
    - is this inorganic and organic? both? could use some clarification.
    - ug/L doesn't seem like the right units. Should check this slots usage in databases
      and re-evaluate. I couldn't find any references that provided this data in this
      format
    examples:
    - value: 1 ug/L
    domain_of:
    - Biosample
  tot_nitro_cont_meth:
    name: tot_nitro_cont_meth
    examples:
    - value: https://doi.org/10.2134/agronmonogr9.2.c32
    - value: https://acsess.onlinelibrary.wiley.com/doi/full/10.2136/sssaj2009.0389?casa_token=bm0pYIUdNMgAAAAA%3AOWVRR0STHaOe-afTcTdxn5m1hM8n2ltM0wY-b1iYpYdD9dhwppk5j3LvC2IO5yhOIvyLVeQz4NZRCZo
    domain_of:
    - Biosample
  tot_nitro_content:
    name: tot_nitro_content
    examples:
    - value: 5 mg N/ L
    domain_of:
    - Biosample
  tot_org_c_meth:
    name: tot_org_c_meth
    examples:
    - value: https://doi.org/10.1080/07352680902776556
    domain_of:
    - Biosample
  tot_org_carb:
    name: tot_org_carb
    todos:
    - check description. How are they different?
    examples:
    - value: 5 mg N/ L
    domain_of:
    - Biosample
  salinity_meth:
    name: salinity_meth
    examples:
    - value: https://doi.org/10.1007/978-1-61779-986-0_28
    domain_of:
    - Biosample
  sieving:
    name: sieving
    todos:
    - check validation and examples
    comments:
    - Describe how samples were composited or sieved.
    - Use 'sample link' to indicate which samples were combined.
    examples:
    - value: combined 2 cores | 4mm sieved
    - value: 4 mm sieved and homogenized
    - value: 50 g | 5 cores | 2 mm sieved
    domain_of:
    - Biosample
  climate_environment:
    name: climate_environment
    todos:
    - description says "can include multiple climates" but multivalued is set to false
    - add examples, i need to see some examples to add correctly formatted example.
    domain_of:
    - Biosample
  gaseous_environment:
    name: gaseous_environment
    todos:
    - would like to see usage examples for this slot. Requiring micromole/L seems
      too limiting and doesn't match expected_value value
    - did I do this right? keep the example that's provided and add another? so as
      to not override
    examples:
    - value: CO2; 500ppm above ambient; constant
    - value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    domain_of:
    - Biosample
  watering_regm:
    name: watering_regm
    examples:
    - value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    - value: 75% water holding capacity; constant
    domain_of:
    - Biosample
  source_mat_id:
    name: source_mat_id
    description: A globally unique identifier assigned to the biological sample.
    title: source material identifier
    todos:
    - Currently, the comments say to use UUIDs. However, if we implement assigning
      NMDC identifiers with the minter we dont need to require a GUID. It can be an
      optional field to fill out only if they already have a resolvable ID.
    comments:
    - Identifiers must be prefixed. Possible FAIR prefixes are IGSNs (http://www.geosamples.org/getigsn),
      NCBI biosample accession numbers, ARK identifiers (https://arks.org/). These
      IDs enable linking to derived analytes and subsamples. If you have not assigned
      FAIR identifiers to your samples, you can generate UUIDs (https://www.uuidgenerator.net/).
    examples:
    - value: IGSN:AU1243
    - value: UUID:24f1467a-40f4-11ed-b878-0242ac120002
    domain_of:
    - Biosample
unique_keys:
  samp_name_unique_key:
    unique_key_name: samp_name_unique_key
    unique_key_slots:
    - samp_name
rules:
- preconditions:
    slot_conditions:
      dna_cont_well:
        name: dna_cont_well
        pattern: .+
  postconditions:
    slot_conditions:
      dna_cont_type:
        name: dna_cont_type
        equals_string: plate
  description: DNA samples shipped to JGI for metagenomic analysis in tubes can't
    have any value for their plate position.
  title: dna_well_requires_plate
- preconditions:
    slot_conditions:
      dna_cont_type:
        name: dna_cont_type
        equals_string: plate
  postconditions:
    slot_conditions:
      dna_cont_well:
        name: dna_cont_well
        pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  description: DNA samples in plates must have a plate position that matches the regex.
    Note the requirement for an empty string in the tube case. Waiting for value_present
    validation to be added to runtime
  title: dna_plate_requires_well
- preconditions:
    slot_conditions:
      rna_cont_well:
        name: rna_cont_well
        pattern: .+
  postconditions:
    slot_conditions:
      rna_cont_type:
        name: rna_cont_type
        equals_string: plate
  description: RNA samples shipped to JGI for metagenomic analysis in tubes can't
    have any value for their plate position.
  title: rna_well_requires_plate
- preconditions:
    slot_conditions:
      rna_cont_type:
        name: rna_cont_type
        equals_string: plate
  postconditions:
    slot_conditions:
      rna_cont_well:
        name: rna_cont_well
        pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  description: RNA samples in plates must have a plate position that matches the regex.
    Note the requirement for an empty string in the tube case. Waiting for value_present
    validation to be added to runtime
  title: rna_plate_requires_well

```
</details>

### Induced

<details>
```yaml
name: Biosample
description: Biological source material which can be characterized by an experiment.
alt_descriptions:
  embl.ena:
    source: embl.ena
    description: A sample contains information about the sequenced source material.
      Samples are associated with checklists, which define the fields used to annotate
      the samples. Samples are always associated with a taxon.
notes:
- could add GOLD and EBI's biosample definitions to the alt_descriptions?
in_subset:
- sample subset
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample
- material sample
- specimen
- biospecimen
exact_mappings:
- OBI:0000747
- NCIT:C43412
- http://purl.obolibrary.org/obo/FBcv_0003024
is_a: MaterialEntity
slot_usage:
  elev:
    name: elev
    title: elevation, meters
    comments:
    - All elevations must be reported in meters. Provide the numerical portion only.
    - Please use https://www.advancedconverter.com/map-tools/find-altitude-by-coordinates,
      if needed, to help estimate the elevation based on latitude and longitude coordinates.
    examples:
    - value: '100'
    domain_of:
    - FieldResearchSite
    - Biosample
    range: float
  oxy_stat_samp:
    name: oxy_stat_samp
    domain_of:
    - Biosample
    range: oxy_stat_samp_enum
  id:
    name: id
    description: An NMDC assigned unique identifier for a biosample submitted to NMDC.
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    required: true
    structured_pattern:
      syntax: '{id_nmdc_prefix}:bsm-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true
  gold_biosample_identifiers:
    name: gold_biosample_identifiers
    annotations:
      display_hint:
        tag: display_hint
        value: Provide the GOLD biosample IDs associated with this biosample.
    description: Unique identifier for a biosample submitted to GOLD that matches
      the NMDC submitted biosample
    comments:
    - This is the ID provided by GOLD that starts with 'GB'
    domain_of:
    - Biosample
    range: uriorcurie
  alternative_identifiers:
    name: alternative_identifiers
    description: Unique identifier for a biosample submitted to additional resources.
      Matches the entity that has been submitted to NMDC
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
  lat_lon:
    name: lat_lon
    notes:
    - This is currently a required field but it's not clear if this should be required
      for human hosts
    domain_of:
    - FieldResearchSite
    - Biosample
  env_broad_scale:
    name: env_broad_scale
    domain_of:
    - Biosample
    required: true
  env_local_scale:
    name: env_local_scale
    domain_of:
    - Biosample
    required: true
  env_medium:
    name: env_medium
    domain_of:
    - Biosample
    required: true
  part_of:
    name: part_of
    domain_of:
    - FieldResearchSite
    - Biosample
    - Study
    - OmicsProcessing
    - WorkflowExecutionActivity
    range: Study
    required: true
    pattern: ^nmdc:sty-[0-9][a-z]{0,6}[0-9]-[A-Za-z0-9]{1,}(\.[A-Za-z0-9]{1,})*(_[A-Za-z0-9_\.-]+)?$
  fire:
    name: fire
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    comments:
    - Provide the date the fire occurred. If extended burning occurred provide the
      date range.
    examples:
    - value: '1871-10-10'
    - value: 1871-10-01 to 1871-10-31
    domain_of:
    - Biosample
    range: string
    pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?(\s+to\s+[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?)?$
  flooding:
    name: flooding
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    - What about if the "day" isn't known? Is this ok?
    comments:
    - Provide the date the flood occurred. If extended flooding occurred provide the
      date range.
    examples:
    - value: '1927-04-15'
    - value: 1927-04 to 1927-05
    domain_of:
    - Biosample
    range: string
  extreme_event:
    name: extreme_event
    annotations:
      expected_value:
        tag: expected_value
        value: date, string
    examples:
    - value: 1980-05-18, volcanic eruption
    domain_of:
    - Biosample
    range: string
  slope_aspect:
    name: slope_aspect
    description: The direction a slope faces. While looking down a slope use a compass
      to record the direction you are facing (direction or degrees). This measure
      provides an indication of sun and wind exposure that will influence soil temperature
      and evapotranspiration.
    comments:
    - Aspect is the orientation of slope, measured clockwise in degrees from 0 to
      360, where 0 is north-facing, 90 is east-facing, 180 is south-facing, and 270
      is west-facing.
    examples:
    - value: '35'
    domain_of:
    - Biosample
  slope_gradient:
    name: slope_gradient
    todos:
    - Slope is a percent. How does the validation work? Check to correct examples
    examples:
    - value: 10%
    - value: 10 %
    - value: '0.10'
    domain_of:
    - Biosample
  al_sat:
    name: al_sat
    description: The relative abundance of aluminum in the sample
    title: aluminum saturation/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    notes:
    - Aluminum saturation is the percentage of the CEC occupies by aluminum. Like
      all cations, aluminum held by the cation exchange complex is in equilibrium
      with aluminum in the soil solution.
    examples:
    - value: 27%
    domain_of:
    - Biosample
  al_sat_meth:
    name: al_sat_meth
    description: Reference or method used in determining Aluminum saturation
    title: aluminum saturation method/ extreme unusual properties
    todos:
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
    comments:
    - Required when aluminum saturation is provided.
    examples:
    - value: https://doi.org/10.1371/journal.pone.0176357
    domain_of:
    - Biosample
  annual_precpt:
    name: annual_precpt
    examples:
    - value: 8.94 inch
    domain_of:
    - Biosample
  cur_vegetation:
    name: cur_vegetation
    description: Vegetation classification from one or more standard classification
      systems, or agricultural crop
    todos:
    - Recommend changing this from text value to some king of ontology?
    comments:
    - Values provided here can be specific species of vegetation or vegetation regions
    - See for vegetation regions- https://education.nationalgeographic.org/resource/vegetation-region
    examples:
    - value: deciduous forest
    - value: forest
    - value: Bauhinia variegata
    domain_of:
    - FieldResearchSite
    - Biosample
  cur_vegetation_meth:
    name: cur_vegetation_meth
    todos:
    - I'm not sure this is a DOI, PMID, or URI. Should pool the community and find
      out how they accomplish this if provided.
    comments:
    - Required when current vegetation is provided.
    examples:
    - value: https://doi.org/10.1111/j.1654-109X.2011.01154.x
    domain_of:
    - Biosample
  heavy_metals:
    name: heavy_metals
    description: Heavy metals present in the sample and their concentrations.
    title: heavy metals/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    comments:
    - For multiple heavy metals and concentrations, separate by ;
    examples:
    - value: mercury 0.09 micrograms per gram
    - value: mercury 0.09 ug/g; chromium 0.03 ug/g
    domain_of:
    - Biosample
  heavy_metals_meth:
    name: heavy_metals_meth
    title: heavy metals method/ extreme unusual properties
    comments:
    - Required when heavy metals are provided
    - If different methods are used for multiple metals, indicate the metal and method.
      Separate metals by ;
    examples:
    - value: https://doi.org/10.3390/ijms9040434
    - value: mercury https://doi.org/10.1007/BF01056090; chromium https://doi.org/10.1007/s00216-006-0322-8
    multivalued: true
    domain_of:
    - Biosample
  season_precpt:
    name: season_precpt
    title: average seasonal precipitation
    todos:
    - check validation & examples. always mm? so value only? Or value + unit
    notes:
    - mean and average are the same thing, but it seems like bad practice to not be
      consistent. Changed mean to average
    comments:
    - Seasons are defined as spring (March, April, May), summer (June, July, August),
      autumn (September, October, November) and winter (December, January, February).
    examples:
    - value: 0.4 inch
    - value: 10.16 mm
    domain_of:
    - Biosample
  water_cont_soil_meth:
    name: water_cont_soil_meth
    todos:
    - Why is it soil water content method in the name but not the title? Is this slot
      used in other samples?
    - Soil water content can be measure MANY ways and often, multiple ways are used
      in one experiment (gravimetric water content and water holding capacity and
      water filled pore space, to name a few).
    - Should this be multi valued? How to we manage and validate this?
    comments:
    - Required if providing water content
    examples:
    - value: J. Nat. Prod. Plant Resour., 2012, 2 (4):500-503
    - value: https://dec.alaska.gov/applications/spar/webcalc/definitions.htm
    domain_of:
    - Biosample
  water_content:
    name: water_content
    annotations:
      expected_value:
        tag: expected_value
        value: string
      preferred_unit:
        tag: preferred_unit
        value: gram per gram or cubic centimeter per cubic centimeter
    todos:
    - value in preferred unit is too limiting. need to change this
    - check and correct validation so examples are accepted
    - how to manage multiple water content methods?
    examples:
    - value: 0.75 g water/g dry soil
    - value: 75% water holding capacity
    - value: 1.1 g fresh weight/ dry weight
    - value: 10% water filled pore space
    multivalued: true
    domain_of:
    - Biosample
    range: string
  ph_meth:
    name: ph_meth
    comments:
    - This can include a link to the instrument used or a citation for the method.
    examples:
    - value: https://www.southernlabware.com/pc9500-benchtop-ph-conductivity-meter-kit-ph-accuracy-2000mv-ph-range-2-000-to-20-000.html?gclid=Cj0KCQiAwJWdBhCYARIsAJc4idCO5vtvbVMf545fcvdROFqa6zjzNSoywNx6K4k9Coo9cCc2pybtvGsaAiR0EALw_wcB
    - value: https://doi.org/10.2136/sssabookser5.3.c16
    domain_of:
    - Biosample
  tot_carb:
    name: tot_carb
    todos:
    - is this inorganic and organic? both? could use some clarification.
    - ug/L doesn't seem like the right units. Should check this slots usage in databases
      and re-evaluate. I couldn't find any references that provided this data in this
      format
    examples:
    - value: 1 ug/L
    domain_of:
    - Biosample
  tot_nitro_cont_meth:
    name: tot_nitro_cont_meth
    examples:
    - value: https://doi.org/10.2134/agronmonogr9.2.c32
    - value: https://acsess.onlinelibrary.wiley.com/doi/full/10.2136/sssaj2009.0389?casa_token=bm0pYIUdNMgAAAAA%3AOWVRR0STHaOe-afTcTdxn5m1hM8n2ltM0wY-b1iYpYdD9dhwppk5j3LvC2IO5yhOIvyLVeQz4NZRCZo
    domain_of:
    - Biosample
  tot_nitro_content:
    name: tot_nitro_content
    examples:
    - value: 5 mg N/ L
    domain_of:
    - Biosample
  tot_org_c_meth:
    name: tot_org_c_meth
    examples:
    - value: https://doi.org/10.1080/07352680902776556
    domain_of:
    - Biosample
  tot_org_carb:
    name: tot_org_carb
    todos:
    - check description. How are they different?
    examples:
    - value: 5 mg N/ L
    domain_of:
    - Biosample
  salinity_meth:
    name: salinity_meth
    examples:
    - value: https://doi.org/10.1007/978-1-61779-986-0_28
    domain_of:
    - Biosample
  sieving:
    name: sieving
    todos:
    - check validation and examples
    comments:
    - Describe how samples were composited or sieved.
    - Use 'sample link' to indicate which samples were combined.
    examples:
    - value: combined 2 cores | 4mm sieved
    - value: 4 mm sieved and homogenized
    - value: 50 g | 5 cores | 2 mm sieved
    domain_of:
    - Biosample
  climate_environment:
    name: climate_environment
    todos:
    - description says "can include multiple climates" but multivalued is set to false
    - add examples, i need to see some examples to add correctly formatted example.
    domain_of:
    - Biosample
  gaseous_environment:
    name: gaseous_environment
    todos:
    - would like to see usage examples for this slot. Requiring micromole/L seems
      too limiting and doesn't match expected_value value
    - did I do this right? keep the example that's provided and add another? so as
      to not override
    examples:
    - value: CO2; 500ppm above ambient; constant
    - value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    domain_of:
    - Biosample
  watering_regm:
    name: watering_regm
    examples:
    - value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    - value: 75% water holding capacity; constant
    domain_of:
    - Biosample
  source_mat_id:
    name: source_mat_id
    description: A globally unique identifier assigned to the biological sample.
    title: source material identifier
    todos:
    - Currently, the comments say to use UUIDs. However, if we implement assigning
      NMDC identifiers with the minter we dont need to require a GUID. It can be an
      optional field to fill out only if they already have a resolvable ID.
    comments:
    - Identifiers must be prefixed. Possible FAIR prefixes are IGSNs (http://www.geosamples.org/getigsn),
      NCBI biosample accession numbers, ARK identifiers (https://arks.org/). These
      IDs enable linking to derived analytes and subsamples. If you have not assigned
      FAIR identifiers to your samples, you can generate UUIDs (https://www.uuidgenerator.net/).
    examples:
    - value: IGSN:AU1243
    - value: UUID:24f1467a-40f4-11ed-b878-0242ac120002
    domain_of:
    - Biosample
attributes:
  host_disease_stat:
    name: host_disease_stat
    annotations:
      expected_value:
        tag: expected_value
        value: disease name or Disease Ontology term
    description: List of diseases with which the host has been diagnosed; can include
      multiple diagnoses. The value of the field depends on host; for humans the terms
      should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org,
      non-human host diseases are free text
    title: host disease status
    examples:
    - value: rabies [DOID:11260]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host disease status
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{termLabel} {[termID]}|{text}'
    slot_uri: MIXS:0000031
    multivalued: false
    alias: host_disease_stat
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  neon_biosample_identifiers:
    name: neon_biosample_identifiers
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: biosample_identifiers
    mixins:
    - neon_identifiers
    multivalued: true
    alias: neon_biosample_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: external_identifier
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
  host_taxid:
    name: host_taxid
    annotations:
      expected_value:
        tag: expected_value
        value: NCBI taxon identifier
      occurrence:
        tag: occurrence
        value: '1'
    description: NCBI taxon id of the host, e.g. 9606
    title: host taxid
    comments:
    - Homo sapiens [NCBITaxon:9606] would be a reasonable has_raw_value
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host taxid
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000250
    multivalued: false
    alias: host_taxid
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledIdentifiedTermValue
  embargoed:
    name: embargoed
    description: If true, the data are embargoed and not available for public access.
    todos:
    - make this required?
    - first apply to Biosample
    - try to apply to all Biosamples in a particular nmdc-server SubmissionMetadata?
    - applying to a Study may not be granular enough
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: embargoed
    owner: Biosample
    domain_of:
    - Biosample
    range: boolean
    recommended: true
  collected_from:
    name: collected_from
    description: The Site from which a Biosample was collected
    todos:
    - add an OBO slot_uri ?
    comments:
    - this illustrates implementing a Biosample relation with a (binary) slot
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: Biosample
    alias: collected_from
    owner: Biosample
    domain_of:
    - Biosample
    range: FieldResearchSite
  type:
    name: type
    description: An optional string that specifies the type object.  This is used
      to allow for searches for different kinds of objects.
    deprecated: Due to confusion about what values are used for this slot, it is best
      not to use this slot. See https://github.com/microbiomedata/nmdc-schema/issues/248.
      MAM removed designates_type and rdf:type slot uri 2022-11-30
    examples:
    - value: nmdc:Biosample
    - value: nmdc:Study
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://github.com/microbiomedata/nmdc-schema/issues/1233
    rank: 1000
    alias: type
    owner: Biosample
    domain_of:
    - DataObject
    - Biosample
    - Study
    - OmicsProcessing
    - CreditAssociation
    - WorkflowExecutionActivity
    - MetagenomeAssembly
    - MetagenomeAnnotationActivity
    - MetatranscriptomeAnnotationActivity
    - MetatranscriptomeActivity
    - MagsAnalysisActivity
    - ReadQcAnalysisActivity
    - ReadBasedTaxonomyAnalysisActivity
    - MagBin
    - GenomeFeature
    range: string
  img_identifiers:
    name: img_identifiers
    description: A list of identifiers that relate the biosample to records in the
      IMG database.
    title: IMG Identifiers
    todos:
    - add is_a or mixin modeling, like other external_database_identifiers
    - what class would IMG records belong to?! Are they Studies, Biosamples, or something
      else?
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: external_database_identifiers
    multivalued: true
    alias: img_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: external_identifier
    pattern: ^img\.taxon:[a-zA-Z0-9_][a-zA-Z0-9_\/\.]*$
  samp_name:
    name: samp_name
    annotations:
      expected_value:
        tag: expected_value
        value: text
    description: A local identifier or name that for the material sample used for
      extracting nucleic acids, and subsequent sequencing. It can refer either to
      the original material collected or to any derived sub-samples. It can have any
      format, but we suggest that you make it concise, unique and consistent within
      your lab, and as informative as possible. INSDC requires every sample name from
      a single Submitter to be unique. Use of a globally unique identifier for the
      field source_mat_id is recommended in addition to sample_name.
    title: sample name
    examples:
    - value: ISDsoil1
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample name
    rank: 1000
    is_a: investigation field
    string_serialization: '{text}'
    slot_uri: MIXS:0001107
    multivalued: false
    alias: samp_name
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  biosample_categories:
    name: biosample_categories
    title: Categories the biosample belongs to
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    multivalued: true
    alias: biosample_categories
    owner: Biosample
    domain_of:
    - Biosample
    range: BiosampleCategoryEnum
  part_of:
    name: part_of
    description: Links a resource to another resource that either logically or physically
      includes it.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    domain: NamedThing
    slot_uri: dcterms:isPartOf
    multivalued: true
    alias: part_of
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    - Study
    - OmicsProcessing
    - WorkflowExecutionActivity
    range: Study
    required: true
    pattern: ^nmdc:sty-[0-9][a-z]{0,6}[0-9]-[A-Za-z0-9]{1,}(\.[A-Za-z0-9]{1,})*(_[A-Za-z0-9_\.-]+)?$
  id:
    name: id
    description: An NMDC assigned unique identifier for a biosample submitted to NMDC.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    identifier: true
    alias: id
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - Activity
    range: uriorcurie
    required: true
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
    structured_pattern:
      syntax: '{id_nmdc_prefix}:bsm-{id_shoulder}-{id_blade}{id_version}{id_locus}'
      interpolated: true
  alternative_identifiers:
    name: alternative_identifiers
    description: Unique identifier for a biosample submitted to additional resources.
      Matches the entity that has been submitted to NMDC
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    multivalued: true
    alias: alternative_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    - NamedThing
    - MetaboliteQuantification
    range: uriorcurie
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
  gold_biosample_identifiers:
    name: gold_biosample_identifiers
    annotations:
      display_hint:
        tag: display_hint
        value: Provide the GOLD biosample IDs associated with this biosample.
    description: Unique identifier for a biosample submitted to GOLD that matches
      the NMDC submitted biosample
    comments:
    - This is the ID provided by GOLD that starts with 'GB'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: biosample_identifiers
    multivalued: true
    alias: gold_biosample_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: uriorcurie
    pattern: ^gold:Gb[0-9]+$
  insdc_biosample_identifiers:
    name: insdc_biosample_identifiers
    description: identifiers for corresponding sample in INSDC
    examples:
    - value: https://bioregistry.io/biosample:SAMEA5989477
    - value: https://bioregistry.io/biosample:SAMD00212331
      description: I13_N_5-10 sample from Soil fungal diversity along elevational
        gradients
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://github.com/bioregistry/bioregistry/issues/108
    - https://www.ebi.ac.uk/biosamples/
    - https://www.ncbi.nlm.nih.gov/biosample
    - https://www.ddbj.nig.ac.jp/biosample/index-e.html
    aliases:
    - EBI biosample identifiers
    - NCBI biosample identifiers
    - DDBJ biosample identifiers
    rank: 1000
    is_a: biosample_identifiers
    mixins:
    - insdc_identifiers
    multivalued: true
    alias: insdc_biosample_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: external_identifier
    pattern: ^biosample:SAM[NED]([A-Z])?[0-9]+$
  emsl_biosample_identifiers:
    name: emsl_biosample_identifiers
    description: A list of identifiers for the biosample from the EMSL database.  This
      is used to link the biosample, as modeled by NMDC, to the biosample in the planned
      EMSL NEXUS database.
    title: EMSL Biosample Identifiers
    todos:
    - removed "planned" once NEXUS is online
    - determine real expansion for emsl prefix
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: biosample_identifiers
    mixins:
    - emsl_identifiers
    multivalued: true
    alias: emsl_biosample_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: external_identifier
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
  igsn_biosample_identifiers:
    name: igsn_biosample_identifiers
    description: A list of identifiers for the biosample from the IGSN database.
    title: IGSN Biosample Identifiers
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: biosample_identifiers
    mixins:
    - igsn_identifiers
    multivalued: true
    alias: igsn_biosample_identifiers
    owner: Biosample
    domain_of:
    - Biosample
    range: external_identifier
    pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$
  abs_air_humidity:
    name: abs_air_humidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram per gram, kilogram per kilogram, kilogram, pound
      occurrence:
        tag: occurrence
        value: '1'
    description: Actual mass of water vapor - mh20 - present in the air water vapor
      mixture
    title: absolute air humidity
    examples:
    - value: 9 gram per gram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - absolute air humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000122
    multivalued: false
    alias: abs_air_humidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  add_recov_method:
    name: add_recov_method
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration;timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: Additional (i.e. Secondary, tertiary, etc.) recovery methods deployed
      for increase of hydrocarbon recovery from resource and start date for each one
      of them. If "other" is specified, please propose entry in "additional info"
      field
    title: secondary and tertiary recovery methods and start date
    examples:
    - value: Polymer Addition;2018-06-21T14:30Z
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - secondary and tertiary recovery methods and start date
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001009
    multivalued: false
    alias: add_recov_method
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  additional_info:
    name: additional_info
    annotations:
      expected_value:
        tag: expected_value
        value: text
      occurrence:
        tag: occurrence
        value: '1'
    description: Information that doesn't fit anywhere else. Can also be used to propose
      new entries for fields with controlled vocabulary
    title: additional info
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - additional info
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000300
    multivalued: false
    alias: additional_info
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  address:
    name: address
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The street name and building number where the sampling occurred.
    title: address
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - address
    rank: 1000
    is_a: core field
    string_serialization: '{integer}{text}'
    slot_uri: MIXS:0000218
    multivalued: false
    alias: address
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  adj_room:
    name: adj_room
    annotations:
      expected_value:
        tag: expected_value
        value: room name;room number
      occurrence:
        tag: occurrence
        value: '1'
    description: List of rooms (room number, room name) immediately adjacent to the
      sampling room
    title: adjacent rooms
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - adjacent rooms
    rank: 1000
    is_a: core field
    string_serialization: '{text};{integer}'
    slot_uri: MIXS:0000219
    multivalued: false
    alias: adj_room
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  aero_struc:
    name: aero_struc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Aerospace structures typically consist of thin plates with stiffeners
      for the external surfaces, bulkheads and frames to support the shape and fasteners
      such as welds, rivets, screws and bolts to hold the components together
    title: aerospace structure
    examples:
    - value: plane
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - aerospace structure
    rank: 1000
    is_a: core field
    string_serialization: '[plane|glider]'
    slot_uri: MIXS:0000773
    multivalued: false
    alias: aero_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  agrochem_addition:
    name: agrochem_addition
    annotations:
      expected_value:
        tag: expected_value
        value: agrochemical name;agrochemical amount;timestamp
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Addition of fertilizers, pesticides, etc. - amount and time of applications
    title: history/agrochemical additions
    examples:
    - value: roundup;5 milligram per liter;2018-06-21
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - history/agrochemical additions
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{timestamp}'
    slot_uri: MIXS:0000639
    multivalued: true
    alias: agrochem_addition
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  air_PM_concen:
    name: air_PM_concen
    annotations:
      expected_value:
        tag: expected_value
        value: particulate matter name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: micrograms per cubic meter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of substances that remain suspended in the air, and
      comprise mixtures of organic and inorganic substances (PM10 and PM2.5); can
      report multiple PM's by entering numeric values preceded by name of PM
    title: air particulate matter concentration
    examples:
    - value: PM2.5;10 microgram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - air particulate matter concentration
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000108
    multivalued: true
    alias: air_PM_concen
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  air_temp:
    name: air_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Temperature of the air at the time of sampling
    title: air temperature
    examples:
    - value: 20 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - air temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000124
    multivalued: false
    alias: air_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  air_temp_regm:
    name: air_temp_regm
    annotations:
      expected_value:
        tag: expected_value
        value: temperature value;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving an exposure to varying temperatures;
      should include the temperature, treatment regimen including how many times the
      treatment was repeated, how long each treatment lasted, and the start and end
      time of the entire treatment; can include different temperature regimens
    title: air temperature regimen
    examples:
    - value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - air temperature regimen
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000551
    multivalued: true
    alias: air_temp_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  al_sat:
    name: al_sat
    description: The relative abundance of aluminum in the sample
    title: aluminum saturation/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    notes:
    - Aluminum saturation is the percentage of the CEC occupies by aluminum. Like
      all cations, aluminum held by the cation exchange complex is in equilibrium
      with aluminum in the soil solution.
    examples:
    - value: 27%
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000607
    multivalued: false
    alias: al_sat
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  al_sat_meth:
    name: al_sat_meth
    description: Reference or method used in determining Aluminum saturation
    title: aluminum saturation method/ extreme unusual properties
    todos:
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
    comments:
    - Required when aluminum saturation is provided.
    examples:
    - value: https://doi.org/10.1371/journal.pone.0176357
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000324
    multivalued: false
    alias: al_sat_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  alkalinity:
    name: alkalinity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milliequivalent per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Alkalinity, the ability of a solution to neutralize acids to the
      equivalence point of carbonate or bicarbonate
    title: alkalinity
    examples:
    - value: 50 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - alkalinity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000421
    multivalued: false
    alias: alkalinity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  alkalinity_method:
    name: alkalinity_method
    annotations:
      expected_value:
        tag: expected_value
        value: description of method
      occurrence:
        tag: occurrence
        value: '1'
    description: Method used for alkalinity measurement
    title: alkalinity method
    examples:
    - value: titration
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - alkalinity method
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000298
    multivalued: false
    alias: alkalinity_method
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  alkyl_diethers:
    name: alkyl_diethers
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of alkyl diethers
    title: alkyl diethers
    examples:
    - value: 0.005 mole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - alkyl diethers
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000490
    multivalued: false
    alias: alkyl_diethers
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  alt:
    name: alt
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
    description: Altitude is a term used to identify heights of objects such as airplanes,
      space shuttles, rockets, atmospheric balloons and heights of places such as
      atmospheric layers and clouds. It is used to measure the height of an object
      which is above the earth's surface. In this context, the altitude measurement
      is the vertical distance between the earth's surface above sea level and the
      sampled position in the air
    title: altitude
    examples:
    - value: 100 meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - altitude
    rank: 1000
    is_a: environment field
    slot_uri: MIXS:0000094
    multivalued: false
    alias: alt
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  aminopept_act:
    name: aminopept_act
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mole per liter per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of aminopeptidase activity
    title: aminopeptidase activity
    examples:
    - value: 0.269 mole per liter per hour
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - aminopeptidase activity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000172
    multivalued: false
    alias: aminopept_act
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ammonium:
    name: ammonium
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of ammonium in the sample
    title: ammonium
    examples:
    - value: 1.5 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ammonium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000427
    multivalued: false
    alias: ammonium
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ammonium_nitrogen:
    name: ammonium_nitrogen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mg/kg
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of ammonium nitrogen in the sample
    title: ammonium nitrogen
    examples:
    - value: 2.3 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - ammonium_nitrogen
    - NH4-N
    rank: 1000
    alias: ammonium_nitrogen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  amount_light:
    name: amount_light
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: lux, lumens per square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The unit of illuminance and luminous emittance, measuring luminous
      flux per unit area
    title: amount of light
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - amount of light
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000140
    multivalued: false
    alias: amount_light
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ances_data:
    name: ances_data
    annotations:
      expected_value:
        tag: expected_value
        value: free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Information about either pedigree or other ancestral information
      description (e.g. parental variety in case of mutant or selection), e.g. A/3*B
      (meaning [(A x B) x B] x B)
    title: ancestral data
    examples:
    - value: A/3*B
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ancestral data
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000247
    multivalued: false
    alias: ances_data
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  annual_precpt:
    name: annual_precpt
    description: The average of all annual precipitation values known, or an estimated
      equivalent value derived by such methods as regional indexes or Isohyetal maps.
    title: mean annual precipitation
    examples:
    - value: 8.94 inch
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000644
    multivalued: false
    alias: annual_precpt
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  annual_temp:
    name: annual_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Mean annual temperature
    title: mean annual temperature
    examples:
    - value: 12.5 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mean annual temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000642
    multivalued: false
    alias: annual_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  antibiotic_regm:
    name: antibiotic_regm
    annotations:
      expected_value:
        tag: expected_value
        value: antibiotic name;antibiotic amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: milligram
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving antibiotic administration;
      should include the name of antibiotic, amount administered, treatment regimen
      including how many times the treatment was repeated, how long each treatment
      lasted, and the start and end time of the entire treatment; can include multiple
      antibiotic regimens
    title: antibiotic regimen
    examples:
    - value: penicillin;5 milligram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - antibiotic regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000553
    multivalued: true
    alias: antibiotic_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  api:
    name: api
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degrees API
      occurrence:
        tag: occurrence
        value: '1'
    description: 'API gravity is a measure of how heavy or light a petroleum liquid
      is compared to water (source: https://en.wikipedia.org/wiki/API_gravity) (e.g.
      31.1¬∞ API)'
    title: API gravity
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - API gravity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000157
    multivalued: false
    alias: api
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  arch_struc:
    name: arch_struc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: An architectural structure is a human-made, free-standing, immobile
      outdoor construction
    title: architectural structure
    examples:
    - value: shed
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - architectural structure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000774
    multivalued: false
    alias: arch_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: arch_struc_enum
  aromatics_pc:
    name: aromatics_pc
    annotations:
      expected_value:
        tag: expected_value
        value: name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis
      method that divides¬†crude oil¬†components according to their polarizability
      and polarity. There are three main methods to obtain SARA results. The most
      popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source:
      https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
    title: aromatics wt%
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - aromatics wt%
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000133
    multivalued: false
    alias: aromatics_pc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  asphaltenes_pc:
    name: asphaltenes_pc
    annotations:
      expected_value:
        tag: expected_value
        value: name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis
      method that divides¬†crude oil¬†components according to their polarizability
      and polarity. There are three main methods to obtain SARA results. The most
      popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source:
      https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
    title: asphaltenes wt%
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - asphaltenes wt%
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000135
    multivalued: false
    alias: asphaltenes_pc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  atmospheric_data:
    name: atmospheric_data
    annotations:
      expected_value:
        tag: expected_value
        value: atmospheric data name;measurement value
      occurrence:
        tag: occurrence
        value: m
    description: Measurement of atmospheric data; can include multiple data
    title: atmospheric data
    examples:
    - value: wind speed;9 knots
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - atmospheric data
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0001097
    multivalued: true
    alias: atmospheric_data
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  avg_dew_point:
    name: avg_dew_point
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The average of dew point measures taken at the beginning of every
      hour over a 24 hour period on the sampling day
    title: average dew point
    examples:
    - value: 25.5 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - average dew point
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000141
    multivalued: false
    alias: avg_dew_point
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  avg_occup:
    name: avg_occup
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: Daily average occupancy of room. Indicate the number of person(s)
      daily occupying the sampling room.
    title: average daily occupancy
    examples:
    - value: '2'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - average daily occupancy
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000775
    multivalued: false
    alias: avg_occup
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  avg_temp:
    name: avg_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The average of temperatures taken at the beginning of every hour
      over a 24 hour period on the sampling day
    title: average temperature
    examples:
    - value: 12.5 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - average temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000142
    multivalued: false
    alias: avg_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  bac_prod:
    name: bac_prod
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per cubic meter per day
      occurrence:
        tag: occurrence
        value: '1'
    description: Bacterial production in the water column measured by isotope uptake
    title: bacterial production
    examples:
    - value: 5 milligram per cubic meter per day
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bacterial production
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000683
    multivalued: false
    alias: bac_prod
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  bac_resp:
    name: bac_resp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per cubic meter per day, micromole oxygen per liter per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of bacterial respiration in the water column
    title: bacterial respiration
    examples:
    - value: 300 micromole oxygen per liter per hour
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bacterial respiration
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000684
    multivalued: false
    alias: bac_resp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  bacteria_carb_prod:
    name: bacteria_carb_prod
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: nanogram per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of bacterial carbon production
    title: bacterial carbon production
    examples:
    - value: 2.53 microgram per liter per hour
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bacterial carbon production
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000173
    multivalued: false
    alias: bacteria_carb_prod
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  barometric_press:
    name: barometric_press
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millibar
      occurrence:
        tag: occurrence
        value: '1'
    description: Force per unit area exerted against a surface by the weight of air
      above that surface
    title: barometric pressure
    examples:
    - value: 5 millibar
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - barometric pressure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000096
    multivalued: false
    alias: barometric_press
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  basin:
    name: basin
    annotations:
      expected_value:
        tag: expected_value
        value: name
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of the basin (e.g. Campos)
    title: basin name
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - basin name
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000290
    multivalued: false
    alias: basin
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  bathroom_count:
    name: bathroom_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of bathrooms in the building
    title: bathroom count
    examples:
    - value: '1'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bathroom count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000776
    multivalued: false
    alias: bathroom_count
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  bedroom_count:
    name: bedroom_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of bedrooms in the building
    title: bedroom count
    examples:
    - value: '2'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bedroom count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000777
    multivalued: false
    alias: bedroom_count
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  benzene:
    name: benzene
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of benzene in the sample
    title: benzene
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - benzene
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000153
    multivalued: false
    alias: benzene
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  biochem_oxygen_dem:
    name: biochem_oxygen_dem
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Amount of dissolved oxygen needed by aerobic biological organisms
      in a body of water to break down organic material present in a given water sample
      at certain temperature over a specific time period
    title: biochemical oxygen demand
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biochemical oxygen demand
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000653
    multivalued: false
    alias: biochem_oxygen_dem
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  biocide:
    name: biocide
    annotations:
      expected_value:
        tag: expected_value
        value: name;name;timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: List of biocides (commercial name of product and supplier) and date
      of administration
    title: biocide administration
    examples:
    - value: ALPHA 1427;Baker Hughes;2008-01-23
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biocide administration
    rank: 1000
    is_a: core field
    string_serialization: '{text};{text};{timestamp}'
    slot_uri: MIXS:0001011
    multivalued: false
    alias: biocide
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  biocide_admin_method:
    name: biocide_admin_method
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;frequency;duration;duration
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Method of biocide administration (dose, frequency, duration, time
      elapsed between last biociding and sampling) (e.g. 150 mg/l; weekly; 4 hr; 3
      days)
    title: biocide administration method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biocide administration method
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration}'
    slot_uri: MIXS:0000456
    multivalued: false
    alias: biocide_admin_method
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  biol_stat:
    name: biol_stat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The level of genome modification.
    title: biological status
    examples:
    - value: natural
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biological status
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000858
    multivalued: false
    alias: biol_stat
    owner: Biosample
    domain_of:
    - Biosample
    range: biol_stat_enum
  biomass:
    name: biomass
    annotations:
      expected_value:
        tag: expected_value
        value: biomass type;measurement value
      preferred_unit:
        tag: preferred_unit
        value: ton, kilogram, gram
      occurrence:
        tag: occurrence
        value: m
    description: Amount of biomass; should include the name for the part of biomass
      measured, e.g. Microbial, total. Can include multiple measurements
    title: biomass
    examples:
    - value: total;20 gram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biomass
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000174
    multivalued: true
    alias: biomass
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  biotic_regm:
    name: biotic_regm
    annotations:
      expected_value:
        tag: expected_value
        value: free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Information about treatment(s) involving use of biotic factors, such
      as bacteria, viruses or fungi.
    title: biotic regimen
    examples:
    - value: sample inoculated with Rhizobium spp. Culture
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - biotic regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0001038
    multivalued: false
    alias: biotic_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  biotic_relationship:
    name: biotic_relationship
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
    description: Description of relationship(s) between the subject organism and other
      organism(s) it is associated with. E.g., parasite on species X; mutualist with
      species Y. The target organism is the subject of the relationship, and the other
      organism(s) is the object
    title: observed biotic relationship
    examples:
    - value: free living
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - observed biotic relationship
    rank: 1000
    is_a: nucleic acid sequence source field
    slot_uri: MIXS:0000028
    multivalued: false
    alias: biotic_relationship
    owner: Biosample
    domain_of:
    - Biosample
    range: biotic_relationship_enum
  bishomohopanol:
    name: bishomohopanol
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, microgram per gram
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of bishomohopanol
    title: bishomohopanol
    examples:
    - value: 14 microgram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bishomohopanol
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000175
    multivalued: false
    alias: bishomohopanol
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  blood_press_diast:
    name: blood_press_diast
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millimeter mercury
      occurrence:
        tag: occurrence
        value: '1'
    description: Resting diastolic blood pressure, measured as mm mercury
    title: host blood pressure diastolic
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host blood pressure diastolic
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000258
    multivalued: false
    alias: blood_press_diast
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  blood_press_syst:
    name: blood_press_syst
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millimeter mercury
      occurrence:
        tag: occurrence
        value: '1'
    description: Resting systolic blood pressure, measured as mm mercury
    title: host blood pressure systolic
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host blood pressure systolic
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000259
    multivalued: false
    alias: blood_press_syst
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  bromide:
    name: bromide
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of bromide
    title: bromide
    examples:
    - value: 0.05 parts per million
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - bromide
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000176
    multivalued: false
    alias: bromide
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  build_docs:
    name: build_docs
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The building design, construction and operation documents
    title: design, construction, and operation documents
    examples:
    - value: maintenance plans
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - design, construction, and operation documents
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000787
    multivalued: false
    alias: build_docs
    owner: Biosample
    domain_of:
    - Biosample
    range: build_docs_enum
  build_occup_type:
    name: build_occup_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: The primary function for which a building or discrete part of a building
      is intended to be used
    title: building occupancy type
    examples:
    - value: market
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - building occupancy type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000761
    multivalued: true
    alias: build_occup_type
    owner: Biosample
    domain_of:
    - Biosample
    range: build_occup_type_enum
  building_setting:
    name: building_setting
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: A location (geography) where a building is set
    title: building setting
    examples:
    - value: rural
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - building setting
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000768
    multivalued: false
    alias: building_setting
    owner: Biosample
    domain_of:
    - Biosample
    range: building_setting_enum
  built_struc_age:
    name: built_struc_age
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: year
      occurrence:
        tag: occurrence
        value: '1'
    description: The age of the built structure since construction
    title: built structure age
    examples:
    - value: '15'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - built structure age
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000145
    multivalued: false
    alias: built_struc_age
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  built_struc_set:
    name: built_struc_set
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The characterization of the location of the built structure as high
      or low human density
    title: built structure setting
    examples:
    - value: rural
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - built structure setting
    rank: 1000
    is_a: core field
    string_serialization: '[urban|rural]'
    slot_uri: MIXS:0000778
    multivalued: false
    alias: built_struc_set
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  built_struc_type:
    name: built_struc_type
    annotations:
      expected_value:
        tag: expected_value
        value: free text
      occurrence:
        tag: occurrence
        value: '1'
    description: A physical structure that is a body or assemblage of bodies in space
      to form a system capable of supporting loads
    title: built structure type
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - built structure type
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000721
    multivalued: false
    alias: built_struc_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  calcium:
    name: calcium
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, micromole per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of calcium in the sample
    title: calcium
    examples:
    - value: 0.2 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - calcium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000432
    multivalued: false
    alias: calcium
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  carb_dioxide:
    name: carb_dioxide
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Carbon dioxide (gas) amount or concentration at the time of sampling
    title: carbon dioxide
    examples:
    - value: 410 parts per million
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - carbon dioxide
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000097
    multivalued: false
    alias: carb_dioxide
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  carb_monoxide:
    name: carb_monoxide
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Carbon monoxide (gas) amount or concentration at the time of sampling
    title: carbon monoxide
    examples:
    - value: 0.1 parts per million
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - carbon monoxide
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000098
    multivalued: false
    alias: carb_monoxide
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  carb_nitro_ratio:
    name: carb_nitro_ratio
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Ratio of amount or concentrations of carbon to nitrogen
    title: carbon/nitrogen ratio
    examples:
    - value: '0.417361111'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - carbon/nitrogen ratio
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000310
    multivalued: false
    alias: carb_nitro_ratio
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ceil_area:
    name: ceil_area
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The area of the ceiling space within the room
    title: ceiling area
    examples:
    - value: 25 square meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling area
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000148
    multivalued: false
    alias: ceil_area
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ceil_cond:
    name: ceil_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The physical condition of the ceiling at the time of sampling; photos
      or video preferred; use drawings to indicate location of damaged areas
    title: ceiling condition
    examples:
    - value: damaged
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000779
    multivalued: false
    alias: ceil_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: ceil_cond_enum
  ceil_finish_mat:
    name: ceil_finish_mat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of material used to finish a ceiling
    title: ceiling finish material
    examples:
    - value: stucco
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling finish material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000780
    multivalued: false
    alias: ceil_finish_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: ceil_finish_mat_enum
  ceil_struc:
    name: ceil_struc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The construction format of the ceiling
    title: ceiling structure
    examples:
    - value: concrete
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling structure
    rank: 1000
    is_a: core field
    string_serialization: '[wood frame|concrete]'
    slot_uri: MIXS:0000782
    multivalued: false
    alias: ceil_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  ceil_texture:
    name: ceil_texture
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The feel, appearance, or consistency of a ceiling surface
    title: ceiling texture
    examples:
    - value: popcorn
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling texture
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000783
    multivalued: false
    alias: ceil_texture
    owner: Biosample
    domain_of:
    - Biosample
    range: ceil_texture_enum
  ceil_thermal_mass:
    name: ceil_thermal_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: joule per degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The ability of the ceiling to provide inertia against temperature
      fluctuations. Generally this means concrete that is exposed. A metal deck that
      supports a concrete slab will act thermally as long as it is exposed to room
      air flow
    title: ceiling thermal mass
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling thermal mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000143
    multivalued: false
    alias: ceil_thermal_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ceil_type:
    name: ceil_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of ceiling according to the ceiling's appearance or construction
    title: ceiling type
    examples:
    - value: coffered
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000784
    multivalued: false
    alias: ceil_type
    owner: Biosample
    domain_of:
    - Biosample
    range: ceil_type_enum
  ceil_water_mold:
    name: ceil_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew on the ceiling
    title: ceiling signs of water/mold
    examples:
    - value: presence of mold visible
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ceiling signs of water/mold
    rank: 1000
    is_a: core field
    string_serialization: '[presence of mold visible|no presence of mold visible]'
    slot_uri: MIXS:0000781
    multivalued: false
    alias: ceil_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  chem_administration:
    name: chem_administration
    annotations:
      expected_value:
        tag: expected_value
        value: CHEBI;timestamp
      occurrence:
        tag: occurrence
        value: m
    description: List of chemical compounds administered to the host or site where
      sampling occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can
      include multiple compounds. For chemical entities of biological interest ontology
      (chebi) (v 163), http://purl.bioontology.org/ontology/chebi
    title: chemical administration
    examples:
    - value: agar [CHEBI:2509];2018-05-11T20:00Z
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chemical administration
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]};{timestamp}'
    slot_uri: MIXS:0000751
    multivalued: true
    alias: chem_administration
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  chem_mutagen:
    name: chem_mutagen
    annotations:
      expected_value:
        tag: expected_value
        value: mutagen name;mutagen amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Treatment involving use of mutagens; should include the name of mutagen,
      amount administered, treatment regimen including how many times the treatment
      was repeated, how long each treatment lasted, and the start and end time of
      the entire treatment; can include multiple mutagen regimens
    title: chemical mutagen
    examples:
    - value: nitrous acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chemical mutagen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000555
    multivalued: true
    alias: chem_mutagen
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  chem_oxygen_dem:
    name: chem_oxygen_dem
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: A measure of the capacity of water to consume oxygen during the decomposition
      of organic matter and the oxidation of inorganic chemicals such as ammonia and
      nitrite
    title: chemical oxygen demand
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chemical oxygen demand
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000656
    multivalued: false
    alias: chem_oxygen_dem
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  chem_treat_method:
    name: chem_treat_method
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;frequency;duration;duration
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Method of chemical administration(dose, frequency, duration, time
      elapsed between administration and sampling) (e.g. 50 mg/l; twice a week; 1
      hr; 0 days)
    title: chemical treatment method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chemical treatment method
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration};{duration};{duration}'
    slot_uri: MIXS:0000457
    multivalued: false
    alias: chem_treat_method
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  chem_treatment:
    name: chem_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: name;name;timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: List of chemical compounds administered upstream the sampling location
      where sampling occurred (e.g. Glycols, H2S scavenger, corrosion and scale inhibitors,
      demulsifiers, and other production chemicals etc.). The commercial name of the
      product and name of the supplier should be provided. The date of administration
      should also be included
    title: chemical treatment
    examples:
    - value: ACCENT 1125;DOW;2010-11-17
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chemical treatment
    rank: 1000
    is_a: core field
    string_serialization: '{text};{text};{timestamp}'
    slot_uri: MIXS:0001012
    multivalued: false
    alias: chem_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  chimera_check:
    name: chimera_check
    annotations:
      expected_value:
        tag: expected_value
        value: name and version of software, parameters used
    description: Tool(s) used for chimera checking, including version number and parameters,
      to discover and remove chimeric sequences. A chimeric sequence is comprised
      of two or more phylogenetically distinct parent sequences.
    title: chimera check software
    examples:
    - value: uchime;v4.1;default parameters
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chimera check software
    rank: 1000
    is_a: sequencing field
    string_serialization: '{software};{version};{parameters}'
    slot_uri: MIXS:0000052
    multivalued: false
    alias: chimera_check
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  chloride:
    name: chloride
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of chloride in the sample
    title: chloride
    examples:
    - value: 5000 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chloride
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000429
    multivalued: false
    alias: chloride
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  chlorophyll:
    name: chlorophyll
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per cubic meter, microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of chlorophyll
    title: chlorophyll
    examples:
    - value: 5 milligram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - chlorophyll
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000177
    multivalued: false
    alias: chlorophyll
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  climate_environment:
    name: climate_environment
    description: Treatment involving an exposure to a particular climate; treatment
      regimen including how many times the treatment was repeated, how long each treatment
      lasted, and the start and end time of the entire treatment; can include multiple
      climates
    title: climate environment
    todos:
    - description says "can include multiple climates" but multivalued is set to false
    - add examples, i need to see some examples to add correctly formatted example.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0001040
    multivalued: true
    alias: climate_environment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  collection_date:
    name: collection_date
    annotations:
      expected_value:
        tag: expected_value
        value: date and time
    description: 'The time of sampling, either as an instance (single point in time)
      or interval. In case no exact time is available, the date/time can be right
      truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10;
      2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant'
    title: collection date
    examples:
    - value: 2018-05-11T10:00:00+01:00; 2018-05-11
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - collection date
    rank: 1000
    is_a: environment field
    slot_uri: MIXS:0000011
    multivalued: false
    alias: collection_date
    owner: Biosample
    domain_of:
    - Biosample
    range: TimestampValue
  conduc:
    name: conduc
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milliSiemens per centimeter
      occurrence:
        tag: occurrence
        value: '1'
    description: Electrical conductivity of water
    title: conductivity
    examples:
    - value: 10 milliSiemens per centimeter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - conductivity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000692
    multivalued: false
    alias: conduc
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  cool_syst_id:
    name: cool_syst_id
    annotations:
      expected_value:
        tag: expected_value
        value: unique identifier
      occurrence:
        tag: occurrence
        value: '1'
    description: The cooling system identifier
    title: cooling system identifier
    examples:
    - value: '12345'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - cooling system identifier
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000785
    multivalued: false
    alias: cool_syst_id
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  core field:
    name: core field
    description: basic fields
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    abstract: true
    alias: core_field
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  crop_rotation:
    name: crop_rotation
    annotations:
      expected_value:
        tag: expected_value
        value: crop rotation status;schedule
      occurrence:
        tag: occurrence
        value: '1'
    description: Whether or not crop is rotated, and if yes, rotation schedule
    title: history/crop rotation
    examples:
    - value: yes;R2/2017-01-01/2018-12-31/P6M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - history/crop rotation
    rank: 1000
    is_a: core field
    string_serialization: '{boolean};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000318
    multivalued: false
    alias: crop_rotation
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  cult_root_med:
    name: cult_root_med
    annotations:
      expected_value:
        tag: expected_value
        value: name, PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Name or reference for the hydroponic or in vitro culture rooting
      medium; can be the name of a commonly used medium or reference to a specific
      medium, e.g. Murashige and Skoog medium. If the medium has not been formally
      published, use the rooting medium descriptors.
    title: culture rooting medium
    examples:
    - value: http://himedialabs.com/TD/PT158.pdf
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - culture rooting medium
    rank: 1000
    is_a: core field
    string_serialization: '{text}|{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0001041
    multivalued: false
    alias: cult_root_med
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  cur_land_use:
    name: cur_land_use
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Present state of sample site
    title: current land use
    examples:
    - value: conifers
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - current land use
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001080
    multivalued: false
    alias: cur_land_use
    owner: Biosample
    domain_of:
    - Biosample
    range: cur_land_use_enum
  cur_vegetation:
    name: cur_vegetation
    description: Vegetation classification from one or more standard classification
      systems, or agricultural crop
    title: current vegetation
    todos:
    - Recommend changing this from text value to some king of ontology?
    comments:
    - Values provided here can be specific species of vegetation or vegetation regions
    - See for vegetation regions- https://education.nationalgeographic.org/resource/vegetation-region
    examples:
    - value: deciduous forest
    - value: forest
    - value: Bauhinia variegata
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000312
    multivalued: false
    alias: cur_vegetation
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: TextValue
  cur_vegetation_meth:
    name: cur_vegetation_meth
    description: Reference or method used in vegetation classification
    title: current vegetation method
    todos:
    - I'm not sure this is a DOI, PMID, or URI. Should pool the community and find
      out how they accomplish this if provided.
    comments:
    - Required when current vegetation is provided.
    examples:
    - value: https://doi.org/10.1111/j.1654-109X.2011.01154.x
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000314
    multivalued: false
    alias: cur_vegetation_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  date_last_rain:
    name: date_last_rain
    annotations:
      expected_value:
        tag: expected_value
        value: timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: The date of the last time it rained
    title: date last rain
    examples:
    - value: 2018-05-11:T14:30Z
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - date last rain
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000786
    multivalued: false
    alias: date_last_rain
    owner: Biosample
    domain_of:
    - Biosample
    range: TimestampValue
  density:
    name: density
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram per cubic meter, gram per cubic centimeter
      occurrence:
        tag: occurrence
        value: '1'
    description: Density of the sample, which is its mass per unit volume (aka volumetric
      mass density)
    title: density
    examples:
    - value: 1000 kilogram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - density
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000435
    multivalued: false
    alias: density
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  depos_env:
    name: depos_env
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment).
      If "other" is specified, please propose entry in "additional info" field
    title: depositional environment
    examples:
    - value: Continental - Alluvial
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - depositional environment
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000992
    multivalued: false
    alias: depos_env
    owner: Biosample
    domain_of:
    - Biosample
    range: depos_env_enum
  depth:
    name: depth
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
    description: The vertical distance below local surface, e.g. for sediment or soil
      samples depth is measured from sediment or soil surface, respectively. Depth
      can be reported as an interval for subsurface samples.
    title: depth
    examples:
    - value: 10 meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - depth
    rank: 1000
    is_a: environment field
    slot_uri: MIXS:0000018
    multivalued: false
    alias: depth
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  dew_point:
    name: dew_point
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The temperature to which a given parcel of humid air must be cooled,
      at constant barometric pressure, for water vapor to condense into water.
    title: dew point
    examples:
    - value: 22 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dew point
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000129
    multivalued: false
    alias: dew_point
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diether_lipids:
    name: diether_lipids
    annotations:
      expected_value:
        tag: expected_value
        value: diether lipid name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: nanogram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of diether lipids; can include multiple types of diether
      lipids
    title: diether lipids
    examples:
    - value: 0.2 nanogram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - diether lipids
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000178
    multivalued: true
    alias: diether_lipids
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  diss_carb_dioxide:
    name: diss_carb_dioxide
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved carbon dioxide in the sample or liquid
      portion of the sample
    title: dissolved carbon dioxide
    examples:
    - value: 5 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved carbon dioxide
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000436
    multivalued: false
    alias: diss_carb_dioxide
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_hydrogen:
    name: diss_hydrogen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved hydrogen
    title: dissolved hydrogen
    examples:
    - value: 0.3 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved hydrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000179
    multivalued: false
    alias: diss_hydrogen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_inorg_carb:
    name: diss_inorg_carb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Dissolved inorganic carbon concentration in the sample, typically
      measured after filtering the sample using a 0.45 micrometer filter
    title: dissolved inorganic carbon
    examples:
    - value: 2059 micromole per kilogram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved inorganic carbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000434
    multivalued: false
    alias: diss_inorg_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_inorg_nitro:
    name: diss_inorg_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved inorganic nitrogen
    title: dissolved inorganic nitrogen
    examples:
    - value: 761 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved inorganic nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000698
    multivalued: false
    alias: diss_inorg_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_inorg_phosp:
    name: diss_inorg_phosp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved inorganic phosphorus in the sample
    title: dissolved inorganic phosphorus
    examples:
    - value: 56.5 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved inorganic phosphorus
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000106
    multivalued: false
    alias: diss_inorg_phosp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_iron:
    name: diss_iron
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved iron in the sample
    title: dissolved iron
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved iron
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000139
    multivalued: false
    alias: diss_iron
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_org_carb:
    name: diss_org_carb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved organic carbon in the sample, liquid portion
      of the sample, or aqueous phase of the fluid
    title: dissolved organic carbon
    examples:
    - value: 197 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved organic carbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000433
    multivalued: false
    alias: diss_org_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_org_nitro:
    name: diss_org_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Dissolved organic nitrogen concentration measured as; total dissolved
      nitrogen - NH4 - NO3 - NO2
    title: dissolved organic nitrogen
    examples:
    - value: 0.05 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved organic nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000162
    multivalued: false
    alias: diss_org_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_oxygen:
    name: diss_oxygen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per kilogram, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved oxygen
    title: dissolved oxygen
    examples:
    - value: 175 micromole per kilogram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved oxygen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000119
    multivalued: false
    alias: diss_oxygen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  diss_oxygen_fluid:
    name: diss_oxygen_fluid
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per kilogram, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of dissolved oxygen in the oil field produced fluids
      as it contributes to oxgen-corrosion and microbial activity (e.g. Mic).
    title: dissolved oxygen in fluids
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - dissolved oxygen in fluids
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000438
    multivalued: false
    alias: diss_oxygen_fluid
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  dna_cont_well:
    name: dna_cont_well
    title: DNA plate position
    comments:
    - Required when 'plate' is selected for container type.
    - Leave blank if the sample will be shipped in a tube.
    - JGI will not process samples in corner wells, so A1, A12, H1 and H12 will not
      pass validation.
    - For partial plates, fill by columns, like B1-G1,A2-H2,A3-D3 (NOT A2-A11,B1-B8).
    examples:
    - value: B2
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 11
    string_serialization: '{96 well plate pos}'
    alias: dna_cont_well
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
    pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  door_comp_type:
    name: door_comp_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The composite type of the door
    title: door type, composite
    examples:
    - value: revolving
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door type, composite
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000795
    multivalued: false
    alias: door_comp_type
    owner: Biosample
    domain_of:
    - Biosample
    range: door_comp_type_enum
  door_cond:
    name: door_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The phsical condition of the door
    title: door condition
    examples:
    - value: new
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000788
    multivalued: false
    alias: door_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: door_cond_enum
  door_direct:
    name: door_direct
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The direction the door opens
    title: door direction of opening
    examples:
    - value: inward
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door direction of opening
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000789
    multivalued: false
    alias: door_direct
    owner: Biosample
    domain_of:
    - Biosample
    range: door_direct_enum
  door_loc:
    name: door_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The relative location of the door in the room
    title: door location
    examples:
    - value: north
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000790
    multivalued: false
    alias: door_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: door_loc_enum
  door_mat:
    name: door_mat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The material the door is composed of
    title: door material
    examples:
    - value: wood
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000791
    multivalued: false
    alias: door_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: door_mat_enum
  door_move:
    name: door_move
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of movement of the door
    title: door movement
    examples:
    - value: swinging
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door movement
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000792
    multivalued: false
    alias: door_move
    owner: Biosample
    domain_of:
    - Biosample
    range: door_move_enum
  door_size:
    name: door_size
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The size of the door
    title: door area or size
    examples:
    - value: 2.5 square meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door area or size
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000158
    multivalued: false
    alias: door_size
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  door_type:
    name: door_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of door material
    title: door type
    examples:
    - value: wooden
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000794
    multivalued: false
    alias: door_type
    owner: Biosample
    domain_of:
    - Biosample
    range: door_type_enum
  door_type_metal:
    name: door_type_metal
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of metal door
    title: door type, metal
    examples:
    - value: hollow
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door type, metal
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000796
    multivalued: false
    alias: door_type_metal
    owner: Biosample
    domain_of:
    - Biosample
    range: door_type_metal_enum
  door_type_wood:
    name: door_type_wood
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of wood door
    title: door type, wood
    examples:
    - value: battened
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door type, wood
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000797
    multivalued: false
    alias: door_type_wood
    owner: Biosample
    domain_of:
    - Biosample
    range: door_type_wood_enum
  door_water_mold:
    name: door_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew on a door
    title: door signs of water/mold
    examples:
    - value: presence of mold visible
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - door signs of water/mold
    rank: 1000
    is_a: core field
    string_serialization: '[presence of mold visible|no presence of mold visible]'
    slot_uri: MIXS:0000793
    multivalued: false
    alias: door_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  down_par:
    name: down_par
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microEinstein per square meter per second, microEinstein per square
          centimeter per second
      occurrence:
        tag: occurrence
        value: '1'
    description: Visible waveband radiance and irradiance measurements in the water
      column
    title: downward PAR
    examples:
    - value: 28.71 microEinstein per square meter per second
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - downward PAR
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000703
    multivalued: false
    alias: down_par
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  drainage_class:
    name: drainage_class
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Drainage classification from a standard system such as the USDA system
    title: drainage classification
    examples:
    - value: well
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - drainage classification
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001085
    multivalued: false
    alias: drainage_class
    owner: Biosample
    domain_of:
    - Biosample
    range: drainage_class_enum
  drawings:
    name: drawings
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The buildings architectural drawings; if design is chosen, indicate
      phase-conceptual, schematic, design development, and construction documents
    title: drawings
    examples:
    - value: sketch
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - drawings
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000798
    multivalued: false
    alias: drawings
    owner: Biosample
    domain_of:
    - Biosample
    range: drawings_enum
  ecosystem:
    name: ecosystem
    description: An ecosystem is a combination of a physical environment (abiotic
      factors) and all the organisms (biotic factors) that interact with this environment.
      Ecosystem is in position 1/5 in a GOLD path.
    comments:
    - The abiotic factors play a profound role on the type and composition of organisms
      in a given environment. The GOLD Ecosystem at the top of the five-level classification
      system is aimed at capturing the broader environment from which an organism
      or environmental sample is collected. The three broad groups under Ecosystem
      are Environmental, Host-associated, and Engineered. They represent samples collected
      from a natural environment or from another organism or from engineered environments
      like bioreactors respectively.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://gold.jgi.doe.gov/help
    rank: 1000
    is_a: gold_path_field
    alias: ecosystem
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    range: string
  ecosystem_category:
    name: ecosystem_category
    description: Ecosystem categories represent divisions within the ecosystem based
      on specific characteristics of the environment from where an organism or sample
      is isolated. Ecosystem category is in position 2/5 in a GOLD path.
    comments:
    - The Environmental ecosystem (for example) is divided into Air, Aquatic and Terrestrial.
      Ecosystem categories for Host-associated samples can be individual hosts or
      phyla and for engineered samples it may be manipulated environments like bioreactors,
      solid waste etc.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://gold.jgi.doe.gov/help
    rank: 1000
    is_a: gold_path_field
    alias: ecosystem_category
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    range: string
  ecosystem_subtype:
    name: ecosystem_subtype
    description: Ecosystem subtypes represent further subdivision of Ecosystem types
      into more distinct subtypes. Ecosystem subtype is in position 4/5 in a GOLD
      path.
    comments:
    - Ecosystem Type Marine (Environmental -> Aquatic -> Marine) is further divided
      (for example) into Intertidal zone, Coastal, Pelagic, Intertidal zone etc. in
      the Ecosystem subtype category.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://gold.jgi.doe.gov/help
    rank: 1000
    is_a: gold_path_field
    alias: ecosystem_subtype
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    range: string
  ecosystem_type:
    name: ecosystem_type
    description: Ecosystem types represent things having common characteristics within
      the Ecosystem Category. These common characteristics based grouping is still
      broad but specific to the characteristics of a given environment. Ecosystem
      type is in position 3/5 in a GOLD path.
    comments:
    - The Aquatic ecosystem category (for example) may have ecosystem types like Marine
      or Thermal springs etc. Ecosystem category Air may have Indoor air or Outdoor
      air as different Ecosystem Types. In the case of Host-associated samples, ecosystem
      type can represent Respiratory system, Digestive system, Roots etc.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://gold.jgi.doe.gov/help
    rank: 1000
    is_a: gold_path_field
    alias: ecosystem_type
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    range: string
  efficiency_percent:
    name: efficiency_percent
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Percentage of volatile solids removed from the anaerobic digestor
    title: efficiency percent
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - efficiency percent
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000657
    multivalued: false
    alias: efficiency_percent
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  elev:
    name: elev
    description: Elevation of the sampling site is its height above a fixed reference
      point, most commonly the mean sea level. Elevation is mainly used when referring
      to points on the earth's surface, while altitude is used for points above the
      surface, such as an aircraft in flight or a spacecraft in orbit.
    title: elevation, meters
    comments:
    - All elevations must be reported in meters. Provide the numerical portion only.
    - Please use https://www.advancedconverter.com/map-tools/find-altitude-by-coordinates,
      if needed, to help estimate the elevation based on latitude and longitude coordinates.
    examples:
    - value: '100'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: environment field
    slot_uri: MIXS:0000093
    multivalued: false
    alias: elev
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: float
  elevator:
    name: elevator
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of elevators within the built structure
    title: elevator count
    examples:
    - value: '2'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - elevator count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000799
    multivalued: false
    alias: elevator
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  emulsions:
    name: emulsions
    annotations:
      expected_value:
        tag: expected_value
        value: emulsion name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Amount or concentration of substances such as paints, adhesives,
      mayonnaise, hair colorants, emulsified oils, etc.; can include multiple emulsion
      types
    title: emulsions
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - emulsions
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000660
    multivalued: true
    alias: emulsions
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  env_broad_scale:
    name: env_broad_scale
    description: 'Report the major environmental system the sample or specimen came
      from. The system(s) identified should have a coarse spatial grain, to provide
      the general environmental context of where the sampling was done (e.g. in the
      desert or a rainforest). We recommend using subclasses of EnvO’s biome class:  http://purl.obolibrary.org/obo/ENVO_00000428.
      EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'
    title: broad-scale environmental context
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: environment field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000012
    multivalued: false
    alias: env_broad_scale
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledIdentifiedTermValue
    required: true
  env_local_scale:
    name: env_local_scale
    description: 'Report the entity or entities which are in the sample or specimen’s
      local vicinity and which you believe have significant causal influences on your
      sample or specimen. We recommend using EnvO terms which are of smaller spatial
      grain than your entry for env_broad_scale. Terms, such as anatomical sites,
      from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON)
      are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS.'
    title: local environmental context
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: environment field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000013
    multivalued: false
    alias: env_local_scale
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledIdentifiedTermValue
    required: true
  env_medium:
    name: env_medium
    description: 'Report the environmental material(s) immediately surrounding the
      sample or specimen at the time of sampling. We recommend using subclasses of
      ''environmental material'' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO
      documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
      . Terms from other OBO ontologies are permissible as long as they reference
      mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities
      (e.g. a tree, a leaf, a table top).'
    title: environmental medium
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: environment field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000014
    multivalued: false
    alias: env_medium
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledIdentifiedTermValue
    required: true
  env_package:
    name: env_package
    description: MIxS extension for reporting of measurements and observations obtained
      from one or more of the environments where the sample was obtained. All environmental
      packages listed here are further defined in separate subtables. By giving the
      name of the environmental package, a selection of fields can be made from the
      subtables and can be reported
    notes:
    - no longer in MIxS as of 6.0?
    in_subset:
    - mixs extension
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - environmental package
    rank: 1000
    alias: env_package
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  environment field:
    name: environment field
    description: field describing environmental aspect of a sample
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    abstract: true
    alias: environment_field
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  escalator:
    name: escalator
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of escalators within the built structure
    title: escalator count
    examples:
    - value: '4'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - escalator count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000800
    multivalued: false
    alias: escalator
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  ethylbenzene:
    name: ethylbenzene
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of ethylbenzene in the sample
    title: ethylbenzene
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ethylbenzene
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000155
    multivalued: false
    alias: ethylbenzene
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  exp_duct:
    name: exp_duct
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The amount of exposed ductwork in the room
    title: exposed ductwork
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - exposed ductwork
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000144
    multivalued: false
    alias: exp_duct
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  exp_pipe:
    name: exp_pipe
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of exposed pipes in the room
    title: exposed pipes
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - exposed pipes
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000220
    multivalued: false
    alias: exp_pipe
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  experimental_factor:
    name: experimental_factor
    annotations:
      expected_value:
        tag: expected_value
        value: text or EFO and/or OBI
    description: Experimental factors are essentially the variable aspects of an experiment
      design which can be used to describe an experiment, or set of experiments, in
      an increasingly detailed manner. This field accepts ontology terms from Experimental
      Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For
      a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO;
      for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
    title: experimental factor
    examples:
    - value: time series design [EFO:EFO_0001779]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - experimental factor
    rank: 1000
    is_a: investigation field
    string_serialization: '{termLabel} {[termID]}|{text}'
    slot_uri: MIXS:0000008
    multivalued: false
    alias: experimental_factor
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  ext_door:
    name: ext_door
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of exterior doors in the built structure
    title: exterior door count
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - exterior door count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000170
    multivalued: false
    alias: ext_door
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  ext_wall_orient:
    name: ext_wall_orient
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The orientation of the exterior wall
    title: orientations of exterior wall
    examples:
    - value: northwest
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - orientations of exterior wall
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000817
    multivalued: false
    alias: ext_wall_orient
    owner: Biosample
    domain_of:
    - Biosample
    range: ext_wall_orient_enum
  ext_window_orient:
    name: ext_window_orient
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The compass direction the exterior window of the room is facing
    title: orientations of exterior window
    examples:
    - value: southwest
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - orientations of exterior window
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000818
    multivalued: false
    alias: ext_window_orient
    owner: Biosample
    domain_of:
    - Biosample
    range: ext_window_orient_enum
  extreme_event:
    name: extreme_event
    annotations:
      expected_value:
        tag: expected_value
        value: date, string
    description: Unusual physical events that may have affected microbial populations
    title: history/extreme events
    examples:
    - value: 1980-05-18, volcanic eruption
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000320
    multivalued: false
    alias: extreme_event
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  fao_class:
    name: fao_class
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Soil classification from the FAO World Reference Database for Soil
      Resources. The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups
    title: soil_taxonomic/FAO classification
    examples:
    - value: Luvisols
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil_taxonomic/FAO classification
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001083
    multivalued: false
    alias: fao_class
    owner: Biosample
    domain_of:
    - Biosample
    range: fao_class_enum
  fertilizer_regm:
    name: fertilizer_regm
    annotations:
      expected_value:
        tag: expected_value
        value: fertilizer name;fertilizer amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving the use of fertilizers; should
      include the name of fertilizer, amount administered, treatment regimen including
      how many times the treatment was repeated, how long each treatment lasted, and
      the start and end time of the entire treatment; can include multiple fertilizer
      regimens
    title: fertilizer regimen
    examples:
    - value: urea;0.6 milligram per liter;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - fertilizer regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000556
    multivalued: true
    alias: fertilizer_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  field:
    name: field
    annotations:
      expected_value:
        tag: expected_value
        value: name
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of the hydrocarbon field (e.g. Albacora)
    title: field name
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - field name
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000291
    multivalued: false
    alias: field
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  filter_type:
    name: filter_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: A device which removes solid particulates or airborne molecular contaminants
    title: filter type
    examples:
    - value: HEPA
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - filter type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000765
    multivalued: true
    alias: filter_type
    owner: Biosample
    domain_of:
    - Biosample
    range: filter_type_enum
  fire:
    name: fire
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    description: Historical and/or physical evidence of fire
    title: history/fire
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    comments:
    - Provide the date the fire occurred. If extended burning occurred provide the
      date range.
    examples:
    - value: '1871-10-10'
    - value: 1871-10-01 to 1871-10-31
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001086
    multivalued: false
    alias: fire
    owner: Biosample
    domain_of:
    - Biosample
    range: string
    pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?(\s+to\s+[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?)?$
  fireplace_type:
    name: fireplace_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: A firebox with chimney
    title: fireplace type
    examples:
    - value: wood burning
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - fireplace type
    rank: 1000
    is_a: core field
    string_serialization: '[gas burning|wood burning]'
    slot_uri: MIXS:0000802
    multivalued: false
    alias: fireplace_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  flooding:
    name: flooding
    annotations:
      expected_value:
        tag: expected_value
        value: date string
    description: Historical and/or physical evidence of flooding
    title: history/flooding
    todos:
    - is "to" acceptable? Is there a better way to request that be written?
    - What about if the "day" isn't known? Is this ok?
    comments:
    - Provide the date the flood occurred. If extended flooding occurred provide the
      date range.
    examples:
    - value: '1927-04-15'
    - value: 1927-04 to 1927-05
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000319
    multivalued: false
    alias: flooding
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  floor_age:
    name: floor_age
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: years, weeks, days
      occurrence:
        tag: occurrence
        value: '1'
    description: The time period since installment of the carpet or flooring
    title: floor age
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor age
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000164
    multivalued: false
    alias: floor_age
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  floor_area:
    name: floor_area
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The area of the floor space within the room
    title: floor area
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor area
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000165
    multivalued: false
    alias: floor_area
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  floor_cond:
    name: floor_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The physical condition of the floor at the time of sampling; photos
      or video preferred; use drawings to indicate location of damaged areas
    title: floor condition
    examples:
    - value: new
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000803
    multivalued: false
    alias: floor_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: floor_cond_enum
  floor_count:
    name: floor_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of floors in the building, including basements and mechanical
      penthouse
    title: floor count
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000225
    multivalued: false
    alias: floor_count
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  floor_finish_mat:
    name: floor_finish_mat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The floor covering type; the finished surface that is walked on
    title: floor finish material
    examples:
    - value: carpet
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor finish material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000804
    multivalued: false
    alias: floor_finish_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: floor_finish_mat_enum
  floor_struc:
    name: floor_struc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Refers to the structural elements and subfloor upon which the finish
      flooring is installed
    title: floor structure
    examples:
    - value: concrete
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor structure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000806
    multivalued: false
    alias: floor_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: floor_struc_enum
  floor_thermal_mass:
    name: floor_thermal_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: joule per degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The ability of the floor to provide inertia against temperature fluctuations
    title: floor thermal mass
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor thermal mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000166
    multivalued: false
    alias: floor_thermal_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  floor_water_mold:
    name: floor_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew in a room
    title: floor signs of water/mold
    examples:
    - value: ceiling discoloration
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - floor signs of water/mold
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000805
    multivalued: false
    alias: floor_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: floor_water_mold_enum
  fluor:
    name: fluor
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram chlorophyll a per cubic meter, volts
      occurrence:
        tag: occurrence
        value: '1'
    description: Raw or converted fluorescence of water
    title: fluorescence
    examples:
    - value: 2.5 volts
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - fluorescence
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000704
    multivalued: false
    alias: fluor
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  freq_clean:
    name: freq_clean
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration or {text}
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of times the sample location is cleaned. Frequency of
      cleaning might be on a Daily basis, Weekly, Monthly, Quarterly or Annually.
    title: frequency of cleaning
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - frequency of cleaning
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000226
    multivalued: false
    alias: freq_clean
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  freq_cook:
    name: freq_cook
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of times a meal is cooked per week
    title: frequency of cooking
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - frequency of cooking
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000227
    multivalued: false
    alias: freq_cook
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  fungicide_regm:
    name: fungicide_regm
    annotations:
      expected_value:
        tag: expected_value
        value: fungicide name;fungicide amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of fungicides; should include
      the name of fungicide, amount administered, treatment regimen including how
      many times the treatment was repeated, how long each treatment lasted, and the
      start and end time of the entire treatment; can include multiple fungicide regimens
    title: fungicide regimen
    examples:
    - value: bifonazole;1 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - fungicide regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000557
    multivalued: true
    alias: fungicide_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  furniture:
    name: furniture
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The types of furniture present in the sampled room
    title: furniture
    examples:
    - value: chair
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - furniture
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000807
    multivalued: false
    alias: furniture
    owner: Biosample
    domain_of:
    - Biosample
    range: furniture_enum
  gaseous_environment:
    name: gaseous_environment
    description: Use of conditions with differing gaseous environments; should include
      the name of gaseous compound, amount administered, treatment duration, interval
      and total experimental duration; can include multiple gaseous environment regimens
    title: gaseous environment
    todos:
    - would like to see usage examples for this slot. Requiring micromole/L seems
      too limiting and doesn't match expected_value value
    - did I do this right? keep the example that's provided and add another? so as
      to not override
    examples:
    - value: CO2; 500ppm above ambient; constant
    - value: nitric oxide;0.5 micromole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000558
    multivalued: true
    alias: gaseous_environment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  gaseous_substances:
    name: gaseous_substances
    annotations:
      expected_value:
        tag: expected_value
        value: gaseous substance name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: m
    description: Amount or concentration of substances such as hydrogen sulfide, carbon
      dioxide, methane, etc.; can include multiple substances
    title: gaseous substances
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - gaseous substances
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000661
    multivalued: true
    alias: gaseous_substances
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  gender_restroom:
    name: gender_restroom
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The gender type of the restroom
    title: gender of restroom
    examples:
    - value: male
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - gender of restroom
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000808
    multivalued: false
    alias: gender_restroom
    owner: Biosample
    domain_of:
    - Biosample
    range: gender_restroom_enum
  genetic_mod:
    name: genetic_mod
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI,url or free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Genetic modifications of the genome of an organism, which may occur
      naturally by spontaneous mutation, or be introduced by some experimental means,
      e.g. specification of a transgene or the gene knocked-out or details of transient
      transfection
    title: genetic modification
    examples:
    - value: aox1A transgenic
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - genetic modification
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}|{text}'
    slot_uri: MIXS:0000859
    multivalued: false
    alias: genetic_mod
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  geo_loc_name:
    name: geo_loc_name
    annotations:
      expected_value:
        tag: expected_value
        value: 'country or sea name (INSDC or GAZ): region(GAZ), specific location
          name'
    description: The geographical origin of the sample as defined by the country or
      sea name followed by specific region name. Country or sea names should be chosen
      from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology
      (http://purl.bioontology.org/ontology/GAZ)
    title: geographic location (country and/or sea,region)
    examples:
    - value: 'USA: Maryland, Bethesda'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - geographic location (country and/or sea,region)
    rank: 1000
    is_a: environment field
    string_serialization: '{term}: {term}, {text}'
    slot_uri: MIXS:0000010
    multivalued: false
    alias: geo_loc_name
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: TextValue
  glucosidase_act:
    name: glucosidase_act
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mol per liter per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of glucosidase activity
    title: glucosidase activity
    examples:
    - value: 5 mol per liter per hour
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - glucosidase activity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000137
    multivalued: false
    alias: glucosidase_act
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  gravidity:
    name: gravidity
    annotations:
      expected_value:
        tag: expected_value
        value: gravidity status;timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: Whether or not subject is gravid, and if yes date due or date post-conception,
      specifying which is used
    title: gravidity
    examples:
    - value: yes;due date:2018-05-11
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - gravidity
    rank: 1000
    is_a: core field
    string_serialization: '{boolean};{timestamp}'
    slot_uri: MIXS:0000875
    multivalued: false
    alias: gravidity
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  gravity:
    name: gravity
    annotations:
      expected_value:
        tag: expected_value
        value: gravity factor value;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: meter per square second, g
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of gravity factor to study
      various types of responses in presence, absence or modified levels of gravity;
      treatment regimen including how many times the treatment was repeated, how long
      each treatment lasted, and the start and end time of the entire treatment; can
      include multiple treatments
    title: gravity
    examples:
    - value: 12 g;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - gravity
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000559
    multivalued: true
    alias: gravity
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  growth_facil:
    name: growth_facil
    annotations:
      expected_value:
        tag: expected_value
        value: free text or CO
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Type of facility where the sampled plant was grown; controlled vocabulary:
      growth chamber, open top chamber, glasshouse, experimental garden, field. Alternatively
      use Crop Ontology (CO) terms, see http://www.cropontology.org/ontology/CO_715/Crop%20Research'
    title: growth facility
    examples:
    - value: Growth chamber [CO_715:0000189]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - growth facility
    rank: 1000
    is_a: core field
    string_serialization: '{text}|{termLabel} {[termID]}'
    slot_uri: MIXS:0001043
    multivalued: false
    alias: growth_facil
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  growth_habit:
    name: growth_habit
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Characteristic shape, appearance or growth form of a plant species
    title: growth habit
    examples:
    - value: spreading
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - growth habit
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001044
    multivalued: false
    alias: growth_habit
    owner: Biosample
    domain_of:
    - Biosample
    range: growth_habit_enum
  growth_hormone_regm:
    name: growth_hormone_regm
    annotations:
      expected_value:
        tag: expected_value
        value: growth hormone name;growth hormone amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of growth hormones; should
      include the name of growth hormone, amount administered, treatment regimen including
      how many times the treatment was repeated, how long each treatment lasted, and
      the start and end time of the entire treatment; can include multiple growth
      hormone regimens
    title: growth hormone regimen
    examples:
    - value: abscisic acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - growth hormone regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000560
    multivalued: true
    alias: growth_hormone_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  hall_count:
    name: hall_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The total count of hallways and cooridors in the built structure
    title: hallway/corridor count
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hallway/corridor count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000228
    multivalued: false
    alias: hall_count
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  handidness:
    name: handidness
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The handidness of the individual sampled
    title: handidness
    examples:
    - value: right handedness
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - handidness
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000809
    multivalued: false
    alias: handidness
    owner: Biosample
    domain_of:
    - Biosample
    range: handidness_enum
  has numeric value:
    name: has numeric value
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: has_numeric_value
    owner: Biosample
    domain_of:
    - Biosample
    range: double
  has raw value:
    name: has raw value
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    string_serialization: '{has numeric value} {has unit}'
    alias: has_raw_value
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  has unit:
    name: has unit
    description: Example "m"
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: has_unit
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  hc_produced:
    name: hc_produced
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Main hydrocarbon type produced from resource (i.e. Oil, gas, condensate,
      etc). If "other" is specified, please propose entry in "additional info" field
    title: hydrocarbon type produced
    examples:
    - value: Gas
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hydrocarbon type produced
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000989
    multivalued: false
    alias: hc_produced
    owner: Biosample
    domain_of:
    - Biosample
    range: hc_produced_enum
  hcr:
    name: hcr
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Main Hydrocarbon Resource type. The term "Hydrocarbon Resource" HCR
      defined as a natural environmental feature containing large amounts of hydrocarbons
      at high concentrations potentially suitable for commercial exploitation. This
      term should not be confused with the Hydrocarbon Occurrence term which also
      includes hydrocarbon-rich environments with currently limited commercial interest
      such as seeps, outcrops, gas hydrates etc. If "other" is specified, please propose
      entry in "additional info" field
    title: hydrocarbon resource type
    examples:
    - value: Oil Sand
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hydrocarbon resource type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000988
    multivalued: false
    alias: hcr
    owner: Biosample
    domain_of:
    - Biosample
    range: hcr_enum
  hcr_fw_salinity:
    name: hcr_fw_salinity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Original formation water salinity (prior to secondary recovery e.g.
      Waterflooding) expressed as TDS
    title: formation water salinity
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - formation water salinity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000406
    multivalued: false
    alias: hcr_fw_salinity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  hcr_geol_age:
    name: hcr_geol_age
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Geological age of hydrocarbon resource (Additional info: https://en.wikipedia.org/wiki/Period_(geology)).
      If "other" is specified, please propose entry in "additional info" field'
    title: hydrocarbon resource geological age
    examples:
    - value: Silurian
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hydrocarbon resource geological age
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000993
    multivalued: false
    alias: hcr_geol_age
    owner: Biosample
    domain_of:
    - Biosample
    range: hcr_geol_age_enum
  hcr_pressure:
    name: hcr_pressure
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value range
      preferred_unit:
        tag: preferred_unit
        value: atmosphere, kilopascal
      occurrence:
        tag: occurrence
        value: '1'
    description: Original pressure of the hydrocarbon resource
    title: hydrocarbon resource original pressure
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hydrocarbon resource original pressure
    rank: 1000
    is_a: core field
    string_serialization: '{float} - {float} {unit}'
    slot_uri: MIXS:0000395
    multivalued: false
    alias: hcr_pressure
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  hcr_temp:
    name: hcr_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value range
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Original temperature of the hydrocarbon resource
    title: hydrocarbon resource original temperature
    examples:
    - value: 150-295 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - hydrocarbon resource original temperature
    rank: 1000
    is_a: core field
    string_serialization: '{float} - {float} {unit}'
    slot_uri: MIXS:0000393
    multivalued: false
    alias: hcr_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  heat_cool_type:
    name: heat_cool_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: Methods of conditioning or heating a room or building
    title: heating and cooling system type
    examples:
    - value: heat pump
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - heating and cooling system type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000766
    multivalued: true
    alias: heat_cool_type
    owner: Biosample
    domain_of:
    - Biosample
    range: heat_cool_type_enum
  heat_deliv_loc:
    name: heat_deliv_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The location of heat delivery within the room
    title: heating delivery locations
    examples:
    - value: north
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - heating delivery locations
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000810
    multivalued: false
    alias: heat_deliv_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: heat_deliv_loc_enum
  heat_sys_deliv_meth:
    name: heat_sys_deliv_meth
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The method by which the heat is delivered through the system
    title: heating system delivery method
    examples:
    - value: radiant
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - heating system delivery method
    rank: 1000
    is_a: core field
    string_serialization: '[conductive|radiant]'
    slot_uri: MIXS:0000812
    multivalued: false
    alias: heat_sys_deliv_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  heat_system_id:
    name: heat_system_id
    annotations:
      expected_value:
        tag: expected_value
        value: unique identifier
      occurrence:
        tag: occurrence
        value: '1'
    description: The heating system identifier
    title: heating system identifier
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - heating system identifier
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000833
    multivalued: false
    alias: heat_system_id
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  heavy_metals:
    name: heavy_metals
    description: Heavy metals present in the sample and their concentrations.
    title: heavy metals/ extreme unusual properties
    todos:
    - Example & validation. Can we configure things so that 27% & 27 % & 0.27 will
      validate?
    - I think it's weird the way GSC writes the title. I recommend this change. Thoughts?
      I would argue this isn't an extreme unusual property. It's just a biogeochemical
      measurement.
    comments:
    - For multiple heavy metals and concentrations, separate by ;
    examples:
    - value: mercury 0.09 micrograms per gram
    - value: mercury 0.09 ug/g; chromium 0.03 ug/g
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000652
    multivalued: true
    alias: heavy_metals
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  heavy_metals_meth:
    name: heavy_metals_meth
    description: Reference or method used in determining heavy metals
    title: heavy metals method/ extreme unusual properties
    comments:
    - Required when heavy metals are provided
    - If different methods are used for multiple metals, indicate the metal and method.
      Separate metals by ;
    examples:
    - value: https://doi.org/10.3390/ijms9040434
    - value: mercury https://doi.org/10.1007/BF01056090; chromium https://doi.org/10.1007/s00216-006-0322-8
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000343
    multivalued: true
    alias: heavy_metals_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  height_carper_fiber:
    name: height_carper_fiber
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: centimeter
      occurrence:
        tag: occurrence
        value: '1'
    description: The average carpet fiber height in the indoor environment
    title: height carpet fiber mat
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - height carpet fiber mat
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000167
    multivalued: false
    alias: height_carper_fiber
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  herbicide_regm:
    name: herbicide_regm
    annotations:
      expected_value:
        tag: expected_value
        value: herbicide name;herbicide amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of herbicides; information
      about treatment involving use of growth hormones; should include the name of
      herbicide, amount administered, treatment regimen including how many times the
      treatment was repeated, how long each treatment lasted, and the start and end
      time of the entire treatment; can include multiple regimens
    title: herbicide regimen
    examples:
    - value: atrazine;10 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - herbicide regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000561
    multivalued: true
    alias: herbicide_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  horizon_meth:
    name: horizon_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining the horizon
    title: soil horizon method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil horizon method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000321
    multivalued: false
    alias: horizon_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_age:
    name: host_age
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: year, day, hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Age of host at the time of sampling; relevant scale depends on species
      and study, e.g. Could be seconds for amoebae or centuries for trees
    title: host age
    examples:
    - value: 10 days
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host age
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000255
    multivalued: false
    alias: host_age
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_body_habitat:
    name: host_body_habitat
    annotations:
      expected_value:
        tag: expected_value
        value: free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Original body habitat where the sample was obtained from
    title: host body habitat
    examples:
    - value: nasopharynx
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host body habitat
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000866
    multivalued: false
    alias: host_body_habitat
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_body_product:
    name: host_body_product
    annotations:
      expected_value:
        tag: expected_value
        value: FMA or UBERON
      occurrence:
        tag: occurrence
        value: '1'
    description: Substance produced by the body, e.g. Stool, mucus, where the sample
      was obtained from. For foundational model of anatomy ontology (fma) or Uber-anatomy
      ontology (UBERON) terms, please see https://www.ebi.ac.uk/ols/ontologies/fma
      or https://www.ebi.ac.uk/ols/ontologies/uberon
    title: host body product
    examples:
    - value: Portion of mucus [fma66938]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host body product
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000888
    multivalued: false
    alias: host_body_product
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  host_body_site:
    name: host_body_site
    annotations:
      expected_value:
        tag: expected_value
        value: FMA or UBERON
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of body site where the sample was obtained from, such as a specific
      organ or tissue (tongue, lung etc...). For foundational model of anatomy ontology
      (fma) (v 4.11.0) or Uber-anatomy ontology (UBERON) (v releases/2014-06-15) terms,
      please see http://purl.bioontology.org/ontology/FMA or http://purl.bioontology.org/ontology/UBERON
    title: host body site
    examples:
    - value: gill [UBERON:0002535]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host body site
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000867
    multivalued: false
    alias: host_body_site
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  host_body_temp:
    name: host_body_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Core body temperature of the host when sample was collected
    title: host body temperature
    examples:
    - value: 15 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host body temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000274
    multivalued: false
    alias: host_body_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_color:
    name: host_color
    annotations:
      expected_value:
        tag: expected_value
        value: color
      occurrence:
        tag: occurrence
        value: '1'
    description: The color of host
    title: host color
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host color
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000260
    multivalued: false
    alias: host_color
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_common_name:
    name: host_common_name
    annotations:
      expected_value:
        tag: expected_value
        value: common name
      occurrence:
        tag: occurrence
        value: '1'
    description: Common name of the host.
    title: host common name
    examples:
    - value: human
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host common name
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000248
    multivalued: false
    alias: host_common_name
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_diet:
    name: host_diet
    annotations:
      expected_value:
        tag: expected_value
        value: diet type
      occurrence:
        tag: occurrence
        value: m
    description: Type of diet depending on the host, for animals omnivore, herbivore
      etc., for humans high-fat, meditteranean etc.; can include multiple diet types
    title: host diet
    examples:
    - value: herbivore
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host diet
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000869
    multivalued: true
    alias: host_diet
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_dry_mass:
    name: host_dry_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: kilogram, gram
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of dry mass
    title: host dry mass
    examples:
    - value: 500 gram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host dry mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000257
    multivalued: false
    alias: host_dry_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_family_relation:
    name: host_family_relation
    annotations:
      expected_value:
        tag: expected_value
        value: relationship type;arbitrary identifier
      occurrence:
        tag: occurrence
        value: m
    description: Familial relationships to other hosts in the same study; can include
      multiple relationships
    title: host family relationship
    examples:
    - value: offspring;Mussel25
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host family relationship
    rank: 1000
    is_a: core field
    string_serialization: '{text};{text}'
    slot_uri: MIXS:0000872
    multivalued: true
    alias: host_family_relation
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  host_genotype:
    name: host_genotype
    annotations:
      expected_value:
        tag: expected_value
        value: genotype
      occurrence:
        tag: occurrence
        value: '1'
    description: Observed genotype
    title: host genotype
    examples:
    - value: C57BL/6
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host genotype
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000365
    multivalued: false
    alias: host_genotype
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_growth_cond:
    name: host_growth_cond
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI,url or free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Literature reference giving growth conditions of the host
    title: host growth conditions
    examples:
    - value: https://academic.oup.com/icesjms/article/68/2/349/617247
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host growth conditions
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}|{text}'
    slot_uri: MIXS:0000871
    multivalued: false
    alias: host_growth_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_height:
    name: host_height
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: centimeter, millimeter, meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The height of subject
    title: host height
    examples:
    - value: 0.1 meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host height
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000264
    multivalued: false
    alias: host_height
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_last_meal:
    name: host_last_meal
    annotations:
      expected_value:
        tag: expected_value
        value: content;duration
      occurrence:
        tag: occurrence
        value: m
    description: Content of last meal and time since feeding; can include multiple
      values
    title: host last meal
    examples:
    - value: corn feed;P2H
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host last meal
    rank: 1000
    is_a: core field
    string_serialization: '{text};{duration}'
    slot_uri: MIXS:0000870
    multivalued: true
    alias: host_last_meal
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_length:
    name: host_length
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: centimeter, millimeter, meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The length of subject
    title: host length
    examples:
    - value: 1 meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host length
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000256
    multivalued: false
    alias: host_length
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_life_stage:
    name: host_life_stage
    annotations:
      expected_value:
        tag: expected_value
        value: stage
      occurrence:
        tag: occurrence
        value: '1'
    description: Description of life stage of host
    title: host life stage
    examples:
    - value: adult
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host life stage
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000251
    multivalued: false
    alias: host_life_stage
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_phenotype:
    name: host_phenotype
    annotations:
      expected_value:
        tag: expected_value
        value: PATO or HP
      occurrence:
        tag: occurrence
        value: '1'
    description: Phenotype of human or other host. For phenotypic quality ontology
      (pato) (v 2018-03-27) terms, please see http://purl.bioontology.org/ontology/pato.
      For Human Phenotype Ontology (HP) (v 2018-06-13) please see http://purl.bioontology.org/ontology/HP
    title: host phenotype
    examples:
    - value: elongated [PATO:0001154]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host phenotype
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000874
    multivalued: false
    alias: host_phenotype
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  host_sex:
    name: host_sex
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Gender or physical sex of the host.
    title: host sex
    examples:
    - value: non-binary
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host sex
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000811
    multivalued: false
    alias: host_sex
    owner: Biosample
    domain_of:
    - Biosample
    range: host_sex_enum
  host_shape:
    name: host_shape
    annotations:
      expected_value:
        tag: expected_value
        value: shape
      occurrence:
        tag: occurrence
        value: '1'
    description: Morphological shape of host
    title: host shape
    examples:
    - value: round
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host shape
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000261
    multivalued: false
    alias: host_shape
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_subject_id:
    name: host_subject_id
    annotations:
      expected_value:
        tag: expected_value
        value: unique identifier
      occurrence:
        tag: occurrence
        value: '1'
    description: A unique identifier by which each subject can be referred to, de-identified.
    title: host subject id
    examples:
    - value: MPI123
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host subject id
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000861
    multivalued: false
    alias: host_subject_id
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_subspecf_genlin:
    name: host_subspecf_genlin
    annotations:
      expected_value:
        tag: expected_value
        value: Genetic lineage below lowest rank of NCBI taxonomy, which is subspecies,
          e.g. serovar, biotype, ecotype, variety, cultivar.
      occurrence:
        tag: occurrence
        value: m
    description: Information about the genetic distinctness of the host organism below
      the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar,
      or any relevant genetic typing schemes like Group I plasmid. Subspecies should
      not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage
      name and the lineage rank separated by a colon, e.g., biovar:abc123.
    title: host subspecific genetic lineage
    examples:
    - value: 'serovar:Newport, variety:glabrum, cultivar: Red Delicious'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host subspecific genetic lineage
    rank: 1000
    is_a: core field
    string_serialization: '{rank name}:{text}'
    slot_uri: MIXS:0001318
    multivalued: true
    alias: host_subspecf_genlin
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  host_substrate:
    name: host_substrate
    annotations:
      expected_value:
        tag: expected_value
        value: substrate name
      occurrence:
        tag: occurrence
        value: '1'
    description: The growth substrate of the host.
    title: host substrate
    examples:
    - value: rock
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host substrate
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000252
    multivalued: false
    alias: host_substrate
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  host_symbiont:
    name: host_symbiont
    annotations:
      expected_value:
        tag: expected_value
        value: species name or common name
      occurrence:
        tag: occurrence
        value: m
    description: The taxonomic name of the organism(s) found living in mutualistic,
      commensalistic, or parasitic symbiosis with the specific host.
    title: observed host symbionts
    examples:
    - value: flukeworms
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - observed host symbionts
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0001298
    multivalued: true
    alias: host_symbiont
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  host_tot_mass:
    name: host_tot_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: kilogram, gram
      occurrence:
        tag: occurrence
        value: '1'
    description: Total mass of the host at collection, the unit depends on host
    title: host total mass
    examples:
    - value: 2500 gram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host total mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000263
    multivalued: false
    alias: host_tot_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  host_wet_mass:
    name: host_wet_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: kilogram, gram
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of wet mass
    title: host wet mass
    examples:
    - value: 1500 gram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - host wet mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000567
    multivalued: false
    alias: host_wet_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  humidity:
    name: humidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram per cubic meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Amount of water vapour in the air, at the time of sampling
    title: humidity
    examples:
    - value: 25 gram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000100
    multivalued: false
    alias: humidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  humidity_regm:
    name: humidity_regm
    annotations:
      expected_value:
        tag: expected_value
        value: humidity value;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram per cubic meter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving an exposure to varying degree
      of humidity; information about treatment involving use of growth hormones; should
      include amount of humidity administered, treatment regimen including how many
      times the treatment was repeated, how long each treatment lasted, and the start
      and end time of the entire treatment; can include multiple regimens
    title: humidity regimen
    examples:
    - value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - humidity regimen
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000568
    multivalued: true
    alias: humidity_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  indoor_space:
    name: indoor_space
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: A distinguishable space within a structure, the purpose for which
      discrete areas of a building is used
    title: indoor space
    examples:
    - value: foyer
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - indoor space
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000763
    multivalued: false
    alias: indoor_space
    owner: Biosample
    domain_of:
    - Biosample
    range: indoor_space_enum
  indoor_surf:
    name: indoor_surf
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Type of indoor surface
    title: indoor surface
    examples:
    - value: wall
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - indoor surface
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000764
    multivalued: false
    alias: indoor_surf
    owner: Biosample
    domain_of:
    - Biosample
    range: indoor_surf_enum
  indust_eff_percent:
    name: indust_eff_percent
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: percentage
      occurrence:
        tag: occurrence
        value: '1'
    description: Percentage of industrial effluents received by wastewater treatment
      plant
    title: industrial effluent percent
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - industrial effluent percent
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000662
    multivalued: false
    alias: indust_eff_percent
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  inorg_particles:
    name: inorg_particles
    annotations:
      expected_value:
        tag: expected_value
        value: inorganic particle name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of particles such as sand, grit, metal particles, ceramics,
      etc.; can include multiple particles
    title: inorganic particles
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - inorganic particles
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000664
    multivalued: true
    alias: inorg_particles
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  inside_lux:
    name: inside_lux
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: kilowatt per square metre
      occurrence:
        tag: occurrence
        value: '1'
    description: The recorded value at sampling time (power density)
    title: inside lux light
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - inside lux light
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000168
    multivalued: false
    alias: inside_lux
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  int_wall_cond:
    name: int_wall_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The physical condition of the wall at the time of sampling; photos
      or video preferred; use drawings to indicate location of damaged areas
    title: interior wall condition
    examples:
    - value: damaged
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - interior wall condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000813
    multivalued: false
    alias: int_wall_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: int_wall_cond_enum
  investigation field:
    name: investigation field
    description: field describing aspect of the investigation/study to which the sample
      belongs
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    abstract: true
    alias: investigation_field
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  iw_bt_date_well:
    name: iw_bt_date_well
    annotations:
      expected_value:
        tag: expected_value
        value: timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: Injection water breakthrough date per well following a secondary
      and/or tertiary recovery
    title: injection water breakthrough date of specific well
    examples:
    - value: '2018-05-11'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - injection water breakthrough date of specific well
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001010
    multivalued: false
    alias: iw_bt_date_well
    owner: Biosample
    domain_of:
    - Biosample
    range: TimestampValue
  iwf:
    name: iwf
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: Proportion of the produced fluids derived from injected water at
      the time of sampling. (e.g. 87%)
    title: injection water fraction
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - injection water fraction
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000455
    multivalued: false
    alias: iwf
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  last_clean:
    name: last_clean
    annotations:
      expected_value:
        tag: expected_value
        value: timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: The last time the floor was cleaned (swept, mopped, vacuumed)
    title: last time swept/mopped/vacuumed
    examples:
    - value: 2018-05-11:T14:30Z
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - last time swept/mopped/vacuumed
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000814
    multivalued: false
    alias: last_clean
    owner: Biosample
    domain_of:
    - Biosample
    range: TimestampValue
  lat_lon:
    name: lat_lon
    description: The geographical origin of the sample as defined by latitude and
      longitude. The values should be reported in decimal degrees and in WGS84 system
    title: geographic location (latitude and longitude)
    notes:
    - This is currently a required field but it's not clear if this should be required
      for human hosts
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: environment field
    string_serialization: '{float} {float}'
    slot_uri: MIXS:0000009
    multivalued: false
    alias: lat_lon
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: GeolocationValue
  lbc_thirty:
    name: lbc_thirty
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: ppm CaCO3/pH
      occurrence:
        tag: occurrence
        value: '1'
    description: lime buffer capacity, determined after 30 minute incubation
    title: lime buffer capacity (at 30 minutes)
    comments:
    - This is the mass of lime, in mg, needed to raise the pH of one kg of soil by
      one pH unit
    examples:
    - value: 543 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    - https://secure.caes.uga.edu/extension/publications/files/pdf/C%20874_5.PDF
    aliases:
    - lbc_thirty
    - lbc30
    - lime buffer capacity (at 30 minutes)
    rank: 1000
    alias: lbc_thirty
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  lbceq:
    name: lbceq
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: ppm CaCO3/pH
      occurrence:
        tag: occurrence
        value: '1'
    description: lime buffer capacity, determined at equilibrium after 5 day incubation
    title: lime buffer capacity (after 5 day incubation)
    comments:
    - This is the mass of lime, in mg, needed to raise the pH of one kg of soil by
      one pH unit
    examples:
    - value: 1575 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - lbceq
    - lime buffer capacity (at 5-day equilibrium)
    rank: 1000
    alias: lbceq
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  light_intensity:
    name: light_intensity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: lux
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of light intensity
    title: light intensity
    examples:
    - value: 0.3 lux
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - light intensity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000706
    multivalued: false
    alias: light_intensity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  light_regm:
    name: light_regm
    annotations:
      expected_value:
        tag: expected_value
        value: exposure type;light intensity;light quality
      preferred_unit:
        tag: preferred_unit
        value: lux; micrometer, nanometer, angstrom
      occurrence:
        tag: occurrence
        value: '1'
    description: Information about treatment(s) involving exposure to light, including
      both light intensity and quality.
    title: light regimen
    examples:
    - value: incandescant light;10 lux;450 nanometer
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - light regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{float} {unit}'
    slot_uri: MIXS:0000569
    multivalued: false
    alias: light_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  light_type:
    name: light_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: Application of light to achieve some practical or aesthetic effect.
      Lighting includes the use of both artificial light sources such as lamps and
      light fixtures, as well as natural illumination by capturing daylight. Can also
      include absence of light
    title: light type
    examples:
    - value: desk lamp
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - light type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000769
    multivalued: true
    alias: light_type
    owner: Biosample
    domain_of:
    - Biosample
    range: light_type_enum
  link_addit_analys:
    name: link_addit_analys
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Link to additional analysis results performed on the sample
    title: links to additional analysis
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - links to additional analysis
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000340
    multivalued: false
    alias: link_addit_analys
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  link_class_info:
    name: link_class_info
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Link to digitized soil maps or other soil classification information
    title: link to classification information
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - link to classification information
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000329
    multivalued: false
    alias: link_class_info
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  link_climate_info:
    name: link_climate_info
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Link to climate resource
    title: link to climate information
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - link to climate information
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000328
    multivalued: false
    alias: link_climate_info
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  lithology:
    name: lithology
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination).
      If "other" is specified, please propose entry in "additional info" field'
    title: lithology
    examples:
    - value: Volcanic
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - lithology
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000990
    multivalued: false
    alias: lithology
    owner: Biosample
    domain_of:
    - Biosample
    range: lithology_enum
  local_class:
    name: local_class
    annotations:
      expected_value:
        tag: expected_value
        value: local classification name
      occurrence:
        tag: occurrence
        value: '1'
    description: Soil classification based on local soil classification system
    title: soil_taxonomic/local classification
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil_taxonomic/local classification
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000330
    multivalued: false
    alias: local_class
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: TextValue
  local_class_meth:
    name: local_class_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining the local soil classification
    title: soil_taxonomic/local classification method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil_taxonomic/local classification method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000331
    multivalued: false
    alias: local_class_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  magnesium:
    name: magnesium
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mole per liter, milligram per liter, parts per million, micromole per
          kilogram
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of magnesium in the sample
    title: magnesium
    examples:
    - value: 52.8 micromole per kilogram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - magnesium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000431
    multivalued: false
    alias: magnesium
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  manganese:
    name: manganese
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mg/kg (ppm)
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of manganese in the sample
    title: manganese
    examples:
    - value: 24.7 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - manganese
    rank: 1000
    alias: manganese
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  max_occup:
    name: max_occup
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The maximum amount of people allowed in the indoor environment
    title: maximum occupancy
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - maximum occupancy
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000229
    multivalued: false
    alias: max_occup
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  mean_frict_vel:
    name: mean_frict_vel
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter per second
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of mean friction velocity
    title: mean friction velocity
    examples:
    - value: 0.5 meter per second
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mean friction velocity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000498
    multivalued: false
    alias: mean_frict_vel
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  mean_peak_frict_vel:
    name: mean_peak_frict_vel
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter per second
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of mean peak friction velocity
    title: mean peak friction velocity
    examples:
    - value: 1 meter per second
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mean peak friction velocity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000502
    multivalued: false
    alias: mean_peak_frict_vel
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  mech_struc:
    name: mech_struc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'mechanical structure: a moving structure'
    title: mechanical structure
    examples:
    - value: elevator
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mechanical structure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000815
    multivalued: false
    alias: mech_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: mech_struc_enum
  mechanical_damage:
    name: mechanical_damage
    annotations:
      expected_value:
        tag: expected_value
        value: damage type;body site
      occurrence:
        tag: occurrence
        value: m
    description: Information about any mechanical damage exerted on the plant; can
      include multiple damages and sites
    title: mechanical damage
    examples:
    - value: pruning;bark
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mechanical damage
    rank: 1000
    is_a: core field
    string_serialization: '{text};{text}'
    slot_uri: MIXS:0001052
    multivalued: true
    alias: mechanical_damage
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  methane:
    name: methane
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, parts per billion, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Methane (gas) amount or concentration at the time of sampling
    title: methane
    examples:
    - value: 1800 parts per billion
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - methane
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000101
    multivalued: false
    alias: methane
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  micro_biomass_meth:
    name: micro_biomass_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining microbial biomass
    title: microbial biomass method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - microbial biomass method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000339
    multivalued: false
    alias: micro_biomass_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  microbial_biomass:
    name: microbial_biomass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: ton, kilogram, gram per kilogram soil
      occurrence:
        tag: occurrence
        value: '1'
    description: The part of the organic matter in the soil that constitutes living
      microorganisms smaller than 5-10 micrometer. If you keep this, you would need
      to have correction factors used for conversion to the final units
    title: microbial biomass
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - microbial biomass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000650
    multivalued: false
    alias: microbial_biomass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  mineral_nutr_regm:
    name: mineral_nutr_regm
    annotations:
      expected_value:
        tag: expected_value
        value: mineral nutrient name;mineral nutrient amount;treatment interval and
          duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving the use of mineral supplements;
      should include the name of mineral nutrient, amount administered, treatment
      regimen including how many times the treatment was repeated, how long each treatment
      lasted, and the start and end time of the entire treatment; can include multiple
      mineral nutrient regimens
    title: mineral nutrient regimen
    examples:
    - value: potassium;15 gram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mineral nutrient regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000570
    multivalued: true
    alias: mineral_nutr_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  misc_param:
    name: misc_param
    annotations:
      expected_value:
        tag: expected_value
        value: parameter name;measurement value
      occurrence:
        tag: occurrence
        value: m
    description: Any other measurement performed or parameter collected, that is not
      listed here
    title: miscellaneous parameter
    examples:
    - value: Bicarbonate ion concentration;2075 micromole per kilogram
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - miscellaneous parameter
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000752
    multivalued: true
    alias: misc_param
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  n_alkanes:
    name: n_alkanes
    annotations:
      expected_value:
        tag: expected_value
        value: n-alkane name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of n-alkanes; can include multiple n-alkanes
    title: n-alkanes
    examples:
    - value: n-hexadecane;100 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - n-alkanes
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000503
    multivalued: true
    alias: n_alkanes
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  nitrate:
    name: nitrate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of nitrate in the sample
    title: nitrate
    examples:
    - value: 65 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - nitrate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000425
    multivalued: false
    alias: nitrate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  nitrate_nitrogen:
    name: nitrate_nitrogen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mg/kg
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of nitrate nitrogen in the sample
    title: nitrate_nitrogen
    comments:
    - often below some specified limit of detection
    examples:
    - value: 0.29 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - nitrate_nitrogen
    - NO3-N
    rank: 1000
    alias: nitrate_nitrogen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  nitrite:
    name: nitrite
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of nitrite in the sample
    title: nitrite
    examples:
    - value: 0.5 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - nitrite
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000426
    multivalued: false
    alias: nitrite
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  nitrite_nitrogen:
    name: nitrite_nitrogen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mg/kg
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of nitrite nitrogen in the sample
    title: nitrite_nitrogen
    examples:
    - value: 1.2 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - nitrite_nitrogen
    - NO2-N
    rank: 1000
    alias: nitrite_nitrogen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  nitro:
    name: nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of nitrogen (total)
    title: nitrogen
    examples:
    - value: 4.2 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000504
    multivalued: false
    alias: nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  non_min_nutr_regm:
    name: non_min_nutr_regm
    annotations:
      expected_value:
        tag: expected_value
        value: non-mineral nutrient name;non-mineral nutrient amount;treatment interval
          and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving the exposure of plant to non-mineral
      nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral
      nutrient, amount administered, treatment regimen including how many times the
      treatment was repeated, how long each treatment lasted, and the start and end
      time of the entire treatment; can include multiple non-mineral nutrient regimens
    title: non-mineral nutrient regimen
    examples:
    - value: carbon dioxide;10 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - non-mineral nutrient regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000571
    multivalued: true
    alias: non_min_nutr_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  nucl_acid_amp:
    name: nucl_acid_amp
    annotations:
      expected_value:
        tag: expected_value
        value: PMID, DOI or URL
    description: A link to a literature reference, electronic resource or a standard
      operating procedure (SOP), that describes the enzymatic amplification (PCR,
      TMA, NASBA) of specific nucleic acids
    title: nucleic acid amplification
    examples:
    - value: https://phylogenomics.me/protocols/16s-pcr-protocol/
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - nucleic acid amplification
    rank: 1000
    is_a: sequencing field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000038
    multivalued: false
    alias: nucl_acid_amp
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  nucl_acid_ext:
    name: nucl_acid_ext
    annotations:
      expected_value:
        tag: expected_value
        value: PMID, DOI or URL
    description: A link to a literature reference, electronic resource or a standard
      operating procedure (SOP), that describes the material separation to recover
      the nucleic acid fraction from a sample
    title: nucleic acid extraction
    examples:
    - value: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - nucleic acid extraction
    rank: 1000
    is_a: sequencing field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000037
    multivalued: false
    alias: nucl_acid_ext
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  nucleic acid sequence source field:
    name: nucleic acid sequence source field
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    abstract: true
    alias: nucleic_acid_sequence_source_field
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  number_pets:
    name: number_pets
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of pets residing in the sampled space
    title: number of pets
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - number of pets
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000231
    multivalued: false
    alias: number_pets
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  number_plants:
    name: number_plants
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of plant(s) in the sampling space
    title: number of houseplants
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - number of houseplants
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000230
    multivalued: false
    alias: number_plants
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  number_resident:
    name: number_resident
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of individuals currently occupying in the sampling location
    title: number of residents
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - number of residents
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000232
    multivalued: false
    alias: number_resident
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  occup_density_samp:
    name: occup_density_samp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Average number of occupants at time of sampling per square footage
    title: occupant density at sampling
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - occupant density at sampling
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000217
    multivalued: false
    alias: occup_density_samp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  occup_document:
    name: occup_document
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of documentation of occupancy
    title: occupancy documentation
    examples:
    - value: estimate
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - occupancy documentation
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000816
    multivalued: false
    alias: occup_document
    owner: Biosample
    domain_of:
    - Biosample
    range: occup_document_enum
  occup_samp:
    name: occup_samp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Number of occupants present at time of sample within the given space
    title: occupancy at sampling
    examples:
    - value: '10'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - occupancy at sampling
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000772
    multivalued: false
    alias: occup_samp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  org_carb:
    name: org_carb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of organic carbon
    title: organic carbon
    examples:
    - value: 1.5 microgram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organic carbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000508
    multivalued: false
    alias: org_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  org_count_qpcr_info:
    name: org_count_qpcr_info
    annotations:
      expected_value:
        tag: expected_value
        value: gene name;FWD:forward primer sequence;REV:reverse primer sequence;initial
          denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
          elongation:degrees_minutes; total cycles
      preferred_unit:
        tag: preferred_unit
        value: number of cells per gram (or ml or cm^2)
      occurrence:
        tag: occurrence
        value: '1'
    description: 'If qpcr was used for the cell count, the target gene name, the primer
      sequence and the cycling conditions should also be provided. (Example: 16S rrna;
      FWD:ACGTAGCTATGACGT REV:GTGCTAGTCGAGTAC; initial denaturation:90C_5min; denaturation:90C_2min;
      annealing:52C_30 sec; elongation:72C_30 sec; 90 C for 1 min; final elongation:72C_5min;
      30 cycles)'
    title: organism count qPCR information
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organism count qPCR information
    rank: 1000
    is_a: core field
    string_serialization: '{text};FWD:{dna};REV:{dna};initial denaturation:degrees_minutes;denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
      elongation:degrees_minutes; total cycles'
    slot_uri: MIXS:0000099
    multivalued: false
    alias: org_count_qpcr_info
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  org_matter:
    name: org_matter
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of organic matter
    title: organic matter
    examples:
    - value: 1.75 milligram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organic matter
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000204
    multivalued: false
    alias: org_matter
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  org_nitro:
    name: org_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of organic nitrogen
    title: organic nitrogen
    examples:
    - value: 4 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organic nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000205
    multivalued: false
    alias: org_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  org_particles:
    name: org_particles
    annotations:
      expected_value:
        tag: expected_value
        value: particle name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of particles such as faeces, hairs, food, vomit, paper
      fibers, plant material, humus, etc.
    title: organic particles
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organic particles
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000665
    multivalued: true
    alias: org_particles
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  organism_count:
    name: organism_count
    annotations:
      expected_value:
        tag: expected_value
        value: organism name;measurement value;enumeration
      preferred_unit:
        tag: preferred_unit
        value: number of cells per cubic meter, number of cells per milliliter, number
          of cells per cubic centimeter
      occurrence:
        tag: occurrence
        value: m
    description: 'Total cell count of any organism (or group of organisms) per gram,
      volume or area of sample, should include name of organism followed by count.
      The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should
      also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr)'
    title: organism count
    examples:
    - value: total prokaryotes;3.5e7 cells per milliliter;qPCR
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - organism count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000103
    multivalued: true
    alias: organism_count
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  owc_tvdss:
    name: owc_tvdss
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Depth of the original oil water contact (OWC) zone (average) (m TVDSS)
    title: oil water contact depth
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - oil water contact depth
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000405
    multivalued: false
    alias: owc_tvdss
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  oxy_stat_samp:
    name: oxy_stat_samp
    description: Oxygenation status of sample
    title: oxygenation status of sample
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000753
    multivalued: false
    alias: oxy_stat_samp
    owner: Biosample
    domain_of:
    - Biosample
    range: oxy_stat_samp_enum
  oxygen:
    name: oxygen
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Oxygen (gas) amount or concentration at the time of sampling
    title: oxygen
    examples:
    - value: 600 parts per million
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - oxygen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000104
    multivalued: false
    alias: oxygen
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  part_org_carb:
    name: part_org_carb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of particulate organic carbon
    title: particulate organic carbon
    examples:
    - value: 1.92 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - particulate organic carbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000515
    multivalued: false
    alias: part_org_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  part_org_nitro:
    name: part_org_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of particulate organic nitrogen
    title: particulate organic nitrogen
    examples:
    - value: 0.3 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - particulate organic nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000719
    multivalued: false
    alias: part_org_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  particle_class:
    name: particle_class
    annotations:
      expected_value:
        tag: expected_value
        value: particle name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: micrometer
      occurrence:
        tag: occurrence
        value: m
    description: Particles are classified, based on their size, into six general categories:clay,
      silt, sand, gravel, cobbles, and boulders; should include amount of particle
      preceded by the name of the particle type; can include multiple values
    title: particle classification
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - particle classification
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000206
    multivalued: true
    alias: particle_class
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  pcr_cond:
    name: pcr_cond
    annotations:
      expected_value:
        tag: expected_value
        value: initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
          elongation:degrees_minutes;total cycles
    description: Description of reaction conditions and components of PCR in the form
      of 'initial denaturation:94degC_1.5min; annealing=...'
    title: pcr conditions
    examples:
    - value: initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pcr conditions
    rank: 1000
    is_a: sequencing field
    string_serialization: initial denaturation:degrees_minutes;annealing:degrees_minutes;elongation:degrees_minutes;final
      elongation:degrees_minutes;total cycles
    slot_uri: MIXS:0000049
    multivalued: false
    alias: pcr_cond
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  pcr_primers:
    name: pcr_primers
    annotations:
      expected_value:
        tag: expected_value
        value: 'FWD: forward primer sequence;REV:reverse primer sequence'
    description: PCR primers that were used to amplify the sequence of the targeted
      gene, locus or subfragment. This field should contain all the primers used for
      a single PCR reaction if multiple forward or reverse primers are present in
      a single PCR reaction. The primer sequence should be reported in uppercase letters
    title: pcr primers
    examples:
    - value: FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pcr primers
    rank: 1000
    is_a: sequencing field
    string_serialization: FWD:{dna};REV:{dna}
    slot_uri: MIXS:0000046
    multivalued: false
    alias: pcr_primers
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  permeability:
    name: permeability
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value range
      preferred_unit:
        tag: preferred_unit
        value: mD
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Measure of the ability of a hydrocarbon resource to allow fluids
      to pass through it. (Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences))'
    title: permeability
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - permeability
    rank: 1000
    is_a: core field
    string_serialization: '{integer} - {integer} {unit}'
    slot_uri: MIXS:0000404
    multivalued: false
    alias: permeability
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  perturbation:
    name: perturbation
    annotations:
      expected_value:
        tag: expected_value
        value: perturbation type name;perturbation interval and duration
      occurrence:
        tag: occurrence
        value: m
    description: Type of perturbation, e.g. chemical administration, physical disturbance,
      etc., coupled with perturbation regimen including how many times the perturbation
      was repeated, how long each perturbation lasted, and the start and end time
      of the entire perturbation period; can include multiple perturbation types
    title: perturbation
    examples:
    - value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - perturbation
    rank: 1000
    is_a: core field
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000754
    multivalued: true
    alias: perturbation
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  pesticide_regm:
    name: pesticide_regm
    annotations:
      expected_value:
        tag: expected_value
        value: pesticide name;pesticide amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of insecticides; should
      include the name of pesticide, amount administered, treatment regimen including
      how many times the treatment was repeated, how long each treatment lasted, and
      the start and end time of the entire treatment; can include multiple pesticide
      regimens
    title: pesticide regimen
    examples:
    - value: pyrethrum;0.6 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pesticide regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000573
    multivalued: true
    alias: pesticide_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  petroleum_hydrocarb:
    name: petroleum_hydrocarb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of petroleum hydrocarbon
    title: petroleum hydrocarbon
    examples:
    - value: 0.05 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - petroleum hydrocarbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000516
    multivalued: false
    alias: petroleum_hydrocarb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ph:
    name: ph
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Ph measurement of the sample, or liquid portion of sample, or aqueous
      phase of the fluid
    title: pH
    examples:
    - value: '7.2'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pH
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001001
    multivalued: false
    alias: ph
    owner: Biosample
    domain_of:
    - Biosample
    range: double
  ph_meth:
    name: ph_meth
    description: Reference or method used in determining ph
    title: pH method
    comments:
    - This can include a link to the instrument used or a citation for the method.
    examples:
    - value: https://www.southernlabware.com/pc9500-benchtop-ph-conductivity-meter-kit-ph-accuracy-2000mv-ph-range-2-000-to-20-000.html?gclid=Cj0KCQiAwJWdBhCYARIsAJc4idCO5vtvbVMf545fcvdROFqa6zjzNSoywNx6K4k9Coo9cCc2pybtvGsaAiR0EALw_wcB
    - value: https://doi.org/10.2136/sssabookser5.3.c16
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0001106
    multivalued: false
    alias: ph_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  ph_regm:
    name: ph_regm
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;treatment interval and duration
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving exposure of plants to varying
      levels of ph of the growth media, treatment regimen including how many times
      the treatment was repeated, how long each treatment lasted, and the start and
      end time of the entire treatment; can include multiple regimen
    title: pH regimen
    examples:
    - value: 7.6;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pH regimen
    rank: 1000
    is_a: core field
    string_serialization: '{float};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0001056
    multivalued: true
    alias: ph_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  phaeopigments:
    name: phaeopigments
    annotations:
      expected_value:
        tag: expected_value
        value: phaeopigment name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per cubic meter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of phaeopigments; can include multiple phaeopigments
    title: phaeopigments
    examples:
    - value: 2.5 milligram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - phaeopigments
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000180
    multivalued: true
    alias: phaeopigments
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  phosphate:
    name: phosphate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of phosphate
    title: phosphate
    examples:
    - value: 0.7 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - phosphate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000505
    multivalued: false
    alias: phosphate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  phosplipid_fatt_acid:
    name: phosplipid_fatt_acid
    annotations:
      expected_value:
        tag: expected_value
        value: phospholipid fatty acid name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: mole per gram, mole per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of phospholipid fatty acids; can include multiple values
    title: phospholipid fatty acid
    examples:
    - value: 2.98 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - phospholipid fatty acid
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000181
    multivalued: true
    alias: phosplipid_fatt_acid
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  photon_flux:
    name: photon_flux
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: number of photons per second per unit area
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of photon flux
    title: photon flux
    examples:
    - value: 3.926 micromole photons per second per square meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - photon flux
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000725
    multivalued: false
    alias: photon_flux
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  plant_growth_med:
    name: plant_growth_med
    annotations:
      expected_value:
        tag: expected_value
        value: EO or enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Specification of the media for growing the plants or tissue cultured
      samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in
      vitro liquid culture medium. Recommended value is a specific value from EO:plant
      growth medium (follow this link for terms http://purl.obolibrary.org/obo/EO_0007147)
      or other controlled vocabulary
    title: plant growth medium
    examples:
    - value: hydroponic plant culture media [EO:0007067]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - plant growth medium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001057
    multivalued: false
    alias: plant_growth_med
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  plant_product:
    name: plant_product
    annotations:
      expected_value:
        tag: expected_value
        value: product name
      occurrence:
        tag: occurrence
        value: '1'
    description: Substance produced by the plant, where the sample was obtained from
    title: plant product
    examples:
    - value: xylem sap [PO:0025539]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - plant product
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0001058
    multivalued: false
    alias: plant_product
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  plant_sex:
    name: plant_sex
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Sex of the reproductive parts on the whole plant, e.g. pistillate,
      staminate, monoecieous, hermaphrodite.
    title: plant sex
    examples:
    - value: Hermaphroditic
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - plant sex
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001059
    multivalued: false
    alias: plant_sex
    owner: Biosample
    domain_of:
    - Biosample
    range: plant_sex_enum
  plant_struc:
    name: plant_struc
    annotations:
      expected_value:
        tag: expected_value
        value: PO
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of plant structure the sample was obtained from; for Plant Ontology
      (PO) (v releases/2017-12-14) terms, see http://purl.bioontology.org/ontology/PO,
      e.g. petiole epidermis (PO_0000051). If an individual flower is sampled, the
      sex of it can be recorded here.
    title: plant structure
    examples:
    - value: epidermis [PO:0005679]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - plant structure
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0001060
    multivalued: false
    alias: plant_struc
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  pollutants:
    name: pollutants
    annotations:
      expected_value:
        tag: expected_value
        value: pollutant name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram, mole per liter, milligram per liter, microgram per cubic meter
      occurrence:
        tag: occurrence
        value: m
    description: Pollutant types and, amount or concentrations measured at the time
      of sampling; can report multiple pollutants by entering numeric values preceded
      by name of pollutant
    title: pollutants
    examples:
    - value: lead;0.15 microgram per cubic meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pollutants
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000107
    multivalued: true
    alias: pollutants
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  pool_dna_extracts:
    name: pool_dna_extracts
    annotations:
      expected_value:
        tag: expected_value
        value: pooling status;number of pooled extracts
      occurrence:
        tag: occurrence
        value: '1'
    description: Indicate whether multiple DNA extractions were mixed. If the answer
      yes, the number of extracts that were pooled should be given
    title: pooling of DNA extracts (if done)
    examples:
    - value: yes;5
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pooling of DNA extracts (if done)
    rank: 1000
    is_a: core field
    string_serialization: '{boolean};{integer}'
    slot_uri: MIXS:0000325
    multivalued: false
    alias: pool_dna_extracts
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  porosity:
    name: porosity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value or range
      preferred_unit:
        tag: preferred_unit
        value: percentage
      occurrence:
        tag: occurrence
        value: '1'
    description: Porosity of deposited sediment is volume of voids divided by the
      total volume of sample
    title: porosity
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - porosity
    rank: 1000
    is_a: core field
    string_serialization: '{float} - {float} {unit}'
    slot_uri: MIXS:0000211
    multivalued: false
    alias: porosity
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  potassium:
    name: potassium
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of potassium in the sample
    title: potassium
    examples:
    - value: 463 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - potassium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000430
    multivalued: false
    alias: potassium
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  pour_point:
    name: pour_point
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Temperature at which a liquid becomes semi solid and loses its flow
      characteristics. In crude oil a high¬†pour point¬†is generally associated with
      a high paraffin content, typically found in crude deriving from a larger proportion
      of plant material. (soure: https://en.wikipedia.org/wiki/pour_point)'
    title: pour point
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pour point
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000127
    multivalued: false
    alias: pour_point
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  pre_treatment:
    name: pre_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: pre-treatment type
      occurrence:
        tag: occurrence
        value: '1'
    description: The process of pre-treatment removes materials that can be easily
      collected from the raw wastewater
    title: pre-treatment
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pre-treatment
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000348
    multivalued: false
    alias: pre_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  pres_animal_insect:
    name: pres_animal_insect
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration;count
      occurrence:
        tag: occurrence
        value: '1'
    description: The type and number of animals or insects present in the sampling
      space.
    title: presence of pets, animals, or insects
    examples:
    - value: cat;5
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - presence of pets, animals, or insects
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000819
    multivalued: false
    alias: pres_animal_insect
    owner: Biosample
    domain_of:
    - Biosample
    range: string
    pattern: ^(cat|dog|rodent|snake|other);\d+$
  pressure:
    name: pressure
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: atmosphere
      occurrence:
        tag: occurrence
        value: '1'
    description: Pressure to which the sample is subject to, in atmospheres
    title: pressure
    examples:
    - value: 50 atmosphere
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - pressure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000412
    multivalued: false
    alias: pressure
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  prev_land_use_meth:
    name: prev_land_use_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining previous land use and dates
    title: history/previous land use method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - history/previous land use method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000316
    multivalued: false
    alias: prev_land_use_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  previous_land_use:
    name: previous_land_use
    annotations:
      expected_value:
        tag: expected_value
        value: land use name;date
      occurrence:
        tag: occurrence
        value: '1'
    description: Previous land use and dates
    title: history/previous land use
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - history/previous land use
    rank: 1000
    is_a: core field
    string_serialization: '{text};{timestamp}'
    slot_uri: MIXS:0000315
    multivalued: false
    alias: previous_land_use
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  primary_prod:
    name: primary_prod
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per cubic meter per day, gram per square meter per day
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of primary production, generally measured as isotope
      uptake
    title: primary production
    examples:
    - value: 100 milligram per cubic meter per day
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - primary production
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000728
    multivalued: false
    alias: primary_prod
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  primary_treatment:
    name: primary_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: primary treatment type
      occurrence:
        tag: occurrence
        value: '1'
    description: The process to produce both a generally homogeneous liquid capable
      of being treated biologically and a sludge that can be separately treated or
      processed
    title: primary treatment
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - primary treatment
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000349
    multivalued: false
    alias: primary_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  prod_rate:
    name: prod_rate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: cubic meter per day
      occurrence:
        tag: occurrence
        value: '1'
    description: Oil and/or gas production rates per well (e.g. 524 m3 / day)
    title: production rate
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - production rate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000452
    multivalued: false
    alias: prod_rate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  prod_start_date:
    name: prod_start_date
    annotations:
      expected_value:
        tag: expected_value
        value: timestamp
      occurrence:
        tag: occurrence
        value: '1'
    description: Date of field's first production
    title: production start date
    examples:
    - value: '2018-05-11'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - production start date
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001008
    multivalued: false
    alias: prod_start_date
    owner: Biosample
    domain_of:
    - Biosample
    range: TimestampValue
  profile_position:
    name: profile_position
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Cross-sectional position in the hillslope where sample was collected.sample
      area position in relation to surrounding areas
    title: profile position
    examples:
    - value: summit
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - profile position
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001084
    multivalued: false
    alias: profile_position
    owner: Biosample
    domain_of:
    - Biosample
    range: profile_position_enum
  quad_pos:
    name: quad_pos
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The quadrant position of the sampling room within the building
    title: quadrant position
    examples:
    - value: West side
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - quadrant position
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000820
    multivalued: false
    alias: quad_pos
    owner: Biosample
    domain_of:
    - Biosample
    range: quad_pos_enum
  radiation_regm:
    name: radiation_regm
    annotations:
      expected_value:
        tag: expected_value
        value: radiation type name;radiation amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: rad, gray
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving exposure of plant or a plant
      part to a particular radiation regimen; should include the radiation type, amount
      or intensity administered, treatment regimen including how many times the treatment
      was repeated, how long each treatment lasted, and the start and end time of
      the entire treatment; can include multiple radiation regimens
    title: radiation regimen
    examples:
    - value: gamma radiation;60 gray;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - radiation regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000575
    multivalued: true
    alias: radiation_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  rainfall_regm:
    name: rainfall_regm
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: millimeter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving an exposure to a given amount
      of rainfall, treatment regimen including how many times the treatment was repeated,
      how long each treatment lasted, and the start and end time of the entire treatment;
      can include multiple regimens
    title: rainfall regimen
    examples:
    - value: 15 millimeter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rainfall regimen
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000576
    multivalued: true
    alias: rainfall_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  reactor_type:
    name: reactor_type
    annotations:
      expected_value:
        tag: expected_value
        value: reactor type name
      occurrence:
        tag: occurrence
        value: '1'
    description: Anaerobic digesters can be designed and engineered to operate using
      a number of different process configurations, as batch or continuous, mesophilic,
      high solid or low solid, and single stage or multistage
    title: reactor type
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - reactor type
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000350
    multivalued: false
    alias: reactor_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  redox_potential:
    name: redox_potential
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millivolt
      occurrence:
        tag: occurrence
        value: '1'
    description: Redox potential, measured relative to a hydrogen cell, indicating
      oxidation or reduction potential
    title: redox potential
    examples:
    - value: 300 millivolt
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - redox potential
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000182
    multivalued: false
    alias: redox_potential
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  rel_air_humidity:
    name: rel_air_humidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: percentage
      occurrence:
        tag: occurrence
        value: '1'
    description: Partial vapor and air pressure, density of the vapor and air, or
      by the actual mass of the vapor and air
    title: relative air humidity
    examples:
    - value: 80%
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - relative air humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000121
    multivalued: false
    alias: rel_air_humidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  rel_humidity_out:
    name: rel_humidity_out
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram of air, kilogram of air
      occurrence:
        tag: occurrence
        value: '1'
    description: The recorded outside relative humidity value at the time of sampling
    title: outside relative humidity
    examples:
    - value: 12 per kilogram of air
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - outside relative humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000188
    multivalued: false
    alias: rel_humidity_out
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  rel_samp_loc:
    name: rel_samp_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The sampling location within the train car
    title: relative sampling location
    examples:
    - value: center of car
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - relative sampling location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000821
    multivalued: false
    alias: rel_samp_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: rel_samp_loc_enum
  reservoir:
    name: reservoir
    annotations:
      expected_value:
        tag: expected_value
        value: name
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of the reservoir (e.g. Carapebus)
    title: reservoir name
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - reservoir name
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000303
    multivalued: false
    alias: reservoir
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  resins_pc:
    name: resins_pc
    annotations:
      expected_value:
        tag: expected_value
        value: name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis
      method that divides¬†crude oil¬†components according to their polarizability
      and polarity. There are three main methods to obtain SARA results. The most
      popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source:
      https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
    title: resins wt%
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - resins wt%
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000134
    multivalued: false
    alias: resins_pc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_air_exch_rate:
    name: room_air_exch_rate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: liter per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: The rate at which outside air replaces indoor air in a given space
    title: room air exchange rate
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room air exchange rate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000169
    multivalued: false
    alias: room_air_exch_rate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  room_architec_elem:
    name: room_architec_elem
    annotations:
      expected_value:
        tag: expected_value
        value: free text
      occurrence:
        tag: occurrence
        value: '1'
    description: The unique details and component parts that, together, form the architecture
      of a distinguisahable space within a built structure
    title: room architectural elements
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room architectural elements
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000233
    multivalued: false
    alias: room_architec_elem
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  room_condt:
    name: room_condt
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The condition of the room at the time of sampling
    title: room condition
    examples:
    - value: new
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000822
    multivalued: false
    alias: room_condt
    owner: Biosample
    domain_of:
    - Biosample
    range: room_condt_enum
  room_connected:
    name: room_connected
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: List of rooms connected to the sampling room by a doorway
    title: rooms connected by a doorway
    examples:
    - value: office
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooms connected by a doorway
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000826
    multivalued: false
    alias: room_connected
    owner: Biosample
    domain_of:
    - Biosample
    range: room_connected_enum
  room_count:
    name: room_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The total count of rooms in the built structure including all room
      types
    title: room count
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000234
    multivalued: false
    alias: room_count
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_dim:
    name: room_dim
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The length, width and height of sampling room
    title: room dimensions
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room dimensions
    rank: 1000
    is_a: core field
    string_serialization: '{integer} {unit} x {integer} {unit} x {integer} {unit}'
    slot_uri: MIXS:0000192
    multivalued: false
    alias: room_dim
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_door_dist:
    name: room_door_dist
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Distance between doors (meters) in the hallway between the sampling
      room and adjacent rooms
    title: room door distance
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room door distance
    rank: 1000
    is_a: core field
    string_serialization: '{integer} {unit}'
    slot_uri: MIXS:0000193
    multivalued: false
    alias: room_door_dist
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_door_share:
    name: room_door_share
    annotations:
      expected_value:
        tag: expected_value
        value: room name;room number
      occurrence:
        tag: occurrence
        value: '1'
    description: List of room(s) (room number, room name) sharing a door with the
      sampling room
    title: rooms that share a door with sampling room
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooms that share a door with sampling room
    rank: 1000
    is_a: core field
    string_serialization: '{text};{integer}'
    slot_uri: MIXS:0000242
    multivalued: false
    alias: room_door_share
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_hallway:
    name: room_hallway
    annotations:
      expected_value:
        tag: expected_value
        value: room name;room number
      occurrence:
        tag: occurrence
        value: '1'
    description: List of room(s) (room number, room name) located in the same hallway
      as sampling room
    title: rooms that are on the same hallway
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooms that are on the same hallway
    rank: 1000
    is_a: core field
    string_serialization: '{text};{integer}'
    slot_uri: MIXS:0000238
    multivalued: false
    alias: room_hallway
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_loc:
    name: room_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The position of the room within the building
    title: room location in building
    examples:
    - value: interior room
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room location in building
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000823
    multivalued: false
    alias: room_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: room_loc_enum
  room_moist_dam_hist:
    name: room_moist_dam_hist
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The history of moisture damage or mold in the past 12 months. Number
      of events of moisture damage or mold observed
    title: room moisture damage or mold history
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room moisture damage or mold history
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000235
    multivalued: false
    alias: room_moist_dam_hist
    owner: Biosample
    domain_of:
    - Biosample
    range: integer
  room_net_area:
    name: room_net_area
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square feet, square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The net floor area of sampling room. Net area excludes wall thicknesses
    title: room net area
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room net area
    rank: 1000
    is_a: core field
    string_serialization: '{integer} {unit}'
    slot_uri: MIXS:0000194
    multivalued: false
    alias: room_net_area
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_occup:
    name: room_occup
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Count of room occupancy at time of sampling
    title: room occupancy
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room occupancy
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000236
    multivalued: false
    alias: room_occup
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  room_samp_pos:
    name: room_samp_pos
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The horizontal sampling position in the room relative to architectural
      elements
    title: room sampling position
    examples:
    - value: south corner
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room sampling position
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000824
    multivalued: false
    alias: room_samp_pos
    owner: Biosample
    domain_of:
    - Biosample
    range: room_samp_pos_enum
  room_type:
    name: room_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The main purpose or activity of the sampling room. A room is any
      distinguishable space within a structure
    title: room type
    examples:
    - value: bathroom
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000825
    multivalued: false
    alias: room_type
    owner: Biosample
    domain_of:
    - Biosample
    range: room_type_enum
  room_vol:
    name: room_vol
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: cubic feet, cubic meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Volume of sampling room
    title: room volume
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room volume
    rank: 1000
    is_a: core field
    string_serialization: '{integer} {unit}'
    slot_uri: MIXS:0000195
    multivalued: false
    alias: room_vol
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_wall_share:
    name: room_wall_share
    annotations:
      expected_value:
        tag: expected_value
        value: room name;room number
      occurrence:
        tag: occurrence
        value: '1'
    description: List of room(s) (room number, room name) sharing a wall with the
      sampling room
    title: rooms that share a wall with sampling room
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooms that share a wall with sampling room
    rank: 1000
    is_a: core field
    string_serialization: '{text};{integer}'
    slot_uri: MIXS:0000243
    multivalued: false
    alias: room_wall_share
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  room_window_count:
    name: room_window_count
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: Number of windows in the room
    title: room window count
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - room window count
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000237
    multivalued: false
    alias: room_window_count
    owner: Biosample
    domain_of:
    - Biosample
    range: integer
  root_cond:
    name: root_cond
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI,url or free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Relevant rooting conditions such as field plot size, sowing density,
      container dimensions, number of plants per container.
    title: rooting conditions
    examples:
    - value: http://himedialabs.com/TD/PT158.pdf
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting conditions
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}|{text}'
    slot_uri: MIXS:0001061
    multivalued: false
    alias: root_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_carbon:
    name: root_med_carbon
    annotations:
      expected_value:
        tag: expected_value
        value: carbon source name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Source of organic carbon in the culture rooting medium; e.g. sucrose.
    title: rooting medium carbon
    examples:
    - value: sucrose
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium carbon
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000577
    multivalued: false
    alias: root_med_carbon
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_macronutr:
    name: root_med_macronutr
    annotations:
      expected_value:
        tag: expected_value
        value: macronutrient name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of the culture rooting medium macronutrients (N,P, K,
      Ca, Mg, S); e.g. KH2PO4 (170¬†mg/L).
    title: rooting medium macronutrients
    examples:
    - value: KH2PO4;170¬†milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium macronutrients
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000578
    multivalued: false
    alias: root_med_macronutr
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_micronutr:
    name: root_med_micronutr
    annotations:
      expected_value:
        tag: expected_value
        value: micronutrient name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of the culture rooting medium micronutrients (Fe, Mn,
      Zn, B, Cu, Mo); e.g. H3BO3 (6.2¬†mg/L).
    title: rooting medium micronutrients
    examples:
    - value: H3BO3;6.2¬†milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium micronutrients
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000579
    multivalued: false
    alias: root_med_micronutr
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_ph:
    name: root_med_ph
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: pH measurement of the culture rooting medium; e.g. 5.5.
    title: rooting medium pH
    examples:
    - value: '7.5'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium pH
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001062
    multivalued: false
    alias: root_med_ph
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  root_med_regl:
    name: root_med_regl
    annotations:
      expected_value:
        tag: expected_value
        value: regulator name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Growth regulators in the culture rooting medium such as cytokinins,
      auxins, gybberellins, abscisic acid; e.g. 0.5¬†mg/L NAA.
    title: rooting medium regulators
    examples:
    - value: abscisic acid;0.75 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium regulators
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000581
    multivalued: false
    alias: root_med_regl
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_solid:
    name: root_med_solid
    annotations:
      expected_value:
        tag: expected_value
        value: name
      occurrence:
        tag: occurrence
        value: '1'
    description: Specification of the solidifying agent in the culture rooting medium;
      e.g. agar.
    title: rooting medium solidifier
    examples:
    - value: agar
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium solidifier
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0001063
    multivalued: false
    alias: root_med_solid
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  root_med_suppl:
    name: root_med_suppl
    annotations:
      expected_value:
        tag: expected_value
        value: supplement name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Organic supplements of the culture rooting medium, such as vitamins,
      amino acids, organic acids, antibiotics activated charcoal; e.g. nicotinic acid
      (0.5¬†mg/L).
    title: rooting medium organic supplements
    examples:
    - value: nicotinic acid;0.5 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - rooting medium organic supplements
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000580
    multivalued: false
    alias: root_med_suppl
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  salinity:
    name: salinity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: practical salinity unit, percentage
      occurrence:
        tag: occurrence
        value: '1'
    description: The total concentration of all dissolved salts in a liquid or solid
      sample. While salinity can be measured by a complete chemical analysis, this
      method is difficult and time consuming. More often, it is instead derived from
      the conductivity measurement. This is known as practical salinity. These derivations
      compare the specific conductance of the sample to a salinity standard such as
      seawater.
    title: salinity
    examples:
    - value: 25 practical salinity unit
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - salinity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000183
    multivalued: false
    alias: salinity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  salinity_meth:
    name: salinity_meth
    description: Reference or method used in determining salinity
    title: salinity method
    examples:
    - value: https://doi.org/10.1007/978-1-61779-986-0_28
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000341
    multivalued: false
    alias: salinity_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  salt_regm:
    name: salt_regm
    annotations:
      expected_value:
        tag: expected_value
        value: salt name;salt amount;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: gram, microgram, mole per liter, gram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving use of salts as supplement
      to liquid and soil growth media; should include the name of salt, amount administered,
      treatment regimen including how many times the treatment was repeated, how long
      each treatment lasted, and the start and end time of the entire treatment; can
      include multiple salt regimens
    title: salt regimen
    examples:
    - value: NaCl;5 gram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - salt regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000582
    multivalued: true
    alias: salt_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_capt_status:
    name: samp_capt_status
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Reason for the sample
    title: sample capture status
    examples:
    - value: farm sample
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample capture status
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000860
    multivalued: false
    alias: samp_capt_status
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_capt_status_enum
  samp_collec_device:
    name: samp_collec_device
    annotations:
      expected_value:
        tag: expected_value
        value: device name
    description: The device used to collect an environmental sample. This field accepts
      terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO).
      This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094).
    title: sample collection device
    examples:
    - value: swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample collection device
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{termLabel} {[termID]}|{text}'
    slot_uri: MIXS:0000002
    multivalued: false
    alias: samp_collec_device
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  samp_collec_method:
    name: samp_collec_method
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI,url , or text
    description: The method employed for collecting the sample.
    title: sample collection method
    examples:
    - value: swabbing
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample collection method
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{PMID}|{DOI}|{URL}|{text}'
    slot_uri: MIXS:0001225
    multivalued: false
    alias: samp_collec_method
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  samp_collect_point:
    name: samp_collect_point
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Sampling point on the asset were sample was collected (e.g. Wellhead,
      storage tank, separator, etc). If "other" is specified, please propose entry
      in "additional info" field
    title: sample collection point
    examples:
    - value: well
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample collection point
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001015
    multivalued: false
    alias: samp_collect_point
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_collect_point_enum
  samp_dis_stage:
    name: samp_dis_stage
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Stage of the disease at the time of sample collection, e.g. inoculation,
      penetration, infection, growth and reproduction, dissemination of pathogen.
    title: sample disease stage
    examples:
    - value: infection
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample disease stage
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000249
    multivalued: false
    alias: samp_dis_stage
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_dis_stage_enum
  samp_floor:
    name: samp_floor
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The floor of the building, where the sampling room is located
    title: sampling floor
    examples:
    - value: 4th floor
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sampling floor
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000828
    multivalued: false
    alias: samp_floor
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_floor_enum
  samp_loc_corr_rate:
    name: samp_loc_corr_rate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value range
      preferred_unit:
        tag: preferred_unit
        value: millimeter per year
      occurrence:
        tag: occurrence
        value: '1'
    description: Metal corrosion rate is the speed of metal deterioration due to environmental
      conditions. As environmental conditions change corrosion rates change accordingly.
      Therefore, long term corrosion rates are generally more informative than short
      term rates and for that reason they are preferred during reporting. In the case
      of suspected MIC, corrosion rate measurements at the time of sampling might
      provide insights into the involvement of certain microbial community members
      in MIC as well as potential microbial interplays
    title: corrosion rate at sample location
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - corrosion rate at sample location
    rank: 1000
    is_a: core field
    string_serialization: '{float} - {float} {unit}'
    slot_uri: MIXS:0000136
    multivalued: false
    alias: samp_loc_corr_rate
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_mat_process:
    name: samp_mat_process
    annotations:
      expected_value:
        tag: expected_value
        value: text
    description: A brief description of any processing applied to the sample during
      or after retrieving the sample from environment, or a link to the relevant protocol(s)
      performed.
    title: sample material processing
    examples:
    - value: filtering of seawater, storing samples in ethanol
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample material processing
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{text}'
    slot_uri: MIXS:0000016
    multivalued: false
    alias: samp_mat_process
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledTermValue
  samp_md:
    name: samp_md
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;enumeration
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: In non deviated well, measured depth is equal to the true vertical
      depth, TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated
      wells, the MD is the length of trajectory of the borehole measured from the
      same reference or datum. Common datums used are ground level (GL), drilling
      rig floor (DF), rotary table (RT), kelly bushing (KB) and mean sea level (MSL).
      If "other" is specified, please propose entry in "additional info" field
    title: sample measured depth
    examples:
    - value: 1534 meter;MSL
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample measured depth
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000413
    multivalued: false
    alias: samp_md
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  samp_preserv:
    name: samp_preserv
    annotations:
      expected_value:
        tag: expected_value
        value: name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: milliliter
      occurrence:
        tag: occurrence
        value: '1'
    description: Preservative added to the sample (e.g. Rnalater, alcohol, formaldehyde,
      etc.). Where appropriate include volume added (e.g. Rnalater; 2 ml)
    title: preservative added to sample
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - preservative added to sample
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000463
    multivalued: false
    alias: samp_preserv
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_room_id:
    name: samp_room_id
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: Sampling room number. This ID should be consistent with the designations
      on the building floor plans
    title: sampling room ID or name
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sampling room ID or name
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000244
    multivalued: false
    alias: samp_room_id
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_size:
    name: samp_size
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millliter, gram, milligram, liter
    description: The total amount or size (volume (ml), mass (g) or area (m2) ) of
      sample collected.
    title: amount or size of sample collected
    examples:
    - value: 5 liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - amount or size of sample collected
    rank: 1000
    is_a: nucleic acid sequence source field
    slot_uri: MIXS:0000001
    multivalued: false
    alias: samp_size
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  samp_sort_meth:
    name: samp_sort_meth
    annotations:
      expected_value:
        tag: expected_value
        value: description of method
      occurrence:
        tag: occurrence
        value: m
    description: Method by which samples are sorted; open face filter collecting total
      suspended particles, prefilter to remove particles larger than X micrometers
      in diameter, where common values of X would be 10 and 2.5 full size sorting
      in a cascade impactor.
    title: sample size sorting method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample size sorting method
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000216
    multivalued: true
    alias: samp_sort_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_store_dur:
    name: samp_store_dur
    annotations:
      expected_value:
        tag: expected_value
        value: duration
      occurrence:
        tag: occurrence
        value: '1'
    description: Duration for which the sample was stored
    title: sample storage duration
    examples:
    - value: P1Y6M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample storage duration
    rank: 1000
    is_a: core field
    string_serialization: '{duration}'
    slot_uri: MIXS:0000116
    multivalued: false
    alias: samp_store_dur
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_store_loc:
    name: samp_store_loc
    annotations:
      expected_value:
        tag: expected_value
        value: location name
      occurrence:
        tag: occurrence
        value: '1'
    description: Location at which sample was stored, usually name of a specific freezer/room
    title: sample storage location
    examples:
    - value: Freezer no:5
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample storage location
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000755
    multivalued: false
    alias: samp_store_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_store_temp:
    name: samp_store_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Temperature at which sample was stored, e.g. -80 degree Celsius
    title: sample storage temperature
    examples:
    - value: -80 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample storage temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000110
    multivalued: false
    alias: samp_store_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  samp_subtype:
    name: samp_subtype
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of sample sub-type. For example if "sample type" is "Produced
      Water" then subtype could be "Oil Phase" or "Water Phase". If "other" is specified,
      please propose entry in "additional info" field
    title: sample subtype
    examples:
    - value: biofilm
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample subtype
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000999
    multivalued: false
    alias: samp_subtype
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_subtype_enum
  samp_taxon_id:
    name: samp_taxon_id
    annotations:
      expected_value:
        tag: expected_value
        value: Taxonomy ID
    description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa
      sample. Use 'synthetic metagenome’ for mock community/positive controls, or
      'blank sample' for negative controls.
    title: Taxonomy ID of DNA sample
    comments:
    - coal metagenome [NCBITaxon:1260732] would be a reasonable has_raw_value
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - Taxonomy ID of DNA sample
    rank: 1000
    is_a: investigation field
    slot_uri: MIXS:0001320
    multivalued: false
    alias: samp_taxon_id
    owner: Biosample
    domain_of:
    - Biosample
    range: ControlledIdentifiedTermValue
  samp_time_out:
    name: samp_time_out
    annotations:
      expected_value:
        tag: expected_value
        value: time
      preferred_unit:
        tag: preferred_unit
        value: hour
      occurrence:
        tag: occurrence
        value: '1'
    description: The recent and long term history of outside sampling
    title: sampling time outside
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sampling time outside
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000196
    multivalued: false
    alias: samp_time_out
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_transport_cond:
    name: samp_transport_cond
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;measurement value
      preferred_unit:
        tag: preferred_unit
        value: days;degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Sample transport duration (in days or hrs) and temperature the sample
      was exposed to (e.g. 5.5 days; 20 ¬∞C)
    title: sample transport conditions
    examples:
    - value: 5 days;-20 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample transport conditions
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{float} {unit}'
    slot_uri: MIXS:0000410
    multivalued: false
    alias: samp_transport_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_tvdss:
    name: samp_tvdss
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value or measurement value range
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Depth of the sample i.e. The vertical distance between the sea level
      and the sampled position in the subsurface. Depth can be reported as an interval
      for subsurface samples e.g. 1325.75-1362.25 m
    title: sample true vertical depth subsea
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample true vertical depth subsea
    rank: 1000
    is_a: core field
    string_serialization: '{float}-{float} {unit}'
    slot_uri: MIXS:0000409
    multivalued: false
    alias: samp_tvdss
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_type:
    name: samp_type
    annotations:
      expected_value:
        tag: expected_value
        value: GENEPIO:0001246
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of material from which the sample was obtained. For the
      Hydrocarbon package, samples include types like core, rock trimmings, drill
      cuttings, piping section, coupon, pigging debris, solid deposit, produced fluid,
      produced water, injected water, swabs, etc. For the Food Package, samples are
      usually categorized as food, body products or tissues, or environmental material.
      This field accepts terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246).
    title: sample type
    examples:
    - value: built environment sample [GENEPIO:0001248]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample type
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000998
    multivalued: false
    alias: samp_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  samp_vol_we_dna_ext:
    name: samp_vol_we_dna_ext
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: millliter, gram, milligram, square centimeter
    description: 'Volume (ml) or mass (g) of total collected sample processed for
      DNA extraction. Note: total sample collected should be entered under the term
      Sample Size (MIXS:0000001).'
    title: sample volume or weight for DNA extraction
    examples:
    - value: 1500 milliliter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample volume or weight for DNA extraction
    rank: 1000
    is_a: nucleic acid sequence source field
    slot_uri: MIXS:0000111
    multivalued: false
    alias: samp_vol_we_dna_ext
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: QuantityValue
  samp_weather:
    name: samp_weather
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The weather on the sampling day
    title: sampling day weather
    examples:
    - value: foggy
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sampling day weather
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000827
    multivalued: false
    alias: samp_weather
    owner: Biosample
    domain_of:
    - Biosample
    range: samp_weather_enum
  samp_well_name:
    name: samp_well_name
    annotations:
      expected_value:
        tag: expected_value
        value: name
      occurrence:
        tag: occurrence
        value: '1'
    description: Name of the well (e.g. BXA1123) where sample was taken
    title: sample well name
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sample well name
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000296
    multivalued: false
    alias: samp_well_name
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  saturates_pc:
    name: saturates_pc
    annotations:
      expected_value:
        tag: expected_value
        value: name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis
      method that divides¬†crude oil¬†components according to their polarizability
      and polarity. There are three main methods to obtain SARA results. The most
      popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source:
      https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
    title: saturates wt%
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - saturates wt%
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000131
    multivalued: false
    alias: saturates_pc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  season:
    name: season
    annotations:
      expected_value:
        tag: expected_value
        value: NCIT:C94729
      occurrence:
        tag: occurrence
        value: '1'
    description: The season when sampling occurred. Any of the four periods into which
      the year is divided by the equinoxes and solstices. This field accepts terms
      listed under season (http://purl.obolibrary.org/obo/NCIT_C94729).
    title: season
    examples:
    - value: autumn [NCIT:C94733]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - season
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000829
    multivalued: false
    alias: season
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  season_environment:
    name: season_environment
    annotations:
      expected_value:
        tag: expected_value
        value: seasonal environment name;treatment interval and duration
      occurrence:
        tag: occurrence
        value: m
    description: Treatment involving an exposure to a particular season (e.g. Winter,
      summer, rabi, rainy etc.), treatment regimen including how many times the treatment
      was repeated, how long each treatment lasted, and the start and end time of
      the entire treatment
    title: seasonal environment
    examples:
    - value: rainy;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - seasonal environment
    rank: 1000
    is_a: core field
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0001068
    multivalued: true
    alias: season_environment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  season_precpt:
    name: season_precpt
    description: The average of all seasonal precipitation values known, or an estimated
      equivalent value derived by such methods as regional indexes or Isohyetal maps.
    title: average seasonal precipitation
    todos:
    - check validation & examples. always mm? so value only? Or value + unit
    notes:
    - mean and average are the same thing, but it seems like bad practice to not be
      consistent. Changed mean to average
    comments:
    - Seasons are defined as spring (March, April, May), summer (June, July, August),
      autumn (September, October, November) and winter (December, January, February).
    examples:
    - value: 0.4 inch
    - value: 10.16 mm
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000645
    multivalued: false
    alias: season_precpt
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  season_temp:
    name: season_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Mean seasonal temperature
    title: mean seasonal temperature
    examples:
    - value: 18 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - mean seasonal temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000643
    multivalued: false
    alias: season_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  season_use:
    name: season_use
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The seasons the space is occupied
    title: seasonal use
    examples:
    - value: Winter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - seasonal use
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000830
    multivalued: false
    alias: season_use
    owner: Biosample
    domain_of:
    - Biosample
    range: season_use_enum
  secondary_treatment:
    name: secondary_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: secondary treatment type
      occurrence:
        tag: occurrence
        value: '1'
    description: The process for substantially degrading the biological content of
      the sewage
    title: secondary treatment
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - secondary treatment
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000351
    multivalued: false
    alias: secondary_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  sediment_type:
    name: sediment_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Information about the sediment type based on major constituents
    title: sediment type
    examples:
    - value: biogenous
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sediment type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001078
    multivalued: false
    alias: sediment_type
    owner: Biosample
    domain_of:
    - Biosample
    range: sediment_type_enum
  seq_meth:
    name: seq_meth
    annotations:
      expected_value:
        tag: expected_value
        value: Text or OBI
    description: Sequencing machine used. Where possible the term should be taken
      from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103).
    title: sequencing method
    examples:
    - value: 454 Genome Sequencer FLX [OBI:0000702]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sequencing method
    rank: 1000
    is_a: sequencing field
    string_serialization: '{termLabel} {[termID]}|{text}'
    slot_uri: MIXS:0000050
    multivalued: false
    alias: seq_meth
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  seq_quality_check:
    name: seq_quality_check
    annotations:
      expected_value:
        tag: expected_value
        value: none or manually edited
    description: Indicate if the sequence has been called by automatic systems (none)
      or undergone a manual editing procedure (e.g. by inspecting the raw data or
      chromatograms). Applied only for sequences that are not submitted to SRA,ENA
      or DRA
    title: sequence quality check
    examples:
    - value: none
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sequence quality check
    rank: 1000
    is_a: sequencing field
    string_serialization: '[none|manually edited]'
    slot_uri: MIXS:0000051
    multivalued: false
    alias: seq_quality_check
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  sequencing field:
    name: sequencing field
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    abstract: true
    alias: sequencing_field
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  sewage_type:
    name: sewage_type
    annotations:
      expected_value:
        tag: expected_value
        value: sewage type name
      occurrence:
        tag: occurrence
        value: '1'
    description: Type of wastewater treatment plant as municipial or industrial
    title: sewage type
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sewage type
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000215
    multivalued: false
    alias: sewage_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  shad_dev_water_mold:
    name: shad_dev_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew on the shading device
    title: shading device signs of water/mold
    examples:
    - value: no presence of mold visible
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - shading device signs of water/mold
    rank: 1000
    is_a: core field
    string_serialization: '[presence of mold visible|no presence of mold visible]'
    slot_uri: MIXS:0000834
    multivalued: false
    alias: shad_dev_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  shading_device_cond:
    name: shading_device_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The physical condition of the shading device at the time of sampling
    title: shading device condition
    examples:
    - value: new
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - shading device condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000831
    multivalued: false
    alias: shading_device_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: shading_device_cond_enum
  shading_device_loc:
    name: shading_device_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The location of the shading device in relation to the built structure
    title: shading device location
    examples:
    - value: exterior
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - shading device location
    rank: 1000
    is_a: core field
    string_serialization: '[exterior|interior]'
    slot_uri: MIXS:0000832
    multivalued: false
    alias: shading_device_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  shading_device_mat:
    name: shading_device_mat
    annotations:
      expected_value:
        tag: expected_value
        value: material name
      occurrence:
        tag: occurrence
        value: '1'
    description: The material the shading device is composed of
    title: shading device material
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - shading device material
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000245
    multivalued: false
    alias: shading_device_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  shading_device_type:
    name: shading_device_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of shading device
    title: shading device type
    examples:
    - value: slatted aluminum awning
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - shading device type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000835
    multivalued: false
    alias: shading_device_type
    owner: Biosample
    domain_of:
    - Biosample
    range: shading_device_type_enum
  sieving:
    name: sieving
    description: Collection design of pooled samples and/or sieve size and amount
      of sample sieved
    title: composite design/sieving
    todos:
    - check validation and examples
    comments:
    - Describe how samples were composited or sieved.
    - Use 'sample link' to indicate which samples were combined.
    examples:
    - value: combined 2 cores | 4mm sieved
    - value: 4 mm sieved and homogenized
    - value: 50 g | 5 cores | 2 mm sieved
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{{text}|{float} {unit}};{float} {unit}'
    slot_uri: MIXS:0000322
    multivalued: false
    alias: sieving
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  silicate:
    name: silicate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of silicate
    title: silicate
    examples:
    - value: 0.05 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - silicate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000184
    multivalued: false
    alias: silicate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  size_frac:
    name: size_frac
    annotations:
      expected_value:
        tag: expected_value
        value: filter size value range
    description: Filtering pore size used in sample preparation
    title: size fraction selected
    examples:
    - value: 0-0.22 micrometer
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - size fraction selected
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{float}-{float} {unit}'
    slot_uri: MIXS:0000017
    multivalued: false
    alias: size_frac
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  size_frac_low:
    name: size_frac_low
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: micrometer
      occurrence:
        tag: occurrence
        value: '1'
    description: Refers to the mesh/pore size used to pre-filter/pre-sort the sample.
      Materials larger than the size threshold are excluded from the sample
    title: size-fraction lower threshold
    examples:
    - value: 0.2 micrometer
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - size-fraction lower threshold
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000735
    multivalued: false
    alias: size_frac_low
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  size_frac_up:
    name: size_frac_up
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: micrometer
      occurrence:
        tag: occurrence
        value: '1'
    description: Refers to the mesh/pore size used to retain the sample. Materials
      smaller than the size threshold are excluded from the sample
    title: size-fraction upper threshold
    examples:
    - value: 20 micrometer
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - size-fraction upper threshold
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000736
    multivalued: false
    alias: size_frac_up
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  slope_aspect:
    name: slope_aspect
    description: The direction a slope faces. While looking down a slope use a compass
      to record the direction you are facing (direction or degrees). This measure
      provides an indication of sun and wind exposure that will influence soil temperature
      and evapotranspiration.
    title: slope aspect
    comments:
    - Aspect is the orientation of slope, measured clockwise in degrees from 0 to
      360, where 0 is north-facing, 90 is east-facing, 180 is south-facing, and 270
      is west-facing.
    examples:
    - value: '35'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000647
    multivalued: false
    alias: slope_aspect
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  slope_gradient:
    name: slope_gradient
    description: Commonly called 'slope'. The angle between ground surface and a horizontal
      line (in percent). This is the direction that overland water would flow. This
      measure is usually taken with a hand level meter or clinometer
    title: slope gradient
    todos:
    - Slope is a percent. How does the validation work? Check to correct examples
    examples:
    - value: 10%
    - value: 10 %
    - value: '0.10'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000646
    multivalued: false
    alias: slope_gradient
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  sludge_retent_time:
    name: sludge_retent_time
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: hours
      occurrence:
        tag: occurrence
        value: '1'
    description: The time activated sludge remains in reactor
    title: sludge retention time
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sludge retention time
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000669
    multivalued: false
    alias: sludge_retent_time
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  sodium:
    name: sodium
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Sodium concentration in the sample
    title: sodium
    examples:
    - value: 10.5 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sodium
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000428
    multivalued: false
    alias: sodium
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  soil_horizon:
    name: soil_horizon
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Specific layer in the land area which measures parallel to the soil
      surface and possesses physical characteristics which differ from the layers
      above and beneath
    title: soil horizon
    examples:
    - value: A horizon
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil horizon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001082
    multivalued: false
    alias: soil_horizon
    owner: Biosample
    domain_of:
    - Biosample
    range: soil_horizon_enum
  soil_text_measure:
    name: soil_text_measure
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: The relative proportion of different grain sizes of mineral particles
      in a soil, as described using a standard system; express as % sand (50 um to
      2 mm), silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty
      clay loam) optional.
    title: soil texture measurement
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil texture measurement
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000335
    multivalued: false
    alias: soil_text_measure
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  soil_texture_meth:
    name: soil_texture_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining soil texture
    title: soil texture method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil texture method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000336
    multivalued: false
    alias: soil_texture_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  soil_type:
    name: soil_type
    annotations:
      expected_value:
        tag: expected_value
        value: ENVO_00001998
      occurrence:
        tag: occurrence
        value: '1'
    description: Description of the soil type or classification. This field accepts
      terms under soil (http://purl.obolibrary.org/obo/ENVO_00001998).  Multiple terms
      can be separated by pipes.
    title: soil type
    examples:
    - value: plinthosol [ENVO:00002250]
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil type
    rank: 1000
    is_a: core field
    string_serialization: '{termLabel} {[termID]}'
    slot_uri: MIXS:0000332
    multivalued: false
    alias: soil_type
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: TextValue
  soil_type_meth:
    name: soil_type_meth
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI or url
      occurrence:
        tag: occurrence
        value: '1'
    description: Reference or method used in determining soil series name or other
      lower-level classification
    title: soil type method
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soil type method
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000334
    multivalued: false
    alias: soil_type_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  solar_irradiance:
    name: solar_irradiance
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: kilowatts per square meter per day, ergs per square centimeter per
          second
      occurrence:
        tag: occurrence
        value: '1'
    description: The amount of solar energy that arrives at a specific area of a surface
      during a specific time interval
    title: solar irradiance
    examples:
    - value: 1.36 kilowatts per square meter per day
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - solar irradiance
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000112
    multivalued: false
    alias: solar_irradiance
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  soluble_inorg_mat:
    name: soluble_inorg_mat
    annotations:
      expected_value:
        tag: expected_value
        value: soluble inorganic material name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram, microgram, mole per liter, gram per liter, parts per million
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of substances such as ammonia, road-salt, sea-salt,
      cyanide, hydrogen sulfide, thiocyanates, thiosulfates, etc.
    title: soluble inorganic material
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soluble inorganic material
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000672
    multivalued: true
    alias: soluble_inorg_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  soluble_org_mat:
    name: soluble_org_mat
    annotations:
      expected_value:
        tag: expected_value
        value: soluble organic material name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram, microgram, mole per liter, gram per liter, parts per million
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of substances such as urea, fruit sugars, soluble proteins,
      drugs, pharmaceuticals, etc.
    title: soluble organic material
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soluble organic material
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000673
    multivalued: true
    alias: soluble_org_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  soluble_react_phosp:
    name: soluble_react_phosp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of soluble reactive phosphorus
    title: soluble reactive phosphorus
    examples:
    - value: 0.1 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - soluble reactive phosphorus
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000738
    multivalued: false
    alias: soluble_react_phosp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  source_mat_id:
    name: source_mat_id
    description: A globally unique identifier assigned to the biological sample.
    title: source material identifier
    todos:
    - Currently, the comments say to use UUIDs. However, if we implement assigning
      NMDC identifiers with the minter we dont need to require a GUID. It can be an
      optional field to fill out only if they already have a resolvable ID.
    comments:
    - Identifiers must be prefixed. Possible FAIR prefixes are IGSNs (http://www.geosamples.org/getigsn),
      NCBI biosample accession numbers, ARK identifiers (https://arks.org/). These
      IDs enable linking to derived analytes and subsamples. If you have not assigned
      FAIR identifiers to your samples, you can generate UUIDs (https://www.uuidgenerator.net/).
    examples:
    - value: IGSN:AU1243
    - value: UUID:24f1467a-40f4-11ed-b878-0242ac120002
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: nucleic acid sequence source field
    string_serialization: '{text}'
    slot_uri: MIXS:0000026
    multivalued: false
    alias: source_mat_id
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  space_typ_state:
    name: space_typ_state
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Customary or normal state of the space
    title: space typical state
    examples:
    - value: typically occupied
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - space typical state
    rank: 1000
    is_a: core field
    string_serialization: '[typically occupied|typically unoccupied]'
    slot_uri: MIXS:0000770
    multivalued: false
    alias: space_typ_state
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  specific:
    name: specific
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'The building specifications. If design is chosen, indicate phase:
      conceptual, schematic, design development, construction documents'
    title: specifications
    examples:
    - value: construction
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - specifications
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000836
    multivalued: false
    alias: specific
    owner: Biosample
    domain_of:
    - Biosample
    range: specific_enum
  specific_ecosystem:
    name: specific_ecosystem
    description: Specific ecosystems represent specific features of the environment
      like aphotic zone in an ocean or gastric mucosa within a host digestive system.
      Specific ecosystem is in position 5/5 in a GOLD path.
    comments:
    - Specific ecosystems help to define samples based on very specific characteristics
      of an environment under the five-level classification system.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://gold.jgi.doe.gov/help
    rank: 1000
    is_a: gold_path_field
    alias: specific_ecosystem
    owner: Biosample
    domain_of:
    - Biosample
    - Study
    range: string
  specific_humidity:
    name: specific_humidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram of air, kilogram of air
      occurrence:
        tag: occurrence
        value: '1'
    description: The mass of water vapour in a unit mass of moist air, usually expressed
      as grams of vapour per kilogram of air, or, in air conditioning, as grains per
      pound.
    title: specific humidity
    examples:
    - value: 15 per kilogram of air
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - specific humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000214
    multivalued: false
    alias: specific_humidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  sr_dep_env:
    name: sr_dep_env
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock).
      If "other" is specified, please propose entry in "additional info" field
    title: source rock depositional environment
    examples:
    - value: Marine
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - source rock depositional environment
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000996
    multivalued: false
    alias: sr_dep_env
    owner: Biosample
    domain_of:
    - Biosample
    range: sr_dep_env_enum
  sr_geol_age:
    name: sr_geol_age
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Geological age of source rock (Additional info: https://en.wikipedia.org/wiki/Period_(geology)).
      If "other" is specified, please propose entry in "additional info" field'
    title: source rock geological age
    examples:
    - value: Silurian
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - source rock geological age
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000997
    multivalued: false
    alias: sr_geol_age
    owner: Biosample
    domain_of:
    - Biosample
    range: sr_geol_age_enum
  sr_kerog_type:
    name: sr_kerog_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Origin of kerogen. Type I: Algal (aquatic), Type II: planktonic
      and soft plant material (aquatic or terrestrial), Type III: terrestrial woody/
      fibrous plant material (terrestrial), Type IV: oxidized recycled woody debris
      (terrestrial) (additional information: https://en.wikipedia.org/wiki/Kerogen).
      If "other" is specified, please propose entry in "additional info" field'
    title: source rock kerogen type
    examples:
    - value: Type IV
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - source rock kerogen type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000994
    multivalued: false
    alias: sr_kerog_type
    owner: Biosample
    domain_of:
    - Biosample
    range: sr_kerog_type_enum
  sr_lithology:
    name: sr_lithology
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Lithology of source rock (https://en.wikipedia.org/wiki/Source_rock).
      If "other" is specified, please propose entry in "additional info" field
    title: source rock lithology
    examples:
    - value: Coal
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - source rock lithology
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000995
    multivalued: false
    alias: sr_lithology
    owner: Biosample
    domain_of:
    - Biosample
    range: sr_lithology_enum
  standing_water_regm:
    name: standing_water_regm
    annotations:
      expected_value:
        tag: expected_value
        value: standing water type;treatment interval and duration
      occurrence:
        tag: occurrence
        value: m
    description: Treatment involving an exposure to standing water during a plant's
      life span, types can be flood water or standing water, treatment regimen including
      how many times the treatment was repeated, how long each treatment lasted, and
      the start and end time of the entire treatment; can include multiple regimens
    title: standing water regimen
    examples:
    - value: standing water;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - standing water regimen
    rank: 1000
    is_a: core field
    string_serialization: '{text};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0001069
    multivalued: true
    alias: standing_water_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  store_cond:
    name: store_cond
    annotations:
      expected_value:
        tag: expected_value
        value: storage condition type;duration
      occurrence:
        tag: occurrence
        value: '1'
    description: Explain how and for how long the soil sample was stored before DNA
      extraction (fresh/frozen/other).
    title: storage conditions
    examples:
    - value: -20 degree Celsius freezer;P2Y10D
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - storage conditions
    rank: 1000
    is_a: core field
    string_serialization: '{text};{duration}'
    slot_uri: MIXS:0000327
    multivalued: false
    alias: store_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  substructure_type:
    name: substructure_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: The substructure or under building is that largely hidden section
      of the building which is built off the foundations to the ground floor level
    title: substructure type
    examples:
    - value: basement
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - substructure type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000767
    multivalued: true
    alias: substructure_type
    owner: Biosample
    domain_of:
    - Biosample
    range: substructure_type_enum
  sulfate:
    name: sulfate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of sulfate in the sample
    title: sulfate
    examples:
    - value: 5 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sulfate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000423
    multivalued: false
    alias: sulfate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  sulfate_fw:
    name: sulfate_fw
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Original sulfate concentration in the hydrocarbon resource
    title: sulfate in formation water
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sulfate in formation water
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000407
    multivalued: false
    alias: sulfate_fw
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  sulfide:
    name: sulfide
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of sulfide in the sample
    title: sulfide
    examples:
    - value: 2 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - sulfide
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000424
    multivalued: false
    alias: sulfide
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  surf_air_cont:
    name: surf_air_cont
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: Contaminant identified on surface
    title: surface-air contaminant
    examples:
    - value: radon
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface-air contaminant
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000759
    multivalued: true
    alias: surf_air_cont
    owner: Biosample
    domain_of:
    - Biosample
    range: surf_air_cont_enum
  surf_humidity:
    name: surf_humidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: percentage
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Surfaces: water activity as a function of air and material moisture'
    title: surface humidity
    examples:
    - value: 10%
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface humidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000123
    multivalued: false
    alias: surf_humidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  surf_material:
    name: surf_material
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Surface materials at the point of sampling
    title: surface material
    examples:
    - value: wood
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000758
    multivalued: false
    alias: surf_material
    owner: Biosample
    domain_of:
    - Biosample
    range: surf_material_enum
  surf_moisture:
    name: surf_moisture
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: parts per million, gram per cubic meter, gram per square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Water held on a surface
    title: surface moisture
    examples:
    - value: 0.01 gram per square meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface moisture
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000128
    multivalued: false
    alias: surf_moisture
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  surf_moisture_ph:
    name: surf_moisture_ph
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: ph measurement of surface
    title: surface moisture pH
    examples:
    - value: '7'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface moisture pH
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000760
    multivalued: false
    alias: surf_moisture_ph
    owner: Biosample
    domain_of:
    - Biosample
    range: double
  surf_temp:
    name: surf_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: Temperature of the surface at the time of sampling
    title: surface temperature
    examples:
    - value: 15 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - surface temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000125
    multivalued: false
    alias: surf_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  suspend_part_matter:
    name: suspend_part_matter
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of suspended particulate matter
    title: suspended particulate matter
    examples:
    - value: 0.5 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - suspended particulate matter
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000741
    multivalued: false
    alias: suspend_part_matter
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  suspend_solids:
    name: suspend_solids
    annotations:
      expected_value:
        tag: expected_value
        value: suspended solid name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: gram, microgram, milligram per liter, mole per liter, gram per liter,
          part per million
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of substances including a wide variety of material,
      such as silt, decaying plant and animal matter; can include multiple substances
    title: suspended solids
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - suspended solids
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000150
    multivalued: true
    alias: suspend_solids
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  tan:
    name: tan
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Total Acid Number¬†(TAN) is a measurement of acidity that is determined
      by the amount of¬†potassium hydroxide¬†in milligrams that is needed to neutralize
      the acids in one gram of oil.¬†It is an important quality measurement of¬†crude
      oil. (source: https://en.wikipedia.org/wiki/Total_acid_number)'
    title: total acid number
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total acid number
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000120
    multivalued: false
    alias: tan
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  target_gene:
    name: target_gene
    annotations:
      expected_value:
        tag: expected_value
        value: gene name
    description: Targeted gene or locus name for marker gene studies
    title: target gene
    examples:
    - value: 16S rRNA, 18S rRNA, nif, amoA, rpo
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - target gene
    rank: 1000
    is_a: sequencing field
    string_serialization: '{text}'
    slot_uri: MIXS:0000044
    multivalued: false
    alias: target_gene
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  target_subfragment:
    name: target_subfragment
    annotations:
      expected_value:
        tag: expected_value
        value: gene fragment name
    description: Name of subfragment of a gene or locus. Important to e.g. identify
      special regions on marker genes like V6 on 16S rRNA
    title: target subfragment
    examples:
    - value: V6, V9, ITS
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - target subfragment
    rank: 1000
    is_a: sequencing field
    string_serialization: '{text}'
    slot_uri: MIXS:0000045
    multivalued: false
    alias: target_subfragment
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: TextValue
  temp:
    name: temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
    description: Temperature of the sample at the time of sampling.
    title: temperature
    examples:
    - value: 25 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - temperature
    rank: 1000
    is_a: environment field
    slot_uri: MIXS:0000113
    multivalued: false
    alias: temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  temp_out:
    name: temp_out
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The recorded temperature value at sampling time outside
    title: temperature outside house
    examples:
    - value: 5 degree Celsius
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - temperature outside house
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000197
    multivalued: false
    alias: temp_out
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tertiary_treatment:
    name: tertiary_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: tertiary treatment type
      occurrence:
        tag: occurrence
        value: '1'
    description: The process providing a final treatment stage to raise the effluent
      quality before it is discharged to the receiving environment
    title: tertiary treatment
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - tertiary treatment
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000352
    multivalued: false
    alias: tertiary_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  tidal_stage:
    name: tidal_stage
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Stage of tide
    title: tidal stage
    examples:
    - value: high tide
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - tidal stage
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000750
    multivalued: false
    alias: tidal_stage
    owner: Biosample
    domain_of:
    - Biosample
    range: tidal_stage_enum
  tillage:
    name: tillage
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: m
    description: Note method(s) used for tilling
    title: history/tillage
    examples:
    - value: chisel
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - history/tillage
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0001081
    multivalued: true
    alias: tillage
    owner: Biosample
    domain_of:
    - Biosample
    range: tillage_enum
  tiss_cult_growth_med:
    name: tiss_cult_growth_med
    annotations:
      expected_value:
        tag: expected_value
        value: PMID,DOI,url or free text
      occurrence:
        tag: occurrence
        value: '1'
    description: Description of plant tissue culture growth media used
    title: tissue culture growth media
    examples:
    - value: https://link.springer.com/content/pdf/10.1007/BF02796489.pdf
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - tissue culture growth media
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}|{text}'
    slot_uri: MIXS:0001070
    multivalued: false
    alias: tiss_cult_growth_med
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  toluene:
    name: toluene
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of toluene in the sample
    title: toluene
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - toluene
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000154
    multivalued: false
    alias: toluene
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_carb:
    name: tot_carb
    description: Total carbon content
    title: total carbon
    todos:
    - is this inorganic and organic? both? could use some clarification.
    - ug/L doesn't seem like the right units. Should check this slots usage in databases
      and re-evaluate. I couldn't find any references that provided this data in this
      format
    examples:
    - value: 1 ug/L
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000525
    multivalued: false
    alias: tot_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_depth_water_col:
    name: tot_depth_water_col
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of total depth of water column
    title: total depth of water column
    examples:
    - value: 500 meter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total depth of water column
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000634
    multivalued: false
    alias: tot_depth_water_col
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_diss_nitro:
    name: tot_diss_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Total dissolved nitrogen concentration, reported as nitrogen, measured
      by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen'
    title: total dissolved nitrogen
    examples:
    - value: 40 microgram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total dissolved nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000744
    multivalued: false
    alias: tot_diss_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_inorg_nitro:
    name: tot_inorg_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Total inorganic nitrogen content
    title: total inorganic nitrogen
    examples:
    - value: 40 microgram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total inorganic nitrogen
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000745
    multivalued: false
    alias: tot_inorg_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_iron:
    name: tot_iron
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, milligram per kilogram
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of total iron in the sample
    title: total iron
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total iron
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000105
    multivalued: false
    alias: tot_iron
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_nitro:
    name: tot_nitro
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, micromole per liter, milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Total nitrogen concentration of water samples, calculated by: total
      nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured
      without filtering, reported as nitrogen'
    title: total nitrogen concentration
    examples:
    - value: 50 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total nitrogen concentration
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000102
    multivalued: false
    alias: tot_nitro
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_nitro_cont_meth:
    name: tot_nitro_cont_meth
    description: Reference or method used in determining the total nitrogen
    title: total nitrogen content method
    examples:
    - value: https://doi.org/10.2134/agronmonogr9.2.c32
    - value: https://acsess.onlinelibrary.wiley.com/doi/full/10.2136/sssaj2009.0389?casa_token=bm0pYIUdNMgAAAAA%3AOWVRR0STHaOe-afTcTdxn5m1hM8n2ltM0wY-b1iYpYdD9dhwppk5j3LvC2IO5yhOIvyLVeQz4NZRCZo
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000338
    multivalued: false
    alias: tot_nitro_cont_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  tot_nitro_content:
    name: tot_nitro_content
    description: Total nitrogen content of the sample
    title: total nitrogen content
    examples:
    - value: 5 mg N/ L
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000530
    multivalued: false
    alias: tot_nitro_content
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_org_c_meth:
    name: tot_org_c_meth
    description: Reference or method used in determining total organic carbon
    title: total organic carbon method
    examples:
    - value: https://doi.org/10.1080/07352680902776556
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000337
    multivalued: false
    alias: tot_org_c_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  tot_org_carb:
    name: tot_org_carb
    description: 'Definition for soil: total organic carbon content of the soil, definition
      otherwise: total organic carbon content'
    title: total organic carbon
    todos:
    - check description. How are they different?
    examples:
    - value: 5 mg N/ L
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000533
    multivalued: false
    alias: tot_org_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_part_carb:
    name: tot_part_carb
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Total particulate carbon content
    title: total particulate carbon
    examples:
    - value: 35 micromole per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total particulate carbon
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000747
    multivalued: false
    alias: tot_part_carb
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_phosp:
    name: tot_phosp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: micromole per liter, milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: 'Total phosphorus concentration in the sample, calculated by: total
      phosphorus = total dissolved phosphorus + particulate phosphorus'
    title: total phosphorus
    examples:
    - value: 0.03 milligram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total phosphorus
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000117
    multivalued: false
    alias: tot_phosp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_phosphate:
    name: tot_phosphate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per liter, micromole per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Total amount or concentration of phosphate
    title: total phosphate
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total phosphate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000689
    multivalued: false
    alias: tot_phosphate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tot_sulfur:
    name: tot_sulfur
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of total sulfur in the sample
    title: total sulfur
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - total sulfur
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000419
    multivalued: false
    alias: tot_sulfur
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  train_line:
    name: train_line
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The subway line name
    title: train line
    examples:
    - value: red
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - train line
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000837
    multivalued: false
    alias: train_line
    owner: Biosample
    domain_of:
    - Biosample
    range: train_line_enum
  train_stat_loc:
    name: train_stat_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The train station collection location
    title: train station collection location
    examples:
    - value: forest hills
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - train station collection location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000838
    multivalued: false
    alias: train_stat_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: train_stat_loc_enum
  train_stop_loc:
    name: train_stop_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The train stop collection location
    title: train stop collection location
    examples:
    - value: end
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - train stop collection location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000839
    multivalued: false
    alias: train_stop_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: train_stop_loc_enum
  turbidity:
    name: turbidity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: formazin turbidity unit, formazin nephelometric units
      occurrence:
        tag: occurrence
        value: '1'
    description: Measure of the amount of cloudiness or haziness in water caused by
      individual particles
    title: turbidity
    examples:
    - value: 0.3 nephelometric turbidity units
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - turbidity
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000191
    multivalued: false
    alias: turbidity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tvdss_of_hcr_press:
    name: tvdss_of_hcr_press
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: True vertical depth subsea (TVDSS) of the hydrocarbon resource where
      the original pressure was measured (e.g. 1578 m).
    title: depth (TVDSS) of hydrocarbon resource pressure
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - depth (TVDSS) of hydrocarbon resource pressure
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000397
    multivalued: false
    alias: tvdss_of_hcr_press
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  tvdss_of_hcr_temp:
    name: tvdss_of_hcr_temp
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter
      occurrence:
        tag: occurrence
        value: '1'
    description: True vertical depth subsea (TVDSS) of the hydrocarbon resource where
      the original temperature was measured (e.g. 1345 m).
    title: depth (TVDSS) of hydrocarbon resource temperature
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - depth (TVDSS) of hydrocarbon resource temperature
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000394
    multivalued: false
    alias: tvdss_of_hcr_temp
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  typ_occup_density:
    name: typ_occup_density
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      occurrence:
        tag: occurrence
        value: '1'
    description: Customary or normal density of occupants
    title: typical occupant density
    examples:
    - value: '25'
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - typical occupant density
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000771
    multivalued: false
    alias: typ_occup_density
    owner: Biosample
    domain_of:
    - Biosample
    range: double
  ventilation_rate:
    name: ventilation_rate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: cubic meter per minute, liters per second
      occurrence:
        tag: occurrence
        value: '1'
    description: Ventilation rate of the system in the sampled premises
    title: ventilation rate
    examples:
    - value: 750 cubic meter per minute
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ventilation rate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000114
    multivalued: false
    alias: ventilation_rate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  ventilation_type:
    name: ventilation_type
    annotations:
      expected_value:
        tag: expected_value
        value: ventilation type name
      occurrence:
        tag: occurrence
        value: '1'
    description: Ventilation system used in the sampled premises
    title: ventilation type
    examples:
    - value: Operable windows
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - ventilation type
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000756
    multivalued: false
    alias: ventilation_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  vfa:
    name: vfa
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of Volatile Fatty Acids in the sample
    title: volatile fatty acids
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - volatile fatty acids
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000152
    multivalued: false
    alias: vfa
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  vfa_fw:
    name: vfa_fw
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter
      occurrence:
        tag: occurrence
        value: '1'
    description: Original volatile fatty acid concentration in the hydrocarbon resource
    title: vfa in formation water
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - vfa in formation water
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000408
    multivalued: false
    alias: vfa_fw
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  vis_media:
    name: vis_media
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The building visual media
    title: visual media
    examples:
    - value: 3D scans
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - visual media
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000840
    multivalued: false
    alias: vis_media
    owner: Biosample
    domain_of:
    - Biosample
    range: vis_media_enum
  viscosity:
    name: viscosity
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;measurement value
      preferred_unit:
        tag: preferred_unit
        value: cP at degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: A measure of oil's resistance¬†to gradual deformation by¬†shear stress¬†or¬†tensile
      stress (e.g. 3.5 cp; 100 ¬∞C)
    title: viscosity
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - viscosity
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{float} {unit}'
    slot_uri: MIXS:0000126
    multivalued: false
    alias: viscosity
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  volatile_org_comp:
    name: volatile_org_comp
    annotations:
      expected_value:
        tag: expected_value
        value: volatile organic compound name;measurement value
      preferred_unit:
        tag: preferred_unit
        value: microgram per cubic meter, parts per million, nanogram per liter
      occurrence:
        tag: occurrence
        value: m
    description: Concentration of carbon-based chemicals that easily evaporate at
      room temperature; can report multiple volatile organic compounds by entering
      numeric values preceded by name of compound
    title: volatile organic compounds
    examples:
    - value: formaldehyde;500 nanogram per liter
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - volatile organic compounds
    rank: 1000
    is_a: core field
    string_serialization: '{text};{float} {unit}'
    slot_uri: MIXS:0000115
    multivalued: true
    alias: volatile_org_comp
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  wall_area:
    name: wall_area
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The total area of the sampled room's walls
    title: wall area
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall area
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000198
    multivalued: false
    alias: wall_area
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  wall_const_type:
    name: wall_const_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The building class of the wall defined by the composition of the
      building elements and fire-resistance rating.
    title: wall construction type
    examples:
    - value: fire resistive
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall construction type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000841
    multivalued: false
    alias: wall_const_type
    owner: Biosample
    domain_of:
    - Biosample
    range: wall_const_type_enum
  wall_finish_mat:
    name: wall_finish_mat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The material utilized to finish the outer most layer of the wall
    title: wall finish material
    examples:
    - value: wood
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall finish material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000842
    multivalued: false
    alias: wall_finish_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: wall_finish_mat_enum
  wall_height:
    name: wall_height
    annotations:
      expected_value:
        tag: expected_value
        value: value
      preferred_unit:
        tag: preferred_unit
        value: centimeter
      occurrence:
        tag: occurrence
        value: '1'
    description: The average height of the walls in the sampled room
    title: wall height
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall height
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000221
    multivalued: false
    alias: wall_height
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  wall_loc:
    name: wall_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The relative location of the wall within the room
    title: wall location
    examples:
    - value: north
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000843
    multivalued: false
    alias: wall_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: wall_loc_enum
  wall_surf_treatment:
    name: wall_surf_treatment
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The surface treatment of interior wall
    title: wall surface treatment
    examples:
    - value: paneling
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall surface treatment
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000845
    multivalued: false
    alias: wall_surf_treatment
    owner: Biosample
    domain_of:
    - Biosample
    range: wall_surf_treatment_enum
  wall_texture:
    name: wall_texture
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The feel, appearance, or consistency of a wall surface
    title: wall texture
    examples:
    - value: popcorn
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall texture
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000846
    multivalued: false
    alias: wall_texture
    owner: Biosample
    domain_of:
    - Biosample
    range: wall_texture_enum
  wall_thermal_mass:
    name: wall_thermal_mass
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: joule per degree Celsius
      occurrence:
        tag: occurrence
        value: '1'
    description: The ability of the wall to provide inertia against temperature fluctuations.
      Generally this means concrete or concrete block that is either exposed or covered
      only with paint
    title: wall thermal mass
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall thermal mass
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000222
    multivalued: false
    alias: wall_thermal_mass
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  wall_water_mold:
    name: wall_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew on a wall
    title: wall signs of water/mold
    examples:
    - value: no presence of mold visible
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wall signs of water/mold
    rank: 1000
    is_a: core field
    string_serialization: '[presence of mold visible|no presence of mold visible]'
    slot_uri: MIXS:0000844
    multivalued: false
    alias: wall_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  wastewater_type:
    name: wastewater_type
    annotations:
      expected_value:
        tag: expected_value
        value: wastewater type name
      occurrence:
        tag: occurrence
        value: '1'
    description: The origin of wastewater such as human waste, rainfall, storm drains,
      etc.
    title: wastewater type
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wastewater type
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000353
    multivalued: false
    alias: wastewater_type
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  water_cont_soil_meth:
    name: water_cont_soil_meth
    description: Reference or method used in determining the water content of soil
    title: water content method
    todos:
    - Why is it soil water content method in the name but not the title? Is this slot
      used in other samples?
    - Soil water content can be measure MANY ways and often, multiple ways are used
      in one experiment (gravimetric water content and water holding capacity and
      water filled pore space, to name a few).
    - Should this be multi valued? How to we manage and validate this?
    comments:
    - Required if providing water content
    examples:
    - value: J. Nat. Prod. Plant Resour., 2012, 2 (4):500-503
    - value: https://dec.alaska.gov/applications/spar/webcalc/definitions.htm
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{PMID}|{DOI}|{URL}'
    slot_uri: MIXS:0000323
    multivalued: false
    alias: water_cont_soil_meth
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  water_content:
    name: water_content
    annotations:
      expected_value:
        tag: expected_value
        value: string
      preferred_unit:
        tag: preferred_unit
        value: gram per gram or cubic centimeter per cubic centimeter
    description: Water content measurement
    title: water content
    todos:
    - value in preferred unit is too limiting. need to change this
    - check and correct validation so examples are accepted
    - how to manage multiple water content methods?
    examples:
    - value: 0.75 g water/g dry soil
    - value: 75% water holding capacity
    - value: 1.1 g fresh weight/ dry weight
    - value: 10% water filled pore space
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000185
    multivalued: true
    alias: water_content
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  water_current:
    name: water_current
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: cubic meter per second, knots
      occurrence:
        tag: occurrence
        value: '1'
    description: Measurement of magnitude and direction of flow within a fluid
    title: water current
    examples:
    - value: 10 cubic meter per second
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water current
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000203
    multivalued: false
    alias: water_current
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  water_cut:
    name: water_cut
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: percent
      occurrence:
        tag: occurrence
        value: '1'
    description: Current amount of water (%) in a produced fluid stream; or the average
      of the combined streams
    title: water cut
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water cut
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000454
    multivalued: false
    alias: water_cut
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  water_feat_size:
    name: water_feat_size
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: square meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The size of the water feature
    title: water feature size
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water feature size
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000223
    multivalued: false
    alias: water_feat_size
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  water_feat_type:
    name: water_feat_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of water feature present within the building being sampled
    title: water feature type
    examples:
    - value: stream
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water feature type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000847
    multivalued: false
    alias: water_feat_type
    owner: Biosample
    domain_of:
    - Biosample
    range: water_feat_type_enum
  water_prod_rate:
    name: water_prod_rate
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: cubic meter per day
      occurrence:
        tag: occurrence
        value: '1'
    description: Water production rates per well (e.g. 987 m3 / day)
    title: water production rate
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water production rate
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000453
    multivalued: false
    alias: water_prod_rate
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  water_temp_regm:
    name: water_temp_regm
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value;treatment interval and duration
      preferred_unit:
        tag: preferred_unit
        value: degree Celsius
      occurrence:
        tag: occurrence
        value: m
    description: Information about treatment involving an exposure to water with varying
      degree of temperature, treatment regimen including how many times the treatment
      was repeated, how long each treatment lasted, and the start and end time of
      the entire treatment; can include multiple regimens
    title: water temperature regimen
    examples:
    - value: 15 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - water temperature regimen
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000590
    multivalued: true
    alias: water_temp_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  watering_regm:
    name: watering_regm
    description: Information about treatment involving an exposure to watering frequencies,
      treatment regimen including how many times the treatment was repeated, how long
      each treatment lasted, and the start and end time of the entire treatment; can
      include multiple regimens
    title: watering regimen
    examples:
    - value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
    - value: 75% water holding capacity; constant
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
    slot_uri: MIXS:0000591
    multivalued: true
    alias: watering_regm
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  weekday:
    name: weekday
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The day of the week when sampling occurred
    title: weekday
    examples:
    - value: Sunday
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - weekday
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000848
    multivalued: false
    alias: weekday
    owner: Biosample
    domain_of:
    - Biosample
    range: weekday_enum
  win:
    name: win
    annotations:
      expected_value:
        tag: expected_value
        value: text
      occurrence:
        tag: occurrence
        value: '1'
    description: 'A unique identifier of a well or wellbore. This is part of the Global
      Framework for Well Identification initiative which is compiled by the Professional
      Petroleum Data Management Association (PPDM) in an effort to improve well identification
      systems. (Supporting information: https://ppdm.org/ and http://dl.ppdm.org/dl/690)'
    title: well identification number
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - well identification number
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000297
    multivalued: false
    alias: win
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  wind_direction:
    name: wind_direction
    annotations:
      expected_value:
        tag: expected_value
        value: wind direction name
      occurrence:
        tag: occurrence
        value: '1'
    description: Wind direction is the direction from which a wind originates
    title: wind direction
    examples:
    - value: Northwest
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wind direction
    rank: 1000
    is_a: core field
    string_serialization: '{text}'
    slot_uri: MIXS:0000757
    multivalued: false
    alias: wind_direction
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  wind_speed:
    name: wind_speed
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: meter per second, kilometer per hour
      occurrence:
        tag: occurrence
        value: '1'
    description: Speed of wind measured at the time of sampling
    title: wind speed
    examples:
    - value: 21 kilometer per hour
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - wind speed
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000118
    multivalued: false
    alias: wind_speed
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  window_cond:
    name: window_cond
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The physical condition of the window at the time of sampling
    title: window condition
    examples:
    - value: rupture
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window condition
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000849
    multivalued: false
    alias: window_cond
    owner: Biosample
    domain_of:
    - Biosample
    range: window_cond_enum
  window_cover:
    name: window_cover
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of window covering
    title: window covering
    examples:
    - value: curtains
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window covering
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000850
    multivalued: false
    alias: window_cover
    owner: Biosample
    domain_of:
    - Biosample
    range: window_cover_enum
  window_horiz_pos:
    name: window_horiz_pos
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The horizontal position of the window on the wall
    title: window horizontal position
    examples:
    - value: middle
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window horizontal position
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000851
    multivalued: false
    alias: window_horiz_pos
    owner: Biosample
    domain_of:
    - Biosample
    range: window_horiz_pos_enum
  window_loc:
    name: window_loc
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The relative location of the window within the room
    title: window location
    examples:
    - value: west
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window location
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000852
    multivalued: false
    alias: window_loc
    owner: Biosample
    domain_of:
    - Biosample
    range: window_loc_enum
  window_mat:
    name: window_mat
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of material used to finish a window
    title: window material
    examples:
    - value: wood
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window material
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000853
    multivalued: false
    alias: window_mat
    owner: Biosample
    domain_of:
    - Biosample
    range: window_mat_enum
  window_open_freq:
    name: window_open_freq
    annotations:
      expected_value:
        tag: expected_value
        value: value
      occurrence:
        tag: occurrence
        value: '1'
    description: The number of times windows are opened per week
    title: window open frequency
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window open frequency
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000246
    multivalued: false
    alias: window_open_freq
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  window_size:
    name: window_size
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: inch, meter
      occurrence:
        tag: occurrence
        value: '1'
    description: The window's length and width
    title: window area/size
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window area/size
    rank: 1000
    is_a: core field
    string_serialization: '{float} {unit} x {float} {unit}'
    slot_uri: MIXS:0000224
    multivalued: false
    alias: window_size
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  window_status:
    name: window_status
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Defines whether the windows were open or closed during environmental
      testing
    title: window status
    examples:
    - value: open
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window status
    rank: 1000
    is_a: core field
    string_serialization: '[closed|open]'
    slot_uri: MIXS:0000855
    multivalued: false
    alias: window_status
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  window_type:
    name: window_type
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The type of windows
    title: window type
    examples:
    - value: fixed window
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window type
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000856
    multivalued: false
    alias: window_type
    owner: Biosample
    domain_of:
    - Biosample
    range: window_type_enum
  window_vert_pos:
    name: window_vert_pos
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: The vertical position of the window on the wall
    title: window vertical position
    examples:
    - value: middle
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window vertical position
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000857
    multivalued: false
    alias: window_vert_pos
    owner: Biosample
    domain_of:
    - Biosample
    range: window_vert_pos_enum
  window_water_mold:
    name: window_water_mold
    annotations:
      expected_value:
        tag: expected_value
        value: enumeration
      occurrence:
        tag: occurrence
        value: '1'
    description: Signs of the presence of mold or mildew on the window.
    title: window signs of water/mold
    examples:
    - value: no presence of mold visible
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - window signs of water/mold
    rank: 1000
    is_a: core field
    string_serialization: '[presence of mold visible|no presence of mold visible]'
    slot_uri: MIXS:0000854
    multivalued: false
    alias: window_water_mold
    owner: Biosample
    domain_of:
    - Biosample
    range: TextValue
  xylene:
    name: xylene
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: milligram per liter, parts per million
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of xylene in the sample
    title: xylene
    examples:
    - value: ''
    from_schema: https://w3id.org/nmdc/nmdc
    aliases:
    - xylene
    rank: 1000
    is_a: core field
    slot_uri: MIXS:0000156
    multivalued: false
    alias: xylene
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  zinc:
    name: zinc
    annotations:
      expected_value:
        tag: expected_value
        value: measurement value
      preferred_unit:
        tag: preferred_unit
        value: mg/kg (ppm)
      occurrence:
        tag: occurrence
        value: '1'
    description: Concentration of zinc in the sample
    title: zinc
    examples:
    - value: 2.5 mg/kg
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://www.ornl.gov/content/bio-scales-0
    aliases:
    - zinc
    rank: 1000
    alias: zinc
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  add_date:
    name: add_date
    description: The date on which the information was added to the database.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: add_date
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: string
  community:
    name: community
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: community
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  habitat:
    name: habitat
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: habitat
    owner: Biosample
    domain_of:
    - FieldResearchSite
    - Biosample
    range: string
  host_name:
    name: host_name
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: host_name
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  location:
    name: location
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: location
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  mod_date:
    name: mod_date
    description: The last date on which the database information was modified.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: mod_date
    owner: Biosample
    domain_of:
    - Biosample
    - OmicsProcessing
    range: string
  ncbi_taxonomy_name:
    name: ncbi_taxonomy_name
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: ncbi_taxonomy_name
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  proport_woa_temperature:
    name: proport_woa_temperature
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: proport_woa_temperature
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  salinity_category:
    name: salinity_category
    description: 'Categorical description of the sample''s salinity. Examples: halophile,
      halotolerant, hypersaline, huryhaline'
    notes:
    - maps to gold:salinity
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - https://github.com/microbiomedata/nmdc-metadata/pull/297
    rank: 1000
    alias: salinity_category
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  sample_collection_site:
    name: sample_collection_site
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: sample_collection_site
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  soluble_iron_micromol:
    name: soluble_iron_micromol
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: soluble_iron_micromol
    owner: Biosample
    domain_of:
    - Biosample
    range: string
  subsurface_depth:
    name: subsurface_depth
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: subsurface_depth
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  dna_absorb1:
    name: dna_absorb1
    description: 260/280 measurement of DNA sample purity
    title: DNA absorbance 260/280
    comments:
    - Recommended value is between 1 and 3.
    examples:
    - value: '2.02'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 7
    is_a: biomaterial_purity
    domain: ProcessedSample
    alias: dna_absorb1
    owner: Biosample
    domain_of:
    - Biosample
    - ProcessedSample
    slot_group: JGI-Metagenomics
    range: float
    recommended: true
  dna_absorb2:
    name: dna_absorb2
    description: 260/230 measurement of DNA sample purity
    title: DNA absorbance 260/230
    comments:
    - Recommended value is between 1 and 3.
    examples:
    - value: '2.02'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 8
    is_a: biomaterial_purity
    domain: ProcessedSample
    alias: dna_absorb2
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: float
    recommended: true
  dna_collect_site:
    name: dna_collect_site
    description: Provide information on the site your DNA sample was collected from
    title: DNA collection site
    examples:
    - value: untreated pond water
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 15
    string_serialization: '{text}'
    alias: dna_collect_site
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_concentration:
    name: dna_concentration
    title: DNA concentration in ng/ul
    comments:
    - Units must be in ng/uL. Enter the numerical part only. Must be calculated using
      a fluorometric method. Acceptable values are 0-2000.
    examples:
    - value: '100'
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - nmdc:nucleic_acid_concentration
    rank: 5
    alias: dna_concentration
    owner: Biosample
    domain_of:
    - Biosample
    - ProcessedSample
    slot_group: JGI-Metagenomics
    range: float
    recommended: true
    minimum_value: 0
    maximum_value: 2000
  dna_cont_type:
    name: dna_cont_type
    description: Tube or plate (96-well)
    title: DNA container type
    examples:
    - value: plate
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 10
    alias: dna_cont_type
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: JgiContTypeEnum
    recommended: true
  dna_container_id:
    name: dna_container_id
    title: DNA container label
    comments:
    - Must be unique across all tubes and plates, and <20 characters. All samples
      in a plate should have the same plate label.
    examples:
    - value: Pond_MT_041618
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 9
    string_serialization: '{text < 20 characters}'
    alias: dna_container_id
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_dnase:
    name: dna_dnase
    title: DNase treatment DNA
    comments:
    - Note DNase treatment is required for all RNA samples.
    examples:
    - value: 'no'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 13
    alias: dna_dnase
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: YesNoEnum
    recommended: true
  dna_isolate_meth:
    name: dna_isolate_meth
    description: Describe the method/protocol/kit used to extract DNA/RNA.
    title: DNA isolation method
    examples:
    - value: phenol/chloroform extraction
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 16
    string_serialization: '{text}'
    alias: dna_isolate_meth
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_organisms:
    name: dna_organisms
    description: List any organisms known or suspected to grow in co-culture, as well
      as estimated % of the organism in that culture.
    title: DNA expected organisms
    examples:
    - value: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
        (1%)
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 14
    string_serialization: '{text}'
    alias: dna_organisms
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_project_contact:
    name: dna_project_contact
    title: DNA seq project contact
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: John Jones
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 18
    string_serialization: '{text}'
    alias: dna_project_contact
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_samp_id:
    name: dna_samp_id
    title: DNA sample ID
    todos:
    - Removed identifier = TRUE from dna_samp_ID in JGI_sample_slots, as a class can't
      have two identifiers. How to force uniqueness? Moot because that column will
      be prefilled?
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '187654'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 3
    string_serialization: '{text}'
    alias: dna_samp_id
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_sample_format:
    name: dna_sample_format
    description: Solution in which the DNA sample has been suspended
    title: DNA sample format
    examples:
    - value: Water
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 12
    alias: dna_sample_format
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: dna_sample_format_enum
    recommended: true
  dna_sample_name:
    name: dna_sample_name
    description: Give the DNA sample a name that is meaningful to you. Sample names
      must be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only.
    title: DNA sample name
    examples:
    - value: JGI_pond_041618
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 4
    string_serialization: '{text}'
    alias: dna_sample_name
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_seq_project:
    name: dna_seq_project
    title: DNA seq project ID
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '1191234'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1
    string_serialization: '{text}'
    alias: dna_seq_project
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_seq_project_pi:
    name: dna_seq_project_pi
    title: DNA seq project PI
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: Jane Johnson
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 17
    string_serialization: '{text}'
    alias: dna_seq_project_pi
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_seq_project_name:
    name: dna_seq_project_name
    title: DNA seq project name
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: JGI Pond metagenomics
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 2
    string_serialization: '{text}'
    alias: dna_seq_project_name
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dna_volume:
    name: dna_volume
    title: DNA volume in ul
    comments:
    - Units must be in uL. Enter the numerical part only. Value must be 0-1000. This
      form accepts values < 25, but JGI may refuse to process them unless permission
      has been granted by a project manager
    examples:
    - value: '25'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 6
    string_serialization: '{float}'
    alias: dna_volume
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: float
    recommended: true
    minimum_value: 0
    maximum_value: 1000
  proposal_dna:
    name: proposal_dna
    title: DNA proposal ID
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '504000'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 19
    string_serialization: '{text}'
    alias: proposal_dna
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metagenomics
    range: string
    recommended: true
  dnase_rna:
    name: dnase_rna
    title: DNase treated
    comments:
    - Note DNase treatment is required for all RNA samples.
    examples:
    - value: 'no'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 13
    alias: dnase_rna
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: YesNoEnum
    recommended: true
  proposal_rna:
    name: proposal_rna
    title: RNA proposal ID
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '504000'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 19
    string_serialization: '{text}'
    alias: proposal_rna
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_absorb1:
    name: rna_absorb1
    description: 260/280 measurement of RNA sample purity
    title: RNA absorbance 260/280
    comments:
    - Recommended value is between 1 and 3.
    examples:
    - value: '2.02'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 7
    is_a: biomaterial_purity
    string_serialization: '{float}'
    domain: ProcessedSample
    alias: rna_absorb1
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: float
    recommended: true
  rna_absorb2:
    name: rna_absorb2
    description: 260/230 measurement of RNA sample purity
    title: RNA absorbance 260/230
    comments:
    - Recommended value is between 1 and 3.
    examples:
    - value: '2.02'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 8
    is_a: biomaterial_purity
    string_serialization: '{float}'
    domain: ProcessedSample
    alias: rna_absorb2
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: float
    recommended: true
  rna_collect_site:
    name: rna_collect_site
    description: Provide information on the site your RNA sample was collected from
    title: RNA collection site
    examples:
    - value: untreated pond water
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 15
    string_serialization: '{text}'
    alias: rna_collect_site
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_concentration:
    name: rna_concentration
    title: RNA concentration in ng/ul
    comments:
    - Units must be in ng/uL. Enter the numerical part only. Must be calculated using
      a fluorometric method. Acceptable values are 0-2000.
    examples:
    - value: '100'
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - nmdc:nucleic_acid_concentration
    rank: 5
    string_serialization: '{float}'
    alias: rna_concentration
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: float
    recommended: true
    minimum_value: 0
    maximum_value: 1000
  rna_cont_type:
    name: rna_cont_type
    description: Tube or plate (96-well)
    title: RNA container type
    examples:
    - value: plate
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 10
    alias: rna_cont_type
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: JgiContTypeEnum
    recommended: true
  rna_cont_well:
    name: rna_cont_well
    title: RNA plate position
    comments:
    - Required when 'plate' is selected for container type.
    - Leave blank if the sample will be shipped in a tube.
    - JGI will not process samples in corner wells, so A1, A12, H1 and H12 will not
      pass validation.
    - For partial plates, fill by columns, like B1-G1,A2-H2,A3-D3 (NOT A2-A11,B1-B8).
    examples:
    - value: B2
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 11
    string_serialization: '{96 well plate pos}'
    alias: rna_cont_well
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
    pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  rna_container_id:
    name: rna_container_id
    title: RNA container label
    comments:
    - Must be unique across all tubes and plates, and <20 characters. All samples
      in a plate should have the same plate label.
    examples:
    - value: Pond_MT_041618
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 9
    string_serialization: '{text < 20 characters}'
    alias: rna_container_id
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_isolate_meth:
    name: rna_isolate_meth
    description: Describe the method/protocol/kit used to extract DNA/RNA.
    title: RNA isolation method
    examples:
    - value: phenol/chloroform extraction
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 16
    string_serialization: '{text}'
    alias: rna_isolate_meth
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_organisms:
    name: rna_organisms
    description: List any organisms known or suspected to grow in co-culture, as well
      as estimated % of the organism in that culture.
    title: RNA expected organisms
    examples:
    - value: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles
        (1%)
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 14
    string_serialization: '{text}'
    alias: rna_organisms
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_project_contact:
    name: rna_project_contact
    title: RNA seq project contact
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: John Jones
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 18
    string_serialization: '{text}'
    alias: rna_project_contact
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_samp_id:
    name: rna_samp_id
    title: RNA sample ID
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '187654'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 3
    string_serialization: '{text}'
    alias: rna_samp_id
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_sample_format:
    name: rna_sample_format
    description: Solution in which the RNA sample has been suspended
    title: RNA sample format
    examples:
    - value: Water
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 12
    alias: rna_sample_format
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: rna_sample_format_enum
    recommended: true
  rna_sample_name:
    name: rna_sample_name
    description: Give the RNA sample a name that is meaningful to you. Sample names
      must be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only.
    title: RNA sample name
    examples:
    - value: JGI_pond_041618
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 4
    string_serialization: '{text}'
    alias: rna_sample_name
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
    minimum_value: 0
    maximum_value: 2000
  rna_seq_project:
    name: rna_seq_project
    title: RNA seq project ID
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: '1191234'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1
    string_serialization: '{text}'
    alias: rna_seq_project
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_seq_project_pi:
    name: rna_seq_project_pi
    title: RNA seq project PI
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: Jane Johnson
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 17
    string_serialization: '{text}'
    alias: rna_seq_project_pi
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_seq_project_name:
    name: rna_seq_project_name
    title: RNA seq project name
    comments:
    - Do not edit these values. A template will be provided by NMDC in which these
      values have been pre-filled.
    examples:
    - value: JGI Pond metatranscriptomics
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 2
    string_serialization: '{text}'
    alias: rna_seq_project_name
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: string
    recommended: true
  rna_volume:
    name: rna_volume
    title: RNA volume in ul
    comments:
    - Units must be in uL. Enter the numerical part only. Value must be 0-1000. This
      form accepts values < 25, but JGI may refuse to process them unless permission
      has been granted by a project manager
    examples:
    - value: '25'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 6
    string_serialization: '{float}'
    alias: rna_volume
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: JGI-Metatranscriptomics
    range: float
    recommended: true
    minimum_value: 0
    maximum_value: 1000
  collection_date_inc:
    name: collection_date_inc
    description: Date the incubation was harvested/collected/ended. Only relevant
      for incubation samples.
    title: incubation collection date
    notes:
    - MIxS collection_date accepts (truncated) ISO8601. DH taking arbitrary precision
      date only
    comments:
    - Date should be formatted as YYYY(-MM(-DD)). Ie, 2021-04-15, 2021-04 and 2021
      are all acceptable.
    examples:
    - value: 2021-04-15, 2021-04 and 2021 are all acceptable.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000011
    rank: 2
    string_serialization: '{date, arbitrary precision}'
    alias: collection_date_inc
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  collection_time:
    name: collection_time
    description: The time of sampling, either as an instance (single point) or interval.
    title: collection time, GMT
    notes:
    - MIxS collection_date accepts (truncated) ISO8601. DH taking seconds optional
      time only
    comments:
    - 'Time should be entered as HH:MM(:SS) in GMT. See here for a converter: https://www.worldtimebuddy.com/pst-to-gmt-converter'
    examples:
    - value: 13:33 or 13:33:55
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000011
    rank: 1
    string_serialization: '{time, seconds optional}'
    alias: collection_time
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  collection_time_inc:
    name: collection_time_inc
    description: Time the incubation was harvested/collected/ended. Only relevant
      for incubation samples.
    title: incubation collection time, GMT
    notes:
    - MIxS collection_date accepts (truncated) ISO8601. DH taking seconds optional
      time only
    comments:
    - 'Time should be entered as HH:MM(:SS) in GMT. See here for a converter: https://www.worldtimebuddy.com/pst-to-gmt-converter'
    examples:
    - value: 13:33 or 13:33:55
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000011
    rank: 3
    string_serialization: '{time, seconds optional}'
    alias: collection_time_inc
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  experimental_factor_other:
    name: experimental_factor_other
    description: Other details about your sample that you feel can't be accurately
      represented in the available columns.
    title: experimental factor- other
    comments:
    - This slot accepts open-ended text about your sample.
    - We recommend using key:value pairs.
    - Provided pairs will be considered for inclusion as future slots/terms in this
      data collection template.
    examples:
    - value: 'experimental treatment: value'
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000008
    - MIXS:0000300
    rank: 7
    string_serialization: '{text}'
    alias: experimental_factor_other
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  filter_method:
    name: filter_method
    description: Type of filter used or how the sample was filtered
    title: filter method
    comments:
    - describe the filter or provide a catalog number and manufacturer
    examples:
    - value: C18
    - value: Basix PES, 13-100-106 FisherSci
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000765
    rank: 6
    string_serialization: '{text}'
    alias: filter_method
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  isotope_exposure:
    name: isotope_exposure
    description: List isotope exposure or addition applied to your sample.
    title: isotope exposure/addition
    todos:
    - Can we make the H218O correctly super and subscripted?
    comments:
    - This is required when your experimental design includes the use of isotopically
      labeled compounds
    examples:
    - value: 13C glucose
    - value: H218O
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000751
    rank: 16
    string_serialization: '{termLabel} {[termID]}; {timestamp}'
    alias: isotope_exposure
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  micro_biomass_c_meth:
    name: micro_biomass_c_meth
    description: Reference or method used in determining microbial biomass carbon
    title: microbial biomass carbon method
    todos:
    - How should we separate values? | or ;? lets be consistent
    comments:
    - required if "microbial_biomass_c" is provided
    examples:
    - value: https://doi.org/10.1016/0038-0717(87)90052-6
    - value: https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000339
    rank: 11
    string_serialization: '{PMID}|{DOI}|{URL}'
    alias: micro_biomass_c_meth
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  micro_biomass_n_meth:
    name: micro_biomass_n_meth
    description: Reference or method used in determining microbial biomass nitrogen
    title: microbial biomass nitrogen method
    comments:
    - required if "microbial_biomass_n" is provided
    examples:
    - value: https://doi.org/10.1016/0038-0717(87)90052-6
    - value: https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000339
    rank: 13
    string_serialization: '{PMID}|{DOI}|{URL}'
    alias: micro_biomass_n_meth
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  microbial_biomass_c:
    name: microbial_biomass_c
    description: The part of the organic matter in the soil that constitutes living
      microorganisms smaller than 5-10 micrometer.
    title: microbial biomass carbon
    comments:
    - If you provide this, correction factors used for conversion to the final units
      and method are required
    examples:
    - value: 0.05 ug C/g dry soil
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000650
    rank: 10
    string_serialization: '{float} {unit}'
    alias: microbial_biomass_c
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  microbial_biomass_n:
    name: microbial_biomass_n
    description: The part of the organic matter in the soil that constitutes living
      microorganisms smaller than 5-10 micrometer.
    title: microbial biomass nitrogen
    comments:
    - If you provide this, correction factors used for conversion to the final units
      and method are required
    examples:
    - value: 0.05 ug N/g dry soil
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000650
    rank: 12
    string_serialization: '{float} {unit}'
    alias: microbial_biomass_n
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  non_microb_biomass:
    name: non_microb_biomass
    description: Amount of biomass; should include the name for the part of biomass
      measured, e.g.insect, plant, total. Can include multiple measurements separated
      by ;
    title: non-microbial biomass
    examples:
    - value: insect 0.23 ug; plant 1g
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000174
    - MIXS:0000650
    rank: 8
    string_serialization: '{text};{float} {unit}'
    alias: non_microb_biomass
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  non_microb_biomass_method:
    name: non_microb_biomass_method
    description: Reference or method used in determining biomass
    title: non-microbial biomass method
    comments:
    - required if "non-microbial biomass" is provided
    examples:
    - value: https://doi.org/10.1038/s41467-021-26181-3
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000650
    rank: 9
    string_serialization: '{PMID}|{DOI}|{URL}'
    alias: non_microb_biomass_method
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  org_nitro_method:
    name: org_nitro_method
    description: Method used for obtaining organic nitrogen
    title: organic nitrogen method
    comments:
    - required if "org_nitro" is provided
    examples:
    - value: https://doi.org/10.1016/0038-0717(85)90144-0
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000338
    - MIXS:0000205
    rank: 14
    string_serialization: '{PMID}|{DOI}|{URL}'
    alias: org_nitro_method
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
  other_treatment:
    name: other_treatment
    description: Other treatments applied to your samples that are not applicable
      to the provided fields
    title: other treatments
    notes:
    - Values entered here will be used to determine potential new slots.
    comments:
    - This is an open text field to provide any treatments that cannot be captured
      in the provided slots.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000300
    rank: 15
    string_serialization: '{text}'
    alias: other_treatment
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  start_date_inc:
    name: start_date_inc
    description: Date the incubation was started. Only relevant for incubation samples.
    title: incubation start date
    notes:
    - MIxS collection_date accepts (truncated) ISO8601. DH taking arbitrary precision
      date only
    comments:
    - Date should be formatted as YYYY(-MM(-DD)). Ie, 2021-04-15, 2021-04 and 2021
      are all acceptable.
    examples:
    - value: 2021-04-15, 2021-04 and 2021 are all acceptable.
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000011
    rank: 4
    string_serialization: '{date, arbitrary precision}'
    alias: start_date_inc
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  start_time_inc:
    name: start_time_inc
    description: Time the incubation was started. Only relevant for incubation samples.
    title: incubation start time, GMT
    notes:
    - MIxS collection_date accepts (truncated) ISO8601. DH taking seconds optional
      time only
    comments:
    - 'Time should be entered as HH:MM(:SS) in GMT. See here for a converter: https://www.worldtimebuddy.com/pst-to-gmt-converter'
    examples:
    - value: 13:33 or 13:33:55
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIXS:0000011
    rank: 5
    string_serialization: '{time, seconds optional}'
    alias: start_time_inc
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: MIxS Inspired
    range: string
    recommended: true
  project_id:
    name: project_id
    description: Proposal IDs or names associated with dataset
    title: project ID
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1
    string_serialization: '{text}'
    alias: project_id
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: EMSL
    range: string
    recommended: true
  replicate_number:
    name: replicate_number
    description: If sending biological replicates, indicate the rep number here.
    title: replicate number
    comments:
    - This will guide staff in ensuring your samples are blocked & randomized correctly
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 6
    string_serialization: '{integer}'
    alias: replicate_number
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: EMSL
    range: string
    recommended: true
  sample_shipped:
    name: sample_shipped
    description: The total amount or size (volume (ml), mass (g) or area (m2) ) of
      sample sent to EMSL.
    title: sample shipped amount
    comments:
    - This field is only required when completing metadata for samples being submitted
      to EMSL for analyses.
    examples:
    - value: 15 g
    - value: 100 uL
    - value: 5 mL
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 3
    string_serialization: '{float} {unit}'
    alias: sample_shipped
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: EMSL
    range: string
    recommended: true
  sample_type:
    name: sample_type
    description: Type of sample being submitted
    title: sample type
    comments:
    - This can vary from 'environmental package' if the sample is an extraction.
    examples:
    - value: water extracted soil
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 2
    alias: sample_type
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: EMSL
    range: sample_type_enum
    recommended: true
  technical_reps:
    name: technical_reps
    description: If sending technical replicates of the same sample, indicate the
      replicate count.
    title: number technical replicate
    comments:
    - This field is only required when completing metadata for samples being submitted
      to EMSL for analyses.
    examples:
    - value: '2'
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 5
    string_serialization: '{integer}'
    alias: technical_reps
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: EMSL
    range: string
    recommended: true
  analysis_type:
    name: analysis_type
    description: Select all the data types associated or available for this biosample
    title: analysis/data type
    examples:
    - value: metagenomics; metabolomics; proteomics
    from_schema: https://w3id.org/nmdc/nmdc
    see_also:
    - MIxS:investigation_type
    rank: 3
    multivalued: true
    alias: analysis_type
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: Sample ID
    range: analysis_type_enum
    recommended: true
  sample_link:
    name: sample_link
    description: A unique identifier to assign parent-child, subsample, or sibling
      samples. This is relevant when a sample or other material was used to generate
      the new sample.
    title: sample linkage
    comments:
    - 'This field allows multiple entries separated by ; (Examples: Soil collected
      from the field will link with the soil used in an incubation. The soil a plant
      was grown in links to the plant sample. An original culture sample was transferred
      to a new vial and generated a new sample)'
    examples:
    - value: IGSN:DSJ0284
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 5
    string_serialization: '{text}:{text}'
    multivalued: true
    alias: sample_link
    owner: Biosample
    domain_of:
    - Biosample
    slot_group: Sample ID
    range: string
    recommended: true
  bulk_elect_conductivity:
    name: bulk_elect_conductivity
    description: Electrical conductivity is a measure of the ability to carry electric
      current, which is mostly dictated by the chemistry of and amount of water.
    title: bulk electrical conductivity
    comments:
    - Provide the value output of the field instrument.
    examples:
    - value: JsonObj(has_raw_value='0.017 mS/cm', has_numeric_value=0.017, has_unit='mS/cm')
      description: The conductivity measurement was 0.017 millisiemens per centimeter.
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: bulk_elect_conductivity
    owner: Biosample
    domain_of:
    - Biosample
    range: QuantityValue
  name:
    name: name
    description: A human readable label for an entity
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    alias: name
    owner: Biosample
    domain_of:
    - Protocol
    - QualityControlReport
    - NamedThing
    - PersonValue
    - Activity
    range: string
  description:
    name: description
    description: a human-readable description of a thing
    from_schema: https://w3id.org/nmdc/nmdc
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: Biosample
    domain_of:
    - Study
    - NamedThing
    - ImageValue
    range: string
unique_keys:
  samp_name_unique_key:
    unique_key_name: samp_name_unique_key
    unique_key_slots:
    - samp_name
rules:
- preconditions:
    slot_conditions:
      dna_cont_well:
        name: dna_cont_well
        pattern: .+
  postconditions:
    slot_conditions:
      dna_cont_type:
        name: dna_cont_type
        equals_string: plate
  description: DNA samples shipped to JGI for metagenomic analysis in tubes can't
    have any value for their plate position.
  title: dna_well_requires_plate
- preconditions:
    slot_conditions:
      dna_cont_type:
        name: dna_cont_type
        equals_string: plate
  postconditions:
    slot_conditions:
      dna_cont_well:
        name: dna_cont_well
        pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  description: DNA samples in plates must have a plate position that matches the regex.
    Note the requirement for an empty string in the tube case. Waiting for value_present
    validation to be added to runtime
  title: dna_plate_requires_well
- preconditions:
    slot_conditions:
      rna_cont_well:
        name: rna_cont_well
        pattern: .+
  postconditions:
    slot_conditions:
      rna_cont_type:
        name: rna_cont_type
        equals_string: plate
  description: RNA samples shipped to JGI for metagenomic analysis in tubes can't
    have any value for their plate position.
  title: rna_well_requires_plate
- preconditions:
    slot_conditions:
      rna_cont_type:
        name: rna_cont_type
        equals_string: plate
  postconditions:
    slot_conditions:
      rna_cont_well:
        name: rna_cont_well
        pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$
  description: RNA samples in plates must have a plate position that matches the regex.
    Note the requirement for an empty string in the tube case. Waiting for value_present
    validation to be added to runtime
  title: rna_plate_requires_well

```
</details>