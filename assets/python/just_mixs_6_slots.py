from linkml_runtime import SchemaView

schema_file = "../mixs/model/schema/mixs.yaml"

schema_view = SchemaView(schema_file)

schema_slots = schema_view.all_slots()

ss_names = list(schema_slots.keys())

ss_names.sort()

for current_slot in ss_names:
    print(current_slot)
