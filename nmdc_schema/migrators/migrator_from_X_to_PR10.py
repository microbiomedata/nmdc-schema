from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator_from_X_to_PR10(MigratorBase):
    """Migrates data from schema X to PR10"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            biosample_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Biosample")],
            data_object_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:DataObject")],
            functional_annotation_agg=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:FunctionalAnnotationAggMember")],
            study_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Study")],
            extraction_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Extraction")],
            field_research_site_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:FieldResearchSite")],
            library_preparation_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:LibraryPreparation")],
            mags_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MagsAnalysis")],
            metabolomics_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetabolomicsAnalysis")],
            metagenome_annotation_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeAnnotation")],
            metagenome_assembly_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeAssembly")],
            metagenome_sequencing_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeSequencing")],
            metaproteomics_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetaproteomicsAnalysis")],
            metatranscriptome_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetatranscriptomeAnalysis")],
            nom_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:NomAnalysis")],
            omics_processing_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:DataGeneration")],
            pooling_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Pooling")],
            processed_sample_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:ProcessedSample")],
            read_based_taxonomy_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:ReadBasedTaxonomyAnalysis")],
            read_qc_analysis_activity_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:ReadQcAnalysis")],
        )

    def add_type_slot_with_class_uri(self, document: dict, collection_name: str):
        r"""
        Adds a type slot to each collection with the appropriate class uri as the value. E.g. type: nmdc:Biosample. If a type
        slot exists, it will overwrite to the types listed below.
        
        >>> m = Migrator_from_X_to_PR10()
        >>> m.add_type_slot_with_class_uri({'id': 123}, 'nmdc:ProcessedSample') 
        {'id': 123, 'type': 'nmdc:ProcessedSample'}
        >>> m.add_type_slot_with_class_uri({'id': 567, 'type': 'nmdc:OmicsProcessing'}, 'nmdc:DataGeneration')
        {'id': 567, 'type': 'nmdc:DataGeneration'}
        """
        
        document["type"] = collection_name
        
        return document

    