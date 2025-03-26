from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.5.1"
    _to_version = "11.6.0"

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
                  they are represented by objects having a type value of `MobilePhaseSegment`
                  in the multivalued `ordered_mobile_phases` fields of instances of the following schema classes:
                  - [x] A. `ChromatographyConfiguration`
                    - Docs: https://microbiomedata.github.io/nmdc-schema/ChromatographyConfiguration/
                    - All of these are documents in the `configuration_set` collection,
                      having a type value of `nmdc:ChromatographyConfiguration`.
                  - [x] B. `ChromatographicSeparationProcess`
                    - Docs: https://microbiomedata.github.io/nmdc-schema/ChromatographicSeparationProcess/
                    - All of these are documents in the `material_processing_set` collection,
                      having a type value of `nmdc:ChromatographicSeparationProcess`.
        """

        self.adapter.process_each_document("material_processing_set", [
            self.remove_sample_state_information_field_within_material_processing_or_storage_process,
            self.remove_sample_state_information_field_within_chromatographic_separation_process_or_configuration,
        ])
        self.adapter.process_each_document("storage_process_set", [
            self.remove_sample_state_information_field_within_material_processing_or_storage_process
        ])
        self.adapter.process_each_document("configuration_set", [
            self.remove_sample_state_information_field_within_chromatographic_separation_process_or_configuration
        ])

    @staticmethod
    def remove_sample_state_information_from_substances_used(substances_used: list) -> list:
        r"""
        Removes the `sample_state_information` key from each `nmdc:PortionOfSubstance` dictionary
        in the specified `substances_used` list. Although the function modifies the list "in place",
        it also returns the modified list to facilitate unit testing (see doctests below).

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
        >>> Migrator.remove_sample_state_information_from_substances_used([
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ... ])
        [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'Other', 'sample_state_information': 'solid', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]
        """

        for substance_used in substances_used:
            if substance_used.get("type") == "nmdc:PortionOfSubstance":
                substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return substances_used

    def remove_sample_state_information_field_within_chromatographic_separation_process_or_configuration(self, document: dict) -> dict:
        r"""
        If the document has a type value of `nmdc:ChromatographicSeparationProcess` or `nmdc:ChromatographyConfiguration`,
        process the objects in its multivalued `ordered_mobile_phases` field that have type `nmdc:MobilePhaseSegment`.
        For each such object, remove the `sample_state_information` field from any `PortionOfSubstance` objects in its
        `substances_used` field.

        >>> m = Migrator()

        # Test: Removes the `sample_state_information` field from all qualifying item within the `substances_used` list.
        >>> transformed_document = m.remove_sample_state_information_field_within_chromatographic_separation_process_or_configuration({
        ...     'id': 123,
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
        >>> transformed_document = m.remove_sample_state_information_field_within_chromatographic_separation_process_or_configuration({
        ...     'id': 123,
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

        if document.get("type", None) in ["nmdc:ChromatographicSeparationProcess", "nmdc:ChromatographyConfiguration"]:
            ordered_mobile_phases = document.get("ordered_mobile_phases", [])  # slot is multivalued
            for mobile_phase_segment in ordered_mobile_phases:
                if mobile_phase_segment.get("type") == "nmdc:MobilePhaseSegment":
                    substances_used = mobile_phase_segment.get("substances_used", [])  # slot is multivalued
                    Migrator.remove_sample_state_information_from_substances_used(substances_used)

        return document

    def remove_sample_state_information_field_within_material_processing_or_storage_process(self, document: dict) -> dict:
        r"""
        If the specified document has a type value of `nmdc:Extraction`, `nmdc:DissolvingProcess`,
        `nmdc:ChemicalConversionProcess`, or `nmdc:StorageProcess`, remove the `sample_state_information` field from any
        `PortionOfSubstance` instances that are in the document's `substances_used` field.

        >>> m = Migrator()

        # Test: No changes are made to the document.
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction'
        ... })
        {'id': 123, 'type': 'nmdc:Extraction'}
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': []
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': []}
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...    'id': 123,
        ...    'type': 'SomethingElse',  # not a type that we are targeting
        ...    'substances_used': [
        ...        {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     ]
        ... })
        {'id': 123, 'type': 'SomethingElse', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'}]}

        # Test: Removes the `sample_state_information` field from the only `substances_used` dictionary.
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...    'id': 123,
        ...    'type': 'nmdc:Extraction',
        ...    'substances_used': [
        ...        {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...    ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}

        # Test: Removes the `sample_state_information` field from multiple `substances_used` dictionaries.
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]}

        # Test: Handles documents of type `nmdc:StorageProcess`.
        >>> m.remove_sample_state_information_field_within_material_processing_or_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:StorageProcess',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:StorageProcess', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]}
        """

        if document.get("type", None) in ["nmdc:Extraction",
                                          "nmdc:DissolvingProcess",
                                          "nmdc:ChemicalConversionProcess",
                                          "nmdc:StorageProcess"]:
            substances_used = document.get("substances_used", [])  # `substances_used` is multivalued
            Migrator.remove_sample_state_information_from_substances_used(substances_used)

        return document
