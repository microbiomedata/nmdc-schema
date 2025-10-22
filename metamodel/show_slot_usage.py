#!/usr/bin/env python3
"""
Show which classes use a specific slot.
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView

if len(sys.argv) < 3:
    print("Usage: python show_slot_usage.py <schema_path> <slot_name>")
    sys.exit(1)

schema_path = sys.argv[1]
slot_name = sys.argv[2]

sv = SchemaView(schema_path)
slot = sv.get_slot(slot_name)

if slot is None:
    print(f"Slot '{slot_name}' not found in schema")
    sys.exit(1)

print(f"Slot: {slot_name}")
print(f"From Schema: {getattr(slot, 'from_schema', 'N/A')}")
print(f"Range: {slot.range}")
print()

# Get domain_of (classes that directly declare this slot)
domain_of = getattr(slot, 'domain_of', [])
if domain_of:
    print(f"Domain Of (classes that declare this slot): {len(domain_of)}")
    for cls_name in sorted(domain_of):
        print(f"  - {cls_name}")
else:
    print("Domain Of: None (not directly declared by any class)")

print()

# Use SchemaView to find all classes that can use this slot (including via inheritance)
classes_using_slot = []
for class_name in sv.all_classes():
    class_slots = sv.class_slots(class_name)
    if slot_name in class_slots:
        classes_using_slot.append(class_name)

if classes_using_slot:
    print(f"All Classes That Can Use This Slot (including via inheritance): {len(classes_using_slot)}")
    for cls_name in sorted(classes_using_slot):
        print(f"  - {cls_name}")
else:
    print("No classes use this slot")
