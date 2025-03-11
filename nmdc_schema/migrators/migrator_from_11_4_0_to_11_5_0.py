from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.4.0"
    _to_version = "11.5.0"

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        Summary of schema change
        ------------------------
        Slot `sample_state_information` was removed from schema class `PortionOfSubstance`.

        Notes about writing migrator
        ----------------------------
        In a database conforming to schema 11.4.0, instances of the `PortionOfSubstance` class can reside in
        the multivalued `substances_used` field of instances of the following schema classes:
        - [x] `Extraction` (https://microbiomedata.github.io/nmdc-schema/Extraction/)
           - All of these are documents in the `material_processing_set` collection,
             having a type value of `nmdc:Extraction`.
        - [x] `StorageProcess` (https://microbiomedata.github.io/nmdc-schema/StorageProcess/)
           - All of these are documents in the `storage_process_set` collection,
             having a type value of `nmdc:StorageProcess`.
        - [x] `DissolvingProcess` (https://microbiomedata.github.io/nmdc-schema/DissolvingProcess/)
          - All of these are documents in the `material_processing_set` collection,
            having a type value of `nmdc:DissolvingProcess`.
        - [x] `ChemicalConversionProcess` (https://microbiomedata.github.io/nmdc-schema/ChemicalConversionProcess/)
          - All of these are documents in the `material_processing_set` collection,
            having a type value of `nmdc:ChemicalConversionProcess`.
        - [ ] `MobilePhaseSegment` (https://microbiomedata.github.io/nmdc-schema/MobilePhaseSegment/)
          - These are not represented by entire documents in any collection. Instead,
            they are represented by objects having a type value of `MobilePhaseSegment`
            in the multivalued `ordered_mobile_phases` fields of instances of the following schema classes:
            - [x] `ChromatographyConfiguration` (https://microbiomedata.github.io/nmdc-schema/ChromatographyConfiguration/)
              - All of these are documents in the `configuration_set` collection,
                having a type value of `nmdc:ChromatographyConfiguration`.
            - [ ] `ChromatographicSeparationProcess` (https://microbiomedata.github.io/nmdc-schema/ChromatographicSeparationProcess/)
              - All of these are documents in the `material_processing_set` collection,
                having a type value of `nmdc:ChromatographicSeparationProcess`.
        """

        self.adapter.process_each_document("material_processing_set", [
            self.remove_sample_state_information_field_within_material_processing
        ])
        self.adapter.process_each_document("storage_process_set", [
            self.remove_sample_state_information_field_within_storage_process
        ])
        self.adapter.process_each_document("configuration_set", [
            self.remove_sample_state_information_field_within_configuration
        ])

    def remove_sample_state_information_field_within_configuration(self, configuration: dict) -> dict:
        r"""
        If the specified document has a type value of `nmdc:ChromatographyConfiguration`,
        process the `MobilePhaseSegment` instances in its `ordered_mobile_phases` field.
        For each such instance, remove the `sample_state_information` field from any
        `PortionOfSubstance` instances that are in its `substances_used` field.

        >>> m = Migrator()

        # Test: Removes the `sample_state_information` field from multiple `substances_used` dictionaries.
        >>> transformed_document = m.remove_sample_state_information_field_within_configuration({
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
        >>> transformed_document["id"]
        123
        >>> transformed_document["type"]
        'nmdc:ChromatographyConfiguration'
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][0]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}
        >>> transformed_document["ordered_mobile_phases"][0]["substances_used"][1]
        {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}
        """

        target_document_type = "nmdc:ChromatographyConfiguration"
        if configuration.get("type", None) == target_document_type:
            ordered_mobile_phases = configuration.get("ordered_mobile_phases", [])  # slot is multivalued
            for mobile_phase_segment in ordered_mobile_phases:
                if mobile_phase_segment.get("type") == "nmdc:MobilePhaseSegment":
                    substances_used = mobile_phase_segment.get("substances_used", [])  # slot is multivalued
                    for substance_used in substances_used:
                        if substance_used.get("type") == "nmdc:PortionOfSubstance":
                            substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return configuration

    def remove_sample_state_information_field_within_storage_process(self, storage_process: dict) -> dict:
        r"""
        If the specified document has a type value of `nmdc:StorageProcess`, remove the
        `sample_state_information` field from any `PortionOfSubstance` instances that are in the
        document's `substances_used` field.

        >>> m = Migrator()

        # Test: Removes the `sample_state_information` field from multiple `substances_used` dictionaries.
        >>> m.remove_sample_state_information_field_within_storage_process({
        ...     'id': 123,
        ...     'type': 'nmdc:StorageProcess',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:StorageProcess', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]}
        """

        target_document_type = "nmdc:StorageProcess"
        if storage_process.get("type", None) == target_document_type:
            substances_used = storage_process.get("substances_used", [])  # `substances_used` is multivalued
            for substance_used in substances_used:
                if substance_used.get("type") == "nmdc:PortionOfSubstance":
                    substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return storage_process

    def remove_sample_state_information_field_within_material_processing(self, material_processing: dict) -> dict:
        r"""
        If the specified document has a type value of `nmdc:Extraction`, `nmdc:DissolvingProcess`,
        or `nmdc:ChemicalConversionProcess`, remove the `sample_state_information` field from any
        `PortionOfSubstance` instances that are in the document's `substances_used` field.

        >>> m = Migrator()

        # Test: No changes are made to the document.
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction'
        ... })
        {'id': 123, 'type': 'nmdc:Extraction'}
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': []
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': []}
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...    'id': 123,
        ...    'type': 'SomethingElse',  # not a type that we are targeting
        ...    'substances_used': [
        ...        {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     ]
        ... })
        {'id': 123, 'type': 'SomethingElse', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'}]}

        # Test: Removes the `sample_state_information` field from the only `substances_used` dictionary.
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...    'id': 123,
        ...    'type': 'nmdc:Extraction',
        ...    'substances_used': [
        ...        {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...    ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}

        # Test: Removes the `sample_state_information` field from multiple `substances_used` dictionaries.
        >>> m.remove_sample_state_information_field_within_material_processing({
        ...     'id': 123,
        ...     'type': 'nmdc:Extraction',
        ...     'substances_used': [
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...         {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ...     ]
        ... })
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]}
        """

        # Note: We'll check whether the `type` field of the specified document consists of one of these strings.
        target_document_types = ["nmdc:Extraction", "nmdc:DissolvingProcess", "nmdc:ChemicalConversionProcess"]

        if material_processing.get("type", None) in target_document_types:
            substances_used = material_processing.get("substances_used", [])  # `substances_used` is multivalued
            for substance_used in substances_used:
                if substance_used.get("type") == "nmdc:PortionOfSubstance":
                    substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return material_processing
