import logging
import re
import importlib
import inspect

import click
import click_log
import yaml
from linkml_runtime import SchemaView

from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

# todo: log before and after states of migration

CURIE_PATTERN = r'^[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z0-9_][a-zA-Z0-9_.-]*$'


class CurieMigrator:
    """Properties and methods related to migrating CURIE strings."""

    def __init__(self):
        self.forced_prefix = None

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
            match = re.match(CURIE_PATTERN, curie_string)
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

    def fix_curies_recursively_by_key(self, o, keys_to_migrate, migration_eligible=False):
        if isinstance(o, dict):
            migration_eligible = False
            for k, v in o.items():
                o[k] = self.fix_curies_recursively_by_key(
                    v, keys_to_migrate, migration_eligible or k in keys_to_migrate
                )
            return o
        elif isinstance(o, list):
            return [
                self.fix_curies_recursively_by_key(
                    v, keys_to_migrate, migration_eligible)
                for v in o
            ]
        else:
            return self.check_and_normalize_one_curie(o) if migration_eligible else o


def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--schema-path", default='nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file to which the input YAML data file conforms")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Path to the output YAML data file")
@click.option("--salvage-prefix", required=True, type=str,
              help="A prefix, defined in the schema, to force for each value that the schema indicates is a CURIE but that has no prefix")
@click.option("--migrator-name", type=str, multiple=True,
              help="The name of a migrator module that you want to use to migrate data. If you specify this option "
                   "multiple times, the specified migrator modules will be used in the order specified.\n\n"
                   "Migrator modules are Python modules residing in the `nmdc_schema/migrators/` directory. "
                   "Their names begin with `migrator_from_`.")
def main(schema_path, input_path, output_path, salvage_prefix, migrator_name):
    """
    Generates a data file that conforms to a different schema version than the input data file does.

    See source code for initial and final schema versions.
    """

    migrators = []

    for current_name in migrator_name:
        try:
            # Import the module whose name matches the specified migrator module name.
            # Reference: https://docs.python.org/3/library/importlib.html#importlib.import_module
            migrator_module = importlib.import_module(f".{current_name}", package="nmdc_schema.migrators")

            # Get the `Migrator` class defined in that module.
            # Reference: https://docs.python.org/3/library/inspect.html#inspect.isclass
            migrator_class = getattr(migrator_module, "Migrator")
            if not inspect.isclass(migrator_class):
                raise TypeError

            # Append that class to the list of migrator classes.
            migrators.append(migrator_class)
            logger.info(f"Will use migrator: {current_name}")
        except (KeyError, ImportError, AttributeError, TypeError) as exception:
            logger.error(f"ERROR: {current_name} is not a valid migrator module name. {exception}.")
            continue

    if len(migrators) == 0:
        logger.info("No valid migrators specified. Will perform default migration")
        # exit()

    # Load the input data
    logger.info(f"Loading data from {input_path}")
    total_dict = load_yaml_file(input_path)

    # Load the schema and determine which of its slots we can migrate.
    logger.info(f"Loading schema from {schema_path}")
    view = SchemaView(schema_path)
    slots = view.all_slots()
    curie_slots = set()
    for sk, sv in slots.items():
        s_range = sv.range
        if s_range == "uriorcurie":
            slot_descendants = view.slot_descendants(sk)
            for i in slot_descendants:
                curie_slots.add(i)
        elif s_range:
            range_type_name = type(view.get_element(s_range)).class_name
            if range_type_name == "class_definition":
                if view.get_identifier_slot(s_range):
                    slot_descendants = view.slot_descendants(sk)
                    for i in slot_descendants:
                        curie_slots.add(i)

    logger.info(curie_slots)

    curie_migrator = CurieMigrator()
    curie_migrator.forced_prefix = salvage_prefix

    # iterate over collections, applying CURIe fixes
    for tdk, tdv in total_dict.items():
        logger.info(f"Fixing CURIes in {tdk} if necessary")

        total_dict[tdk] = curie_migrator.fix_curies_recursively_by_key(
            tdv, set(curie_slots))

    # Instantiate an adapter that the migrator can use to manipulate a "database" represented as a Python dictionary.
    # Also, specify some callback functions, so we can react when certain events occur.
    dictionary_adapter = DictionaryAdapter(
        database=total_dict,
        on_collection_created=lambda name: logger.info(f'Created collection "{name}"'),
        on_collection_renamed=lambda old_name, name: logger.info(f'Renamed collection "{old_name}" to "{name}"'),
        on_collection_deleted=lambda name: logger.info(f'Deleted collection "{name}"'),
    )

    # Iterate over the specified Migrator classes:
    for current_migrator in migrators:
        # Instantiate this migrator, binding it to the adapter we instantiated earlier.
        migrator = current_migrator(adapter=dictionary_adapter, logger=logger)
        # Invoke this migrator's `upgrade` method; effectively "doing" the migration.
        migrator.upgrade()

    # all migrations complete. save data.
    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(total_dict, f)


if __name__ == "__main__":
    main()
