# NMDC

Schema for National Microbiome Data Collaborative (NMDC).
This schema is organized into multiple modules, such as:

 * a set of core types for representing data values
 * a subset of the mixs schema
 * an annotation schema
 * the NMDC schema itself, into which the other modules are imported

URI: <a href=https://w3id.org/nmdc/nmdc>https://w3id.org/nmdc/nmdc</a>


## Classes

| Class | Description |
| --- | --- |
| [Activity](Activity.md) | Something that occurs over a period of time and acts upon or with entities; i... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WorkflowExecutionActivity](WorkflowExecutionActivity.md) | Represents an instance of an execution of a particular workflow |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MagsAnalysisActivity](MagsAnalysisActivity.md) | A workflow execution activity that uses computational binning tools to group ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md) | A workflow execution activity that provides functional and structural annotat... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetagenomeAssembly](MetagenomeAssembly.md) | A workflow execution activity that converts sequencing reads into an assemble... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetagenomeSequencingActivity](MetagenomeSequencingActivity.md) | Initial sequencing activity that precedes any analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetatranscriptomeActivity](MetatranscriptomeActivity.md) | A metatranscriptome activity that e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetatranscriptomeAnnotationActivity](MetatranscriptomeAnnotationActivity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MetatranscriptomeAssembly](MetatranscriptomeAssembly.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NomAnalysisActivity](NomAnalysisActivity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReadBasedTaxonomyAnalysisActivity](ReadBasedTaxonomyAnalysisActivity.md) | A workflow execution activity that performs taxonomy classification using seq... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReadQcAnalysisActivity](ReadQcAnalysisActivity.md) | A workflow execution activity that performs quality control on raw Illumina r... |
| [AttributeValue](AttributeValue.md) | The value for any value of a attribute for a sample |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BooleanValue](BooleanValue.md) | A value that is a boolean |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlledTermValue](ControlledTermValue.md) | A controlled term or class from an ontology |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md) | A controlled term or class from an ontology, requiring the presence of term w... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeolocationValue](GeolocationValue.md) | A normalized value for a location on the earth's surface |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ImageValue](ImageValue.md) | An attribute value representing an image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IntegerValue](IntegerValue.md) | A value that is an integer |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PersonValue](PersonValue.md) | An attribute value representing a person |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QuantityValue](QuantityValue.md) | A simple quantity, e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextValue](TextValue.md) | A basic string value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TimestampValue](TimestampValue.md) | A value that is a timestamp |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UrlValue](UrlValue.md) | A value that is a string that conforms to URL syntax |
| [CreditAssociation](CreditAssociation.md) | This class supports binding associated researchers to studies |
| [Database](Database.md) | An abstract holder for any set of metadata and data |
| [Doi](Doi.md) | A centrally registered identifier symbol used to uniquely identify objects gi... |
| [FunctionalAnnotation](FunctionalAnnotation.md) | An assignment of a function term (e |
| [FunctionalAnnotationAggMember](FunctionalAnnotationAggMember.md) |  |
| [GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |
| [MagBin](MagBin.md) |  |
| [MetaboliteQuantification](MetaboliteQuantification.md) | This is used to link a metabolomics analysis workflow to a specific metabolit... |
| [NamedThing](NamedThing.md) | a databased entity or concept/class |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataObject](DataObject.md) | An object that primarily consists of symbols that represent information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProduct](GeneProduct.md) | A molecule encoded by a gene that has an evolved function |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialEntity](MaterialEntity.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnalyticalSample](AnalyticalSample.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessedSample](ProcessedSample.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Site](Site.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OntologyClass](OntologyClass.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntity](ChemicalEntity.md) | An atom or molecule that can be represented with a chemical formula |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) | Abstract grouping class for any term/descriptor that can be applied to a func... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrthologyGroup](OrthologyGroup.md) | A set of genes or gene products in which all members are orthologous |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathway](Pathway.md) | A pathway is a sequence of steps/reactions carried out by an organism or comm... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Reaction](Reaction.md) | An individual biochemical transformation carried out by a functional unit of ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlannedProcess](PlannedProcess.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiosampleProcessing](BiosampleProcessing.md) | A process that takes one or more biosamples as inputs and generates one or mo... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LibraryPreparation](LibraryPreparation.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pooling](Pooling.md) | physical combination of several instances of like material |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChromatographicSeparationProcess](ChromatographicSeparationProcess.md) | The process of using a selective partitioning of the analyte or interferent b... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CollectingBiosamplesFromSite](CollectingBiosamplesFromSite.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Extraction](Extraction.md) | A material separation in which a desired component of an input material is se... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FiltrationProcess](FiltrationProcess.md) | The process of segregation of phases; e |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MixingProcess](MixingProcess.md) | The combining of components, particles or layers into a more homogeneous stat... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SubSamplingProcess](SubSamplingProcess.md) | Separating a sample aliquot from the starting material for downstream activit... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |
| [PeptideQuantification](PeptideQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific peptide... |
| [ProteinQuantification](ProteinQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific protein |
| [Protocol](Protocol.md) |  |
| [QualityControlReport](QualityControlReport.md) |  |
| [ReactionParticipant](ReactionParticipant.md) | Instances of this link a reaction to a chemical entity participant |
| [Solution](Solution.md) | A mixture that is homogeneous, made up of two or more scattered molecular agg... |
| [SolutionComponent](SolutionComponent.md) | One constituent of a solution |


## Slots

| Slot | Description |
| --- | --- |
| [abs_air_humidity](abs_air_humidity.md) | Actual mass of water vapor - mh20 - present in the air water vapor mixture |
| [activity_set](activity_set.md) | This property links a database object to the set of workflow activities |
| [add_date](add_date.md) | The date on which the information was added to the database |
| [add_recov_method](add_recov_method.md) | Additional (i |
| [additional_info](additional_info.md) | Information that doesn't fit anywhere else |
| [address](address.md) | The street name and building number where the sampling occurred |
| [adj_room](adj_room.md) | List of rooms (room number, room name) immediately adjacent to the sampling r... |
| [aero_struc](aero_struc.md) | Aerospace structures typically consist of thin plates with stiffeners for the... |
| [agrochem_addition](agrochem_addition.md) | Addition of fertilizers, pesticides, etc |
| [air_PM_concen](air_PM_concen.md) | Concentration of substances that remain suspended in the air, and comprise mi... |
| [air_temp](air_temp.md) | Temperature of the air at the time of sampling |
| [air_temp_regm](air_temp_regm.md) | Information about treatment involving an exposure to varying temperatures; sh... |
| [al_sat](al_sat.md) | Aluminum saturation (esp |
| [al_sat_meth](al_sat_meth.md) | Reference or method used in determining Al saturation |
| [alkalinity](alkalinity.md) | Alkalinity, the ability of a solution to neutralize acids to the equivalence ... |
| [alkalinity_method](alkalinity_method.md) | Method used for alkalinity measurement |
| [alkyl_diethers](alkyl_diethers.md) | Concentration of alkyl diethers |
| [all_proteins](all_proteins.md) | the list of protein identifiers that are associated with the peptide sequence |
| [alt](alt.md) | Altitude is a term used to identify heights of objects such as airplanes, spa... |
| [alternate_emails](alternate_emails.md) | One or more other email addresses for an entity |
| [alternative_descriptions](alternative_descriptions.md) | A list of alternative descriptions for the entity |
| [alternative_identifiers](alternative_identifiers.md) | A list of alternative identifiers for the entity |
| [alternative_names](alternative_names.md) | A list of alternative names used to refer to the entity |
| [alternative_titles](alternative_titles.md) | A list of alternative titles for the entity |
| [aminopept_act](aminopept_act.md) | Measurement of aminopeptidase activity |
| [ammonium](ammonium.md) | Concentration of ammonium in the sample |
| [ammonium_nitrogen](ammonium_nitrogen.md) | Concentration of ammonium nitrogen in the sample |
| [amount_light](amount_light.md) | The unit of illuminance and luminous emittance, measuring luminous flux per u... |
| [analysis_identifiers](analysis_identifiers.md) |  |
| [analysis_type](analysis_type.md) | Select all the data types associated or available for this biosample |
| [ances_data](ances_data.md) | Information about either pedigree or other ancestral information description ... |
| [annual_precpt](annual_precpt.md) | The average of all annual precipitation values known, or an estimated equival... |
| [annual_temp](annual_temp.md) | Mean annual temperature |
| [antibiotic_regm](antibiotic_regm.md) | Information about treatment involving antibiotic administration; should inclu... |
| [api](api.md) | API gravity is a measure of how heavy or light a petroleum liquid is compared... |
| [applied_roles](applied_roles.md) |  |
| [applies_to_person](applies_to_person.md) |  |
| [arch_struc](arch_struc.md) | An architectural structure is a human-made, free-standing, immobile outdoor c... |
| [aromatics_pc](aromatics_pc.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... |
| [asm_score](asm_score.md) | A score for comparing metagenomic assembly quality from same sample |
| [asphaltenes_pc](asphaltenes_pc.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... |
| [assembly_identifiers](assembly_identifiers.md) |  |
| [associated_dois](associated_dois.md) | A list of DOIs associated with a resource, such as a list of DOIS associated ... |
| [atmospheric_data](atmospheric_data.md) | Measurement of atmospheric data; can include multiple data |
| [avg_dew_point](avg_dew_point.md) | The average of dew point measures taken at the beginning of every hour over a... |
| [avg_occup](avg_occup.md) | Daily average occupancy of room |
| [avg_temp](avg_temp.md) | The average of temperatures taken at the beginning of every hour over a 24 ho... |
| [bac_prod](bac_prod.md) | Bacterial production in the water column measured by isotope uptake |
| [bac_resp](bac_resp.md) | Measurement of bacterial respiration in the water column |
| [bacteria_carb_prod](bacteria_carb_prod.md) | Measurement of bacterial carbon production |
| [barometric_press](barometric_press.md) | Force per unit area exerted against a surface by the weight of air above that... |
| [basin](basin.md) | Name of the basin (e |
| [bathroom_count](bathroom_count.md) | The number of bathrooms in the building |
| [bedroom_count](bedroom_count.md) | The number of bedrooms in the building |
| [benzene](benzene.md) | Concentration of benzene in the sample |
| [best_protein](best_protein.md) | the specific protein identifier most correctly associated with the peptide se... |
| [bin_name](bin_name.md) |  |
| [bin_quality](bin_quality.md) |  |
| [binned_contig_num](binned_contig_num.md) |  |
| [biochem_oxygen_dem](biochem_oxygen_dem.md) | Amount of dissolved oxygen needed by aerobic biological organisms in a body o... |
| [biocide](biocide.md) | List of biocides (commercial name of product and supplier) and date of admini... |
| [biocide_admin_method](biocide_admin_method.md) | Method of biocide administration (dose, frequency, duration, time elapsed bet... |
| [biogas_retention_time](biogas_retention_time.md) |  |
| [biogas_temperature](biogas_temperature.md) |  |
| [biol_stat](biol_stat.md) | The level of genome modification |
| [biomass](biomass.md) | Amount of biomass; should include the name for the part of biomass measured, ... |
| [biomaterial_purity](biomaterial_purity.md) |  |
| [biosample_categories](biosample_categories.md) |  |
| [biosample_identifiers](biosample_identifiers.md) |  |
| [biosample_set](biosample_set.md) | This property links a database object to the set of samples within it |
| [biotic_regm](biotic_regm.md) | Information about treatment(s) involving use of biotic factors, such as bacte... |
| [biotic_relationship](biotic_relationship.md) | Description of relationship(s) between the subject organism and other organis... |
| [bishomohopanol](bishomohopanol.md) | Concentration of bishomohopanol |
| [blood_press_diast](blood_press_diast.md) | Resting diastolic blood pressure, measured as mm mercury |
| [blood_press_syst](blood_press_syst.md) | Resting systolic blood pressure, measured as mm mercury |
| [bromide](bromide.md) | Concentration of bromide |
| [build_docs](build_docs.md) | The building design, construction and operation documents |
| [build_occup_type](build_occup_type.md) | The primary function for which a building or discrete part of a building is i... |
| [building_setting](building_setting.md) | A location (geography) where a building is set |
| [built_struc_age](built_struc_age.md) | The age of the built structure since construction |
| [built_struc_set](built_struc_set.md) | The characterization of the location of the built structure as high or low hu... |
| [built_struc_type](built_struc_type.md) | A physical structure that is a body or assemblage of bodies in space to form ... |
| [bulk_elect_conductivity](bulk_elect_conductivity.md) | Electrical conductivity is a measure of the ability to carry electric current... |
| [calcium](calcium.md) | Concentration of calcium in the sample |
| [carb_dioxide](carb_dioxide.md) | Carbon dioxide (gas) amount or concentration at the time of sampling |
| [carb_monoxide](carb_monoxide.md) | Carbon monoxide (gas) amount or concentration at the time of sampling |
| [carb_nitro_ratio](carb_nitro_ratio.md) | Ratio of amount or concentrations of carbon to nitrogen |
| [ceil_area](ceil_area.md) | The area of the ceiling space within the room |
| [ceil_cond](ceil_cond.md) | The physical condition of the ceiling at the time of sampling; photos or vide... |
| [ceil_finish_mat](ceil_finish_mat.md) | The type of material used to finish a ceiling |
| [ceil_struc](ceil_struc.md) | The construction format of the ceiling |
| [ceil_texture](ceil_texture.md) | The feel, appearance, or consistency of a ceiling surface |
| [ceil_thermal_mass](ceil_thermal_mass.md) | The ability of the ceiling to provide inertia against temperature fluctuation... |
| [ceil_type](ceil_type.md) | The type of ceiling according to the ceiling's appearance or construction |
| [ceil_water_mold](ceil_water_mold.md) | Signs of the presence of mold or mildew on the ceiling |
| [chem_administration](chem_administration.md) | List of chemical compounds administered to the host or site where sampling oc... |
| [chem_mutagen](chem_mutagen.md) | Treatment involving use of mutagens; should include the name of mutagen, amou... |
| [chem_oxygen_dem](chem_oxygen_dem.md) | A measure of the capacity of water to consume oxygen during the decomposition... |
| [chem_treat_method](chem_treat_method.md) | Method of chemical administration(dose, frequency, duration, time elapsed bet... |
| [chem_treatment](chem_treatment.md) | List of chemical compounds administered upstream the sampling location where ... |
| [chemical](chemical.md) | from reaction participant class |
| [chemical_formula](chemical_formula.md) | A generic grouping for molecular formulae and empirical formulae |
| [chimera_check](chimera_check.md) | Tool(s) used for chimera checking, including version number and parameters, t... |
| [chloride](chloride.md) | Concentration of chloride in the sample |
| [chlorophyll](chlorophyll.md) | Concentration of chlorophyll |
| [climate_environment](climate_environment.md) | Treatment involving an exposure to a particular climate; treatment regimen in... |
| [collected_from](collected_from.md) | The Site from which a Biosample was collected |
| [collecting_biosamples_from_site_set](collecting_biosamples_from_site_set.md) |  |
| [collection_date](collection_date.md) | The time of sampling, either as an instance (single point in time) or interva... |
| [collection_date_inc](collection_date_inc.md) | Date the incubation was harvested/collected/ended |
| [collection_time](collection_time.md) | The time of sampling, either as an instance (single point) or interval |
| [collection_time_inc](collection_time_inc.md) | Time the incubation was harvested/collected/ended |
| [community](community.md) |  |
| [completeness](completeness.md) |  |
| [completion_date](completion_date.md) |  |
| [compound](compound.md) | A substance that consists of more than one atom or ion |
| [compression_type](compression_type.md) | If provided, specifies the compression type |
| [concentration](concentration.md) | The concentration of a substance used in a process |
| [conditionings](conditionings.md) | Preliminary treatment of either phase with a suitable solution of the other p... |
| [conduc](conduc.md) | Electrical conductivity of water |
| [contained_in](contained_in.md) | A type of container |
| [container_size](container_size.md) | The volume of the container an analyte is stored in or an activity takes plac... |
| [contamination](contamination.md) |  |
| [contig_bp](contig_bp.md) | Total size in bp of all contigs |
| [contigs](contigs.md) | The sum of the (length*log(length)) of all contigs, times some constant |
| [cool_syst_id](cool_syst_id.md) | The cooling system identifier |
| [core_field](core_field.md) | basic fields |
| [count](count.md) |  |
| [crop_rotation](crop_rotation.md) | Whether or not crop is rotated, and if yes, rotation schedule |
| [ctg_l50](ctg_l50.md) | Given a set of contigs, the L50 is defined as the sequence length of the shor... |
| [ctg_l90](ctg_l90.md) | The L90 statistic is less than or equal to the L50 statistic; it is the lengt... |
| [ctg_logsum](ctg_logsum.md) | Maximum contig length |
| [ctg_max](ctg_max.md) | Maximum contig length |
| [ctg_n50](ctg_n50.md) | Given a set of contigs, each with its own length, the N50 count is defined as... |
| [ctg_n90](ctg_n90.md) | Given a set of contigs, each with its own length, the N90 count is defined as... |
| [ctg_powsum](ctg_powsum.md) | Powersum of all contigs is the same as logsum except that it uses the sum of ... |
| [cult_root_med](cult_root_med.md) | Name or reference for the hydroponic or in vitro culture rooting medium; can ... |
| [cur_land_use](cur_land_use.md) | Present state of sample site |
| [cur_vegetation](cur_vegetation.md) | Vegetation classification from one or more standard classification systems, o... |
| [cur_vegetation_meth](cur_vegetation_meth.md) | Reference or method used in vegetation classification |
| [data_object_set](data_object_set.md) | This property links a database object to the set of data objects within it |
| [data_object_type](data_object_type.md) | The type of file represented by the data object |
| [date_created](date_created.md) | from database class |
| [date_last_rain](date_last_rain.md) | The date of the last time it rained |
| [density](density.md) | Density of the sample, which is its mass per unit volume (aka volumetric mass... |
| [depos_env](depos_env.md) | Main depositional environment (https://en |
| [depth](depth.md) | The vertical distance below local surface, e |
| [description](description.md) | a human-readable description of a thing |
| [designated_class](designated_class.md) |  |
| [dew_point](dew_point.md) | The temperature to which a given parcel of humid air must be cooled, at const... |
| [diether_lipids](diether_lipids.md) | Concentration of diether lipids; can include multiple types of diether lipids |
| [direction](direction.md) | One of l->r, r->l, bidirectional, neutral |
| [display_order](display_order.md) | When rendering information, this attribute to specify the order in which the ... |
| [diss_carb_dioxide](diss_carb_dioxide.md) | Concentration of dissolved carbon dioxide in the sample or liquid portion of ... |
| [diss_hydrogen](diss_hydrogen.md) | Concentration of dissolved hydrogen |
| [diss_inorg_carb](diss_inorg_carb.md) | Dissolved inorganic carbon concentration in the sample, typically measured af... |
| [diss_inorg_nitro](diss_inorg_nitro.md) | Concentration of dissolved inorganic nitrogen |
| [diss_inorg_phosp](diss_inorg_phosp.md) | Concentration of dissolved inorganic phosphorus in the sample |
| [diss_iron](diss_iron.md) | Concentration of dissolved iron in the sample |
| [diss_org_carb](diss_org_carb.md) | Concentration of dissolved organic carbon in the sample, liquid portion of th... |
| [diss_org_nitro](diss_org_nitro.md) | Dissolved organic nitrogen concentration measured as; total dissolved nitroge... |
| [diss_oxygen](diss_oxygen.md) | Concentration of dissolved oxygen |
| [diss_oxygen_fluid](diss_oxygen_fluid.md) | Concentration of dissolved oxygen in the oil field produced fluids as it cont... |
| [dna_absorb1](dna_absorb1.md) | 260/280 measurement of DNA sample purity |
| [dna_absorb2](dna_absorb2.md) | 260/230 measurement of DNA sample purity |
| [dna_collect_site](dna_collect_site.md) | Provide information on the site your DNA sample was collected from |
| [dna_concentration](dna_concentration.md) |  |
| [dna_cont_type](dna_cont_type.md) | Tube or plate (96-well) |
| [dna_cont_well](dna_cont_well.md) |  |
| [dna_container_id](dna_container_id.md) |  |
| [dna_dnase](dna_dnase.md) |  |
| [dna_isolate_meth](dna_isolate_meth.md) | Describe the method/protocol/kit used to extract DNA/RNA |
| [dna_organisms](dna_organisms.md) | List any organisms known or suspected to grow in co-culture, as well as estim... |
| [dna_project_contact](dna_project_contact.md) |  |
| [dna_samp_id](dna_samp_id.md) |  |
| [dna_sample_format](dna_sample_format.md) | Solution in which the DNA sample has been suspended |
| [dna_sample_name](dna_sample_name.md) | Give the DNA sample a name that is meaningful to you |
| [dna_seq_project](dna_seq_project.md) |  |
| [dna_seq_project_name](dna_seq_project_name.md) |  |
| [dna_seq_project_pi](dna_seq_project_pi.md) |  |
| [dna_volume](dna_volume.md) |  |
| [dnase_rna](dnase_rna.md) |  |
| [doi_category](doi_category.md) | The resource type the corresponding doi resolves to |
| [doi_provider](doi_provider.md) | The authority, or organization, the DOI is associated with |
| [doi_value](doi_value.md) | A digital object identifier, which is intended to persistantly identify some ... |
| [door_comp_type](door_comp_type.md) | The composite type of the door |
| [door_cond](door_cond.md) | The phsical condition of the door |
| [door_direct](door_direct.md) | The direction the door opens |
| [door_loc](door_loc.md) | The relative location of the door in the room |
| [door_mat](door_mat.md) | The material the door is composed of |
| [door_move](door_move.md) | The type of movement of the door |
| [door_size](door_size.md) | The size of the door |
| [door_type](door_type.md) | The type of door material |
| [door_type_metal](door_type_metal.md) | The type of metal door |
| [door_type_wood](door_type_wood.md) | The type of wood door |
| [door_water_mold](door_water_mold.md) | Signs of the presence of mold or mildew on a door |
| [down_par](down_par.md) | Visible waveband radiance and irradiance measurements in the water column |
| [drainage_class](drainage_class.md) | Drainage classification from a standard system such as the USDA system |
| [drawings](drawings.md) | The buildings architectural drawings; if design is chosen, indicate phase-con... |
| [duration](duration.md) | The elapsed time of an activity |
| [ecosystem](ecosystem.md) | An ecosystem is a combination of a physical environment (abiotic factors) and... |
| [ecosystem_category](ecosystem_category.md) | Ecosystem categories represent divisions within the ecosystem based on specif... |
| [ecosystem_path_id](ecosystem_path_id.md) | A unique id representing the GOLD classifiers associated with a sample |
| [ecosystem_subtype](ecosystem_subtype.md) | Ecosystem subtypes represent further subdivision of Ecosystem types into more... |
| [ecosystem_type](ecosystem_type.md) | Ecosystem types represent things having common characteristics within the Eco... |
| [efficiency_percent](efficiency_percent.md) | Percentage of volatile solids removed from the anaerobic digestor |
| [elev](elev.md) | Elevation of the sampling site is its height above a fixed reference point, m... |
| [elevator](elevator.md) | The number of elevators within the built structure |
| [email](email.md) | An email address for an entity such as a person |
| [embargoed](embargoed.md) | If true, the data are embargoed and not available for public access |
| [emsl_biosample_identifiers](emsl_biosample_identifiers.md) | A list of identifiers for the biosample from the EMSL database |
| [emsl_identifiers](emsl_identifiers.md) |  |
| [emsl_project_identifiers](emsl_project_identifiers.md) | an identifier that links to an EMSL user facility project |
| [emsl_store_temp](emsl_store_temp.md) | The temperature at which the sample should be stored upon delivery to EMSL |
| [emulsions](emulsions.md) | Amount or concentration of substances such as paints, adhesives, mayonnaise, ... |
| [encodes](encodes.md) | The gene product encoded by this feature |
| [end](end.md) | The end of the feature in positive 1-based integer coordinates |
| [end_date](end_date.md) | The date on which any process or activity was ended |
| [ended_at_time](ended_at_time.md) |  |
| [env_broad_scale](env_broad_scale.md) | Report the major environmental system the sample or specimen came from |
| [env_local_scale](env_local_scale.md) | Report the entity or entities which are in the sample or specimen’s local vic... |
| [env_medium](env_medium.md) | Report the environmental material(s) immediately surrounding the sample or sp... |
| [env_package](env_package.md) | MIxS extension for reporting of measurements and observations obtained from o... |
| [environment_field](environment_field.md) | field describing environmental aspect of a sample |
| [escalator](escalator.md) | The number of escalators within the built structure |
| [ethylbenzene](ethylbenzene.md) | Concentration of ethylbenzene in the sample |
| [etl_software_version](etl_software_version.md) | from database class |
| [execution_resource](execution_resource.md) |  |
| [exp_duct](exp_duct.md) | The amount of exposed ductwork in the room |
| [exp_pipe](exp_pipe.md) | The number of exposed pipes in the room |
| [experimental_factor](experimental_factor.md) | Experimental factors are essentially the variable aspects of an experiment de... |
| [experimental_factor_other](experimental_factor_other.md) | Other details about your sample that you feel can't be accurately represented... |
| [ext_door](ext_door.md) | The number of exterior doors in the built structure |
| [ext_wall_orient](ext_wall_orient.md) | The orientation of the exterior wall |
| [ext_window_orient](ext_window_orient.md) | The compass direction the exterior window of the room is facing |
| [external_database_identifiers](external_database_identifiers.md) | Link to corresponding identifier in external database |
| [extractant](extractant.md) | The active component(s) primarily responsible for transfer of a solute from o... |
| [extraction_method](extraction_method.md) |  |
| [extraction_set](extraction_set.md) | This property links a database object to the set of extractions within it |
| [extraction_target](extraction_target.md) |  |
| [extreme_event](extreme_event.md) | Unusual physical events that may have affected microbial populations |
| [fao_class](fao_class.md) | Soil classification from the FAO World Reference Database for Soil Resources |
| [feature_type](feature_type.md) | TODO: Yuri to write |
| [fertilizer_regm](fertilizer_regm.md) | Information about treatment involving the use of fertilizers; should include ... |
| [field](field.md) | Name of the hydrocarbon field (e |
| [field_research_site_set](field_research_site_set.md) |  |
| [file_size_bytes](file_size_bytes.md) | Size of the file in bytes |
| [filter_material](filter_material.md) | A porous material on which solid particles present in air or other fluid whic... |
| [filter_method](filter_method.md) | Type of filter used or how the sample was filtered |
| [filter_pore_size](filter_pore_size.md) | A quantitative or qualitative measurement of the physical dimensions of the p... |
| [filter_type](filter_type.md) | A device which removes solid particulates or airborne molecular contaminants |
| [filtration_category](filtration_category.md) | The type of conditioning applied to a filter, device, etc |
| [fire](fire.md) | Historical and/or physical evidence of fire |
| [fireplace_type](fireplace_type.md) | A firebox with chimney |
| [flooding](flooding.md) | Historical and/or physical evidence of flooding |
| [floor_age](floor_age.md) | The time period since installment of the carpet or flooring |
| [floor_area](floor_area.md) | The area of the floor space within the room |
| [floor_cond](floor_cond.md) | The physical condition of the floor at the time of sampling; photos or video ... |
| [floor_count](floor_count.md) | The number of floors in the building, including basements and mechanical pent... |
| [floor_finish_mat](floor_finish_mat.md) | The floor covering type; the finished surface that is walked on |
| [floor_struc](floor_struc.md) | Refers to the structural elements and subfloor upon which the finish flooring... |
| [floor_thermal_mass](floor_thermal_mass.md) | The ability of the floor to provide inertia against temperature fluctuations |
| [floor_water_mold](floor_water_mold.md) | Signs of the presence of mold or mildew in a room |
| [fluor](fluor.md) | Raw or converted fluorescence of water |
| [freq_clean](freq_clean.md) | The number of times the sample location is cleaned |
| [freq_cook](freq_cook.md) | The number of times a meal is cooked per week |
| [functional_annotation_agg](functional_annotation_agg.md) |  |
| [functional_annotation_set](functional_annotation_set.md) | This property links a database object to the set of all functional annotation... |
| [funding_sources](funding_sources.md) | A list of organizations, along with the award numbers, that underwrite financ... |
| [fungicide_regm](fungicide_regm.md) | Information about treatment involving use of fungicides; should include the n... |
| [furniture](furniture.md) | The types of furniture present in the sampled room |
| [gap_pct](gap_pct.md) | The gap size percentage of all scaffolds |
| [gaseous_environment](gaseous_environment.md) | Use of conditions with differing gaseous environments; should include the nam... |
| [gaseous_substances](gaseous_substances.md) | Amount or concentration of substances such as hydrogen sulfide, carbon dioxid... |
| [gc_avg](gc_avg.md) | Average of GC content of all contigs |
| [gc_std](gc_std.md) | Standard deviation of GC content of all contigs |
| [gender_restroom](gender_restroom.md) | The gender type of the restroom |
| [gene_count](gene_count.md) |  |
| [gene_function_id](gene_function_id.md) |  |
| [genetic_mod](genetic_mod.md) | Genetic modifications of the genome of an organism, which may occur naturally... |
| [genome_feature_set](genome_feature_set.md) | This property links a database object to the set of all features |
| [geo_loc_name](geo_loc_name.md) | The geographical origin of the sample as defined by the country or sea name f... |
| [gff_coordinate](gff_coordinate.md) | A positive 1-based integer coordinate indicating start or end |
| [git_url](git_url.md) |  |
| [glucosidase_act](glucosidase_act.md) | Measurement of glucosidase activity |
| [gnps_identifiers](gnps_identifiers.md) |  |
| [gnps_task_identifiers](gnps_task_identifiers.md) | identifiers that link a NMDC study to a web-based report about metabolomics a... |
| [gold_analysis_project_identifiers](gold_analysis_project_identifiers.md) | identifiers for corresponding analysis project in GOLD |
| [gold_biosample_identifiers](gold_biosample_identifiers.md) | identifiers for corresponding sample in GOLD |
| [gold_identifiers](gold_identifiers.md) |  |
| [gold_path_field](gold_path_field.md) | This is a grouping for any of the gold path fields |
| [gold_sequencing_project_identifiers](gold_sequencing_project_identifiers.md) | identifiers for corresponding sequencing project in GOLD |
| [gold_study_identifiers](gold_study_identifiers.md) | identifiers for corresponding project(s) in GOLD |
| [gravidity](gravidity.md) | Whether or not subject is gravid, and if yes date due or date post-conception... |
| [gravity](gravity.md) | Information about treatment involving use of gravity factor to study various ... |
| [growth_facil](growth_facil.md) | Type of facility where the sampled plant was grown; controlled vocabulary: gr... |
| [growth_habit](growth_habit.md) | Characteristic shape, appearance or growth form of a plant species |
| [growth_hormone_regm](growth_hormone_regm.md) | Information about treatment involving use of growth hormones; should include ... |
| [gtdbtk_class](gtdbtk_class.md) |  |
| [gtdbtk_domain](gtdbtk_domain.md) |  |
| [gtdbtk_family](gtdbtk_family.md) |  |
| [gtdbtk_genus](gtdbtk_genus.md) |  |
| [gtdbtk_order](gtdbtk_order.md) |  |
| [gtdbtk_phylum](gtdbtk_phylum.md) |  |
| [gtdbtk_species](gtdbtk_species.md) |  |
| [habitat](habitat.md) |  |
| [hall_count](hall_count.md) | The total count of hallways and cooridors in the built structure |
| [handidness](handidness.md) | The handidness of the individual sampled |
| [has_numeric_value](has_numeric_value.md) |  |
| [has_raw_value](has_raw_value.md) |  |
| [has_unit](has_unit.md) | Example "m" |
| [has_boolean_value](has_boolean_value.md) | Links a quantity value to a boolean |
| [has_calibration](has_calibration.md) | A reference to a file that holds calibration information |
| [has_credit_associations](has_credit_associations.md) | This slot links a study to a credit association |
| [has_function](has_function.md) |  |
| [has_input](has_input.md) | An input to a process |
| [has_maximum_numeric_value](has_maximum_numeric_value.md) | The maximum value part, expressed as number, of the quantity value when the v... |
| [has_metabolite_quantifications](has_metabolite_quantifications.md) |  |
| [has_minimum_numeric_value](has_minimum_numeric_value.md) | The minimum value part, expressed as number, of the quantity value when the v... |
| [has_numeric_value](has_numeric_value.md) | Links a quantity value to a number |
| [has_output](has_output.md) | An output biosample to a processing step |
| [has_part](has_part.md) |  |
| [has_participants](has_participants.md) |  |
| [has_peptide_quantifications](has_peptide_quantifications.md) |  |
| [has_raw_value](has_raw_value.md) | The value that was specified for an annotation in raw form, i |
| [has_solution_components](has_solution_components.md) | Relationship from a Solution to one or more constituent solution components |
| [has_unit](has_unit.md) | Links a QuantityValue to a unit |
| [hc_produced](hc_produced.md) | Main hydrocarbon type produced from resource (i |
| [hcr](hcr.md) | Main Hydrocarbon Resource type |
| [hcr_fw_salinity](hcr_fw_salinity.md) | Original formation water salinity (prior to secondary recovery e |
| [hcr_geol_age](hcr_geol_age.md) | Geological age of hydrocarbon resource (Additional info: https://en |
| [hcr_pressure](hcr_pressure.md) | Original pressure of the hydrocarbon resource |
| [hcr_temp](hcr_temp.md) | Original temperature of the hydrocarbon resource |
| [heat_cool_type](heat_cool_type.md) | Methods of conditioning or heating a room or building |
| [heat_deliv_loc](heat_deliv_loc.md) | The location of heat delivery within the room |
| [heat_sys_deliv_meth](heat_sys_deliv_meth.md) | The method by which the heat is delivered through the system |
| [heat_system_id](heat_system_id.md) | The heating system identifier |
| [heavy_metals](heavy_metals.md) | Heavy metals present in the sequenced sample and their concentrations |
| [heavy_metals_meth](heavy_metals_meth.md) | Reference or method used in determining heavy metals |
| [height_carper_fiber](height_carper_fiber.md) | The average carpet fiber height in the indoor environment |
| [herbicide_regm](herbicide_regm.md) | Information about treatment involving use of herbicides; information about tr... |
| [highest_similarity_score](highest_similarity_score.md) |  |
| [horizon_meth](horizon_meth.md) | Reference or method used in determining the horizon |
| [host_age](host_age.md) | Age of host at the time of sampling; relevant scale depends on species and st... |
| [host_body_habitat](host_body_habitat.md) | Original body habitat where the sample was obtained from |
| [host_body_product](host_body_product.md) | Substance produced by the body, e |
| [host_body_site](host_body_site.md) | Name of body site where the sample was obtained from, such as a specific orga... |
| [host_body_temp](host_body_temp.md) | Core body temperature of the host when sample was collected |
| [host_color](host_color.md) | The color of host |
| [host_common_name](host_common_name.md) | Common name of the host |
| [host_diet](host_diet.md) | Type of diet depending on the host, for animals omnivore, herbivore etc |
| [host_disease_stat](host_disease_stat.md) | List of diseases with which the host has been diagnosed; can include multiple... |
| [host_dry_mass](host_dry_mass.md) | Measurement of dry mass |
| [host_family_relation](host_family_relation.md) | Familial relationships to other hosts in the same study; can include multiple... |
| [host_genotype](host_genotype.md) | Observed genotype |
| [host_growth_cond](host_growth_cond.md) | Literature reference giving growth conditions of the host |
| [host_height](host_height.md) | The height of subject |
| [host_last_meal](host_last_meal.md) | Content of last meal and time since feeding; can include multiple values |
| [host_length](host_length.md) | The length of subject |
| [host_life_stage](host_life_stage.md) | Description of life stage of host |
| [host_name](host_name.md) |  |
| [host_phenotype](host_phenotype.md) | Phenotype of human or other host |
| [host_sex](host_sex.md) | Gender or physical sex of the host |
| [host_shape](host_shape.md) | Morphological shape of host |
| [host_subject_id](host_subject_id.md) | A unique identifier by which each subject can be referred to, de-identified |
| [host_subspecf_genlin](host_subspecf_genlin.md) | Information about the genetic distinctness of the host organism below the sub... |
| [host_substrate](host_substrate.md) | The growth substrate of the host |
| [host_symbiont](host_symbiont.md) | The taxonomic name of the organism(s) found living in mutualistic, commensali... |
| [host_taxid](host_taxid.md) | NCBI taxon id of the host, e |
| [host_tot_mass](host_tot_mass.md) | Total mass of the host at collection, the unit depends on host |
| [host_wet_mass](host_wet_mass.md) | Measurement of wet mass |
| [humidity](humidity.md) | Amount of water vapour in the air, at the time of sampling |
| [humidity_regm](humidity_regm.md) | Information about treatment involving an exposure to varying degree of humidi... |
| [id](id.md) | A unique identifier for a thing |
| [igsn_biosample_identifiers](igsn_biosample_identifiers.md) | A list of identifiers for the biosample from the IGSN database |
| [igsn_identifiers](igsn_identifiers.md) |  |
| [img_identifiers](img_identifiers.md) | A list of identifiers that relate the biosample to records in the IMG databas... |
| [inchi](inchi.md) |  |
| [inchi_key](inchi_key.md) |  |
| [indoor_space](indoor_space.md) | A distinguishable space within a structure, the purpose for which discrete ar... |
| [indoor_surf](indoor_surf.md) | Type of indoor surface |
| [indust_eff_percent](indust_eff_percent.md) | Percentage of industrial effluents received by wastewater treatment plant |
| [inorg_particles](inorg_particles.md) | Concentration of particles such as sand, grit, metal particles, ceramics, etc |
| [input_base_count](input_base_count.md) | The nucleotide base count number of input reads for QC analysis |
| [input_contig_num](input_contig_num.md) |  |
| [input_mass](input_mass.md) | Total mass of sample used in activity |
| [input_read_bases](input_read_bases.md) | TODO       |
| [input_read_count](input_read_count.md) | The sequence count number of input reads for QC analysis |
| [input_volume](input_volume.md) | The volume of the input sample |
| [insdc_analysis_identifiers](insdc_analysis_identifiers.md) |  |
| [insdc_assembly_identifiers](insdc_assembly_identifiers.md) |  |
| [insdc_bioproject_identifiers](insdc_bioproject_identifiers.md) | identifiers for corresponding project in INSDC Bioproject |
| [insdc_biosample_identifiers](insdc_biosample_identifiers.md) | identifiers for corresponding sample in INSDC |
| [insdc_experiment_identifiers](insdc_experiment_identifiers.md) |  |
| [insdc_identifiers](insdc_identifiers.md) | Any identifier covered by the International Nucleotide Sequence Database Coll... |
| [insdc_secondary_sample_identifiers](insdc_secondary_sample_identifiers.md) | secondary identifiers for corresponding sample in INSDC |
| [insdc_sra_ena_study_identifiers](insdc_sra_ena_study_identifiers.md) | identifiers for corresponding project in INSDC SRA / ENA |
| [inside_lux](inside_lux.md) | The recorded value at sampling time (power density) |
| [instrument_name](instrument_name.md) | The name of the instrument that was used for processing the sample |
| [int_wall_cond](int_wall_cond.md) | The physical condition of the wall at the time of sampling; photos or video p... |
| [investigation_field](investigation_field.md) | field describing aspect of the investigation/study to which the sample belong... |
| [is_balanced](is_balanced.md) |  |
| [is_diastereoselective](is_diastereoselective.md) |  |
| [is_fully_characterized](is_fully_characterized.md) | False if includes R-groups |
| [is_pressurized](is_pressurized.md) | Whether or not pressure was applied to a thing or process |
| [is_stereo](is_stereo.md) |  |
| [is_transport](is_transport.md) |  |
| [isotope_exposure](isotope_exposure.md) | List isotope exposure or addition applied to your sample |
| [iw_bt_date_well](iw_bt_date_well.md) | Injection water breakthrough date per well following a secondary and/or terti... |
| [iwf](iwf.md) | Proportion of the produced fluids derived from injected water at the time of ... |
| [jgi_portal_identifiers](jgi_portal_identifiers.md) | identifiers for entities according to JGI Portal |
| [jgi_portal_study_identifiers](jgi_portal_study_identifiers.md) | Identifiers that link a NMDC study to a website hosting raw and analyzed data... |
| [keywords](keywords.md) | A list of keywords that used to associate the entity |
| [language](language.md) | Should use ISO 639-1 code e |
| [last_clean](last_clean.md) | The last time the floor was cleaned (swept, mopped, vacuumed) |
| [lat_lon](lat_lon.md) | The geographical origin of the sample as defined by latitude and longitude |
| [latitude](latitude.md) | latitude |
| [lbc_thirty](lbc_thirty.md) | lime buffer capacity, determined after 30 minute incubation |
| [lbceq](lbceq.md) | lime buffer capacity, determined at equilibrium after 5 day incubation |
| [left_participants](left_participants.md) |  |
| [library_preparation_kit](library_preparation_kit.md) |  |
| [library_preparation_set](library_preparation_set.md) | This property links a database object to the set of DNA extractions within it |
| [library_type](library_type.md) |  |
| [light_intensity](light_intensity.md) | Measurement of light intensity |
| [light_regm](light_regm.md) | Information about treatment(s) involving exposure to light, including both li... |
| [light_type](light_type.md) | Application of light to achieve some practical or aesthetic effect |
| [link_addit_analys](link_addit_analys.md) | Link to additional analysis results performed on the sample |
| [link_class_info](link_class_info.md) | Link to digitized soil maps or other soil classification information |
| [link_climate_info](link_climate_info.md) | Link to climate resource |
| [lithology](lithology.md) | Hydrocarbon resource main lithology (Additional information: http://petrowiki |
| [local_class](local_class.md) | Soil classification based on local soil classification system |
| [local_class_meth](local_class_meth.md) | Reference or method used in determining the local soil classification |
| [location](location.md) |  |
| [longitude](longitude.md) | longitude |
| [low_depth_contig_num](low_depth_contig_num.md) |  |
| [magnesium](magnesium.md) | Concentration of magnesium in the sample |
| [mags_activity_set](mags_activity_set.md) | This property links a database object to the set of MAGs analysis activities |
| [mags_list](mags_list.md) |  |
| [manganese](manganese.md) | Concentration of manganese in the sample |
| [mass](mass.md) | A physical quality that inheres in a bearer by virtue of the proportion of th... |
| [material_component_separation](material_component_separation.md) | A material processing in which components of an input material become segrega... |
| [max_occup](max_occup.md) | The maximum amount of people allowed in the indoor environment |
| [md5_checksum](md5_checksum.md) | MD5 checksum of file (pre-compressed) |
| [mean_frict_vel](mean_frict_vel.md) | Measurement of mean friction velocity |
| [mean_peak_frict_vel](mean_peak_frict_vel.md) | Measurement of mean peak friction velocity |
| [mech_struc](mech_struc.md) | mechanical structure: a moving structure |
| [mechanical_damage](mechanical_damage.md) | Information about any mechanical damage exerted on the plant; can include mul... |
| [members_id](members_id.md) |  |
| [metabolite_quantified](metabolite_quantified.md) | the specific metabolite identifier |
| [metabolomics_analysis_activity_set](metabolomics_analysis_activity_set.md) | This property links a database object to the set of metabolomics analysis act... |
| [metagenome_annotation_activity_set](metagenome_annotation_activity_set.md) | This property links a database object to the set of metagenome annotation act... |
| [metagenome_annotation_id](metagenome_annotation_id.md) |  |
| [metagenome_assembly_parameter](metagenome_assembly_parameter.md) |  |
| [metagenome_assembly_set](metagenome_assembly_set.md) | This property links a database object to the set of metagenome assembly activ... |
| [metagenome_sequencing_activity_set](metagenome_sequencing_activity_set.md) | This property links a database object to the set of metagenome sequencing act... |
| [metaproteomics_analysis_activity_set](metaproteomics_analysis_activity_set.md) | This property links a database object to the set of metaproteomics analysis a... |
| [metatranscriptome_activity_set](metatranscriptome_activity_set.md) | This property links a database object to the set of metatranscriptome analysi... |
| [methane](methane.md) | Methane (gas) amount or concentration at the time of sampling |
| [mgnify_analysis_identifiers](mgnify_analysis_identifiers.md) |  |
| [mgnify_identifiers](mgnify_identifiers.md) |  |
| [mgnify_project_identifiers](mgnify_project_identifiers.md) | identifiers for corresponding project in MGnify |
| [micro_biomass_c_meth](micro_biomass_c_meth.md) | Reference or method used in determining microbial biomass carbon |
| [micro_biomass_meth](micro_biomass_meth.md) | Reference or method used in determining microbial biomass |
| [micro_biomass_n_meth](micro_biomass_n_meth.md) | Reference or method used in determining microbial biomass nitrogen |
| [microbial_biomass](microbial_biomass.md) | The part of the organic matter in the soil that constitutes living microorgan... |
| [microbial_biomass_c](microbial_biomass_c.md) | The part of the organic matter in the soil that constitutes living microorgan... |
| [microbial_biomass_n](microbial_biomass_n.md) | The part of the organic matter in the soil that constitutes living microorgan... |
| [min_q_value](min_q_value.md) | smallest Q-Value associated with the peptide sequence as provided by MSGFPlus... |
| [mineral_nutr_regm](mineral_nutr_regm.md) | Information about treatment involving the use of mineral supplements; should ... |
| [misc_param](misc_param.md) | Any other measurement performed or parameter collected, that is not listed he... |
| [mod_date](mod_date.md) | The last date on which the database information was modified |
| [model](model.md) |  |
| [modifier_substance](modifier_substance.md) | The type of modification being done |
| [n_alkanes](n_alkanes.md) | Concentration of n-alkanes; can include multiple n-alkanes |
| [name](name.md) | A human readable label for an entity |
| [ncbi_project_name](ncbi_project_name.md) |  |
| [ncbi_taxonomy_name](ncbi_taxonomy_name.md) |  |
| [neon_biosample_identifiers](neon_biosample_identifiers.md) |  |
| [neon_identifiers](neon_identifiers.md) | identifiers for entities according to NEON |
| [neon_study_identifiers](neon_study_identifiers.md) |  |
| [nitrate](nitrate.md) | Concentration of nitrate in the sample |
| [nitrate_nitrogen](nitrate_nitrogen.md) | Concentration of nitrate nitrogen in the sample |
| [nitrite](nitrite.md) | Concentration of nitrite in the sample |
| [nitrite_nitrogen](nitrite_nitrogen.md) | Concentration of nitrite nitrogen in the sample |
| [nitro](nitro.md) | Concentration of nitrogen (total) |
| [nom_analysis_activity_set](nom_analysis_activity_set.md) | This property links a database object to the set of natural organic matter (N... |
| [non_microb_biomass](non_microb_biomass.md) | Amount of biomass; should include the name for the part of biomass measured, ... |
| [non_microb_biomass_method](non_microb_biomass_method.md) | Reference or method used in determining biomass |
| [non_min_nutr_regm](non_min_nutr_regm.md) | Information about treatment involving the exposure of plant to non-mineral nu... |
| [notes](notes.md) | from study class |
| [nucl_acid_amp](nucl_acid_amp.md) | A link to a literature reference, electronic resource or a standard operating... |
| [nucl_acid_ext](nucl_acid_ext.md) | A link to a literature reference, electronic resource or a standard operating... |
| [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md) |  |
| [num_16s](num_16s.md) |  |
| [num_23s](num_23s.md) |  |
| [num_5s](num_5s.md) |  |
| [num_aligned_reads](num_aligned_reads.md) | The sequence count number of input reads aligned to assembled contigs |
| [num_input_reads](num_input_reads.md) | The sequence count number of input reads for assembly |
| [num_t_rna](num_t_rna.md) |  |
| [number_of_contig](number_of_contig.md) |  |
| [number_pets](number_pets.md) | The number of pets residing in the sampled space |
| [number_plants](number_plants.md) | The number of plant(s) in the sampling space |
| [number_resident](number_resident.md) | The number of individuals currently occupying in the sampling location |
| [object_set](object_set.md) | Applies to a property that links a database object to a set of objects |
| [objective](objective.md) | The scientific objectives associated with the entity |
| [occup_density_samp](occup_density_samp.md) | Average number of occupants at time of sampling per square footage |
| [occup_document](occup_document.md) | The type of documentation of occupancy |
| [occup_samp](occup_samp.md) | Number of occupants present at time of sample within the given space |
| [omics_processing_identifiers](omics_processing_identifiers.md) |  |
| [omics_processing_set](omics_processing_set.md) | This property links a database object to the set of omics processings within ... |
| [omics_type](omics_type.md) | The type of omics data |
| [orcid](orcid.md) | The ORCID of a person |
| [ordered_mobile_phases](ordered_mobile_phases.md) | The solution(s) that moves through a chromatography column |
| [org_carb](org_carb.md) | Concentration of organic carbon |
| [org_count_qpcr_info](org_count_qpcr_info.md) | If qpcr was used for the cell count, the target gene name, the primer sequenc... |
| [org_matter](org_matter.md) | Concentration of organic matter |
| [org_nitro](org_nitro.md) | Concentration of organic nitrogen |
| [org_nitro_method](org_nitro_method.md) | Method used for obtaining organic nitrogen |
| [org_particles](org_particles.md) | Concentration of particles such as faeces, hairs, food, vomit, paper fibers, ... |
| [organism_count](organism_count.md) | Total cell count of any organism (or group of organisms) per gram, volume or ... |
| [other_treatment](other_treatment.md) | Other treatments applied to your samples that are not applicable to the provi... |
| [output_base_count](output_base_count.md) | After QC analysis nucleotide base count number |
| [output_read_bases](output_read_bases.md) | TODO |
| [output_read_count](output_read_count.md) | After QC analysis sequence count number |
| [owc_tvdss](owc_tvdss.md) | Depth of the original oil water contact (OWC) zone (average) (m TVDSS) |
| [oxy_stat_samp](oxy_stat_samp.md) | Oxygenation status of sample |
| [oxygen](oxygen.md) | Oxygen (gas) amount or concentration at the time of sampling |
| [part_of](part_of.md) | Links a resource to another resource that either logically or physically incl... |
| [part_org_carb](part_org_carb.md) | Concentration of particulate organic carbon |
| [part_org_nitro](part_org_nitro.md) | Concentration of particulate organic nitrogen |
| [particle_class](particle_class.md) | Particles are classified, based on their size, into six general categories:cl... |
| [pcr_cond](pcr_cond.md) | Description of reaction conditions and components of PCR in the form of 'init... |
| [pcr_cycles](pcr_cycles.md) |  |
| [pcr_primers](pcr_primers.md) | PCR primers that were used to amplify the sequence of the targeted gene, locu... |
| [peptide_sequence](peptide_sequence.md) |  |
| [peptide_sequence_count](peptide_sequence_count.md) | count of peptide sequences grouped to the best_protein |
| [peptide_spectral_count](peptide_spectral_count.md) | sum of filter passing MS2 spectra associated with the peptide sequence within... |
| [peptide_sum_masic_abundance](peptide_sum_masic_abundance.md) | combined MS1 extracted ion chromatograms derived from MS2 spectra associated ... |
| [permeability](permeability.md) | Measure of the ability of a hydrocarbon resource to allow fluids to pass thro... |
| [perturbation](perturbation.md) | Type of perturbation, e |
| [pesticide_regm](pesticide_regm.md) | Information about treatment involving use of insecticides; should include the... |
| [petroleum_hydrocarb](petroleum_hydrocarb.md) | Concentration of petroleum hydrocarbon |
| [ph](ph.md) | Ph measurement of the sample, or liquid portion of sample, or aqueous phase o... |
| [ph_meth](ph_meth.md) | Reference or method used in determining ph |
| [ph_regm](ph_regm.md) | Information about treatment involving exposure of plants to varying levels of... |
| [phaeopigments](phaeopigments.md) | Concentration of phaeopigments; can include multiple phaeopigments |
| [phase](phase.md) | The phase for a coding sequence entity |
| [phosphate](phosphate.md) | Concentration of phosphate |
| [phosplipid_fatt_acid](phosplipid_fatt_acid.md) | Concentration of phospholipid fatty acids; can include multiple values |
| [photon_flux](photon_flux.md) | Measurement of photon flux |
| [planned_process_set](planned_process_set.md) | This property links a database object to the set of planned processes within ... |
| [plant_growth_med](plant_growth_med.md) | Specification of the media for growing the plants or tissue cultured samples,... |
| [plant_product](plant_product.md) | Substance produced by the plant, where the sample was obtained from |
| [plant_sex](plant_sex.md) | Sex of the reproductive parts on the whole plant, e |
| [plant_struc](plant_struc.md) | Name of plant structure the sample was obtained from; for Plant Ontology (PO)... |
| [pollutants](pollutants.md) | Pollutant types and, amount or concentrations measured at the time of samplin... |
| [pool_dna_extracts](pool_dna_extracts.md) | Indicate whether multiple DNA extractions were mixed |
| [pooling_set](pooling_set.md) |  |
| [porosity](porosity.md) | Porosity of deposited sediment is volume of voids divided by the total volume... |
| [potassium](potassium.md) | Concentration of potassium in the sample |
| [pour_point](pour_point.md) | Temperature at which a liquid becomes semi solid and loses its flow character... |
| [pre_treatment](pre_treatment.md) | The process of pre-treatment removes materials that can be easily collected f... |
| [pres_animal_insect](pres_animal_insect.md) | The type and number of animals or insects present in the sampling space |
| [pressure](pressure.md) | Pressure to which the sample is subject to, in atmospheres |
| [prev_land_use_meth](prev_land_use_meth.md) | Reference or method used in determining previous land use and dates |
| [previous_land_use](previous_land_use.md) | Previous land use and dates |
| [primary_prod](primary_prod.md) | Measurement of primary production, generally measured as isotope uptake |
| [primary_treatment](primary_treatment.md) | The process to produce both a generally homogeneous liquid capable of being t... |
| [principal_investigator](principal_investigator.md) | Principal Investigator who led the study and/or generated the dataset |
| [processed_sample_set](processed_sample_set.md) | This property links a database object to the set of processed samples within ... |
| [processing_institution](processing_institution.md) | The organization that processed the sample |
| [prod_rate](prod_rate.md) | Oil and/or gas production rates per well (e |
| [prod_start_date](prod_start_date.md) | Date of field's first production |
| [profile_image_url](profile_image_url.md) | A url that points to an image of a person |
| [profile_position](profile_position.md) | Cross-sectional position in the hillslope where sample was collected |
| [project_id](project_id.md) | Proposal IDs or names associated with dataset |
| [proport_woa_temperature](proport_woa_temperature.md) |  |
| [proposal_dna](proposal_dna.md) |  |
| [proposal_rna](proposal_rna.md) |  |
| [protein_spectral_count](protein_spectral_count.md) | sum of filter passing MS2 spectra associated with the best protein within a g... |
| [protein_sum_masic_abundance](protein_sum_masic_abundance.md) | combined MS1 extracted ion chromatograms derived from MS2 spectra associated ... |
| [protocol_link](protocol_link.md) |  |
| [quad_pos](quad_pos.md) | The quadrant position of the sampling room within the building |
| [quality_control_report](quality_control_report.md) |  |
| [radiation_regm](radiation_regm.md) | Information about treatment involving exposure of plant or a plant part to a ... |
| [rainfall_regm](rainfall_regm.md) | Information about treatment involving an exposure to a given amount of rainfa... |
| [reactor_type](reactor_type.md) | Anaerobic digesters can be designed and engineered to operate using a number ... |
| [read_based_taxonomy_analysis_activity_set](read_based_taxonomy_analysis_activity_set.md) | This property links a database object to the set of read based analysis activ... |
| [read_qc_analysis_activity_set](read_qc_analysis_activity_set.md) | This property links a database object to the set of read QC analysis activiti... |
| [read_qc_analysis_statistic](read_qc_analysis_statistic.md) |  |
| [redox_potential](redox_potential.md) | Redox potential, measured relative to a hydrogen cell, indicating oxidation o... |
| [rel_air_humidity](rel_air_humidity.md) | Partial vapor and air pressure, density of the vapor and air, or by the actua... |
| [rel_humidity_out](rel_humidity_out.md) | The recorded outside relative humidity value at the time of sampling |
| [rel_samp_loc](rel_samp_loc.md) | The sampling location within the train car |
| [related_identifiers](related_identifiers.md) | Identifiers assigned to a thing that is similar to that which is represented ... |
| [relevant_protocols](relevant_protocols.md) |  |
| [replicate_number](replicate_number.md) | If sending biological replicates, indicate the rep number here |
| [reservoir](reservoir.md) | Name of the reservoir (e |
| [resins_pc](resins_pc.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... |
| [right_participants](right_participants.md) |  |
| [rna_absorb1](rna_absorb1.md) | 260/280 measurement of RNA sample purity |
| [rna_absorb2](rna_absorb2.md) | 260/230 measurement of RNA sample purity |
| [rna_collect_site](rna_collect_site.md) | Provide information on the site your RNA sample was collected from |
| [rna_concentration](rna_concentration.md) |  |
| [rna_cont_type](rna_cont_type.md) | Tube or plate (96-well) |
| [rna_cont_well](rna_cont_well.md) |  |
| [rna_container_id](rna_container_id.md) |  |
| [rna_isolate_meth](rna_isolate_meth.md) | Describe the method/protocol/kit used to extract DNA/RNA |
| [rna_organisms](rna_organisms.md) | List any organisms known or suspected to grow in co-culture, as well as estim... |
| [rna_project_contact](rna_project_contact.md) |  |
| [rna_samp_id](rna_samp_id.md) |  |
| [rna_sample_format](rna_sample_format.md) | Solution in which the RNA sample has been suspended |
| [rna_sample_name](rna_sample_name.md) | Give the RNA sample a name that is meaningful to you |
| [rna_seq_project](rna_seq_project.md) |  |
| [rna_seq_project_name](rna_seq_project_name.md) |  |
| [rna_seq_project_pi](rna_seq_project_pi.md) |  |
| [rna_volume](rna_volume.md) |  |
| [room_air_exch_rate](room_air_exch_rate.md) | The rate at which outside air replaces indoor air in a given space |
| [room_architec_elem](room_architec_elem.md) | The unique details and component parts that, together, form the architecture ... |
| [room_condt](room_condt.md) | The condition of the room at the time of sampling |
| [room_connected](room_connected.md) | List of rooms connected to the sampling room by a doorway |
| [room_count](room_count.md) | The total count of rooms in the built structure including all room types |
| [room_dim](room_dim.md) | The length, width and height of sampling room |
| [room_door_dist](room_door_dist.md) | Distance between doors (meters) in the hallway between the sampling room and ... |
| [room_door_share](room_door_share.md) | List of room(s) (room number, room name) sharing a door with the sampling roo... |
| [room_hallway](room_hallway.md) | List of room(s) (room number, room name) located in the same hallway as sampl... |
| [room_loc](room_loc.md) | The position of the room within the building |
| [room_moist_dam_hist](room_moist_dam_hist.md) | The history of moisture damage or mold in the past 12 months |
| [room_net_area](room_net_area.md) | The net floor area of sampling room |
| [room_occup](room_occup.md) | Count of room occupancy at time of sampling |
| [room_samp_pos](room_samp_pos.md) | The horizontal sampling position in the room relative to architectural elemen... |
| [room_type](room_type.md) | The main purpose or activity of the sampling room |
| [room_vol](room_vol.md) | Volume of sampling room |
| [room_wall_share](room_wall_share.md) | List of room(s) (room number, room name) sharing a wall with the sampling roo... |
| [room_window_count](room_window_count.md) | Number of windows in the room |
| [root_cond](root_cond.md) | Relevant rooting conditions such as field plot size, sowing density, containe... |
| [root_med_carbon](root_med_carbon.md) | Source of organic carbon in the culture rooting medium; e |
| [root_med_macronutr](root_med_macronutr.md) | Measurement of the culture rooting medium macronutrients (N,P, K, Ca, Mg, S);... |
| [root_med_micronutr](root_med_micronutr.md) | Measurement of the culture rooting medium micronutrients (Fe, Mn, Zn, B, Cu, ... |
| [root_med_ph](root_med_ph.md) | pH measurement of the culture rooting medium; e |
| [root_med_regl](root_med_regl.md) | Growth regulators in the culture rooting medium such as cytokinins, auxins, g... |
| [root_med_solid](root_med_solid.md) | Specification of the solidifying agent in the culture rooting medium; e |
| [root_med_suppl](root_med_suppl.md) | Organic supplements of the culture rooting medium, such as vitamins, amino ac... |
| [salinity](salinity.md) | The total concentration of all dissolved salts in a liquid or solid sample |
| [salinity_category](salinity_category.md) | Categorical description of the sample's salinity |
| [salinity_meth](salinity_meth.md) | Reference or method used in determining salinity |
| [salt_regm](salt_regm.md) | Information about treatment involving use of salts as supplement to liquid an... |
| [samp_capt_status](samp_capt_status.md) | Reason for the sample |
| [samp_collec_device](samp_collec_device.md) | The device used to collect an environmental sample |
| [samp_collec_method](samp_collec_method.md) | The method employed for collecting the sample |
| [samp_collect_point](samp_collect_point.md) | Sampling point on the asset were sample was collected (e |
| [samp_dis_stage](samp_dis_stage.md) | Stage of the disease at the time of sample collection, e |
| [samp_floor](samp_floor.md) | The floor of the building, where the sampling room is located |
| [samp_loc_corr_rate](samp_loc_corr_rate.md) | Metal corrosion rate is the speed of metal deterioration due to environmental... |
| [samp_mat_process](samp_mat_process.md) | A brief description of any processing applied to the sample during or after r... |
| [samp_md](samp_md.md) | In non deviated well, measured depth is equal to the true vertical depth, TVD... |
| [samp_name](samp_name.md) | A local identifier or name that for the material sample used for extracting n... |
| [samp_preserv](samp_preserv.md) | Preservative added to the sample (e |
| [samp_room_id](samp_room_id.md) | Sampling room number |
| [samp_size](samp_size.md) | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample coll... |
| [samp_sort_meth](samp_sort_meth.md) | Method by which samples are sorted; open face filter collecting total suspend... |
| [samp_store_dur](samp_store_dur.md) | Duration for which the sample was stored |
| [samp_store_loc](samp_store_loc.md) | Location at which sample was stored, usually name of a specific freezer/room |
| [samp_store_temp](samp_store_temp.md) | Temperature at which sample was stored, e |
| [samp_subtype](samp_subtype.md) | Name of sample sub-type |
| [samp_taxon_id](samp_taxon_id.md) | NCBI taxon id of the sample |
| [samp_time_out](samp_time_out.md) | The recent and long term history of outside sampling |
| [samp_transport_cond](samp_transport_cond.md) | Sample transport duration (in days or hrs) and temperature the sample was exp... |
| [samp_tvdss](samp_tvdss.md) | Depth of the sample i |
| [samp_type](samp_type.md) | The type of material from which the sample was obtained |
| [samp_vol_we_dna_ext](samp_vol_we_dna_ext.md) | Volume (ml) or mass (g) of total collected sample processed for DNA extractio... |
| [samp_weather](samp_weather.md) | The weather on the sampling day |
| [samp_well_name](samp_well_name.md) | Name of the well (e |
| [sample_collection_day](sample_collection_day.md) |  |
| [sample_collection_hour](sample_collection_hour.md) |  |
| [sample_collection_minute](sample_collection_minute.md) |  |
| [sample_collection_month](sample_collection_month.md) |  |
| [sample_collection_site](sample_collection_site.md) |  |
| [sample_collection_year](sample_collection_year.md) |  |
| [sample_link](sample_link.md) | A unique identifier to assign parent-child, subsample, or sibling samples |
| [sample_shipped](sample_shipped.md) | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample sent... |
| [sample_type](sample_type.md) | Type of sample being submitted |
| [saturates_pc](saturates_pc.md) | Saturate, Aromatic, Resin and Asphaltene¬†(SARA) is an analysis method that d... |
| [scaf_bp](scaf_bp.md) | Total size in bp of all scaffolds |
| [scaf_l50](scaf_l50.md) | Given a set of scaffolds, the L50 is defined as the sequence length of the sh... |
| [scaf_l90](scaf_l90.md) | The L90 statistic is less than or equal to the L50 statistic; it is the lengt... |
| [scaf_l_gt50k](scaf_l_gt50k.md) | Total size in bp of all scaffolds greater than 50 KB |
| [scaf_logsum](scaf_logsum.md) | The sum of the (length*log(length)) of all scaffolds, times some constant |
| [scaf_max](scaf_max.md) | Maximum scaffold length |
| [scaf_n50](scaf_n50.md) | Given a set of scaffolds, each with its own length, the N50 count is defined ... |
| [scaf_n90](scaf_n90.md) | Given a set of scaffolds, each with its own length, the N90 count is defined ... |
| [scaf_n_gt50k](scaf_n_gt50k.md) | Total sequence count of scaffolds greater than 50 KB |
| [scaf_pct_gt50k](scaf_pct_gt50k.md) | Total sequence size percentage of scaffolds greater than 50 KB |
| [scaf_powsum](scaf_powsum.md) | Powersum of all scaffolds is the same as logsum except that it uses the sum o... |
| [scaffolds](scaffolds.md) | Total sequence count of all scaffolds |
| [season](season.md) | The season when sampling occurred |
| [season_environment](season_environment.md) | Treatment involving an exposure to a particular season (e |
| [season_precpt](season_precpt.md) | The average of all seasonal precipitation values known, or an estimated equiv... |
| [season_temp](season_temp.md) | Mean seasonal temperature |
| [season_use](season_use.md) | The seasons the space is occupied |
| [secondary_treatment](secondary_treatment.md) | The process for substantially degrading the biological content of the sewage |
| [sediment_type](sediment_type.md) | Information about the sediment type based on major constituents |
| [separation_method](separation_method.md) | The method that was used to separate a substance from a solution or mixture |
| [seq_meth](seq_meth.md) | Sequencing machine used |
| [seq_quality_check](seq_quality_check.md) | Indicate if the sequence has been called by automatic systems (none) or under... |
| [seqid](seqid.md) | The ID of the landmark used to establish the coordinate system for the curren... |
| [sequencing_field](sequencing_field.md) |  |
| [sewage_type](sewage_type.md) | Type of wastewater treatment plant as municipial or industrial |
| [shad_dev_water_mold](shad_dev_water_mold.md) | Signs of the presence of mold or mildew on the shading device |
| [shading_device_cond](shading_device_cond.md) | The physical condition of the shading device at the time of sampling |
| [shading_device_loc](shading_device_loc.md) | The location of the shading device in relation to the built structure |
| [shading_device_mat](shading_device_mat.md) | The material the shading device is composed of |
| [shading_device_type](shading_device_type.md) | The type of shading device |
| [sieving](sieving.md) | Collection design of pooled samples and/or sieve size and amount of sample si... |
| [silicate](silicate.md) | Concentration of silicate |
| [size_frac](size_frac.md) | Filtering pore size used in sample preparation |
| [size_frac_low](size_frac_low.md) | Refers to the mesh/pore size used to pre-filter/pre-sort the sample |
| [size_frac_up](size_frac_up.md) | Refers to the mesh/pore size used to retain the sample |
| [slope_aspect](slope_aspect.md) | The direction a slope faces |
| [slope_gradient](slope_gradient.md) | Commonly called 'slope' |
| [sludge_retent_time](sludge_retent_time.md) | The time activated sludge remains in reactor |
| [smarts_string](smarts_string.md) |  |
| [smiles](smiles.md) | A string encoding of a molecular graph, no chiral or isotopic information |
| [sodium](sodium.md) | Sodium concentration in the sample |
| [soil_annual_season_temp](soil_annual_season_temp.md) |  |
| [soil_horizon](soil_horizon.md) | Specific layer in the land area which measures parallel to the soil surface a... |
| [soil_text_measure](soil_text_measure.md) | The relative proportion of different grain sizes of mineral particles in a so... |
| [soil_texture_meth](soil_texture_meth.md) | Reference or method used in determining soil texture |
| [soil_type](soil_type.md) | Description of the soil type or classification |
| [soil_type_meth](soil_type_meth.md) | Reference or method used in determining soil series name or other lower-level... |
| [solar_irradiance](solar_irradiance.md) | The amount of solar energy that arrives at a specific area of a surface durin... |
| [soluble_inorg_mat](soluble_inorg_mat.md) | Concentration of substances such as ammonia, road-salt, sea-salt, cyanide, hy... |
| [soluble_iron_micromol](soluble_iron_micromol.md) |  |
| [soluble_org_mat](soluble_org_mat.md) | Concentration of substances such as urea, fruit sugars, soluble proteins, dru... |
| [soluble_react_phosp](soluble_react_phosp.md) | Concentration of soluble reactive phosphorus |
| [source_mat_id](source_mat_id.md) | A unique identifier assigned to a material sample (as defined by http://rs |
| [space_typ_state](space_typ_state.md) | Customary or normal state of the space |
| [specific](specific.md) | The building specifications |
| [specific_ecosystem](specific_ecosystem.md) | Specific ecosystems represent specific features of the environment like aphot... |
| [specific_humidity](specific_humidity.md) | The mass of water vapour in a unit mass of moist air, usually expressed as gr... |
| [sr_dep_env](sr_dep_env.md) | Source rock depositional environment (https://en |
| [sr_geol_age](sr_geol_age.md) | Geological age of source rock (Additional info: https://en |
| [sr_kerog_type](sr_kerog_type.md) | Origin of kerogen |
| [sr_lithology](sr_lithology.md) | Lithology of source rock (https://en |
| [standing_water_regm](standing_water_regm.md) | Treatment involving an exposure to standing water during a plant's life span,... |
| [start](start.md) | The start of the feature in positive 1-based integer coordinates |
| [start_date](start_date.md) | The date on which any process or activity was started |
| [start_date_inc](start_date_inc.md) | Date the incubation was started |
| [start_time_inc](start_time_inc.md) | Time the incubation was started |
| [started_at_time](started_at_time.md) |  |
| [stationary_phase](stationary_phase.md) | The material the stationary phase is comprised of used in chromatography |
| [status](status.md) |  |
| [stoichiometry](stoichiometry.md) | from reaction participant class |
| [store_cond](store_cond.md) | Explain how and for how long the soil sample was stored before DNA extraction... |
| [strand](strand.md) | The strand on which a feature is located |
| [study_category](study_category.md) | The type of research initiative |
| [study_identifiers](study_identifiers.md) |  |
| [study_image](study_image.md) | Links a study to one or more images |
| [study_set](study_set.md) | This property links a database object to the set of studies within it |
| [subject](subject.md) |  |
| [substructure_type](substructure_type.md) | The substructure or under building is that largely hidden section of the buil... |
| [subsurface_depth](subsurface_depth.md) |  |
| [sulfate](sulfate.md) | Concentration of sulfate in the sample |
| [sulfate_fw](sulfate_fw.md) | Original sulfate concentration in the hydrocarbon resource |
| [sulfide](sulfide.md) | Concentration of sulfide in the sample |
| [surf_air_cont](surf_air_cont.md) | Contaminant identified on surface |
| [surf_humidity](surf_humidity.md) | Surfaces: water activity as a function of air and material moisture |
| [surf_material](surf_material.md) | Surface materials at the point of sampling |
| [surf_moisture](surf_moisture.md) | Water held on a surface |
| [surf_moisture_ph](surf_moisture_ph.md) | ph measurement of surface |
| [surf_temp](surf_temp.md) | Temperature of the surface at the time of sampling |
| [suspend_part_matter](suspend_part_matter.md) | Concentration of suspended particulate matter |
| [suspend_solids](suspend_solids.md) | Concentration of substances including a wide variety of material, such as sil... |
| [tan](tan.md) | Total Acid Number¬†(TAN) is a measurement of acidity that is determined by th... |
| [target_gene](target_gene.md) | Targeted gene or locus name for marker gene studies |
| [target_subfragment](target_subfragment.md) | Name of subfragment of a gene or locus |
| [technical_reps](technical_reps.md) | If sending technical replicates of the same sample, indicate the replicate co... |
| [temp](temp.md) | Temperature of the sample at the time of sampling |
| [temp_out](temp_out.md) | The recorded temperature value at sampling time outside |
| [temperature](temperature.md) | The value of a temperature measurement or temperature used in a process |
| [term](term.md) | pointer to an ontology class |
| [tertiary_treatment](tertiary_treatment.md) | The process providing a final treatment stage to raise the effluent quality b... |
| [tidal_stage](tidal_stage.md) | Stage of tide |
| [tillage](tillage.md) | Note method(s) used for tilling |
| [tiss_cult_growth_med](tiss_cult_growth_med.md) | Description of plant tissue culture growth media used |
| [title](title.md) | A name given to the entity that differs from the name/label programmatically ... |
| [toluene](toluene.md) | Concentration of toluene in the sample |
| [too_short_contig_num](too_short_contig_num.md) |  |
| [tot_carb](tot_carb.md) | Total carbon content |
| [tot_depth_water_col](tot_depth_water_col.md) | Measurement of total depth of water column |
| [tot_diss_nitro](tot_diss_nitro.md) | Total dissolved nitrogen concentration, reported as nitrogen, measured by: to... |
| [tot_inorg_nitro](tot_inorg_nitro.md) | Total inorganic nitrogen content |
| [tot_iron](tot_iron.md) | Concentration of total iron in the sample |
| [tot_nitro](tot_nitro.md) | Total nitrogen concentration of water samples, calculated by: total nitrogen ... |
| [tot_nitro_cont_meth](tot_nitro_cont_meth.md) | Reference or method used in determining the total nitrogen |
| [tot_nitro_content](tot_nitro_content.md) | Total nitrogen content of the sample |
| [tot_org_c_meth](tot_org_c_meth.md) | Reference or method used in determining total organic carbon |
| [tot_org_carb](tot_org_carb.md) | Definition for soil: total organic carbon content of the soil, definition oth... |
| [tot_part_carb](tot_part_carb.md) | Total particulate carbon content |
| [tot_phosp](tot_phosp.md) | Total phosphorus concentration in the sample, calculated by: total phosphorus... |
| [tot_phosphate](tot_phosphate.md) | Total amount or concentration of phosphate |
| [tot_sulfur](tot_sulfur.md) | Concentration of total sulfur in the sample |
| [total_bases](total_bases.md) |  |
| [train_line](train_line.md) | The subway line name |
| [train_stat_loc](train_stat_loc.md) | The train station collection location |
| [train_stop_loc](train_stop_loc.md) | The train stop collection location |
| [turbidity](turbidity.md) | Measure of the amount of cloudiness or haziness in water caused by individual... |
| [tvdss_of_hcr_press](tvdss_of_hcr_press.md) | True vertical depth subsea (TVDSS) of the hydrocarbon resource where the orig... |
| [tvdss_of_hcr_temp](tvdss_of_hcr_temp.md) | True vertical depth subsea (TVDSS) of the hydrocarbon resource where the orig... |
| [typ_occup_density](typ_occup_density.md) | Customary or normal density of occupants |
| [type](type.md) | An optional string that specifies the type object |
| [unbinned_contig_num](unbinned_contig_num.md) |  |
| [url](url.md) |  |
| [used](used.md) |  |
| [value](value.md) |  |
| [vendor](vendor.md) |  |
| [ventilation_rate](ventilation_rate.md) | Ventilation rate of the system in the sampled premises |
| [ventilation_type](ventilation_type.md) | Ventilation system used in the sampled premises |
| [version](version.md) |  |
| [vfa](vfa.md) | Concentration of Volatile Fatty Acids in the sample |
| [vfa_fw](vfa_fw.md) | Original volatile fatty acid concentration in the hydrocarbon resource |
| [vis_media](vis_media.md) | The building visual media |
| [viscosity](viscosity.md) | A measure of oil's resistance¬†to gradual deformation by¬†shear stress¬†or¬†t... |
| [volatile_org_comp](volatile_org_comp.md) | Concentration of carbon-based chemicals that easily evaporate at room tempera... |
| [volume](volume.md) | The volume of a substance |
| [wall_area](wall_area.md) | The total area of the sampled room's walls |
| [wall_const_type](wall_const_type.md) | The building class of the wall defined by the composition of the building ele... |
| [wall_finish_mat](wall_finish_mat.md) | The material utilized to finish the outer most layer of the wall |
| [wall_height](wall_height.md) | The average height of the walls in the sampled room |
| [wall_loc](wall_loc.md) | The relative location of the wall within the room |
| [wall_surf_treatment](wall_surf_treatment.md) | The surface treatment of interior wall |
| [wall_texture](wall_texture.md) | The feel, appearance, or consistency of a wall surface |
| [wall_thermal_mass](wall_thermal_mass.md) | The ability of the wall to provide inertia against temperature fluctuations |
| [wall_water_mold](wall_water_mold.md) | Signs of the presence of mold or mildew on a wall |
| [was_generated_by](was_generated_by.md) |  |
| [was_informed_by](was_informed_by.md) |  |
| [wastewater_type](wastewater_type.md) | The origin of wastewater such as human waste, rainfall, storm drains, etc |
| [water_cont_soil_meth](water_cont_soil_meth.md) | Reference or method used in determining the water content of soil |
| [water_content](water_content.md) | Water content measurement |
| [water_current](water_current.md) | Measurement of magnitude and direction of flow within a fluid |
| [water_cut](water_cut.md) | Current amount of water (%) in a produced fluid stream; or the average of the... |
| [water_feat_size](water_feat_size.md) | The size of the water feature |
| [water_feat_type](water_feat_type.md) | The type of water feature present within the building being sampled |
| [water_prod_rate](water_prod_rate.md) | Water production rates per well (e |
| [water_temp_regm](water_temp_regm.md) | Information about treatment involving an exposure to water with varying degre... |
| [watering_regm](watering_regm.md) | Information about treatment involving an exposure to watering frequencies, tr... |
| [websites](websites.md) | A list of websites that are associated with the entity |
| [weekday](weekday.md) | The day of the week when sampling occurred |
| [win](win.md) | A unique identifier of a well or wellbore |
| [wind_direction](wind_direction.md) | Wind direction is the direction from which a wind originates |
| [wind_speed](wind_speed.md) | Speed of wind measured at the time of sampling |
| [window_cond](window_cond.md) | The physical condition of the window at the time of sampling |
| [window_cover](window_cover.md) | The type of window covering |
| [window_horiz_pos](window_horiz_pos.md) | The horizontal position of the window on the wall |
| [window_loc](window_loc.md) | The relative location of the window within the room |
| [window_mat](window_mat.md) | The type of material used to finish a window |
| [window_open_freq](window_open_freq.md) | The number of times windows are opened per week |
| [window_size](window_size.md) | The window's length and width |
| [window_status](window_status.md) | Defines whether the windows were open or closed during environmental testing |
| [window_type](window_type.md) | The type of windows |
| [window_vert_pos](window_vert_pos.md) | The vertical position of the window on the wall |
| [window_water_mold](window_water_mold.md) | Signs of the presence of mold or mildew on the window |
| [xylene](xylene.md) | Concentration of xylene in the sample |
| [zinc](zinc.md) | Concentration of zinc in the sample |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AnalysisTypeEnum](AnalysisTypeEnum.md) |  |
| [ArchStrucEnum](ArchStrucEnum.md) |  |
| [BiolStatEnum](BiolStatEnum.md) |  |
| [BiosampleCategoryEnum](BiosampleCategoryEnum.md) | Funding-based, sample location-based, or experimental method-based defined ca... |
| [BioticRelationshipEnum](BioticRelationshipEnum.md) |  |
| [BuildDocsEnum](BuildDocsEnum.md) |  |
| [BuildOccupTypeEnum](BuildOccupTypeEnum.md) |  |
| [BuildingSettingEnum](BuildingSettingEnum.md) |  |
| [CeilCondEnum](CeilCondEnum.md) |  |
| [CeilFinishMatEnum](CeilFinishMatEnum.md) |  |
| [CeilTextureEnum](CeilTextureEnum.md) |  |
| [CeilTypeEnum](CeilTypeEnum.md) |  |
| [CompoundEnum](CompoundEnum.md) |  |
| [ContainerCategoryEnum](ContainerCategoryEnum.md) | The permitted types of containers used in processing metabolomic samples |
| [CreditEnum](CreditEnum.md) |  |
| [CurLandUseEnum](CurLandUseEnum.md) |  |
| [DeposEnvEnum](DeposEnvEnum.md) |  |
| [DeviceEnum](DeviceEnum.md) |  |
| [DnaSampleFormatEnum](DnaSampleFormatEnum.md) |  |
| [DoiCategoryEnum](DoiCategoryEnum.md) |  |
| [DoiProviderEnum](DoiProviderEnum.md) |  |
| [DoorCompTypeEnum](DoorCompTypeEnum.md) |  |
| [DoorCondEnum](DoorCondEnum.md) |  |
| [DoorDirectEnum](DoorDirectEnum.md) |  |
| [DoorLocEnum](DoorLocEnum.md) |  |
| [DoorMatEnum](DoorMatEnum.md) |  |
| [DoorMoveEnum](DoorMoveEnum.md) |  |
| [DoorTypeEnum](DoorTypeEnum.md) |  |
| [DoorTypeMetalEnum](DoorTypeMetalEnum.md) |  |
| [DoorTypeWoodEnum](DoorTypeWoodEnum.md) |  |
| [DrainageClassEnum](DrainageClassEnum.md) |  |
| [DrawingsEnum](DrawingsEnum.md) |  |
| [ExtWallOrientEnum](ExtWallOrientEnum.md) |  |
| [ExtWindowOrientEnum](ExtWindowOrientEnum.md) |  |
| [ExtractionTargetEnum](ExtractionTargetEnum.md) |  |
| [FaoClassEnum](FaoClassEnum.md) |  |
| [FileTypeEnum](FileTypeEnum.md) |  |
| [FilterTypeEnum](FilterTypeEnum.md) |  |
| [FloorCondEnum](FloorCondEnum.md) |  |
| [FloorFinishMatEnum](FloorFinishMatEnum.md) |  |
| [FloorStrucEnum](FloorStrucEnum.md) |  |
| [FloorWaterMoldEnum](FloorWaterMoldEnum.md) |  |
| [FreqCleanEnum](FreqCleanEnum.md) |  |
| [FurnitureEnum](FurnitureEnum.md) |  |
| [GenderRestroomEnum](GenderRestroomEnum.md) |  |
| [GrowthHabitEnum](GrowthHabitEnum.md) |  |
| [HandidnessEnum](HandidnessEnum.md) |  |
| [HcProducedEnum](HcProducedEnum.md) |  |
| [HcrEnum](HcrEnum.md) |  |
| [HcrGeolAgeEnum](HcrGeolAgeEnum.md) |  |
| [HeatCoolTypeEnum](HeatCoolTypeEnum.md) |  |
| [HeatDelivLocEnum](HeatDelivLocEnum.md) |  |
| [HostSexEnum](HostSexEnum.md) |  |
| [IndoorSpaceEnum](IndoorSpaceEnum.md) |  |
| [IndoorSurfEnum](IndoorSurfEnum.md) |  |
| [InstrumentModelEnum](InstrumentModelEnum.md) |  |
| [InstrumentVendorEnum](InstrumentVendorEnum.md) |  |
| [IntWallCondEnum](IntWallCondEnum.md) |  |
| [JgiContTypeEnum](JgiContTypeEnum.md) |  |
| [LibraryTypeEnum](LibraryTypeEnum.md) |  |
| [LightTypeEnum](LightTypeEnum.md) |  |
| [LithologyEnum](LithologyEnum.md) |  |
| [MechStrucEnum](MechStrucEnum.md) |  |
| [OccupDocumentEnum](OccupDocumentEnum.md) |  |
| [OrganismCountEnum](OrganismCountEnum.md) |  |
| [OxyStatSampEnum](OxyStatSampEnum.md) |  |
| [PlantGrowthMedEnum](PlantGrowthMedEnum.md) |  |
| [PlantSexEnum](PlantSexEnum.md) |  |
| [ProcessingInstitutionEnum](ProcessingInstitutionEnum.md) |  |
| [ProfilePositionEnum](ProfilePositionEnum.md) |  |
| [QuadPosEnum](QuadPosEnum.md) |  |
| [RelSampLocEnum](RelSampLocEnum.md) |  |
| [RnaSampleFormatEnum](RnaSampleFormatEnum.md) |  |
| [RoomCondtEnum](RoomCondtEnum.md) |  |
| [RoomConnectedEnum](RoomConnectedEnum.md) |  |
| [RoomLocEnum](RoomLocEnum.md) |  |
| [RoomSampPosEnum](RoomSampPosEnum.md) |  |
| [RoomTypeEnum](RoomTypeEnum.md) |  |
| [SampCaptStatusEnum](SampCaptStatusEnum.md) |  |
| [SampCollectPointEnum](SampCollectPointEnum.md) |  |
| [SampDisStageEnum](SampDisStageEnum.md) |  |
| [SampFloorEnum](SampFloorEnum.md) |  |
| [SampMdEnum](SampMdEnum.md) |  |
| [SampSubtypeEnum](SampSubtypeEnum.md) |  |
| [SampWeatherEnum](SampWeatherEnum.md) |  |
| [SampleTypeEnum](SampleTypeEnum.md) |  |
| [SeasonUseEnum](SeasonUseEnum.md) |  |
| [SedimentTypeEnum](SedimentTypeEnum.md) |  |
| [SeparationMethodEnum](SeparationMethodEnum.md) | The tool/substance used to separate or filter a solution or mixture |
| [ShadingDeviceCondEnum](ShadingDeviceCondEnum.md) |  |
| [ShadingDeviceTypeEnum](ShadingDeviceTypeEnum.md) |  |
| [SoilHorizonEnum](SoilHorizonEnum.md) |  |
| [SpecificEnum](SpecificEnum.md) |  |
| [SrDepEnvEnum](SrDepEnvEnum.md) |  |
| [SrGeolAgeEnum](SrGeolAgeEnum.md) |  |
| [SrKerogTypeEnum](SrKerogTypeEnum.md) |  |
| [SrLithologyEnum](SrLithologyEnum.md) |  |
| [StationaryPhaseEnum](StationaryPhaseEnum.md) | The type of stationary phase used in a solid phase extraction process |
| [StatusEnum](StatusEnum.md) |  |
| [StudyCategoryEnum](StudyCategoryEnum.md) |  |
| [SubstructureTypeEnum](SubstructureTypeEnum.md) |  |
| [SurfAirContEnum](SurfAirContEnum.md) |  |
| [SurfMaterialEnum](SurfMaterialEnum.md) |  |
| [TidalStageEnum](TidalStageEnum.md) |  |
| [TillageEnum](TillageEnum.md) |  |
| [TrainLineEnum](TrainLineEnum.md) |  |
| [TrainStatLocEnum](TrainStatLocEnum.md) |  |
| [TrainStopLocEnum](TrainStopLocEnum.md) |  |
| [VisMediaEnum](VisMediaEnum.md) |  |
| [WallConstTypeEnum](WallConstTypeEnum.md) |  |
| [WallFinishMatEnum](WallFinishMatEnum.md) |  |
| [WallLocEnum](WallLocEnum.md) |  |
| [WallSurfTreatmentEnum](WallSurfTreatmentEnum.md) |  |
| [WallTextureEnum](WallTextureEnum.md) |  |
| [WaterFeatTypeEnum](WaterFeatTypeEnum.md) |  |
| [WeekdayEnum](WeekdayEnum.md) |  |
| [WindowCondEnum](WindowCondEnum.md) |  |
| [WindowCoverEnum](WindowCoverEnum.md) |  |
| [WindowHorizPosEnum](WindowHorizPosEnum.md) |  |
| [WindowLocEnum](WindowLocEnum.md) |  |
| [WindowMatEnum](WindowMatEnum.md) |  |
| [WindowTypeEnum](WindowTypeEnum.md) |  |
| [WindowVertPosEnum](WindowVertPosEnum.md) |  |
| [YesNoEnum](YesNoEnum.md) | replaces DnaDnaseEnum and DnaseRnaEnum |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Bytes](Bytes.md) | An integer value that corresponds to a size in bytes |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [DecimalDegree](DecimalDegree.md) | A decimal degree expresses latitude or longitude as decimal fractions |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [ExternalIdentifier](ExternalIdentifier.md) | A CURIE representing an external identifier |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [LanguageCode](LanguageCode.md) | A language code conforming to ISO_639-1 |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Unit](Unit.md) |  |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [Checklist](Checklist.md) | A MIxS checklist |
| [ChecklistPackageCombination](ChecklistPackageCombination.md) | A combination of a checklist and a package |
| [DataObjectSubset](DataObjectSubset.md) | Subset consisting of the data objects that either inputs or outputs of proces... |
| [DataPortalSubset](DataPortalSubset.md) | Subset consisting of entities that Kitware/nmdc-server use to populate the da... |
| [Environment](Environment.md) |  |
| [Investigation](Investigation.md) |  |
| [MixsExtension](MixsExtension.md) |  |
| [MixsEnvironmentalTriad](MixsEnvironmentalTriad.md) |  |
| [NucleicAcidSequenceSource](NucleicAcidSequenceSource.md) |  |
| [Package](Package.md) | A MIxS package |
| [SampleSubset](SampleSubset.md) | Subset consisting of entities linked to the processing of samples |
| [Sequencing](Sequencing.md) |  |
| [WorkflowSubset](WorkflowSubset.md) | Subset consisting of just the workflow execution activities |
