from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.10.0.part_2"
    _to_version = "11.10.0.part_3"

    def upgrade(self, commit_changes: bool = True) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        
        Note: The `commit_changes` parameter is not used, but must be present in the
              method signature to comply with the base class. This migrator does
              not use transactions—all changes are committed immediately.
        """

        self.adapter.process_each_document(
            "data_generation_set", [self.confirm_specific_fields_are_absent]
        )

    def confirm_specific_fields_are_absent(self, data_generation: dict) -> dict:
        r"""
        Raises an exception if the document represents a `NucleotideSequencing` and either
        its `target_gene` field or its `target_subfragment` field is present.

        Note: By raising an exception, we bring this "unexpected" situation to the attention
              of the person performing the migration, so they can take action (e.g., aborting
              the migration and contacting the schema change author).

        Reference: https://microbiomedata.github.io/nmdc-schema/NucleotideSequencing/

        >>> m = Migrator()

        # Test: Document has neither field or is of irrelevant type.
        >>> m.confirm_specific_fields_are_absent({"id": 1, "type": "nmdc:NucleotideSequencing"})
        {'id': 1, 'type': 'nmdc:NucleotideSequencing'}
        >>> m.confirm_specific_fields_are_absent({"id": 2, "type": "nmdc:Other", "target_gene": None})
        {'id': 2, 'type': 'nmdc:Other', 'target_gene': None}

        # Test: Document has either field.
        >>> m.confirm_specific_fields_are_absent({"id": 3, "type": "nmdc:NucleotideSequencing", "target_gene": None})
        Traceback (most recent call last):
            ...
        ValueError: NucleotideSequencing 3 has field(s): ['target_gene']
        >>> m.confirm_specific_fields_are_absent({"id": 4, "type": "nmdc:NucleotideSequencing", "target_subfragment": None})
        Traceback (most recent call last):
            ...
        ValueError: NucleotideSequencing 4 has field(s): ['target_subfragment']
        
        # Test: Document has both fields.
        >>> m.confirm_specific_fields_are_absent({"id": 5, "type": "nmdc:NucleotideSequencing", "target_gene": None, "target_subfragment": None})
        Traceback (most recent call last):
            ...
        ValueError: NucleotideSequencing 5 has field(s): ['target_gene', 'target_subfragment']
        """

        # Note: We only want to process `NucleotideSequencing` documents.
        if data_generation["type"] == "nmdc:NucleotideSequencing":

            # Give the variable a more specific name.
            nucleotide_sequencing = data_generation
            nucleotide_sequencing_id = nucleotide_sequencing["id"]

            # Check which of the fields are present.
            field_presence = {
                "target_gene": "target_gene" in nucleotide_sequencing,
                "target_subfragment": "target_subfragment" in nucleotide_sequencing,
            }

            # If either field is present, raise an exception.
            if any(field_presence.values()):
                present_field_names = [name for name, is_present in field_presence.items() if is_present]
                raise ValueError(
                    f"NucleotideSequencing {nucleotide_sequencing_id} has field(s): {present_field_names}"
                )

        return data_generation
