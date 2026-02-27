from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.5.1"
    _to_version = "11.6.0.part_1"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        Between schema version 11.5.1 and 11.6.0, the slot `sample_state_information` was removed from the schema class
        `PortionOfSubstance`. This function updates all instances of that schema class in the database accordingly.

        Note: In a database conforming to schema 11.5.1, instances of the `PortionOfSubstance` class cannot exist
              as documents in a collection. Instead, they can only exist as objects in the multivalued `substances_used`
              field of instances of specific schema classes. Those schema classes are:
              - [x] 1. `Extraction`
                - Docs: https://microbiomedata.github.io/nmdc-schema/Extraction/
                - All of these are documents in the `material_processing_set` collection,
                  having a type value of `nmdc:Extraction`.
              - [x] 2. `StorageProcess`
                - Docs: https://microbiomedata.github.io/nmdc-schema/StorageProcess/
                - All of these are documents in the `storage_process_set` collection,
                  having a type value of `nmdc:StorageProcess`.
              - [x] 3. `DissolvingProcess`
                - Docs: https://microbiomedata.github.io/nmdc-schema/DissolvingProcess/
                - All of these are documents in the `material_processing_set` collection,
                  having a type value of `nmdc:DissolvingProcess`.
              - [x] 4. `ChemicalConversionProcess`
                - Docs: https://microbiomedata.github.io/nmdc-schema/ChemicalConversionProcess/
                - All of these are documents in the `material_processing_set` collection,
                  having a type value of `nmdc:ChemicalConversionProcess`.
              - [x] 5. `MobilePhaseSegment`
                - Docs: https://microbiomedata.github.io/nmdc-schema/MobilePhaseSegment/
                - These are not represented by entire documents in any collection. Instead,
                  they are represented by objects having a type value of `nmdc:MobilePhaseSegment`
                  in the multivalued `ordered_mobile_phases` fields of instances of the following schema classes:
                  - [x] A. `ChromatographyConfiguration`
                    - Docs: https://microbiomedata.github.io/nmdc-schema/ChromatographyConfiguration/
                    - All of these are documents in the `configuration_set` collection,
                      having a type value of `nmdc:ChromatographyConfiguration`.
                  - [x] B. `ChromatographicSeparationProcess`
                    - Docs: https://microbiomedata.github.io/nmdc-schema/ChromatographicSeparationProcess/
                    - All of these are documents in the `material_processing_set` collection,
                      having a type value of `nmdc:ChromatographicSeparationProcess`.

        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> db = {
        ...     'material_processing_set': [
        ...         {
        ...             'id': 1,
        ...             'type': 'nmdc:Extraction',
        ...             'substances_used': [
        ...                 {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'acid'},
        ...             ]
        ...         },
        ...     ],
        ... }
        >>> a = DictionaryAdapter(database=db)
        >>> m = Migrator(adapter=a)
        >>> m.upgrade()
        >>> db['material_processing_set'][0]['substances_used'][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        self.adapter.process_each_document("material_processing_set", [
            Migrator.remove_sample_state_information_field_within_material_processing_set_document,
        ])
        self.adapter.process_each_document("storage_process_set", [
            Migrator.remove_sample_state_information_field_within_storage_process_set_document,
        ])
        self.adapter.process_each_document("configuration_set", [
            Migrator.remove_sample_state_information_field_within_configuration_set_document,
        ])

    @staticmethod
    def remove_sample_state_information_field_within_material_processing_set_document(document: dict) -> dict:
        r"""
        If the document has a type value of `nmdc:Extraction`, `nmdc:DissolvingProcess`, `nmdc:ChemicalConversionProcess`,
        remove the `sample_state_information` field from any `PortionOfSubstance` instances in the document's `substances_used` field.
        
        If the document has a type value of `nmdc:ChromatographicSeparationProcess`, remove the `sample_state_information`
        field from any `MobilePhaseSegment` instances in the document's `ordered_mobile_phases` field.

        # Test: Document's type is `nmdc:Extraction` (i.e. one of the 3 types that undergo the same treatment).
        >>> transformed_document = Migrator.remove_sample_state_information_field_within_material_processing_set_document({
        ...     'id': 1,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        >>> transformed_document["type"]
        'nmdc:Extraction'
        >>> transformed_document["substances_used"][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_document["substances_used"][1]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}

        # Test: Document's type is `nmdc:ChromatographicSeparationProcess`.
        >>> transformed_document = Migrator.remove_sample_state_information_field_within_material_processing_set_document({
        ...     'id': 1,
        ...     'type': 'nmdc:ChromatographicSeparationProcess',
        ...     'ordered_mobile_phases': [
        ...         {
        ...              'id': 4,
        ...              'type': 'nmdc:MobilePhaseSegment',
        ...              'substances_used': [
        ...                  {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...                  {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...              ]
        ...         }
        ...     ],
        ... })
        >>> transformed_document["type"]
        'nmdc:ChromatographicSeparationProcess'
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][1]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        if document.get("type") in ["nmdc:Extraction", "nmdc:DissolvingProcess", "nmdc:ChemicalConversionProcess"]:
            if "substances_used" in document:
                Migrator.remove_sample_state_information_from_substances_used(document.get("substances_used", []))

        elif document.get("type") == "nmdc:ChromatographicSeparationProcess":
            if "ordered_mobile_phases" in document:
                for item in document.get("ordered_mobile_phases", []):
                    if item.get("type") == "nmdc:MobilePhaseSegment":
                        if "substances_used" in item:
                            Migrator.remove_sample_state_information_from_substances_used(item.get("substances_used", []))
        
        return document

    @staticmethod
    def remove_sample_state_information_field_within_storage_process_set_document(document: dict) -> dict:
        r"""
        If the document has a type value of `nmdc:StorageProcess`, remove the `sample_state_information` field from each
        `PortionOfSubstance` instance in the document's `substances_used` field.

        # Test: Document's type is `nmdc:StorageProcess`.
        >>> transformed_document = Migrator.remove_sample_state_information_field_within_storage_process_set_document({
        ...     'id': 1,
        ...     'type': 'nmdc:StorageProcess',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        >>> transformed_document["type"]
        'nmdc:StorageProcess'
        >>> transformed_document["substances_used"][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_document["substances_used"][1]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        if document.get("type") == "nmdc:StorageProcess":
            if "substances_used" in document:
                Migrator.remove_sample_state_information_from_substances_used(document.get("substances_used", []))
        
        return document

    @staticmethod
    def remove_sample_state_information_field_within_configuration_set_document(document: dict) -> dict:
        r"""
        If the document has a type value of `nmdc:ChromatographyConfiguration`, remove the `sample_state_information`
        field from any `MobilePhaseSegment` instances in the document's `ordered_mobile_phases` field.

        # Test: Document's type is `nmdc:ChromatographyConfiguration`.
        >>> transformed_document = Migrator.remove_sample_state_information_field_within_configuration_set_document({
        ...     'id': 1,
        ...     'type': 'nmdc:ChromatographyConfiguration',
        ...     'ordered_mobile_phases': [
        ...         {
        ...              'id': 4,
        ...              'type': 'nmdc:MobilePhaseSegment',
        ...              'substances_used': [
        ...                  {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...                  {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...              ]
        ...         }
        ...     ],
        ... })
        >>> transformed_document["type"]
        'nmdc:ChromatographyConfiguration'
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][1]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        if document.get("type") == "nmdc:ChromatographyConfiguration":
            if "ordered_mobile_phases" in document:
                for item in document.get("ordered_mobile_phases", []):
                    if item.get("type") == "nmdc:MobilePhaseSegment":
                        if "substances_used" in item:
                            Migrator.remove_sample_state_information_from_substances_used(item.get("substances_used", []))
        
        return document

    @staticmethod
    def remove_sample_state_information_from_substances_used(substances_used: list) -> list:
        r"""
        Removes the `sample_state_information` key from each `nmdc:PortionOfSubstance` dictionary
        in the specified `substances_used` list. Although the function modifies the list _in place_,
        it also _returns_ the modified list to facilitate unit testing (see doctests below).

        # Test: Returns empty list as is.
        >>> Migrator.remove_sample_state_information_from_substances_used([])
        []

        # Test: Returns original list if no objects have the target `type`.
        >>> Migrator.remove_sample_state_information_from_substances_used([
        ...     {'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'Other', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ... ])
        [{'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'}, {'type': 'Other', 'sample_state_information': 'gas', 'substance_role': 'acid'}]

        # Test: Returns original list if no objects have the `sample_state_information` field.
        >>> Migrator.remove_sample_state_information_from_substances_used([
        ...     {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'},
        ... ])
        [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]

        # Test: Removes the `sample_state_information` from only—and all—objects having the target `type`.
        >>> transformed_list = Migrator.remove_sample_state_information_from_substances_used([
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ... ])
        >>> len(transformed_list)
        3
        >>> transformed_list[0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_list[1]
        {'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'}
        >>> transformed_list[2]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        for substance_used in substances_used:
            if substance_used.get("type") == "nmdc:PortionOfSubstance":
                substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return substances_used
