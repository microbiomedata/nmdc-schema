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

        self.adapter.process_each_document("material_processing_set",
                                           [self.remove_field_within_extraction])

    def remove_field_within_extraction(self, material_processing: dict) -> dict:
        r"""
        If the specified document has a type value of `nmdc:Extraction`, this function will remove
        the `sample_state_information` field from any `PortionOfSubstance` instance that is
        in this document's `substances_used` field.

        >>> m = Migrator()

        # Test: Nothing to remove.
        >>> m.remove_field_within_extraction({'id': 123, 'type': 'nmdc:Extraction'})
        {'id': 123, 'type': 'nmdc:Extraction'}
        >>> m.remove_field_within_extraction({'id': 123, 'type': 'nmdc:Extraction', 'substances_used': []})
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': []}
        >>> m.remove_field_within_extraction({'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [
        ...     {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'},
        ... ]})
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}

        # Test: Remove the `sample_state_information` field from a single `PortionOfSubstance`.
        >>> m.remove_field_within_extraction({'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ... ]})
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}]}

        # Test: Remove the `sample_state_information` field from multiple `PortionOfSubstance`s.
        >>> m.remove_field_within_extraction({'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'solid', 'substance_role': 'base'},
        ...     {'type': 'nmdc:PortionOfSubstance', 'sample_state_information': 'gas', 'substance_role': 'acid'},
        ... ]})
        {'id': 123, 'type': 'nmdc:Extraction', 'substances_used': [{'type': 'nmdc:PortionOfSubstance', 'substance_role': 'base'}, {'type': 'nmdc:PortionOfSubstance', 'substance_role': 'acid'}]}
        """

        if material_processing.get("type", None) == "nmdc:Extraction":
            substances_used = material_processing.get("substances_used", [])  # `substances_used` is multivalued
            for substance_used in substances_used:
                if substance_used.get("type") == "nmdc:PortionOfSubstance":
                    substance_used.pop("sample_state_information", None)  # deletes the key if it is present

        return material_processing
