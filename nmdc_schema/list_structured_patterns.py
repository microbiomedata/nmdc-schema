from linkml_runtime import SchemaView

schema_file = "../src/schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

print(schema_view.schema.name)

schema_classes = schema_view.all_classes()

for ck, cv in schema_classes.items():
    cis = schema_view.class_induced_slots(ck)
    for induced_slot in cis:

        if "structured_pattern" in induced_slot and induced_slot["structured_pattern"]:
            sp_syntax = induced_slot["structured_pattern"]["syntax"]
            print(f"{ck} {induced_slot.name}: {sp_syntax}")
