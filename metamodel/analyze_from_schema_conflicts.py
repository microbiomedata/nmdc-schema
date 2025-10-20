#!/usr/bin/env python3
"""
Analyze shared elements to find those defined in different schemas.
"""
import csv
import sys

# Read both TSV files
no_orphans = {}
with open('metamodel/no_orphans_elements.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        no_orphans[row['name']] = row

nmdc = {}
with open('metamodel/nmdc_elements.tsv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        nmdc[row['name']] = row

# Find shared names
shared_names = set(no_orphans.keys()) & set(nmdc.keys())

# Analyze from_schema conflicts
same_schema = []
different_schema = []

for name in sorted(shared_names):
    no_from = no_orphans[name]['from_schema']
    nmdc_from = nmdc[name]['from_schema']
    
    if no_from == nmdc_from:
        same_schema.append((name, no_from, no_orphans[name]['type'], nmdc[name]['type']))
    else:
        different_schema.append((name, no_from, nmdc_from, no_orphans[name]['type'], nmdc[name]['type']))

print("=" * 80)
print(f"SHARED ELEMENTS DEFINED IN SAME SCHEMA: {len(same_schema)}")
print("=" * 80)
if same_schema:
    print(f"{'Element':<25} {'From Schema':<45} {'Type Match'}")
    print("-" * 80)
    for name, from_schema, no_type, nmdc_type in same_schema:
        match = "✓" if no_type == nmdc_type else "✗"
        print(f"{name:<25} {from_schema:<45} {match}")

print("\n" + "=" * 80)
print(f"SHARED ELEMENTS DEFINED IN DIFFERENT SCHEMAS: {len(different_schema)}")
print("=" * 80)
if different_schema:
    print(f"{'Element':<15} {'No Orphans Schema':<35} {'NMDC Schema':<35} {'Types Match'}")
    print("-" * 100)
    for name, no_from, nmdc_from, no_type, nmdc_type in different_schema:
        match = "✓" if no_type == nmdc_type else "✗"
        # Truncate long schema URIs for readability
        no_from_short = no_from.replace('https://w3id.org/', '')
        nmdc_from_short = nmdc_from.replace('https://w3id.org/', '')
        print(f"{name:<15} {no_from_short:<35} {nmdc_from_short:<35} {match}")
        if no_type != nmdc_type:
            print(f"{'':15} {no_type:<35} {nmdc_type:<35}")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total shared elements: {len(shared_names)}")
print(f"Defined in same schema: {len(same_schema)} ({len(same_schema)*100//len(shared_names)}%)")
print(f"Defined in different schemas: {len(different_schema)} ({len(different_schema)*100//len(shared_names)}%)")
