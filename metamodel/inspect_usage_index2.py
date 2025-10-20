#!/usr/bin/env python3
from linkml_runtime.utils.schemaview import SchemaView

sv = SchemaView("src/schema/nmdc.yaml")
usage_idx = sv.usage_index()

# Look at what's in the lists
print("Inspecting usage_index list contents:")
print("=" * 80)

# Check 'id' which we know is used
if 'id' in usage_idx:
    print(f"\n'id' slot usage (length {len(usage_idx['id'])}):")
    for i, item in enumerate(usage_idx['id'][:3]):
        print(f"  [{i}] Type: {type(item)}, Value: {item}")

# Check 'value' which we know is orphaned  
if 'value' in usage_idx:
    print(f"\n'value' slot usage (length {len(usage_idx['value'])}):")
    for i, item in enumerate(usage_idx['value'][:3]):
        print(f"  [{i}] Type: {type(item)}, Value: {item}")
else:
    print("\n'value' slot NOT in usage_index")

# Check QuantityValue which is a class
if 'QuantityValue' in usage_idx:
    print(f"\nQuantityValue class usage (length {len(usage_idx['QuantityValue'])}):")
    for i, item in enumerate(usage_idx['QuantityValue'][:5]):
        print(f"  [{i}] Type: {type(item)}, Value: {item}")
