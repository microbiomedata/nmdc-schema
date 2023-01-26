

CREATE TABLE "Activity" (
	id TEXT NOT NULL, 
	name TEXT, 
	started_at_time DATETIME, 
	ended_at_time DATETIME, 
	was_informed_by TEXT, 
	was_associated_with TEXT, 
	used TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "AnalyticalSample" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "BiosampleProcessing" (
	name TEXT, 
	description TEXT, 
	has_input TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	inchi TEXT, 
	inchi_key TEXT, 
	chemical_formula TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "CollectingBiosamplesFromSite" (
	name TEXT, 
	description TEXT, 
	participating_agent TEXT, 
	has_outputs TEXT NOT NULL, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Database" (
	activity_set TEXT, 
	biosample_set TEXT, 
	data_object_set TEXT, 
	dissolving_activity_set TEXT, 
	functional_annotation_set TEXT, 
	genome_feature_set TEXT, 
	mags_activity_set TEXT, 
	material_sample_set TEXT, 
	material_sampling_activity_set TEXT, 
	metabolomics_analysis_activity_set TEXT, 
	metagenome_annotation_activity_set TEXT, 
	metagenome_assembly_set TEXT, 
	metaproteomics_analysis_activity_set TEXT, 
	metatranscriptome_activity_set TEXT, 
	nom_analysis_activity_set TEXT, 
	omics_processing_set TEXT, 
	reaction_activity_set TEXT, 
	read_qc_analysis_activity_set TEXT, 
	read_based_taxonomy_analysis_activity_set TEXT, 
	study_set TEXT, 
	field_research_site_set TEXT, 
	collecting_biosamples_from_site_set TEXT, 
	date_created TEXT, 
	etl_software_version TEXT, 
	PRIMARY KEY (activity_set, biosample_set, data_object_set, dissolving_activity_set, functional_annotation_set, genome_feature_set, mags_activity_set, material_sample_set, material_sampling_activity_set, metabolomics_analysis_activity_set, metagenome_annotation_activity_set, metagenome_assembly_set, metaproteomics_analysis_activity_set, metatranscriptome_activity_set, nom_analysis_activity_set, omics_processing_set, reaction_activity_set, read_qc_analysis_activity_set, read_based_taxonomy_analysis_activity_set, study_set, field_research_site_set, collecting_biosamples_from_site_set, date_created, etl_software_version)
);

CREATE TABLE "EnvironmentalMaterialTerm" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "FieldResearchSite" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "GeneProduct" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Instrument" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "LabDevice" (
	device_type VARCHAR(14), 
	activity_speed TEXT, 
	activity_temperature TEXT, 
	activity_time TEXT, 
	PRIMARY KEY (device_type, activity_speed, activity_temperature, activity_time)
);

CREATE TABLE "MaterialContainer" (
	container_size TEXT, 
	container_type VARCHAR(17), 
	PRIMARY KEY (container_size, container_type)
);

CREATE TABLE "MaterialSample" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "OmicsProcessing" (
	name TEXT, 
	description TEXT, 
	add_date TEXT, 
	mod_date TEXT, 
	instrument_name TEXT, 
	ncbi_project_name TEXT, 
	omics_type TEXT, 
	principal_investigator TEXT, 
	processing_institution VARCHAR(4), 
	type TEXT, 
	samp_vol_we_dna_ext TEXT, 
	nucl_acid_ext TEXT, 
	nucl_acid_amp TEXT, 
	target_gene TEXT, 
	target_subfragment TEXT, 
	pcr_primers TEXT, 
	pcr_cond TEXT, 
	seq_meth TEXT, 
	seq_quality_check TEXT, 
	chimera_check TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "OntologyClass" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OrthologyGroup" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Pathway" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	name TEXT, 
	description TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Study" (
	id TEXT NOT NULL, 
	massive_study_identifier TEXT, 
	related_identifiers TEXT, 
	emsl_proposal_identifier TEXT, 
	emsl_proposal_doi TEXT, 
	mgnify_project_identifiers TEXT, 
	ecosystem TEXT, 
	ecosystem_category TEXT, 
	ecosystem_type TEXT, 
	ecosystem_subtype TEXT, 
	specific_ecosystem TEXT, 
	principal_investigator TEXT, 
	doi TEXT, 
	title TEXT, 
	abstract TEXT, 
	objective TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	notes TEXT, 
	insdc_bioproject_identifiers TEXT, 
	emsl_project_identifier TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Agent" (
	acted_on_behalf_of TEXT, 
	was_informed_by TEXT, 
	PRIMARY KEY (acted_on_behalf_of, was_informed_by), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "AttributeValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "Biosample" (
	name TEXT, 
	description TEXT, 
	embargoed BOOLEAN, 
	collected_from TEXT, 
	type TEXT, 
	samp_name TEXT, 
	id TEXT NOT NULL, 
	agrochem_addition TEXT, 
	alkalinity TEXT, 
	alkalinity_method TEXT, 
	alkyl_diethers TEXT, 
	alt TEXT, 
	al_sat TEXT, 
	al_sat_meth TEXT, 
	aminopept_act TEXT, 
	ammonium TEXT, 
	annual_precpt TEXT, 
	annual_temp TEXT, 
	bacteria_carb_prod TEXT, 
	bishomohopanol TEXT, 
	bromide TEXT, 
	calcium TEXT, 
	carb_nitro_ratio TEXT, 
	chem_administration TEXT, 
	chloride TEXT, 
	chlorophyll TEXT, 
	collection_date TEXT, 
	cur_land_use TEXT, 
	cur_vegetation TEXT, 
	cur_vegetation_meth TEXT, 
	crop_rotation TEXT, 
	density TEXT, 
	depth TEXT, 
	diss_carb_dioxide TEXT, 
	diss_hydrogen TEXT, 
	diss_inorg_carb TEXT, 
	diss_inorg_phosp TEXT, 
	diss_org_carb TEXT, 
	diss_org_nitro TEXT, 
	diss_oxygen TEXT, 
	drainage_class TEXT, 
	elev TEXT, 
	env_package TEXT, 
	env_broad_scale TEXT NOT NULL, 
	env_local_scale TEXT NOT NULL, 
	env_medium TEXT NOT NULL, 
	extreme_event TEXT, 
	fao_class TEXT, 
	fire TEXT, 
	flooding TEXT, 
	geo_loc_name TEXT, 
	glucosidase_act TEXT, 
	heavy_metals TEXT, 
	heavy_metals_meth TEXT, 
	lat_lon TEXT, 
	link_addit_analys TEXT, 
	link_class_info TEXT, 
	link_climate_info TEXT, 
	local_class TEXT, 
	local_class_meth TEXT, 
	magnesium TEXT, 
	mean_frict_vel TEXT, 
	mean_peak_frict_vel TEXT, 
	misc_param TEXT, 
	n_alkanes TEXT, 
	nitrate TEXT, 
	nitrite TEXT, 
	org_matter TEXT, 
	org_nitro TEXT, 
	organism_count TEXT, 
	oxy_stat_samp TEXT, 
	part_org_carb TEXT, 
	perturbation TEXT, 
	petroleum_hydrocarb TEXT, 
	ph TEXT, 
	ph_meth TEXT, 
	phaeopigments TEXT, 
	phosplipid_fatt_acid TEXT, 
	pool_dna_extracts TEXT, 
	potassium TEXT, 
	pressure TEXT, 
	profile_position TEXT, 
	redox_potential TEXT, 
	salinity TEXT, 
	salinity_meth TEXT, 
	samp_mat_process TEXT, 
	samp_store_dur TEXT, 
	samp_store_loc TEXT, 
	samp_taxon_id TEXT, 
	samp_store_temp TEXT, 
	samp_vol_we_dna_ext TEXT, 
	season_temp TEXT, 
	season_precpt TEXT, 
	sieving TEXT, 
	size_frac_low TEXT, 
	size_frac_up TEXT, 
	slope_gradient TEXT, 
	slope_aspect TEXT, 
	sodium TEXT, 
	soil_type TEXT, 
	soil_type_meth TEXT, 
	store_cond TEXT, 
	sulfate TEXT, 
	sulfide TEXT, 
	"temp" TEXT, 
	tillage TEXT, 
	tidal_stage TEXT, 
	tot_carb TEXT, 
	tot_depth_water_col TEXT, 
	tot_diss_nitro TEXT, 
	tot_org_carb TEXT, 
	tot_org_c_meth TEXT, 
	tot_nitro_content TEXT, 
	tot_nitro_cont_meth TEXT, 
	tot_phosp TEXT, 
	water_cont_soil_meth TEXT, 
	ecosystem TEXT, 
	ecosystem_category TEXT, 
	ecosystem_type TEXT, 
	ecosystem_subtype TEXT, 
	specific_ecosystem TEXT, 
	add_date TEXT, 
	community TEXT, 
	habitat TEXT, 
	host_name TEXT, 
	location TEXT, 
	mod_date TEXT, 
	ncbi_taxonomy_name TEXT, 
	proport_woa_temperature TEXT, 
	salinity_category TEXT, 
	sample_collection_site TEXT, 
	soluble_iron_micromol TEXT, 
	subsurface_depth TEXT, 
	air_temp_regm TEXT, 
	biotic_regm TEXT, 
	biotic_relationship TEXT, 
	climate_environment TEXT, 
	experimental_factor TEXT, 
	gaseous_environment TEXT, 
	growth_facil TEXT, 
	humidity_regm TEXT, 
	light_regm TEXT, 
	phosphate TEXT, 
	rel_to_oxygen TEXT, 
	samp_collec_method TEXT, 
	samp_size TEXT, 
	source_mat_id TEXT, 
	watering_regm TEXT, 
	dna_absorb1 TEXT, 
	dna_absorb2 TEXT, 
	dna_collect_site TEXT, 
	dna_concentration TEXT, 
	dna_cont_type VARCHAR(5), 
	dna_cont_well TEXT, 
	dna_container_id TEXT, 
	dna_dnase VARCHAR(3), 
	dna_isolate_meth TEXT, 
	dna_organisms TEXT, 
	dna_project_contact TEXT, 
	dna_samp_id TEXT, 
	dna_sample_format VARCHAR(19), 
	dna_sample_name TEXT, 
	dna_seq_project TEXT, 
	dna_seq_project_pi TEXT, 
	dna_seq_project_name TEXT, 
	dna_volume TEXT, 
	proposal_dna TEXT, 
	dnase_rna VARCHAR(3), 
	proposal_rna TEXT, 
	rna_absorb1 TEXT, 
	rna_absorb2 TEXT, 
	rna_collect_site TEXT, 
	rna_concentration TEXT, 
	rna_cont_type VARCHAR(5), 
	rna_cont_well TEXT, 
	rna_container_id TEXT, 
	rna_isolate_meth TEXT, 
	rna_organisms TEXT, 
	rna_project_contact TEXT, 
	rna_samp_id TEXT, 
	rna_sample_format VARCHAR(19), 
	rna_sample_name TEXT, 
	rna_seq_project TEXT, 
	rna_seq_project_pi TEXT, 
	rna_seq_project_name TEXT, 
	rna_volume TEXT, 
	collection_date_inc TEXT, 
	collection_time TEXT, 
	collection_time_inc TEXT, 
	experimental_factor_other TEXT, 
	filter_method TEXT, 
	isotope_exposure TEXT, 
	micro_biomass_c_meth TEXT, 
	micro_biomass_n_meth TEXT, 
	microbial_biomass_c TEXT, 
	microbial_biomass_n TEXT, 
	non_microb_biomass TEXT, 
	non_microb_biomass_method TEXT, 
	org_nitro_method TEXT, 
	other_treatment TEXT, 
	start_date_inc TEXT, 
	start_time_inc TEXT, 
	project_id TEXT, 
	replicate_number TEXT, 
	sample_shipped TEXT, 
	sample_type VARCHAR(18), 
	technical_reps TEXT, 
	zinc TEXT, 
	manganese TEXT, 
	ammonium_nitrogen TEXT, 
	nitrate_nitrogen TEXT, 
	nitrite_nitrogen TEXT, 
	lbc_thirty TEXT, 
	lbceq TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(collected_from) REFERENCES "FieldResearchSite" (id)
);

CREATE TABLE "BooleanValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	has_boolean_value BOOLEAN, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, has_boolean_value), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "ControlledIdentifiedTermValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	term TEXT NOT NULL, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, term), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(term) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "ControlledTermValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	term TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, term), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(term) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "CreditAssociation" (
	applies_to_person TEXT NOT NULL, 
	applied_role VARCHAR(26), 
	applied_roles VARCHAR(26) NOT NULL, 
	type TEXT, 
	"Study_id" TEXT, 
	PRIMARY KEY (applies_to_person, applied_role, applied_roles, type, "Study_id"), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);

CREATE TABLE "DataObject" (
	file_size_bytes INTEGER, 
	md5_checksum TEXT, 
	data_object_type VARCHAR(51), 
	compression_type TEXT, 
	was_generated_by TEXT, 
	url TEXT, 
	type TEXT, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "DissolvingActivity" (
	dissolution_aided_by TEXT, 
	dissolution_reagent VARCHAR(15), 
	dissolution_volume TEXT, 
	dissolved_in TEXT, 
	material_input TEXT, 
	material_output TEXT, 
	PRIMARY KEY (dissolution_aided_by, dissolution_reagent, dissolution_volume, dissolved_in, material_input, material_output), 
	FOREIGN KEY(material_input) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id)
);

CREATE TABLE "GenomeFeature" (
	seqid TEXT NOT NULL, 
	type TEXT, 
	start INTEGER NOT NULL, 
	"end" INTEGER NOT NULL, 
	strand TEXT, 
	phase INTEGER, 
	encodes TEXT, 
	feature_type TEXT, 
	PRIMARY KEY (seqid, type, start, "end", strand, phase, encodes, feature_type), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id), 
	FOREIGN KEY(encodes) REFERENCES "GeneProduct" (id)
);

CREATE TABLE "GeolocationValue" (
	was_generated_by TEXT, 
	type TEXT, 
	latitude FLOAT, 
	longitude FLOAT, 
	has_raw_value TEXT, 
	PRIMARY KEY (was_generated_by, type, latitude, longitude, has_raw_value), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "ImageValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	url TEXT, 
	description TEXT, 
	display_order TEXT, 
	"Study_id" TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, url, description, display_order, "Study_id"), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);

CREATE TABLE "IntegerValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	has_numeric_value FLOAT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, has_numeric_value), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "PersonValue" (
	was_generated_by TEXT, 
	type TEXT, 
	orcid TEXT, 
	profile_image_url TEXT, 
	email TEXT, 
	name TEXT, 
	websites TEXT, 
	has_raw_value TEXT, 
	PRIMARY KEY (was_generated_by, type, orcid, profile_image_url, email, name, websites, has_raw_value), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "ProteinQuantification" (
	best_protein TEXT, 
	all_proteins TEXT, 
	peptide_sequence_count INTEGER, 
	protein_spectral_count INTEGER, 
	protein_sum_masic_abundance INTEGER, 
	PRIMARY KEY (best_protein, all_proteins, peptide_sequence_count, protein_spectral_count, protein_sum_masic_abundance), 
	FOREIGN KEY(best_protein) REFERENCES "GeneProduct" (id)
);

CREATE TABLE "QuantityValue" (
	was_generated_by TEXT, 
	type TEXT, 
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	has_minimum_numeric_value FLOAT, 
	has_maximum_numeric_value FLOAT, 
	has_raw_value TEXT, 
	PRIMARY KEY (was_generated_by, type, has_unit, has_numeric_value, has_minimum_numeric_value, has_maximum_numeric_value, has_raw_value), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "Reaction" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	left_participants TEXT, 
	right_participants TEXT, 
	direction TEXT, 
	smarts_string TEXT, 
	is_diastereoselective BOOLEAN, 
	is_stereo BOOLEAN, 
	is_balanced BOOLEAN, 
	is_transport BOOLEAN, 
	is_fully_characterized BOOLEAN, 
	"Pathway_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Pathway_id") REFERENCES "Pathway" (id)
);

CREATE TABLE "ReactionActivity" (
	material_input TEXT, 
	material_output TEXT, 
	reaction_aided_by TEXT, 
	reaction_temperature TEXT, 
	reaction_time TEXT, 
	PRIMARY KEY (material_input, material_output, reaction_aided_by, reaction_temperature, reaction_time), 
	FOREIGN KEY(material_input) REFERENCES "MaterialSample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id)
);

CREATE TABLE "ReactionParticipant" (
	chemical TEXT, 
	stoichiometry INTEGER, 
	PRIMARY KEY (chemical, stoichiometry), 
	FOREIGN KEY(chemical) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "TextValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	language TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type, language), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "TimestampValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "UrlValue" (
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	PRIMARY KEY (has_raw_value, was_generated_by, type), 
	FOREIGN KEY(was_generated_by) REFERENCES "Activity" (id)
);

CREATE TABLE "WorkflowExecutionActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	type TEXT, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "AnalyticalSample_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "AnalyticalSample" (id)
);

CREATE TABLE "BiosampleProcessing_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "BiosampleProcessing" (id)
);

CREATE TABLE "ChemicalEntity_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "ChemicalEntity_smiles" (
	backref_id TEXT, 
	smiles TEXT, 
	PRIMARY KEY (backref_id, smiles), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalEntity" (id)
);

CREATE TABLE "CollectingBiosamplesFromSite_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "CollectingBiosamplesFromSite" (id)
);

CREATE TABLE "CollectingBiosamplesFromSite_has_inputs" (
	backref_id TEXT, 
	has_inputs TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_inputs), 
	FOREIGN KEY(backref_id) REFERENCES "CollectingBiosamplesFromSite" (id)
);

CREATE TABLE "EnvironmentalMaterialTerm_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "EnvironmentalMaterialTerm" (id)
);

CREATE TABLE "FieldResearchSite_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "FieldResearchSite" (id)
);

CREATE TABLE "GeneProduct_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "GeneProduct" (id)
);

CREATE TABLE "Instrument_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Instrument" (id)
);

CREATE TABLE "MaterialSample_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MaterialSample" (id)
);

CREATE TABLE "OmicsProcessing_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OmicsProcessing_has_input" (
	backref_id TEXT, 
	has_input TEXT, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OmicsProcessing_has_output" (
	backref_id TEXT, 
	has_output TEXT, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OmicsProcessing_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OmicsProcessing_gold_sequencing_project_identifiers" (
	backref_id TEXT, 
	gold_sequencing_project_identifiers TEXT, 
	PRIMARY KEY (backref_id, gold_sequencing_project_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OmicsProcessing_insdc_experiment_identifiers" (
	backref_id TEXT, 
	insdc_experiment_identifiers TEXT, 
	PRIMARY KEY (backref_id, insdc_experiment_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OmicsProcessing" (id)
);

CREATE TABLE "OntologyClass_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "OrthologyGroup_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "OrthologyGroup" (id)
);

CREATE TABLE "Pathway_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Pathway" (id)
);

CREATE TABLE "Person_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Person" (id)
);

CREATE TABLE "Study_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_gold_study_identifiers" (
	backref_id TEXT, 
	gold_study_identifiers TEXT, 
	PRIMARY KEY (backref_id, gold_study_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_alternative_titles" (
	backref_id TEXT, 
	alternative_titles TEXT, 
	PRIMARY KEY (backref_id, alternative_titles), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_alternative_descriptions" (
	backref_id TEXT, 
	alternative_descriptions TEXT, 
	PRIMARY KEY (backref_id, alternative_descriptions), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_alternative_names" (
	backref_id TEXT, 
	alternative_names TEXT, 
	PRIMARY KEY (backref_id, alternative_names), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_websites" (
	backref_id TEXT, 
	websites TEXT, 
	PRIMARY KEY (backref_id, websites), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_publications" (
	backref_id TEXT, 
	publications TEXT, 
	PRIMARY KEY (backref_id, publications), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_ess_dive_datasets" (
	backref_id TEXT, 
	ess_dive_datasets TEXT, 
	PRIMARY KEY (backref_id, ess_dive_datasets), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_relevant_protocols" (
	backref_id TEXT, 
	relevant_protocols TEXT, 
	PRIMARY KEY (backref_id, relevant_protocols), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "Study_funding_sources" (
	backref_id TEXT, 
	funding_sources TEXT, 
	PRIMARY KEY (backref_id, funding_sources), 
	FOREIGN KEY(backref_id) REFERENCES "Study" (id)
);

CREATE TABLE "MagsAnalysisActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	input_contig_num INTEGER, 
	binned_contig_num INTEGER, 
	too_short_contig_num INTEGER, 
	low_depth_contig_num INTEGER, 
	unbinned_contig_num INTEGER, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MaterialSamplingActivity" (
	amount_collected TEXT, 
	collected_into TEXT, 
	biosample_input TEXT, 
	material_output TEXT, 
	sampling_method VARCHAR(8), 
	PRIMARY KEY (amount_collected, collected_into, biosample_input, material_output, sampling_method), 
	FOREIGN KEY(biosample_input) REFERENCES "Biosample" (id), 
	FOREIGN KEY(material_output) REFERENCES "MaterialSample" (id)
);

CREATE TABLE "MetabolomicsAnalysisActivity" (
	name TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	used TEXT, 
	has_calibration TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(used) REFERENCES "Instrument" (id)
);

CREATE TABLE "MetagenomeAnnotationActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MetagenomeAssembly" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	asm_score FLOAT, 
	scaffolds FLOAT, 
	scaf_logsum FLOAT, 
	scaf_powsum FLOAT, 
	scaf_max FLOAT, 
	scaf_bp FLOAT, 
	scaf_n50 FLOAT, 
	scaf_n90 FLOAT, 
	scaf_l50 FLOAT, 
	scaf_l90 FLOAT, 
	scaf_n_gt50k FLOAT, 
	scaf_l_gt50k FLOAT, 
	scaf_pct_gt50k FLOAT, 
	contigs FLOAT, 
	contig_bp FLOAT, 
	ctg_n50 FLOAT, 
	ctg_l50 FLOAT, 
	ctg_n90 FLOAT, 
	ctg_l90 FLOAT, 
	ctg_logsum FLOAT, 
	ctg_powsum FLOAT, 
	ctg_max FLOAT, 
	gap_pct FLOAT, 
	gc_std FLOAT, 
	gc_avg FLOAT, 
	num_input_reads FLOAT, 
	num_aligned_reads FLOAT, 
	insdc_assembly_identifiers TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MetaproteomicsAnalysisActivity" (
	name TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	used TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(used) REFERENCES "Instrument" (id)
);

CREATE TABLE "MetatranscriptomeActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MetatranscriptomeAnnotationActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "MetatranscriptomeAssembly" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	type TEXT, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	asm_score FLOAT, 
	scaffolds FLOAT, 
	scaf_logsum FLOAT, 
	scaf_powsum FLOAT, 
	scaf_max FLOAT, 
	scaf_bp FLOAT, 
	scaf_n50 FLOAT, 
	scaf_n90 FLOAT, 
	scaf_l50 FLOAT, 
	scaf_l90 FLOAT, 
	scaf_n_gt50k FLOAT, 
	scaf_l_gt50k FLOAT, 
	scaf_pct_gt50k FLOAT, 
	contigs FLOAT, 
	contig_bp FLOAT, 
	ctg_n50 FLOAT, 
	ctg_l50 FLOAT, 
	ctg_n90 FLOAT, 
	ctg_l90 FLOAT, 
	ctg_logsum FLOAT, 
	ctg_powsum FLOAT, 
	ctg_max FLOAT, 
	gap_pct FLOAT, 
	gc_std FLOAT, 
	gc_avg FLOAT, 
	num_input_reads FLOAT, 
	num_aligned_reads FLOAT, 
	insdc_assembly_identifiers TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "NomAnalysisActivity" (
	name TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	used TEXT, 
	has_calibration TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY(used) REFERENCES "Instrument" (id)
);

CREATE TABLE "ReadBasedTaxonomyAnalysisActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "ReadQcAnalysisActivity" (
	name TEXT, 
	used TEXT, 
	execution_resource TEXT NOT NULL, 
	git_url TEXT NOT NULL, 
	was_associated_with TEXT, 
	started_at_time DATETIME NOT NULL, 
	ended_at_time DATETIME NOT NULL, 
	was_informed_by TEXT NOT NULL, 
	type TEXT, 
	input_read_count FLOAT, 
	input_base_count FLOAT, 
	output_read_count FLOAT, 
	output_base_count FLOAT, 
	input_read_bases FLOAT, 
	output_read_bases FLOAT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_associated_with) REFERENCES "WorkflowExecutionActivity" (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);

CREATE TABLE "Biosample_img_identifiers" (
	backref_id TEXT, 
	img_identifiers TEXT, 
	PRIMARY KEY (backref_id, img_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_biosample_categories" (
	backref_id TEXT, 
	biosample_categories VARCHAR(5), 
	PRIMARY KEY (backref_id, biosample_categories), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_part_of" (
	backref_id TEXT, 
	part_of TEXT NOT NULL, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_gold_biosample_identifiers" (
	backref_id TEXT, 
	gold_biosample_identifiers TEXT, 
	PRIMARY KEY (backref_id, gold_biosample_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_insdc_biosample_identifiers" (
	backref_id TEXT, 
	insdc_biosample_identifiers TEXT, 
	PRIMARY KEY (backref_id, insdc_biosample_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_emsl_biosample_identifiers" (
	backref_id TEXT, 
	emsl_biosample_identifiers TEXT, 
	PRIMARY KEY (backref_id, emsl_biosample_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_igsn_biosample_identifiers" (
	backref_id TEXT, 
	igsn_biosample_identifiers TEXT, 
	PRIMARY KEY (backref_id, igsn_biosample_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_water_content" (
	backref_id TEXT, 
	water_content TEXT, 
	PRIMARY KEY (backref_id, water_content), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_analysis_type" (
	backref_id TEXT, 
	analysis_type VARCHAR(22), 
	PRIMARY KEY (backref_id, analysis_type), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "Biosample_sample_link" (
	backref_id TEXT, 
	sample_link TEXT, 
	PRIMARY KEY (backref_id, sample_link), 
	FOREIGN KEY(backref_id) REFERENCES "Biosample" (id)
);

CREATE TABLE "DataObject_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "DataObject" (id)
);

CREATE TABLE "Reaction_alternative_identifiers" (
	backref_id TEXT, 
	alternative_identifiers TEXT, 
	PRIMARY KEY (backref_id, alternative_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "Reaction" (id)
);

CREATE TABLE "WorkflowExecutionActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "WorkflowExecutionActivity" (id)
);

CREATE TABLE "WorkflowExecutionActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "WorkflowExecutionActivity" (id)
);

CREATE TABLE "WorkflowExecutionActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "WorkflowExecutionActivity" (id)
);

CREATE TABLE "FunctionalAnnotation" (
	was_generated_by TEXT, 
	subject TEXT, 
	has_function TEXT, 
	type TEXT, 
	PRIMARY KEY (was_generated_by, subject, has_function, type), 
	FOREIGN KEY(was_generated_by) REFERENCES "MetagenomeAnnotationActivity" (id), 
	FOREIGN KEY(subject) REFERENCES "GeneProduct" (id), 
	FOREIGN KEY(type) REFERENCES "OntologyClass" (id)
);

CREATE TABLE "MagBin" (
	type TEXT, 
	bin_name TEXT, 
	number_of_contig INTEGER, 
	completeness FLOAT, 
	contamination FLOAT, 
	gene_count INTEGER, 
	bin_quality TEXT, 
	num_16s INTEGER, 
	num_5s INTEGER, 
	num_23s INTEGER, 
	num_t_rna INTEGER, 
	gtdbtk_domain TEXT, 
	gtdbtk_phylum TEXT, 
	gtdbtk_class TEXT, 
	gtdbtk_order TEXT, 
	gtdbtk_family TEXT, 
	gtdbtk_genus TEXT, 
	gtdbtk_species TEXT, 
	"MagsAnalysisActivity_id" TEXT, 
	PRIMARY KEY (type, bin_name, number_of_contig, completeness, contamination, gene_count, bin_quality, num_16s, num_5s, num_23s, num_t_rna, gtdbtk_domain, gtdbtk_phylum, gtdbtk_class, gtdbtk_order, gtdbtk_family, gtdbtk_genus, gtdbtk_species, "MagsAnalysisActivity_id"), 
	FOREIGN KEY("MagsAnalysisActivity_id") REFERENCES "MagsAnalysisActivity" (id)
);

CREATE TABLE "MetaboliteQuantification" (
	alternative_identifiers TEXT, 
	metabolite_quantified TEXT, 
	highest_similarity_score FLOAT, 
	"MetabolomicsAnalysisActivity_id" TEXT, 
	PRIMARY KEY (alternative_identifiers, metabolite_quantified, highest_similarity_score, "MetabolomicsAnalysisActivity_id"), 
	FOREIGN KEY(metabolite_quantified) REFERENCES "ChemicalEntity" (id), 
	FOREIGN KEY("MetabolomicsAnalysisActivity_id") REFERENCES "MetabolomicsAnalysisActivity" (id)
);

CREATE TABLE "PeptideQuantification" (
	peptide_sequence TEXT, 
	best_protein TEXT, 
	all_proteins TEXT, 
	min_q_value FLOAT, 
	peptide_spectral_count INTEGER, 
	peptide_sum_masic_abundance INTEGER, 
	"MetaproteomicsAnalysisActivity_id" TEXT, 
	PRIMARY KEY (peptide_sequence, best_protein, all_proteins, min_q_value, peptide_spectral_count, peptide_sum_masic_abundance, "MetaproteomicsAnalysisActivity_id"), 
	FOREIGN KEY(best_protein) REFERENCES "GeneProduct" (id), 
	FOREIGN KEY("MetaproteomicsAnalysisActivity_id") REFERENCES "MetaproteomicsAnalysisActivity" (id)
);

CREATE TABLE "MagsAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MagsAnalysisActivity" (id)
);

CREATE TABLE "MagsAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MagsAnalysisActivity" (id)
);

CREATE TABLE "MagsAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MagsAnalysisActivity" (id)
);

CREATE TABLE "MetabolomicsAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetabolomicsAnalysisActivity" (id)
);

CREATE TABLE "MetabolomicsAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetabolomicsAnalysisActivity" (id)
);

CREATE TABLE "MetabolomicsAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetabolomicsAnalysisActivity" (id)
);

CREATE TABLE "MetagenomeAnnotationActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAnnotationActivity" (id)
);

CREATE TABLE "MetagenomeAnnotationActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAnnotationActivity" (id)
);

CREATE TABLE "MetagenomeAnnotationActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAnnotationActivity" (id)
);

CREATE TABLE "MetagenomeAnnotationActivity_gold_analysis_project_identifiers" (
	backref_id TEXT, 
	gold_analysis_project_identifiers TEXT, 
	PRIMARY KEY (backref_id, gold_analysis_project_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAnnotationActivity" (id)
);

CREATE TABLE "MetagenomeAssembly_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAssembly" (id)
);

CREATE TABLE "MetagenomeAssembly_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAssembly" (id)
);

CREATE TABLE "MetagenomeAssembly_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetagenomeAssembly" (id)
);

CREATE TABLE "MetaproteomicsAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetaproteomicsAnalysisActivity" (id)
);

CREATE TABLE "MetaproteomicsAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetaproteomicsAnalysisActivity" (id)
);

CREATE TABLE "MetaproteomicsAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetaproteomicsAnalysisActivity" (id)
);

CREATE TABLE "MetatranscriptomeActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeActivity" (id)
);

CREATE TABLE "MetatranscriptomeActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeActivity" (id)
);

CREATE TABLE "MetatranscriptomeActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeActivity" (id)
);

CREATE TABLE "MetatranscriptomeAnnotationActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAnnotationActivity" (id)
);

CREATE TABLE "MetatranscriptomeAnnotationActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAnnotationActivity" (id)
);

CREATE TABLE "MetatranscriptomeAnnotationActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAnnotationActivity" (id)
);

CREATE TABLE "MetatranscriptomeAnnotationActivity_gold_analysis_project_identifiers" (
	backref_id TEXT, 
	gold_analysis_project_identifiers TEXT, 
	PRIMARY KEY (backref_id, gold_analysis_project_identifiers), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAnnotationActivity" (id)
);

CREATE TABLE "MetatranscriptomeAssembly_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAssembly" (id)
);

CREATE TABLE "MetatranscriptomeAssembly_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAssembly" (id)
);

CREATE TABLE "MetatranscriptomeAssembly_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "MetatranscriptomeAssembly" (id)
);

CREATE TABLE "NomAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "NomAnalysisActivity" (id)
);

CREATE TABLE "NomAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "NomAnalysisActivity" (id)
);

CREATE TABLE "NomAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "NomAnalysisActivity" (id)
);

CREATE TABLE "ReadBasedTaxonomyAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "ReadBasedTaxonomyAnalysisActivity" (id)
);

CREATE TABLE "ReadBasedTaxonomyAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "ReadBasedTaxonomyAnalysisActivity" (id)
);

CREATE TABLE "ReadBasedTaxonomyAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "ReadBasedTaxonomyAnalysisActivity" (id)
);

CREATE TABLE "ReadQcAnalysisActivity_part_of" (
	backref_id TEXT, 
	part_of TEXT, 
	PRIMARY KEY (backref_id, part_of), 
	FOREIGN KEY(backref_id) REFERENCES "ReadQcAnalysisActivity" (id)
);

CREATE TABLE "ReadQcAnalysisActivity_has_input" (
	backref_id TEXT, 
	has_input TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_input), 
	FOREIGN KEY(backref_id) REFERENCES "ReadQcAnalysisActivity" (id)
);

CREATE TABLE "ReadQcAnalysisActivity_has_output" (
	backref_id TEXT, 
	has_output TEXT NOT NULL, 
	PRIMARY KEY (backref_id, has_output), 
	FOREIGN KEY(backref_id) REFERENCES "ReadQcAnalysisActivity" (id)
);
