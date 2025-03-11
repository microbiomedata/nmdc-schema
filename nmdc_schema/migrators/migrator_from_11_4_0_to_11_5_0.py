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
        - `Extraction` (https://microbiomedata.github.io/nmdc-schema/Extraction/)
           - All of these are documents in the `material_processing_set` collection,
             having a type value of `nmdc:Extraction`.
        - `StorageProcess` (https://microbiomedata.github.io/nmdc-schema/StorageProcess/)
           - All of these are documents in the `storage_process_set` collection,
             having a type value of `nmdc:StorageProcess`.
        - `DissolvingProcess` (https://microbiomedata.github.io/nmdc-schema/DissolvingProcess/)
          - All of these are documents in the `material_processing_set` collection,
            having a type value of `nmdc:DissolvingProcess`.
        - `ChemicalConversionProcess` (https://microbiomedata.github.io/nmdc-schema/ChemicalConversionProcess/)
          - All of these are documents in the `material_processing_set` collection,
            having a type value of `nmdc:ChemicalConversionProcess`.
        - `MobilePhaseSegment` (https://microbiomedata.github.io/nmdc-schema/MobilePhaseSegment/)
          - These are not represented by entire documents in any collection. Instead,
            they are represented by objects having a type value of `MobilePhaseSegment`
            in the multivalued `ordered_mobile_phases` fields of instances of the following schema classes:
            - `ChromatographyConfiguration` (https://microbiomedata.github.io/nmdc-schema/ChromatographyConfiguration/)
              - All of these are documents in the `configuration_set` collection,
                having a type value of `nmdc:ChromatographyConfiguration`.
            - `ChromatographicSeparationProcess` (https://microbiomedata.github.io/nmdc-schema/ChromatographicSeparationProcess/)
              - All of these are documents in the `material_processing_set` collection,
                having a type value of `nmdc:ChromatographicSeparationProcess`.
        """

        self.adapter.process_each_document("material_processing_set", [
            self.remove_sample_state_information_field_within_material_processing
        ])

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
