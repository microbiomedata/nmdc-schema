#!/usr/bin/env python3
"""
Find orphaned elements in a LinkML schema using SchemaView's specialized methods.
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView

if len(sys.argv) < 2:
    print("Usage: python find_orphans.py <schema_path>")
    sys.exit(1)

schema_path = sys.argv[1]
sv = SchemaView(schema_path)

print("Analyzing schema for orphaned elements...")
print("=" * 80)
print()

# Find orphaned slots (slots not used by any class)
orphan_slots = []
for slot_name in sv.all_slots():
    slot = sv.get_slot(slot_name)
    classes = sv.get_classes_by_slot(slot, include_induced=True)
    if not classes:
        orphan_slots.append((slot_name, slot))

# Find orphaned enums (enums not used in any slot range)
orphan_enums = []
for enum_name in sv.all_enums():
    slots = sv.get_slots_by_enum(enum_name)
    if not slots:
        enum = sv.get_enum(enum_name)
        orphan_enums.append((enum_name, enum))

# Find orphaned types (types not used in any slot range)
types_in_use = set()
for slot_name in sv.all_slots():
    slot = sv.get_slot(slot_name)
    if slot.range and slot.range in sv.all_types():
        types_in_use.add(slot.range)

orphan_types = []
for type_name in sv.all_types():
    if type_name not in types_in_use:
        type_def = sv.get_type(type_name)
        orphan_types.append((type_name, type_def))

# Find unreferenced classes (classes not used in any slot range)
classes_in_use = set()
for slot_name in sv.all_slots():
    slot = sv.get_slot(slot_name)
    if slot.range and slot.range in sv.all_classes():
        classes_in_use.add(slot.range)

unreferenced_classes = []
for class_name in sv.all_classes():
    if class_name not in classes_in_use:
        cls = sv.get_class(class_name)
        unreferenced_classes.append((class_name, cls))

# Report results
if orphan_slots:
    print(f"ORPHANED SLOTS: {len(orphan_slots)}")
    print("=" * 80)
    print("Slots not used by any class:")
    print()
    for slot_name, slot in sorted(orphan_slots):
        from_schema = (slot.from_schema or 'unknown').replace('https://w3id.org/', '')
        range_val = slot.range or 'no range'
        print(f"  {slot_name:<40} range: {range_val:<30} from: {from_schema}")
    print()
else:
    print("✓ No orphaned slots")
    print()

if orphan_enums:
    print(f"ORPHANED ENUMS: {len(orphan_enums)}")
    print("=" * 80)
    print("Enums not used as the range of any slot:")
    print()
    for enum_name, enum in sorted(orphan_enums):
        from_schema = (enum.from_schema or 'unknown').replace('https://w3id.org/', '')
        pv_count = len(enum.permissible_values) if enum.permissible_values else 0
        print(f"  {enum_name:<40} values: {pv_count:<5} from: {from_schema}")
    print()
else:
    print("✓ No orphaned enums")
    print()

if orphan_types:
    print(f"ORPHANED TYPES: {len(orphan_types)}")
    print("=" * 80)
    print("Types not used as the range of any slot:")
    print()
    for type_name, type_def in sorted(orphan_types):
        from_schema = (type_def.from_schema or 'unknown').replace('https://w3id.org/', '')
        typeof = type_def.typeof or 'base'
        print(f"  {type_name:<40} typeof: {typeof:<30} from: {from_schema}")
    print()
else:
    print("✓ No orphaned types")
    print()

if unreferenced_classes:
    print(f"UNREFERENCED CLASSES: {len(unreferenced_classes)}")
    print("=" * 80)
    print("Classes not used as the range of any slot.")
    print("(May be abstract, tree_root, or used in other contexts)")
    print()
    for class_name, cls in sorted(unreferenced_classes):
        from_schema = (cls.from_schema or 'unknown').replace('https://w3id.org/', '')
        flags = []
        if cls.abstract:
            flags.append("abstract")
        if cls.tree_root:
            flags.append("tree_root")
        if cls.is_a:
            flags.append(f"is_a:{cls.is_a}")
        flag_str = ", ".join(flags) if flags else "concrete"
        print(f"  {class_name:<40} {flag_str:<40} from: {from_schema}")
    print()
else:
    print("✓ All classes referenced in slot ranges")
    print()

# Summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total slots:    {len(list(sv.all_slots())):<6} Orphaned: {len(orphan_slots)}")
print(f"Total enums:    {len(list(sv.all_enums())):<6} Orphaned: {len(orphan_enums)}")
print(f"Total types:    {len(list(sv.all_types())):<6} Orphaned: {len(orphan_types)}")
print(f"Total classes:  {len(list(sv.all_classes())):<6} Unreferenced: {len(unreferenced_classes)}")
