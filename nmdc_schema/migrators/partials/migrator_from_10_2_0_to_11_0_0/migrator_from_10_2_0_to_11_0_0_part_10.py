from typing import Optional

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.nmdc_data import get_nmdc_schema_definition
from linkml_runtime import SchemaView


def create_schema_view() -> SchemaView:
    """
    Returns a LinkML SchemaView instance that can be used to traverse the schema.
    
    >>> isinstance(create_schema_view(), SchemaView)
    True
    """
    schema_definition = get_nmdc_schema_definition()
    schema_view = SchemaView(schema_definition)
    return schema_view


class Migrator(MigratorBase):
    """Migrates data from schema X to PR10"""

    _from_version = "X"
    _to_version = "PR10"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {
        ...     "data_object_set": [
        ...         {'id': 1},
        ...         {'id': 2, 'type': 'old'}
        ...     ],
        ...     "library_preparation_set": [
        ...         {'id': 1},
        ...         {'id': 2, 'type': 'old'},
        ...         {'id': 3, 'protocol_link': {'name': 'nombre'}},
        ...         {'id': 4, 'protocol_link': {'name': 'nombre', 'type': 'old'}}
        ...     ],
        ... }
        >>> m = Migrator(adapter=DictionaryAdapter(database=database))
        >>> m.upgrade()
        >>> all(document['type'] == 'nmdc:DataObject' for document in database['data_object_set'])
        True
        >>> all(document['type'] == 'nmdc:LibraryPreparation' for document in database['library_preparation_set'])
        True

        Confirm a `type` field has been added to the inline `protocol_link` instance that lacked one.
        >>> library_prep_3 = next(document for document in database['library_preparation_set'] if document['id'] == 3)
        >>> library_prep_3['protocol_link']['name']
        'nombre'
        >>> library_prep_3['protocol_link']['type']
        'nmdc:Protocol'

        Confirm the `type` value has been updated on the inline `protocol_link` instance that had an incorrect one.
        >>> library_prep_4 = next(document for document in database['library_preparation_set'] if document['id'] == 4)
        >>> library_prep_4['protocol_link']['name']
        'nombre'
        >>> library_prep_4['protocol_link']['type']
        'nmdc:Protocol'
        """

        # Get a dictionary of slots and the class uris of their range if they have inlined classes as their range.
        view = create_schema_view()

        slots_with_inlined_classes = {}
        classes_with_inlined_classes = ["Biosample", 
                                        "Study", 
                                        "Extraction", 
                                        "MetabolomicsAnalysis" , 
                                        "MetaproteomicsAnalysis", 
                                        "MagsAnalysis",
                                        "ReadQcAnalysis",
                                        "DataGeneration",
                                        "LibraryPreparation",
                                        "Pooling",
                                        "MetagenomeAnnotation",
                                        "MetagenomeAssembly",
                                        "MetagenomeSequencing",
                                        "NomAnalysis",
                                        "ReadBasedTaxonomyAnalysis",
                                        "MetatranscriptomeAnnotation",
                                        "MetatranscriptomeAssembly",
                                        "MetatranscriptomeExpressionAnalysis",
                                        "CollectingBiosamplesFromSite"
                                        ]
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
                        # need to hardcode because schema prefix is not NMDC
                        if slot_name == "has_credit_associations":
                            class_uri = "prov:Association"
                            slots_with_inlined_classes[slot_name] = class_uri
                        else:
                            class_uri = f"{view.schema.default_prefix}:{element.name}"
                            slots_with_inlined_classes[slot_name] = class_uri

        # Populate the "collection-to-transformers" map for this specific migration.
        agenda = dict(
            biosample_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Biosample", slots_with_inlined_classes)],
            study_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Study", slots_with_inlined_classes)],
            extraction_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Extraction", slots_with_inlined_classes)],
            mags_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MagsAnalysis", slots_with_inlined_classes)],
            metabolomics_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetabolomicsAnalysis", slots_with_inlined_classes)],
            metaproteomics_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetaproteomicsAnalysis", slots_with_inlined_classes)],
            data_generation_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:DataGeneration", slots_with_inlined_classes)],
            read_qc_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:ReadQcAnalysis", slots_with_inlined_classes)],
            library_preparation_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:LibraryPreparation", slots_with_inlined_classes)],
            pooling_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:Pooling", slots_with_inlined_classes)],
            metagenome_annotation_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeAnnotation", slots_with_inlined_classes)],
            metagenome_assembly_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeAssembly", slots_with_inlined_classes)],
            metagenome_sequencing_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetagenomeSequencing", slots_with_inlined_classes)],
            nom_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:NomAnalysis", slots_with_inlined_classes)],
            read_based_taxonomy_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:ReadBasedTaxonomyAnalysis", slots_with_inlined_classes)],
            metatranscriptome_annotation_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetatranscriptomeAnnotation", slots_with_inlined_classes)],
            metatranscriptome_assembly_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetatranscriptomeAssembly", slots_with_inlined_classes)],
            metatranscriptome_expression_analysis_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:MetatranscriptomeExpressionAnalysis", slots_with_inlined_classes)],
            collecting_biosamples_from_site_set=[lambda document: self.add_type_slot_with_class_uri(document, "nmdc:CollectingBiosamplesFromSite", slots_with_inlined_classes)]
        )  
        

        for collection_name, pipeline in agenda.items():
            self.adapter.process_each_document(collection_name=collection_name, pipeline=pipeline)

        # For each collection that is not allowed to contain documents having any slots having inlined classes,
        # we can use this more optimized adapter method to set the `type` field of all documents in that collection.
        self.adapter.set_field_of_each_document("data_object_set", "type", "nmdc:DataObject")
        self.adapter.set_field_of_each_document("functional_annotation_agg", "type", "nmdc:FunctionalAnnotationAggMember")
        self.adapter.set_field_of_each_document("field_research_site_set", "type", "nmdc:FieldResearchSite")
        self.adapter.set_field_of_each_document("processed_sample_set", "type", "nmdc:ProcessedSample")


    def add_type_to_inlined_classes(self, document: dict, slot: str, uri: str):
        r"""
        Adds a type slot to each inlined instance of an NMDC class in the biosample_set, study_set, extraction_set, 
        mags_set, metabolomics_analysis_set, and metaproteomics_analysis_set. 
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
                    

    def add_type_slot_with_class_uri(self, document: dict, class_uri: str, inlined_slots: Optional[dict] = None):
        r"""
            Adds a type slot to each collection with the appropriate class uri as the value. E.g. type: nmdc:Biosample. If a type
            slot exists, it will overwrite to the types listed below. If the optional dictionary argument inlined_slots is given, then
            this function will add the type lost to any slots that have inlined classes as their range.
        
            >>> m = Migrator()
            >>> m.add_type_slot_with_class_uri({'id': 123, 'collection_date': {'has_raw_value': '2017-05-09'}}, 'nmdc:Biosample', {'collection_date': 'nmdc:TimestampValue'}) 
            {'id': 123, 'collection_date': {'has_raw_value': '2017-05-09', 'type': 'nmdc:TimestampValue'}, 'type': 'nmdc:Biosample'}
            >>> m.add_type_slot_with_class_uri({'id': 567, 'type': 'nmdc:DataGeneration'}, 'nmdc:DataGeneration')
            {'id': 567, 'type': 'nmdc:DataGeneration'}
            >>> m.add_type_slot_with_class_uri({'id': 567, 'env_broad_scale': {'term': {'id': 'ENVO:1234'}}}, 'nmdc:Biosample', {'env_broad_scale': 'nmdc:ControlledIdentifiedTermValue'})
            {'id': 567, 'env_broad_scale': {'term': {'id': 'ENVO:1234', 'type': 'nmdc:OntologyClass'}, 'type': 'nmdc:ControlledIdentifiedTermValue'}, 'type': 'nmdc:Biosample'}
            >>> m.add_type_slot_with_class_uri({'id': 456}, 'nmdc:NomAnalysis')
            {'id': 456, 'type': 'nmdc:NomAnalysis'}
        """
        
        # Adds the type slot with the correct class_uri as a value to each collection instance
        document["type"] = class_uri
                
        # Add the type slot to any inlined classes in the Biosample, Study, or Extraction collections
        if inlined_slots:
            for slot, uri in inlined_slots.items():
                self.add_type_to_inlined_classes(document, slot, uri)
                
        return document

    