from nmdc_schema.migrators.migrator_base import MigratorBase
from linkml_runtime import SchemaView
import nmdc_schema.nmdc_data as nd

class Migrator_from_X_to_PR10(MigratorBase):
    """Migrates data from schema X to PR10"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Get a dictionary of slots and the class uris of their range if they have inlined classes as their range.
        schema_string = nd.get_nmdc_yaml_string()
        view = SchemaView(schema_string)

        slots_with_inlined_classes = {}
        classes_with_inlined_classes = ["Biosample", "Study", "Extraction"]
        for nmdc_class in classes_with_inlined_classes:
            induced_slots = view.class_induced_slots(nmdc_class)
            for slot_def in induced_slots:
                slot_name = slot_def.name
                slot_range = slot_def.range
                element = view.get_element(slot_range)
                metatype = type(element).class_name
                if metatype == 'class_definition':
                    class_identifying_slot = view.get_identifier_slot(slot_range)
                    if not class_identifying_slot:
                        class_uri = f"{view.schema.default_prefix}:{element.name}"
                        slots_with_inlined_classes[slot_name] = class_uri

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            biosample_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Biosample", slots_with_inlined_classes)],
            data_object_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:DataObject")],
            functional_annotation_agg=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:FunctionalAnnotationAggMember")],
            study_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Study", slots_with_inlined_classes)],
            extraction_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Extraction", slots_with_inlined_classes)],
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

    def add_type_to_inlined_classes(self, document: dict, slot: str, uri: str):
        r"""
        Adds a type slot to each inlined instance of an NMDC class in the biosmpale_set, study_set, and extraction_set collections. 
        """
        if document.get(slot):
            # If slot is a list, iterate over each item in the list (e.g. chem_administration and has_credit_associations)
            if isinstance(document[slot], list):
                for item in document[slot]:
                    # will exclude non-inlined class slots that use an id
                    if not isinstance(item, str):
                        item["type"] = uri
                        if item.get("term"):
                            item["term"]["type"] = "nmdc:OntologyClass"
                        if item.get("applies_to_person"):
                            item["applies_to_person"]["type"] = "nmdc:PersonValue"
            else:
                # If slot is not multivalued
                document[slot]["type"] = uri
                if document[slot].get("term"):
                    document[slot]["term"]["type"] = "nmdc:OntologyClass"
                    

    def add_type_slot_with_class_uri(self, document: dict, class_uri: str, inlined_slots=None):
        r"""
            Adds a type slot to each collection with the appropriate class uri as the value. E.g. type: nmdc:Biosample. If a type
            slot exists, it will overwrite to the types listed below. If the optional dictionary argument inlined_slots is given, then
            this function will add the type lost to any slots that have inlined classes as their range.
        
            >>> m = Migrator_from_X_to_PR10()
            >>> m.add_type_slot_with_class_uri({'id': 123, 'collection_date': {'has_raw_value': '2017-05-09'}}, 'nmdc:Biosample', {'collection_date': 'nmdc:TimestampValue'}) 
            {'id': 123, 'collection_date': {'has_raw_value': '2017-05-09', 'type': 'nmdc:TimestampValue'}, 'type': 'nmdc:Biosample'}
            >>> m.add_type_slot_with_class_uri({'id': 567, 'type': 'nmdc:OmicsProcessing'}, 'nmdc:DataGeneration')
            {'id': 567, 'type': 'nmdc:DataGeneration'}
            >>> m.add_type_slot_with_class_uri({'id': 567, 'env_broad_scale': {'term': {'id': 'ENVO:1234'}}}, 'nmdc:Biosample', {'env_broad_scale': 'nmdc:ControlledIdentifiedTermValue'})
            {'id': 567, 'env_broad_scale': {'term': {'id': 'ENVO:1234', 'type': 'nmdc:OntologyClass'}, 'type': 'nmdc:ControlledIdentifiedTermValue'}, 'type': 'nmdc:Biosample'}
            >>> m.add_type_slot_with_class_uri({'id': 456}, 'nmdc:NomAnalysis')
            {'id': 456, 'type': 'nmdc:NomAnalysis'}
        """
        
        # Adds the type slot with the correct class_uri as a value to each collection instance
        document["type"] = class_uri
                
        types_with_inlined_classes = ["nmdc:Biosample", "nmdc:Study", "nmdc:Extraction"]
        # Add the type slot to any inlined classes in the Biosample, Study, or Extraction collections
        if class_uri in types_with_inlined_classes:
            if inlined_slots:
                for slot, uri in  inlined_slots.items():
                    self.add_type_to_inlined_classes(document, slot, uri)
                
        return document

    