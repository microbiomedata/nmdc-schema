from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../src/schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

schema_classes = schema_view.all_classes()

schema_class_names = [cv.name for ck, cv in schema_classes.items()]

schema_class_names.sort()

for c in schema_class_names:
    ic = schema_view.induced_class(c)
    ica = ic.attributes
    ica_names = [v.name for k, v in ica.items()]
    if "id" in ica_names:
        print(f"INDUCED id ATTRIBUTE FOR {c}:")
        print(yaml_dumper.dumps(ica['id']))
        print("\n")
    else:
        print(f"CLASS {c} DOESN'T USE THE id SLOT")
        print("\n")
