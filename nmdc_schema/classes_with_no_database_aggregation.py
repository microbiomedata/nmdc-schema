import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../src/schema/nmdc.yaml"
target_class = "Database"

nmdc_view = SchemaView(schema_file)

nmdc_classes = nmdc_view.all_classes()

nmdc_class_names = []
for ck, cv in nmdc_classes.items():
    nmdc_class_names.append(cv.name)

database_slots = nmdc_view.class_induced_slots(target_class)

database_slots_to_ranges = {}
database_slot_ranges = []
for i in database_slots:
    database_slots_to_ranges[i.name] = i.range
    database_slot_ranges.append(i.range)


non_database_classes = list(set(nmdc_class_names) - set(database_slot_ranges))
non_database_classes.sort()
pprint.pprint(non_database_classes)
