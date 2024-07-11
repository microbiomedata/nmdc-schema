from typing import List
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "7.8.0"
    _to_version = "8.0.0"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("biosample_set", [self.standardize_letter_casing_of_gold_biosample_identifiers])
        self.adapter.process_each_document("extraction_set", [self.rename_sample_mass_field])
        self.adapter.process_each_document("omics_processing_set", [self.standardize_letter_casing_of_gold_sequencing_project_identifiers])
        self.adapter.process_each_document("study_set", [self.standardize_letter_casing_of_gold_study_identifier])

    def rename_sample_mass_field(self, extraction: dict) -> dict:
        r"""
        Renames the `sample_mass` field to `input_mass`.

        >>> m = Migrator()
        >>> m.rename_sample_mass_field({'id': 123})  # no `sample_mass` field
        {'id': 123}
        >>> m.rename_sample_mass_field({'id': 123, 'sample_mass': 456})  # test: renames field and preserves value
        {'id': 123, 'input_mass': 456}
        """

        self.logger.info(f"Starting migration of {extraction['id']}")
        if "sample_mass" in extraction:
            extraction["input_mass"] = extraction.pop("sample_mass")
        return extraction

    def standardize_letter_casing_of_gold_identifiers(self, identifiers: List[str]) -> List[str]:
        r"""
        Replaces the prefix `GOLD:` with `gold:` in the list of identifiers.

        >>> m = Migrator()
        >>> m.standardize_letter_casing_of_gold_identifiers(['GOLD:prefix_was_uppercase'])
        ['gold:prefix_was_uppercase']
        >>> m.standardize_letter_casing_of_gold_identifiers(['gold:prefix_was_lowercase'])
        ['gold:prefix_was_lowercase']
        >>> m.standardize_letter_casing_of_gold_identifiers(['Gold:prefix_remains_mixed_case'])
        ['Gold:prefix_remains_mixed_case']

        Note: If the identifier contains more than one colon, everything after and including
              the second colon will be discarded.

        >>> m.standardize_letter_casing_of_gold_identifiers(['GOLD:preserves_this:but_not_this'])
        ['gold:preserves_this']
        """

        standardized_identifiers = []
        for identifier in identifiers:
            self.logger.info(f"Original identifier: {identifier}")
            curie_parts = identifier.split(":")
            curie_prefix = curie_parts[0]  # everything before the first colon
            # everything after the first colon, assuming there are no more colons
            curie_local_id = curie_parts[1]

            # Note: `s.split(":", maxsplit=1)` could be used to divide the string at the
            #       _first_ colon only, so that `parts[1]` contains everything after that.
            #       See: https://docs.python.org/3/library/stdtypes.html#str.split

            if curie_prefix == "GOLD":
                standardized_identifiers.append(f"gold:{curie_local_id}")
            else:
                standardized_identifiers.append(identifier)

        return standardized_identifiers

    def standardize_letter_casing_of_gold_biosample_identifiers(self, biosample: dict) -> dict:
        r"""
        Converts uppercase "GOLD:" prefixes into lowercase "gold:" prefixes, in `gold_biosample_identifiers` values.

        >>> m = Migrator()
        >>> m.standardize_letter_casing_of_gold_biosample_identifiers({'id': 123})
        {'id': 123, 'gold_biosample_identifiers': []}
        >>> m.standardize_letter_casing_of_gold_biosample_identifiers(
        ...     {'id': 123, 'gold_biosample_identifiers': ['GOLD:foo', 'gold:bar']}
        ... )
        {'id': 123, 'gold_biosample_identifiers': ['gold:foo', 'gold:bar']}
        """

        field_name = "gold_biosample_identifiers"
        if field_name in biosample and biosample[field_name]:
            biosample[field_name] = self.standardize_letter_casing_of_gold_identifiers(biosample[field_name])
        else:
            biosample[field_name] = []
        return biosample

    def standardize_letter_casing_of_gold_sequencing_project_identifiers(self, omics_processing: dict) -> dict:
        r"""
        Converts uppercase "GOLD:" prefixes in `gold_sequencing_project_identifiers` values into lowercase "gold:".

        >>> m = Migrator()
        >>> m.standardize_letter_casing_of_gold_sequencing_project_identifiers({'id': 123})
        {'id': 123, 'gold_sequencing_project_identifiers': []}
        >>> m.standardize_letter_casing_of_gold_sequencing_project_identifiers(
        ...     {'id': 123, 'gold_sequencing_project_identifiers': ['GOLD:foo', 'gold:bar']}
        ... )
        {'id': 123, 'gold_sequencing_project_identifiers': ['gold:foo', 'gold:bar']}
        """

        field_name = "gold_sequencing_project_identifiers"
        if field_name in omics_processing and omics_processing[field_name]:
            omics_processing[field_name] = self.standardize_letter_casing_of_gold_identifiers(omics_processing[field_name])
        else:
            omics_processing[field_name] = []
        return omics_processing

    def standardize_letter_casing_of_gold_study_identifier(self, study: dict) -> dict:
        r"""
        Converts uppercase "GOLD:" prefixes in `gold_study_identifiers` values into lowercase "gold:".

        >>> m = Migrator()
        >>> m.standardize_letter_casing_of_gold_study_identifier({'id': 123})
        {'id': 123, 'gold_study_identifiers': []}
        >>> m.standardize_letter_casing_of_gold_study_identifier(
        ...     {'id': 123, 'gold_study_identifiers': ['GOLD:foo', 'gold:bar']}
        ... )
        {'id': 123, 'gold_study_identifiers': ['gold:foo', 'gold:bar']}
        """

        field_name = "gold_study_identifiers"
        if field_name in study and study[field_name]:
            study[field_name] = self.standardize_letter_casing_of_gold_identifiers(study[field_name])
        else:
            study[field_name] = []
        return study
