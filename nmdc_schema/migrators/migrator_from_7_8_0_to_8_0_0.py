from typing import List
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator_from_7_8_0_to_8_0_0(MigratorBase):
    """Migrates data from schema 7.8.0 to 8.0.0"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            biosample_set=[self.standardize_letter_casing_of_gold_biosample_identifiers],
            extraction_set=[self.rename_sample_mass_field],
            omics_processing_set=[self.standardize_letter_casing_of_gold_sequencing_project_identifiers],
            study_set=[self.standardize_letter_casing_of_gold_study_identifier],
        )

    def rename_sample_mass_field(self, extraction: dict) -> dict:
        self.logger.info(f"Starting migration of {extraction['id']}")
        if "sample_mass" in extraction:
            extraction["input_mass"] = extraction.pop("sample_mass")
        return extraction

    def standardize_letter_casing_of_gold_identifiers(self, identifiers: List[str]) -> List[str]:
        """
        Replaces the prefix `GOLD:` with `gold:` in the list of identifiers.

        Note: If the identifier contains more than one colon, everything after the second
              colon will be discarded.
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
        field_name = "gold_biosample_identifiers"
        if field_name in biosample and biosample[field_name]:
            biosample[field_name] = self.standardize_letter_casing_of_gold_identifiers(biosample[field_name])
        else:
            biosample[field_name] = []
        return biosample

    def standardize_letter_casing_of_gold_sequencing_project_identifiers(self, omics_processing: dict) -> dict:
        field_name = "gold_sequencing_project_identifiers"
        if field_name in omics_processing and omics_processing[field_name]:
            omics_processing[field_name] = self.standardize_letter_casing_of_gold_identifiers(omics_processing[field_name])
        else:
            omics_processing[field_name] = []
        return omics_processing

    def standardize_letter_casing_of_gold_study_identifier(self, study: dict) -> dict:
        field_name = "gold_study_identifiers"
        if field_name in study and study[field_name]:
            study[field_name] = self.standardize_letter_casing_of_gold_identifiers(study[field_name])
        else:
            study[field_name] = []
        return study
