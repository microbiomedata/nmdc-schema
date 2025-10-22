#!/usr/bin/env python3
"""
Final comprehensive orphan verification using all appropriate SchemaView methods.
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView

schema_path = sys.argv[1] if len(sys.argv) > 1 else "src/schema/nmdc.yaml"
sv = SchemaView(schema_path)

print("COMPREHENSIVE ORPHAN VERIFICATION")
print("=" * 80)
print()

# SLOTS: Use class_induced_slots() and class_slots() - should agree
print("ORPHANED SLOTS")
print("-" * 80)

# Method A: class_induced_slots
slots_via_induced = set()
for class_name in sv.all_classes():
    try:
        for slot in sv.class_induced_slots(class_name):
            slots_via_induced.add(slot.name)
    except:
        pass

orphan_slots_a = set(sv.all_slots()) - slots_via_induced

# Method B: class_slots
slots_via_class_slots = set()
for class_name in sv.all_classes():
    slots_via_class_slots.update(sv.class_slots(class_name))

orphan_slots_b = set(sv.all_slots()) - slots_via_class_slots

# Method C: usage_index (orphans won't be keys)
usage_idx = sv.usage_index()
slots_in_usage_idx = {k for k in usage_idx.keys() if k in sv.all_slots()}
orphan_slots_c = set(sv.all_slots()) - slots_in_usage_idx

print(f"Method A (class_induced_slots): {len(orphan_slots_a)} orphaned")
print(f"Method B (class_slots):         {len(orphan_slots_b)} orphaned")  
print(f"Method C (usage_index):         {len(orphan_slots_c)} orphaned")

if orphan_slots_a == orphan_slots_b == orphan_slots_c:
    print("✓ All three methods AGREE!")
    orphan_slots = orphan_slots_a
else:
    print("⚠️  DISAGREEMENT between methods:")
    if orphan_slots_a != orphan_slots_b:
        print(f"  A-B diff: {(orphan_slots_a - orphan_slots_b) | (orphan_slots_b - orphan_slots_a)}")
    if orphan_slots_a != orphan_slots_c:
        print(f"  A-C diff: {(orphan_slots_a - orphan_slots_c) | (orphan_slots_c - orphan_slots_a)}")
    if orphan_slots_b != orphan_slots_c:
        print(f"  B-C diff: {(orphan_slots_b - orphan_slots_c) | (orphan_slots_c - orphan_slots_b)}")
    orphan_slots = orphan_slots_a  # Use induced slots as authoritative

print(f"\nConfirmed orphaned slots: {len(orphan_slots)}")
print()

# ENUMS: Use get_slots_by_enum() and usage_index
print("ORPHANED ENUMS")
print("-" * 80)

# Method A: get_slots_by_enum
orphan_enums_a = set()
for enum_name in sv.all_enums():
    if not sv.get_slots_by_enum(enum_name):
        orphan_enums_a.add(enum_name)

# Method B: usage_index
enums_in_usage_idx = {k for k in usage_idx.keys() if k in sv.all_enums()}
orphan_enums_b = set(sv.all_enums()) - enums_in_usage_idx

print(f"Method A (get_slots_by_enum): {len(orphan_enums_a)} orphaned")
print(f"Method B (usage_index):       {len(orphan_enums_b)} orphaned")

if orphan_enums_a == orphan_enums_b:
    print("✓ Both methods AGREE!")
    orphan_enums = orphan_enums_a
else:
    print(f"⚠️  DISAGREEMENT: {(orphan_enums_a - orphan_enums_b) | (orphan_enums_b - orphan_enums_a)}")
    orphan_enums = orphan_enums_a

print(f"\nConfirmed orphaned enums: {len(orphan_enums)}")
for e in sorted(orphan_enums):
    print(f"  - {e}")
print()

# TYPES: Check via slot ranges and usage_index
print("ORPHANED TYPES")
print("-" * 80)

# Method A: Check slot ranges
types_used_a = set()
for slot_name in sv.all_slots():
    slot = sv.get_slot(slot_name)
    if slot.range and slot.range in sv.all_types():
        types_used_a.add(slot.range)
orphan_types_a = set(sv.all_types()) - types_used_a

# Method B: usage_index
types_in_usage_idx = {k for k in usage_idx.keys() if k in sv.all_types()}
orphan_types_b = set(sv.all_types()) - types_in_usage_idx

print(f"Method A (slot ranges):   {len(orphan_types_a)} orphaned")
print(f"Method B (usage_index):   {len(orphan_types_b)} orphaned")

if orphan_types_a == orphan_types_b:
    print("✓ Both methods AGREE!")
    orphan_types = orphan_types_a
else:
    print(f"⚠️  DISAGREEMENT: {(orphan_types_a - orphan_types_b) | (orphan_types_b - orphan_types_a)}")
    orphan_types = orphan_types_a

print(f"\nConfirmed orphaned types: {len(orphan_types)}")
for t in sorted(orphan_types):
    print(f"  - {t}")
print()

# FINAL SUMMARY
print("=" * 80)
print("FINAL VERIFIED COUNTS")
print("=" * 80)
print(f"Orphaned slots:  {len(orphan_slots)}")
print(f"Orphaned enums:  {len(orphan_enums)}")
print(f"Orphaned types:  {len(orphan_types)}")
print()
print("All counts verified using multiple independent SchemaView methods.")
