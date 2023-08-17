import importlib
import pprint

import yaml
from linkml.generators.jsonldcontextgen import ContextGenerator
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper, rdf_dumper
from linkml_runtime.loaders import json_loader
import time
from datetime import datetime

from nmdc_schema.nmdc import Database


# todo add progress indicator for reading large YAML data file and for converting into dict? tqdm?


# staring with data in production database on 2023-08-17
# it already passes the 7.2 schema validation
# but it can;t be converted to RDF TTL
# probably because of un-prefixed ids
# are there modes in which linkml can check for curie prefixes, even if a pattern isn't asserted?
# or inject some base prefix?

# next: dois migration

# semi related: model the functional annotation aggregation

# start thinking about performance with larger datasets

# yaml data load time right after reboot (no swapping and moderate disk use esp for excessive browser tabs)
# execution_time = 593.8099591732025

def load_yaml_file(filename):
    """Loads a YAML file into a Python dict."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data


class NmdcDatabase:
    def __init__(self, schema_path, yaml_data_path):
        print("Loading schema...")
        self.view = SchemaView(schema_path)

        self.context_obj = ContextGenerator(self.view.schema).serialize()

        print("Loading data...")

        start_time = time.time()  # Record the starting time
        start_time_str = datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{start_time_str = }")

        self.data = load_yaml_file(yaml_data_path)

        end_time = time.time()  # Record the ending time
        end_time_str = datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{end_time_str = }")

        execution_time = end_time - start_time
        print(f"{execution_time = }")

    def iterate_over_set_list(self, set_name):
        instance_list = self.data[set_name]
        instances_type = self.view.get_slot(set_name).range

        dynamic_class = getattr(importlib.import_module("nmdc_schema.nmdc"), instances_type)

        for i, instance in enumerate(instance_list):
            print(f"{instances_type} {i}")
            instance = json_loader.load_any(source=instance, target_class=dynamic_class)
            print(yaml_dumper.dumps(instance))

            # what will happen when we see an error?

            # # Exception: Must pass in JSON-LD context via contexts parameter
            # xc =

            # x = rdf_dumper.dumps(element=instance, contexts=self.context_obj)
            x = rdf_dumper.as_rdf_graph(element=instance, contexts="../project/jsonschema/nmdc.schema.json")
            print(x)

    def iterate_over_database_sets(self):
        for set_name, set_list in self.data.items():
            print(f"{set_name = }")
            self.iterate_over_set_list(set_name)


# nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml or nmdc_schema/nmdc_materialized_patterns.yaml
nmdc_database = NmdcDatabase('../nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml',
                             '../mongo_as_unvalidated_nmdc_database.yaml')

nmdc_database.iterate_over_database_sets()
