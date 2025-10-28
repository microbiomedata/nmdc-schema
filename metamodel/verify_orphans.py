#!/usr/bin/env python3
"""
Verify orphan detection using orthogonal SchemaView methods.
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView

if len(sys.argv) < 2:
    print("Usage: python verify_orphans.py <schema_path>")
    sys.exit(1)

schema_path = sys.argv[1]
sv = SchemaView(schema_path)

print("VERIFICATION: Using orthogonal SchemaView methods")
print("=" * 80)
print()

# METHOD 1: Using usage_index() for comprehensive usage tracking
print("METHOD 1: Using usage_index()")
print("-" * 80)
usage_idx = sv.usage_index()

# Check slots
slots_in_usage_index = set()
for element_name, usage in usage_idx.items():
    # Check if this element is used as a slot
    if hasattr(usage, 'used_by') and usage.used_by:
        slots_in_usage_index.add(element_name)

all_slots = set(sv.all_slots())
orphan_slots_v1 = all_slots - slots_in_usage_index
print(f"Orphaned slots (via usage_index): {len(orphan_slots_v1)}")
if len(orphan_slots_v1) <= 10:
    for s in sorted(orphan_slots_v1):
        print(f"  - {s}")
print()

# METHOD 2: Using class_induced_slots() to check all slots including via slot_usage
print("METHOD 2: Using class_induced_slots()")
print("-" * 80)
slots_used_induced = set()
for class_name in sv.all_classes():
    try:
        induced_slots = sv.class_induced_slots(class_name)
        for slot in induced_slots:
            slots_used_induced.add(slot.name)
    except Exception as e:
        # Some classes may not have induced slots
        pass

orphan_slots_v2 = all_slots - slots_used_induced
print(f"Orphaned slots (via induced slots): {len(orphan_slots_v2)}")
if len(orphan_slots_v2) <= 10:
    for s in sorted(orphan_slots_v2):
        print(f"  - {s}")
print()

# METHOD 3: Using class_slots(direct=False) to catch inherited slots
print("METHOD 3: Using class_slots(direct=False, attributes=True)")
print("-" * 80)
slots_used_v3 = set()
for class_name in sv.all_classes():
    class_slot_names = sv.class_slots(class_name, direct=False, attributes=True)
    slots_used_v3.update(class_slot_names)

orphan_slots_v3 = all_slots - slots_used_v3
print(f"Orphaned slots (via class_slots): {len(orphan_slots_v3)}")
if len(orphan_slots_v3) <= 10:
    for s in sorted(orphan_slots_v3):
        print(f"  - {s}")
print()

# METHOD 4: Check if we're counting attributes vs slots correctly
print("METHOD 4: Distinguish between attributes and slots")
print("-" * 80)
all_slots_with_attrs = set(sv.all_slots(attributes=True))
all_slots_no_attrs = set(sv.all_slots(attributes=False))
attrs_only = all_slots_with_attrs - all_slots_no_attrs
print(f"Total elements returned by all_slots(attributes=True): {len(all_slots_with_attrs)}")
print(f"Total elements returned by all_slots(attributes=False): {len(all_slots_no_attrs)}")
print(f"Elements that are attributes only: {len(attrs_only)}")
if attrs_only and len(attrs_only) <= 10:
    print("Sample attributes:")
    for s in sorted(list(attrs_only)[:10]):
        print(f"  - {s}")
print()

# COMPARISON
print("=" * 80)
print("COMPARISON OF METHODS")
print("=" * 80)
print(f"Method 1 (usage_index):        {len(orphan_slots_v1)} orphaned slots")
print(f"Method 2 (induced_slots):      {len(orphan_slots_v2)} orphaned slots")
print(f"Method 3 (class_slots):        {len(orphan_slots_v3)} orphaned slots")
print()

# Find discrepancies
if orphan_slots_v2 != orphan_slots_v3:
    print("⚠️  DISCREPANCY between methods 2 and 3:")
    only_in_v2 = orphan_slots_v2 - orphan_slots_v3
    only_in_v3 = orphan_slots_v3 - orphan_slots_v2
    if only_in_v2:
        print(f"  Only in method 2: {only_in_v2}")
    if only_in_v3:
        print(f"  Only in method 3: {only_in_v3}")
else:
    print("✓ Methods 2 and 3 agree!")

# Verify enums using get_slots_by_enum
print()
print("=" * 80)
print("VERIFY ENUMS")
print("=" * 80)
orphan_enums_check = []
for enum_name in sv.all_enums():
    slots = sv.get_slots_by_enum(enum_name)
    if not slots:
        orphan_enums_check.append(enum_name)

print(f"Orphaned enums (via get_slots_by_enum): {len(orphan_enums_check)}")
for e in sorted(orphan_enums_check):
    print(f"  - {e}")
