import pprint

from linkml_runtime import SchemaView

temp = SchemaView("../mixs/model/schema/mixs.yaml")
temp_slots = temp.all_slots()
ts_names = list(temp_slots.keys())
ts_names.sort()
# pprint.pprint(ts_names)
# # air particulate matter concentration

for k, v in temp_slots.items():
    print(f"key: {k}; name: {v.name}; title: {v.title}")
