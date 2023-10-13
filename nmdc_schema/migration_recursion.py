import logging
import re

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

    logger.info(f"Saving migrated data to {output_path}")
    with open(output_path, "w") as f:
        yaml.dump(end_dict, f)


if __name__ == "__main__":
    main()
