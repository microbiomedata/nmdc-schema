from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.schemaview import OrderedBy

schema_file = "../schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

for ck, cv in schema_view.all_classes(ordered_by=OrderedBy.LEXICAL).items():

    if cv.slot_usage:
        print(f"{ck}:")
        print(yaml_dumper.dumps(cv.slot_usage))
