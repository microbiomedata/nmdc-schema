import logging
import re
import importlib
import inspect
import shutil

import click
import click_log
import yaml
from linkml_runtime import SchemaView

from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter

logger = logging.getLogger(__name__)
click_log.basic_config(logger)

# TODO: Is this script somewhat redundant with nmdc_schema/migrators/cli/run_migrator.py? Can they
#       be consolidated?

# todo: log before and after states of migration


def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


@click.command()
@click_log.simple_verbosity_option(logger)
@click.option("--schema-path", default='nmdc_schema/nmdc_materialized_patterns.yaml', required=True, type=str,
              help="Path to the schema file to which the input YAML data file conforms")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Path to the output YAML data file")
@click.option("--migrator-name", type=str, multiple=True,
              help="The name of a migrator module that you want to use to migrate data. If you specify this option "
                   "multiple times, the specified migrator modules will be used in the order specified.\n\n"
                   "Migrator modules are Python modules residing in the `nmdc_schema/migrators/` directory. "
                   "Their names begin with `migrator_from_`.")
def main(schema_path, input_path, output_path, migrator_name):
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
        logger.info("No valid migrators specified. Just copying the input file to the output file.")
        # Copy the input file to the output file
        shutil.copy(input_path, output_path)
        exit()

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
