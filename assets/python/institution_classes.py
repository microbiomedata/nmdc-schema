from linkml_runtime import SchemaView

schema_source = "../src/schema/nmdc.yaml"

slots_to_classes = {}
classes_to_slots = {}

print(f"Loading schema from {schema_source}")
schema_view = SchemaView(schema_source)
print(f"Loaded {schema_view.schema.name}")

print(f"Getting slots")
all_slots = schema_view.all_slots()

# print(type(all_slots))
# <class 'dict'>

# what do we trust? keys? .names? .alias?

slot_keys = list(all_slots.keys())

print(f"Associating slots with induced classes")
all_classes = schema_view.all_classes()
for k, v in all_classes.items():
    i_c = schema_view.induced_class(k)
    i_c_attribute_names = list(i_c.attributes.keys())
    classes_to_slots[k] = i_c_attribute_names

# I'm still not convinced that these are useful:
# domain=None
# domain_of=[]

print(f"Associating classes with slots")
for k, v in classes_to_slots.items():
    for i in v:
        if i in slots_to_classes:
            slots_to_classes[i].append(k)
        else:
            slots_to_classes[i] = [k]

print(f"Finding slots with the substring 'institution'.")
institution_keys = [i for i in slot_keys if "institution" in i]

print(f"Reporting classes that use a slot with the substring 'institution'")
for i in institution_keys:
    print(f"  {i}: {slots_to_classes[i]}")
