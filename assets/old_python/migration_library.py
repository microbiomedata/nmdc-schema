import importlib
import pprint
import re
import time
from datetime import datetime

import click
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, rdflib_dumper
from linkml_runtime.loaders import json_loader

# todo add progress indicator for reading large YAML data file and for converting into dict? tqdm?


# staring with data in production database on 2023-08-17
# it already passes the 7.2 schema validation (ignoring nmdc ids),
# but it can't be converted to RDF TTL
# probably because of un-prefixed ids/curies
# are there modes in which linkml can check for curie prefixes, even if a pattern isn't asserted?
# or inject some base prefix?

# next: dois migration

# semi related: model the functional annotation aggregation

# start thinking about performance with larger datasets

# yaml data load time right after reboot (no swapping and moderate disk use esp for excessive browser tabs)
# execution_time = 593.8099591732025

curie_regex = r'^[a-zA-Z_][a-zA-Z0-9_-]*:[a-zA-Z0-9_][a-zA-Z0-9_.-]*$'


def check_and_normalize_one_curie(curie_string):
    if not is_valid_curie(curie_string):
        curie_string = normalize_curie(curie_string)
    return curie_string


def is_valid_curie(curie_string):
    if curie_string == "None":
        pass
        # print("curie_string = 'None'")  # at what point do these get converted from None values to 'None' strings?
    else:
        match = re.match(curie_regex, curie_string)
        return match is not None


def normalize_curie(curie_string, forced_prefix="nmdc"):
    # Remove any characters that are not allowed in a CURIE
    curie_cleaned = re.sub(r'[^a-zA-Z0-9_.-]', '', curie_string)

    # Add the "nmdc" prefix if no prefix is present
    if ':' not in curie_cleaned:
        curie_normalized = f'{forced_prefix}:{curie_cleaned}'
    else:
        curie_normalized = curie_cleaned

    return curie_normalized


def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


class NmdcDatabase:
    def __init__(self, schema_path, yaml_data_path):
        print("Loading schema...")
        self.view = SchemaView(schema_path)

        # self.context_dict = load_yaml_file('../project/jsonld/nmdc.context.jsonld') # for injecting base prefix?
        # print(self.context_dict)

        print("Loading data...")

        start_time = time.time()  # Record the starting time
        start_time_str = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{start_time_str = }")

        self.data = load_yaml_file(yaml_data_path)

        end_time = time.time()  # Record the ending time
        end_time_str = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{end_time_str = }")

        execution_time = end_time - start_time
        print(f"{execution_time = }\n")

    def iterate_over_instance_parts(self, instance,
                                    instance_type_string):  # todo insert OK or normalized instances back into a dict
        # todo log all of these changes
        applicable_slots = self.view.class_induced_slots(instance_type_string)
        applicable_slot_names = [i.name for i in applicable_slots]
        for a_s in applicable_slot_names:  # todo recursion?
            a_s_range = applicable_slots[applicable_slot_names.index(a_s)].range
            a_s_range_type = type(self.view.get_element(a_s_range)).class_name
            a_s_multivalued = self.view.get_slot(a_s).multivalued
            a_s_inlined = self.view.get_slot(a_s).inlined
            a_s_inlined_as_list = self.view.get_slot(a_s).inlined_as_list
            if instance[a_s]:  # todo this masks None assertions
                if a_s_range == "uriorcurie":
                    if a_s_multivalued:
                        normalized_curies = []
                        for single_curie in instance[a_s]:
                            normalized_curie = check_and_normalize_one_curie(single_curie)
                            normalized_curies.append(normalized_curie)
                        instance[
                            a_s] = normalized_curies  # todo don't do any of these reassignments if the resulting list is equalivant to the inputs
                    else:
                        normalized_curie = check_and_normalize_one_curie(instance[a_s])
                        instance[a_s] = normalized_curie
                elif a_s_range_type == "class_definition" and not (a_s_inlined or a_s_inlined_as_list):
                    if a_s_multivalued:
                        normalized_curies = []
                        for single_curie in instance[a_s]:
                            normalized_curie = check_and_normalize_one_curie(single_curie)
                            normalized_curies.append(normalized_curie)
                        instance[
                            a_s] = normalized_curies
                    else:
                        normalized_curie = check_and_normalize_one_curie(instance[a_s])
                        instance[a_s] = normalized_curie

        return instance

    def iterate_over_set_list(self, set_name):  # todo fix uris, remove None assertions...
        instance_list = self.data[set_name]
        instances_type = self.view.get_slot(set_name).range

        dynamic_class = getattr(importlib.import_module("nmdc_schema.nmdc"), instances_type)

        repaired_list = []
        for instance_dict in instance_list:
            try:
                instance_obj = json_loader.load_any(source=instance_dict, target_class=dynamic_class)
                try:
                    as_rdf = rdflib_dumper.dumps(element=instance_obj,
                                                 schemaview=self.view)  # todo prefix_map=self.context_dict["@context"] ?
                    repaired_list.append(instance_dict)
                except ValueError as e:
                    # print(f"\nRDF error when converting {instances_type} {e}")
                    # print(yaml_dumper.dumps(instance_obj))
                    repaired_instance = self.iterate_over_instance_parts(instance_obj, instances_type)
                    try:
                        as_rdf = rdflib_dumper.dumps(element=repaired_instance,
                                                     schemaview=self.view)
                        print(f"Repaired instance with legacy id {instance_dict['id']}")
                        repaired_list.append(instance_dict)
                    except TypeError as e:
                        print(f"\nrepair TypeError when converting {instances_type} {e}")
                        print(yaml_dumper.dumps(repaired_instance))
                    except ValueError as e:
                        print(f"\nrepair ValueError when converting {instances_type} {e}")
                        print(yaml_dumper.dumps(repaired_instance))

            except ValueError as e:
                print(f"LinkML error when instantiating {instances_type} {e}")
                print(instance_dict)
                continue

        return repaired_list

    def iterate_over_database_sets(self):
        repaired_dict = {}
        for set_name, set_list in self.data.items():
            print(f"\n{set_name = }\n")
            repaired_list = self.iterate_over_set_list(set_name)
            repaired_dict[set_name] = repaired_list
        return repaired_dict


@click.command()
@click.option("--schema-path", default='../nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml', required=True, type=str,
              help="Path to the schema file")
@click.option("--input-path", default='../mongo_as_unvalidated_nmdc_database.yaml', required=True, type=str,
              help="Path to the input YAML data file")
@click.option("--output-path", default='rdf_safe.yaml', required=True, type=str,
              help="Destination for the YAML data file")
def main(schema_path, input_path, output_path):
    nmdc_database = NmdcDatabase(schema_path, input_path)
    repaired_dict = nmdc_database.iterate_over_database_sets()
    print(f"Writing repaired  data to {output_path}...")
    with open(output_path, "w") as f:
        yaml.dump(repaired_dict, f)


if __name__ == "__main__":
    main()
