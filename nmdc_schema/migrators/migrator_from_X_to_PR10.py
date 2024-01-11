from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator_from_X_to_PR10(MigratorBase):
    """Migrates data from schema X to PR10"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            biosample_set=[lambda document: self.add_type_slot_with_class_uri(document, "biosample_set")],
            data_object_set=[lambda document: self.add_type_slot_with_class_uri(document, "data_object_set")],
            functional_annotation_agg=[lambda document: self.add_type_slot_with_class_uri(document, "functional_annotation_agg")],
            study_set=[lambda document: self.add_type_slot_with_class_uri(document, "study_set")],
            extraction_set=[lambda document: self.add_type_slot_with_class_uri(document, "extraction_set")],
            field_research_site_set=[lambda document: self.add_type_slot_with_class_uri(document, "field_research_site_set")],
            library_preparation_set=[lambda document: self.add_type_slot_with_class_uri(document, "library_preparation_set")],
            mags_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "mags_activity_set")],
            metabolomics_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "metabolomics_analysis_activity_set")],
            metagenome_annotation_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "metagenome_annotation_activity_set")],
            metagenome_assembly_set=[lambda document: self.add_type_slot_with_class_uri(document, "metageneome_assembly_set")],
            metagenome_sequencing_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "metagenome_sequencing_activity_set")],
            metaproteomics_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "metaproteomics_analysis_activity_set")],
            metatranscriptome_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "metatranscriptome_activity_set")],
            nom_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nom_analysis_activity_set")],
            omics_processing_set=[lambda document: self.add_type_slot_with_class_uri(document, "omics_processing_set")],
            pooling_set=[lambda document: self.add_type_slot_with_class_uri(document, "pooling_set")],
            processed_sample_set=[lambda document: self.add_type_slot_with_class_uri(document, "processed_sample_set")],
            read_based_taxonomy_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "read_based_taxonomy_analysis_activity_set")],
            read_qc_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "read_qc_analysis_activity_set")],
        )

    def add_type_slot_with_class_uri(self, document: dict, collection_name: str):
        r"""
        Adds a type slot to each collection with the appropriate class uri as the value. E.g. type: nmdc:Biosample. If a type
        slot exists, it will overwrite to the types listed below.
        
        >>> m = Migrator_from_X_to_PR10()
        >>> m.add_type_slot_with_class_uri({'id': 123}, 'processed_sample_set') 
        {'id': 123, 'type': 'nmdc:ProcessedSample'}
        >>> m.add_type_slot_with_class_uri({'id': 567, 'type': 'nmdc:MagsAnalysisActivity'}, 'mags_activity_set')
        {'id': 567, 'type': 'nmdc:MagsAnalysis'}
        """
        class_uri_dict = {"biosample_set": "nmdc:Biosample",
                           "data_object_set": "nmdc:DataObject",
                           "functional_annotation_agg": "nmdc:FunctionalAnnotationAggMember",
                           "study_set": "nmdc:Study",
                           "extraction_set": "nmdc:Extraction",
                           "field_research_site_set": "nmdc:FieldResearchSite",
                           "library_preparation_set": "nmdc:LibraryPreparation",
                           "mags_activity_set": "nmdc:MagsAnalysis",
                           "metabolomics_analysis_activity_set": "nmdc:MetabolomicsAnalysis",
                           "metagenome_annotation_activity_set": "nmdc:MetagenomeAnnotation",
                           "metagenome_assembly_set": "nmdc:MetagenomeAssembly",
                           "metagenome_sequencing_activity_set": "nmdc:MetagenomeSequencing",
                           "metaproteomics_analysis_activity_set": "nmdc:MetaproteomicsAnalysis", 
                           "metatranscriptome_activity_set": "nmdc:MetatranscriptomeAnalysis",
                           "nom_analysis_activity_set": "nmdc:NomAnalysis",
                           "omics_processing_set": "nmdc:DataGeneration",
                           "pooling_set": "nmdc:Pooling",
                           "processed_sample_set": "nmdc:ProcessedSample",
                           "read_based_taxonomy_analysis_activity_set": "nmdc:ReadBasedTaxonomyAnalysis",
                           "read_qc_analysis_activity_set": "nmdc:ReadQcAnalysis"
                           }
        
        document["type"] = class_uri_dict[collection_name]
        
        
        return document

    