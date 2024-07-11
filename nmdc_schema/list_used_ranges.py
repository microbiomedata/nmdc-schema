from linkml_runtime import SchemaView

schema_file = "../src/schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

schema_classes = schema_view.all_classes()

for ck, _ in schema_classes.items():
    induced_slots = schema_view.class_induced_slots(ck)
    for induced_slot in induced_slots:
        if induced_slot.name == 'used':
            print(f"In class {ck}, slot used has range  {induced_slot.range}")
