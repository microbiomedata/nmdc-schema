import logging
import pprint
import re

import click
import click_log
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


# dois repair
# todo: log before and after states of migration

def migrate_studies_7_7_2_to_dev(retrieved_study):  # esp dois
    pass
    # return migrated_study


curie_regex = r'^[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z0-9_][a-zA-Z0-9_.-]*$'


def check_and_normalize_one_curie(curie_string):
    if not is_valid_curie(curie_string):
        curie_string = normalize_curie(curie_string)
    return curie_string


def is_valid_curie(curie_string):
    if curie_string == "None":
        pass
        # print("curie_string = 'None'")  # at what point do these get converted from None values to 'None' strings?
    elif '\n' in curie_string or '\r' in curie_string:
        pass
        # print("curie_string contains newline characters")
    else:
        match = re.match(curie_regex, curie_string)
        return match is not None


def normalize_curie(curie_string, forced_prefix="nmdc"):
    # Remove any characters that are not allowed in a CURIE
    curie_cleaned = re.sub(r'[^a-zA-Z0-9:_.-]', '', curie_string)

    # Add the "nmdc" prefix if no prefix is present
    if ':' not in curie_cleaned:
        curie_normalized: str = f'{forced_prefix}:{curie_cleaned}'
    else:
        curie_normalized = curie_cleaned

    return curie_normalized


def apply_changes_recursively_by_key(o, keys_to_migrate, migration_eligible=False):
    if isinstance(o, dict):
        migration_eligible = False
        for k, v in o.items():
            o[k] = apply_changes_recursively_by_key(
                v, keys_to_migrate, migration_eligible or k in keys_to_migrate
            )
        return o
    elif isinstance(o, list):
        return [
            apply_changes_recursively_by_key(v, keys_to_migrate, migration_eligible)
            for v in o
        ]
    else:
        return check_and_normalize_one_curie(o) if migration_eligible else o


def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


@click.command()
@click.option("--schema-path", default='nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Destination for the YAML data file")
def main(schema_path, input_path, output_path):
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

    total_dict = load_yaml_file(input_path)
    end_dict = {}
    for tdk, tdv in total_dict.items():
        logger.info(f"Starting migration of {tdk}")
        end_dict[tdk] = apply_changes_recursively_by_key(tdv, set(migrateable_slots))

    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(end_dict, f)


if __name__ == "__main__":
    main()
