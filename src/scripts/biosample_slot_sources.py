import csv
import pprint

from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime import SchemaView

schema_file = "../schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

biosample_induced_class = schema_view.induced_class('Biosample')

# # print(yaml_dumper.dumps(biosample_induced_class))
#
# # depth_slot = schema_view.get_slot('depth')
# #
# # print(yaml_dumper.dumps(depth_slot))
# #
# # name_slot = schema_view.get_slot('name')
# #
# # print(yaml_dumper.dumps(name_slot))
#
# biosample_name_induced_slot = schema_view.induced_slot('name', 'Biosample')
#
# print(yaml_dumper.dumps(biosample_name_induced_slot))
#
# print(schema_view.schema.slots)
#
# # print(schema_view.schema.slots['name'].slot_uri)

class_name = 'Biosample'
# Define the filename for the TSV file
tsv_output_file = "biosample_slot_sources.tsv"

class_induced_slots = biosample_induced_class.attributes

slot_attribs_lod = []

for slotk, slotv in class_induced_slots.items():
    slot_source_file = str(slotv.from_schema).split('/')[-1]
    # print(slot_source_file, end='\t')
    slot_range = slotv.range
    slot_range_obj = schema_view.get_element(slot_range)
    slot_range_obj_type = type(slot_range_obj).class_name
    # print(str(slot_range), end='\t')
    # print(slot_range_obj_type, end='\t')
    # is it a grouping slot or abstract?
    if slotv.abstract:
        # print(f"ABSTRACT: {slotv.name}")
        continue
    if slotv.is_grouping_slot:
        # print(f"GROUPING: {slotv.name}")
        continue
    slot_uri = None
    if slotv.slot_uri is not None:
        # print(str(slotv.slot_uri))
        slot_uri = str(slotv.is_a)
    else:
        # print(f"{str(schema_view.schema.default_prefix)}:{str(slotv.name)}")
        slot_uri = f"{str(schema_view.schema.default_prefix)}:{str(slotv.name)}"
    print(slotv.in_subset)
    slot_attribs_lod.append({
        'slot_name': slotv.name,
        'slot_source_file': slot_source_file,
        'slot_range': str(slot_range),
        'slot_range_obj_type': slot_range_obj_type,
        'slot_uri': slot_uri
    })

# pprint.pprint(slot_attribs_lod)

# Define the fieldnames based on the keys of the dictionaries
fieldnames = slot_attribs_lod[0].keys()

# Write the list of dictionaries to the TSV file
with open(tsv_output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(slot_attribs_lod)

print("TSV file has been created successfully.")
