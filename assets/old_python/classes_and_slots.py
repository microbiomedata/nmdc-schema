from linkml_runtime import SchemaView
import pandas as pd

schema_file = "../src/schema/nmdc.yaml"

schema_view = SchemaView(schema_file)

schema_classes = schema_view.all_classes()
sc_names = list(schema_classes.keys())
sc_names.sort()

lod = []
for current_class in sc_names:
    cis = schema_view.class_induced_slots(current_class)
    for current_slot in cis:
        lod.append({'class': current_class, 'slot': current_slot.name, 'slot_schema': current_slot.from_schema})

df = pd.DataFrame(lod)

# df.to_csv("../reports/nmdc_class_slots.tsv", sep="\t", index=False)
