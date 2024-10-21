import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

from linkml_runtime.linkml_model.meta import ClassDefinition, SlotDefinition

# from terminado.management import preexec_fn

pre_path = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/refs/tags/v10.9.1/src/schema/nmdc.yaml"

berkeley_path = "https://raw.githubusercontent.com/microbiomedata/nmdc-schema/refs/tags/v11.0.1/src/schema/nmdc.yaml"

pre_view = SchemaView(pre_path)

berkeley_view = SchemaView(berkeley_path)

pre_classes = pre_view.all_classes()
pre_class_names = list(pre_classes.keys())
print(len(pre_class_names))

berkeley_classes = berkeley_view.all_classes()
berkeley_class_names = list(berkeley_classes.keys())
print(len(berkeley_class_names))

pre_only = [c for c in pre_class_names if c not in berkeley_class_names]

berkeley_only = [c for c in berkeley_class_names if c not in pre_class_names]

pprint.pprint(pre_only)

pprint.pprint(berkeley_only)

pre_roots = pre_view.class_roots()
pre_roots.sort()
pprint.pprint(pre_roots)
print(len(pre_roots))

berkeley_roots = berkeley_view.class_roots()
berkeley_roots.sort()
pprint.pprint(berkeley_roots)
print(len(berkeley_roots))

pre_only = [c for c in pre_roots if c not in berkeley_roots]
pprint.pprint(pre_only)
print(len(pre_only))

berkeley_only = [c for c in berkeley_roots if c not in pre_roots]
pprint.pprint(berkeley_only)
print(len(berkeley_only))

####

pre_slots = pre_view.all_slots()
pre_slot_names = list(pre_slots.keys())
print(f"{len(pre_slot_names)}")

berkeley_slots = berkeley_view.all_slots()
berkeley_slot_names = list(berkeley_slots.keys())
print(f"{len(berkeley_slot_names)}")

pre_only = [s for s in pre_slot_names if s not in berkeley_slot_names]
pre_only.sort()

berkeley_only = [s for s in berkeley_slot_names if s not in pre_slot_names]
berkeley_only.sort()

pprint.pprint(pre_only)
print(f"{len(pre_only)}")

pprint.pprint(berkeley_only)
print(f"{len(berkeley_only)}")

####

# ChromatographicSeparationProcess, type: <class 'linkml_runtime.linkml_model.meta.ClassDefinition'>
# OmicsProcessing, type: <class 'linkml_runtime.linkml_model.meta.ClassDefinition'>
# CreditAssociation, type: <class 'linkml_runtime.linkml_model.meta.ClassDefinition'>
# total_bases, type: <class 'linkml_runtime.linkml_model.meta.SlotDefinition'>
# members_id, type: <class 'linkml_runtime.linkml_model.meta.SlotDefinition'>
# bin_name, type: <class 'linkml_runtime.linkml_model.meta.SlotDefinition'>

pre_abstract = []
pre_abstract_classes = []
pre_abstract_slots = []
pre_elements = pre_view.all_elements()
for ek, ev in pre_elements.items():
    if isinstance(ev, ClassDefinition) and ev.abstract:
        pre_abstract_classes.append(ek)
    if isinstance(ev, SlotDefinition) and ev.abstract:
        pre_abstract_slots.append(ek)

print(f"pre_abstract_classes: {len(pre_abstract_classes)}")
print(f"pre_abstract_slots: {len(pre_abstract_slots)}")

berkeley_abstract = []
berkeley_abstract_classes = []
berkeley_abstract_slots = []

berkeley_elements = berkeley_view.all_elements()

for ek, ev in berkeley_elements.items():
    if isinstance(ev, ClassDefinition) and ev.abstract:
        berkeley_abstract_classes.append(ek)
    if isinstance(ev, SlotDefinition) and ev.abstract:
        berkeley_abstract_slots.append(ek)

print(f"berkeley_abstract_classes: {len(berkeley_abstract_classes)}")
print(f"berkeley_abstract_slots: {len(berkeley_abstract_slots)}")

print(berkeley_abstract_classes)
print(pre_abstract_classes)

####


pre_study = pre_view.get_class("Study")
yaml_dumper.dump(pre_study, "pre_study.yaml")

berkeley_study = berkeley_view.get_class("Study")
yaml_dumper.dump(berkeley_study, "berkeley_study.yaml")
