from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_yaml = "../src/schema/nmdc.yaml"
schema_view = SchemaView(schema_yaml)

class_names = list(schema_view.all_classes().keys())
class_names.sort()

requirements = {}

for class_name in class_names:
    class_induced_slots = schema_view.induced_class(class_name).attributes
    required_slots = []
    for sk, sv in class_induced_slots.items():
        if sv.required:
            required_slots.append(sk)
    required_slots.sort()
    requirements[class_name] = required_slots

print(yaml_dumper.dumps(requirements))
