#!/usr/bin/env python3
"""
Check if a slot is orphaned (defined but not used by any class).
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView

schema_path = "src/schema/nmdc.yaml"
slot_name = "value"

sv = SchemaView(schema_path)
slot = sv.get_slot(slot_name)

print(f"Slot: {slot_name}")
print(f"From Schema: {slot.from_schema}")
print(f"Range: {slot.range}")
print(f"Defined in slot file: {getattr(slot, 'definition_uri', 'N/A')}")
print()

# Check induced slots (how the slot would appear when used by a class)
print("Checking all classes for usage of this slot...")
print()

found_usage = False
for class_name in sorted(sv.all_classes()):
    cls_slots = sv.class_slots(class_name, direct=False)
    if slot_name in cls_slots:
        found_usage = True
        print(f"✓ Used by class: {class_name}")

if not found_usage:
    print("❌ NOT USED by any class - this is an orphaned slot definition")
    print()
    print("This slot is defined but not referenced in any class's 'slots' list,")
    print("nor inherited, nor used in any slot_usage.")
