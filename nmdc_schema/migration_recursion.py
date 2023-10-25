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


class MigratorBase:
    """Base class containing properties and methods related to migrating data between schema versions."""

    def __init__(self):
        self.forced_prefix = None

        # Define the "agenda" of transformations that constitute this migration.
        # 
        # Note: This is a dictionary that maps a given collection to a list of "transformation" functions.
        #       Each key is a collection name, and each value is a list. Each element of the list is a
        #       so-called "transformation" function. A "transformation" function is a function that
        #       transforms something from one schema version to another. In this case, the "something"
        #       is a dictionary representing a single document from the specified collection.
        #
        # Note: This dictionary is empty here. It will be populated within the "constructor" functions
        #       of the migration-specific classes (i.e. the classes that inherit from this base class).
        #
        self.agenda: Dict[str, List[callable]] = dict()

    def get_transformers_for(self, collection_name: str) -> List[callable]:
        """Returns the list of transformers defined for the specified collection."""
        return self.agenda.get(collection_name, [])

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


class Migrator_from_A_B_C_to_X_Y_Z(MigratorBase):
    """
    Migrates data from schema A.B.C to X.Y.Z

    TUTORIAL: This is an example of a "migrator" class.
              It was designed for use during developer training and
              to serve as a template for production "migrator" classes.
    """

    def __init__(self) -> None:
        """
        TUTORIAL: This is the "constructor" function of the class.
                  As is true about the "constructor" function of any class,
                  it runs whenever that class is instantiated, and its job
                  is to initialize the newly-created instance of that class.
                  
                  When this "constructor" function runs, it does two things:
                  1. It invokes the base class's "constructor" function; and
                  2. It populates a dictionary that keeps track of which
                     transformation functions will be applied to objects
                     from which collections. You can think of this as the
                     "agenda", "itinerary", "plan", or "registry" of
                     transformations that make up this migration. As
                     security guards at marathons say, "If it ain't
                     part of the plan, it ain't gonna be ran."

             -->  As part of creating a new "migration" class, you will
                  populate its "agenda."
        """

        # Invoke the base class's "constructor" function.
        super().__init__()

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.allow_multiple_names],
        )

    def allow_multiple_names(self, study: dict) -> dict:
        """
        TUTORIAL: This is an example "transformation" function within the class.
                  Its jobs is to transform a dictionary that conforms to the
                  initial schema version (in this case, version "A.B.C"), into one
                  that conforms to the target schema version (in this case,
                  version "X.Y.Z"). That might involve adding a field,
                  converting a string into a list of strings, etc.
                  
                  When this "transformation" function runs, it does three things:
                  1. It accepts a single dictionary as a parameter.
                  2. It transforms that dictionary.
                  3. It returns the transformed dictionary.

              --> As part of creating a new "migration" class, you will
                  typically implement one or more "transformation" functions.
                  You will also add them to the "agenda" of the class.
        """

        logger.info(f"Transforming study having id: {study['id']}")  # optional log message

        # Transform the dictionary.
        #
        # TUTORIAL: In this example scenario, I am pretending that:
        #           1. In schema version "A.B.C", the `Study` class has a `name` slot,
        #              which contain a single string.
        #           2. In schema version "X.Y.Z", the `Study` class no longer has that
        #              `name` slot. Instead, it has a `names` slot, which contains
        #              a list of strings.
        #
        original_name = study["name"]  # preserve the original value
        study["names"] = []  # create a new key, whose value is an empty list of names
        study["names"].append(original_name)  # add the original value to that list
        del study["name"]  # delete the obsolete key

        # Return the transformed dictionary.
        return study


class Migrator_from_7_7_2_to_7_8_0(MigratorBase):
    """Migrates data from schema 7.7.2 to 7.8.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
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


class Migrator_from_7_8_0_to_8_0_0(MigratorBase):
    """Migrates data from schema 7.8.0 to 8.0.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
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
            omics_processing[field_name] = self.standardize_letter_casing_of_gold_identifiers(
                omics_processing[field_name])
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


class Migrator_from_8_0_0_to_8_1_0(MigratorBase):
    """Migrates data from schema 8.0.0 to 8.1.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.force_research_study_study_category],
        )

    def force_research_study_study_category(self, study: dict) -> dict:
        if 'study_category' not in study:
            logger.info(f"Forcing 'study_category: research_study' on {study['id']}")
            study['study_category'] = 'research_study'
        return study


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--schema-path", default='nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file to which the input YAML data file conforms")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Path to the output YAML data file")
@click.option("--salvage-prefix", required=True, type=str,
              help=
              "A prefix, defined in the schema, to force for each value that the schema indicates is a CURIE but that has no prefix")
def main(schema_path, input_path, output_path, salvage_prefix):
    """
    Generates a data file that conforms to a different schema version than the input data file does.
    
    See source code for initial and final schema versions.
    """

    migrator = Migrator_from_8_0_0_to_8_1_0()
    migrator.forced_prefix = salvage_prefix

    # Load the schema and determine which of its slots we can migrate.
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

    # Load the input data and migrate the fields in it that correspond to those slots.
    logger.info(f"Loading data from {input_path}")
    total_dict = migrator.load_yaml_file(input_path)
    end_dict = {}
    for tdk, tdv in total_dict.items():
        logger.info(f"Starting migration of {tdk}")

        end_dict[tdk] = migrator.apply_changes_recursively_by_key(tdv, set(migrateable_slots))

        # If the migration specifies any transformers for this collection,
        # apply them—in order—to each document within this collection.
        transformers = migrator.get_transformers_for(collection_name=tdk)
        if len(transformers) > 0:
            logger.info(f"Starting {tdk}-specific transformations")
            for document in tdv:
                for transformer in transformers:
                    transformer(document)  # modifies the document in place

    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(end_dict, f)


if __name__ == "__main__":
    main()
