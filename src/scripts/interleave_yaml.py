import pprint

import yaml
import os
import glob

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

from nmdc_schema.nmdc import Database
from linkml_runtime.loaders import yaml_loader
from collections import defaultdict

# # Specify the directory containing YAML files
# directory_path = '../data/gemini'
directory_path = '../data/valid'

# List all YAML files in the specified directory
file_paths = glob.glob(os.path.join(directory_path, 'Database-*.yaml'))

collector = Database()
schema_file = '../schema/nmdc.yaml'
schema_view = SchemaView(schema_file)
database_slots = schema_view.class_induced_slots('Database')
database_slot_names = [slot.name for slot in database_slots]
database_slot_names.sort()
# print(type(database_slots))
pprint.pprint(database_slot_names)
print(schema_view.schema.name)

for file in file_paths:
    print(f"Processing file: {file}")
    with open(file, 'r') as f:
        # Load the YAML data
        data = yaml.safe_load(f)

        database = yaml_loader.load(data, Database)
        for slot in database_slot_names:
            print(slot)
            payload = getattr(database, slot)
            collector.__dict__[slot].extend(payload)

print(yaml_dumper.dumps(collector))

yaml_dumper.dump(collector, 'interleaved.yaml')
