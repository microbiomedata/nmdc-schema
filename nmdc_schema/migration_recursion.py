import logging
import re
from typing import Dict, List

import click
import click_log
import yaml
from linkml_runtime import SchemaView

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

# todo: log before and after states of migration

doi_url_pattern = r'^https?:\/\/[a-zA-Z\.]+\/10\.'
curie_pattern = r'^[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z0-9_][a-zA-Z0-9_.-]*$'


class Migrator:
    """Base class containing properties and methods useful to its descendants."""

    def __init__(self):
        self.forced_prefix = None

        # Define a dictionary that maps collections to sequences of transformation functions.
        #
        # Note: Each key is a collection name, and each value is a list. Each element of the list is a
        #       function someone performing a migration could call—in the order listed—to transform a
        #       single document from conforming to the _initial_ schema of that migration (e.g. v1),
        #       to conforming to the _final_ schema of that migration (e.g. v2).
        #
        # Note: Descendant classes (i.e. inheriting classes) will populate this dictionary.
        #
        self.transformations_by_collection: Dict[str, List[callable]] = dict()

    def check_and_normalize_one_curie(self, curie_string):
        if not self.is_valid_curie(curie_string):
            curie_string = self.normalize_curie(curie_string)

        return curie_string

    def is_valid_curie(self, curie_string):
        if curie_string == "None":
            pass
            # logger.info("curie_string = 'None'")  # at what point do these get converted from None values to 'None' strings?
        elif '\n' in curie_string or '\r' in curie_string:
            pass
            # logger.info("curie_string contains newline characters")
        else:
            match = re.match(curie_pattern, curie_string)
            return match is not None

    def normalize_curie(self, curie_string):
        # Remove any characters that are not allowed in a CURIE
        # todo add logging!
        curie_cleaned = re.sub(r'[^a-zA-Z0-9:_./-]', '', curie_string)

        # Add a user-specified prefix if no prefix is present
        if ':' not in curie_cleaned:
            curie_normalized: str = f'{self.forced_prefix}:{curie_cleaned}'
        else:
            curie_normalized = curie_cleaned

        return curie_normalized

    def apply_changes_recursively_by_key(self, o, keys_to_migrate, migration_eligible=False):
        if isinstance(o, dict):
            migration_eligible = False
            for k, v in o.items():
                o[k] = self.apply_changes_recursively_by_key(
                    v, keys_to_migrate, migration_eligible or k in keys_to_migrate
                )
            return o
        elif isinstance(o, list):
            return [
                self.apply_changes_recursively_by_key(v, keys_to_migrate, migration_eligible)
                for v in o
            ]
        else:
            return self.check_and_normalize_one_curie(o) if migration_eligible else o

    def load_yaml_file(self, filename):
        """Loads a YAML file into a Python dict."""
        with open(filename, "r") as f:
            data = yaml.safe_load(f)
        return data
    

class Migrator_from_7_7_2_to_7_8_0(Migrator):
    """Methods related to migrating documents from schema 7.7.2 to 7.8.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the collection-to-transformations map for this migration.
        self.transformations_by_collection = dict(
            study_set=[self.replace_doi_field_with_award_dois_list_field],
        )

    def replace_doi_field_with_award_dois_list_field(self, study: dict) -> dict:
        logger.info(f"Starting migration of {study['id']}")
        if "doi" in study:
            match = re.search(doi_url_pattern, study["doi"]['has_raw_value'])
            if match:
                start_index = match.end()
                as_curie = f"doi:10.{study['doi']['has_raw_value'][start_index:]}"
                study["award_dois"] = [as_curie]
            del study["doi"]
        return study


class Migrator_from_7_8_0_to_8_0_0(Migrator):
    """Methods related to migrating documents from schema 7.8.0 to 8.0.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the collection-to-transformations map for this migration.
        self.transformations_by_collection = dict(
            biosample_set=[self.standardize_letter_casing_of_gold_biosample_identifiers],
            extraction_set=[self.rename_sample_mass_field],
            omics_processing_set=[self.standardize_letter_casing_of_gold_sequencing_project_identifiers],
            study_set=[self.standardize_letter_casing_of_gold_study_identifier],
        )

    def rename_sample_mass_field(self, extraction: dict) -> dict:
        logger.info(f"Starting migration of {extraction['id']}")
        if "sample_mass" in extraction:
            extraction['input_mass'] = extraction.pop('sample_mass')
        return extraction

    def standardize_letter_casing_of_gold_identifiers(self, identifiers: List[str]) -> List[str]:
        """
        Replaces the prefix `GOLD:` with `gold:` in the list of identifiers.
        
        Note: If the identifier contains more than one colon, everything after the second
              colon will be discarded.
        """
        
        standardized_identifiers = []
        for identifier in identifiers:
            logger.info(f"Original identifier: {identifier}")
            curie_parts = identifier.split(':')
            curie_prefix = curie_parts[0]  # everything before the first colon
            curie_local_id = curie_parts[1]  # everything after the first colon, assuming there are no more colons

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


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--schema-path", default='nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Destination for the YAML data file")
@click.option("--salvage-prefix", required=True, type=str,
              help=
              "A prefix, defined in the schema, to assert for values that are expected to be CURIes but have no prefix")
def main(schema_path, input_path, output_path, salvage_prefix):
    migrator = Migrator()
    migrator.forced_prefix = salvage_prefix

    logger.info(f"Loading schema from {schema_path}")
    view = SchemaView(schema_path)
    slots = view.all_slots()
    migrateable_slots = set()
    for sk, sv in slots.items():
        s_range = sv.range
        if s_range == "uriorcurie":
            slot_descendants = view.slot_descendants(sk)
            for i in slot_descendants:
                migrateable_slots.add(i)
        elif s_range:
            range_type_name = type(view.get_element(s_range)).class_name
            if range_type_name == "class_definition":
                if view.get_identifier_slot(s_range):
                    slot_descendants = view.slot_descendants(sk)
                    for i in slot_descendants:
                        migrateable_slots.add(i)

    logger.info(f"Loading data from {input_path}")
    total_dict = migrator.load_yaml_file(input_path)
    end_dict = {}
    for tdk, tdv in total_dict.items():
        logger.info(f"Starting migration of {tdk}")
        end_dict[tdk] = migrator.apply_changes_recursively_by_key(tdv, set(migrateable_slots))
        # if tdk == "study_set":
        #     logger.info(f"Starting {tdk}-specific migrations")
        #     for current_study in tdv:
        #         migrator.migrate_studies_7_7_2_to_7_8(current_study)
        if tdk == "extraction_set":
            logger.info(f"Starting {tdk}-specific migrations")
            for current_extraction in tdv:
                migrator.migrate_extractions_7_8_0_to_8_0_0(current_extraction)
        if tdk == "omics_processing_set":
            logger.info(f"Starting {tdk}-specific migrations")
            for current_omics_processing in tdv:
                migrator.migrate_uc_gold_sequencing_project_identifiers_7_8_0_to_8_0_0(current_omics_processing)
        if tdk == "biosample_set":
            logger.info(f"Starting {tdk}-specific migrations")
            for current_biosample in tdv:
                migrator.migrate_uc_gold_biosample_identifiers_7_8_0_to_8_0_0(current_biosample)
        if tdk == "study_set":
            logger.info(f"Starting {tdk}-specific migrations")
            for current_study in tdv:
                migrator.migrate_uc_gold_study_identifiers_7_8_0_to_8_0_0(current_study)

    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(end_dict, f)


if __name__ == "__main__":
    main()
