#!/usr/bin/env python3
"""
Inspect what usage_index() actually returns.
"""
from linkml_runtime.utils.schemaview import SchemaView

sv = SchemaView("src/schema/nmdc.yaml")
usage_idx = sv.usage_index()

print("Sample usage_index entries:")
print("=" * 80)

# Show a few entries
count = 0
for element_name, usage in list(usage_idx.items())[:5]:
    print(f"\nElement: {element_name}")
    print(f"  Type: {type(usage)}")
    print(f"  Attributes: {dir(usage)}")
    if hasattr(usage, '__dict__'):
        print(f"  Dict: {usage.__dict__}")
    count += 1

print(f"\n\nTotal entries in usage_index: {len(usage_idx)}")

# Check a specific slot we know is used
if 'id' in usage_idx:
    print(f"\nLooking at 'id' slot (known to be used):")
    print(f"  {usage_idx['id']}")
    if hasattr(usage_idx['id'], '__dict__'):
        print(f"  Dict: {usage_idx['id'].__dict__}")
