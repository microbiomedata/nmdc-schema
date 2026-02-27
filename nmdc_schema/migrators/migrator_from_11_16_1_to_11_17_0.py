from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.16.1"
    _to_version = "11.17.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "biosample_set", [self.move_dates_to_provenance_metadata]
        )

    def move_dates_to_provenance_metadata(self, biosample: dict) -> dict:
        r"""
        Moves top-level `add_date` and `mod_date` fields from a Biosample
        document into its `provenance_metadata` sub-document.

        >>> m = Migrator()

        Biosample with both dates — moved into provenance_metadata:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-abc', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-abc', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'}}

        Biosample with existing provenance_metadata — preserves other fields:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-def', 'add_date': '2021-03-31', 'mod_date': '2023-01-25', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal'}})
        {'id': 'nmdc:bsm-99-def', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'source_system_of_record': 'NMDC_Submission_Portal', 'add_date': '2021-03-31', 'mod_date': '2023-01-25'}}

        Biosample with neither date — no change:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-ghi'})
        {'id': 'nmdc:bsm-99-ghi'}

        Biosample with only add_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-jkl', 'add_date': '2021-03-31'})
        {'id': 'nmdc:bsm-99-jkl', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '2021-03-31'}}

        Biosample with only mod_date — moves just that one:
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-mno', 'mod_date': '2023-01-25'})
        {'id': 'nmdc:bsm-99-mno', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'mod_date': '2023-01-25'}}

        GOLD-format dates are preserved as-is (no normalization):
        >>> m.move_dates_to_provenance_metadata({'id': 'nmdc:bsm-99-pqr', 'add_date': '28-JUL-14 12.00.00.000000000 AM', 'mod_date': '26-AUG-16 01.50.27.000000000 PM'})
        {'id': 'nmdc:bsm-99-pqr', 'provenance_metadata': {'type': 'nmdc:ProvenanceMetadata', 'add_date': '28-JUL-14 12.00.00.000000000 AM', 'mod_date': '26-AUG-16 01.50.27.000000000 PM'}}
        """

        add_date = biosample.pop("add_date", None)
        mod_date = biosample.pop("mod_date", None)

        if add_date is not None or mod_date is not None:
            if "provenance_metadata" not in biosample:
                biosample["provenance_metadata"] = {
                    "type": "nmdc:ProvenanceMetadata"
                }

            if add_date is not None:
                biosample["provenance_metadata"]["add_date"] = add_date
            if mod_date is not None:
                biosample["provenance_metadata"]["mod_date"] = mod_date

        return biosample
