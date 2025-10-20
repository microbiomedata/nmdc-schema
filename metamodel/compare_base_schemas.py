#!/usr/bin/env python3
"""
Compare shared elements between no_orphans and base nmdc.yaml schemas.
"""
import csv

# Read both TSV files
no_orphans = {}
with open('metamodel/no_orphans_elements.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        no_orphans[row['name']] = row

nmdc_base = {}
with open('metamodel/nmdc_base_elements.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        nmdc_base[row['name']] = row

# Find shared names
shared_names = set(no_orphans.keys()) & set(nmdc_base.keys())

# Categorize
same_schema = []
different_schema = []

for name in sorted(shared_names):
    no_from = no_orphans[name]['from_schema']
    nmdc_from = nmdc_base[name]['from_schema']
    
    if no_from == nmdc_from:
        same_schema.append((name, no_from, no_orphans[name]['type'], nmdc_base[name]['type']))
    else:
        different_schema.append((name, no_from, nmdc_from, no_orphans[name]['type'], nmdc_base[name]['type']))

print("=" * 100)
print(f"COMPARISON: no_orphans.yaml vs nmdc.yaml (base schema with imports)")
print("=" * 100)
print(f"Total shared element names: {len(shared_names)}")
print(f"Same from_schema: {len(same_schema)} ({len(same_schema)*100//len(shared_names) if shared_names else 0}%)")
print(f"Different from_schema: {len(different_schema)} ({len(different_schema)*100//len(shared_names) if shared_names else 0}%)")
print()

if same_schema:
    print("=" * 100)
    print(f"ELEMENTS DEFINED IN SAME SCHEMA: {len(same_schema)}")
    print("=" * 100)
    print(f"{'Element':<25} {'From Schema':<50} {'Match'}")
    print("-" * 100)
    for name, from_schema, no_type, nmdc_type in same_schema[:20]:  # Show first 20
        match = "✓" if no_type == nmdc_type else "✗"
        schema_short = from_schema.replace('https://w3id.org/', '')
        print(f"{name:<25} {schema_short:<50} {match}")
    if len(same_schema) > 20:
        print(f"... and {len(same_schema) - 20} more")
    print()

if different_schema:
    print("=" * 100)
    print(f"ELEMENTS DEFINED IN DIFFERENT SCHEMAS: {len(different_schema)}")
    print("=" * 100)
    print(f"{'Element':<20} {'No Orphans Schema':<40} {'NMDC Schema':<40} {'Match'}")
    print("-" * 100)
    for name, no_from, nmdc_from, no_type, nmdc_type in different_schema:
        match = "✓" if no_type == nmdc_type else "✗"
        no_from_short = no_from.replace('https://w3id.org/', '')
        nmdc_from_short = nmdc_from.replace('https://w3id.org/', '')
        print(f"{name:<20} {no_from_short:<40} {nmdc_from_short:<40} {match}")
        if no_type != nmdc_type:
            print(f"{'':20} {no_type:<40} {nmdc_type:<40}")
