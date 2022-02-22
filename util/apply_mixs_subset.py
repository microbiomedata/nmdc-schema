from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.dumpers import yaml_dumper

mixs_path = "../src/schema/mixs.yaml"

mixs_view = SchemaView(mixs_path)

mixs_elements = mixs_view.all_elements()

# me_string = yaml_dumper.dumps(mixs_elements)
# print(me_string)

for k, v in mixs_elements.items():
    if len(v.in_subset):
        print(f"{v.name}: {v.in_subset}")
