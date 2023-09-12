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

# todo dois repair
#   we want to extract the legacy `doi` values and assert them in one of the new `dois` subproperties
#   matching the expectation of that new slot
#   how will we know which of the `dois` subproperties it should go into?
#   here we are assuming all legacy Study.dois are award_dois
# todo: log before and after states of migration

doi_url_pattern = r'^https?:\/\/[a-zA-Z\.]+\/10\.'
curie_pattern = r'^[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z0-9_][a-zA-Z0-9_.-]*$'


def migrate_studies_7_7_2_to_7_8(retrieved_study):
    logger.info(f"Starting migration of {retrieved_study['id']}")
    if "doi" in retrieved_study:
        # logger.info(f"Before migration: {pprint.pformat(retrieved_study['doi'])}")

        match = re.search(doi_url_pattern, retrieved_study["doi"]['has_raw_value'])
        if match:
            start_index = match.end()
            as_curie = f"doi:10.{retrieved_study['doi']['has_raw_value'][start_index:]}"
            retrieved_study["award_dois"] = [as_curie]
        del retrieved_study["doi"]
    return retrieved_study

def migrate_extractions_7_9_to_NEXT(retrieved_extraction):
    logger.info(f"Starting migration of {retrieved_extraction['id']}")

    # change slot name from sample_mass to input_mass
    if "sample_mass" in retrieved_extraction:
        retrieved_extraction['input_mass'] = retrieved_extraction.pop('sample_mass')
        return retrieved_extraction

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
        match = re.match(curie_pattern, curie_string)
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
@click_log.simple_verbosity_option(logger)
@click.option("--schema-path", default='nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file")
@click.option("--input-path", default='local/mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='local/rdf_safe.yaml', required=True, type=str,
              help="Destination for the YAML data file")
def main(schema_path, input_path, output_path):
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
    total_dict = load_yaml_file(input_path)
    end_dict = {}
    for tdk, tdv in total_dict.items():
        logger.info(f"Starting migration of {tdk}")
        end_dict[tdk] = apply_changes_recursively_by_key(tdv, set(migrateable_slots))
        if tdk == "study_set":
            logger.info(f"Would start {tdk}-specific migrations")
            for current_study in tdv:
                migrate_studies_7_7_2_to_7_8(current_study)
        if tdk == "extraction_set":
            logger.info(f"Would start {tdk}-specific migrations")
            for current_extraction in tdv:
                migrate_extractions_7_9_to_NEXT(current_extraction)

    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(end_dict, f)


if __name__ == "__main__":
    main()
