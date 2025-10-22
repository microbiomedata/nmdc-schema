#!/usr/bin/env python3
"""
Find NMDC elements that share names with LinkML elements but are defined in NMDC modules.
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

# Find shared names where LinkML defines it but NMDC redefines it
redefined = []

for name in sorted(set(no_orphans.keys()) & set(nmdc_base.keys())):
    linkml_from = no_orphans[name]['from_schema']
    nmdc_from = nmdc_base[name]['from_schema']
    
    # Check if LinkML defines it (from linkml namespace)
    # and NMDC redefines it (from nmdc namespace)
    if linkml_from.startswith('https://w3id.org/linkml/') and \
       nmdc_from.startswith('https://w3id.org/nmdc/'):
        
        linkml_type = no_orphans[name]['type']
        nmdc_type = nmdc_base[name]['type']
        type_match = linkml_type == nmdc_type
        
        redefined.append({
            'name': name,
            'linkml_type': linkml_type,
            'nmdc_type': nmdc_type,
            'type_match': type_match,
            'linkml_schema': linkml_from.replace('https://w3id.org/', ''),
            'nmdc_schema': nmdc_from.replace('https://w3id.org/', '')
        })

print("=" * 120)
print("NMDC ELEMENTS THAT SHARE NAMES WITH LINKML BUT ARE DEFINED IN NMDC MODULES")
print("=" * 120)
print(f"\nFound {len(redefined)} elements where NMDC redefines a LinkML element name\n")

# Separate by type match
matching_types = [r for r in redefined if r['type_match']]
conflicting_types = [r for r in redefined if not r['type_match']]

if conflicting_types:
    print("=" * 120)
    print(f"NAMING CONFLICTS (Different Element Types): {len(conflicting_types)}")
    print("=" * 120)
    print(f"{'Element':<20} {'LinkML Type':<25} {'NMDC Type':<25} {'LinkML Module':<30} {'NMDC Module'}")
    print("-" * 120)
    for r in conflicting_types:
        print(f"{r['name']:<20} {r['linkml_type']:<25} {r['nmdc_type']:<25} {r['linkml_schema']:<30} {r['nmdc_schema']}")
    print()

if matching_types:
    print("=" * 120)
    print(f"INTENTIONAL REDEFINITIONS (Same Element Type): {len(matching_types)}")
    print("=" * 120)
    print(f"{'Element':<20} {'Type':<25} {'LinkML Module':<35} {'NMDC Module'}")
    print("-" * 120)
    for r in matching_types:
        print(f"{r['name']:<20} {r['linkml_type']:<25} {r['linkml_schema']:<35} {r['nmdc_schema']}")

# Generate summary table
print("\n" + "=" * 120)
print("SUMMARY BY NMDC MODULE")
print("=" * 120)

from collections import defaultdict
by_nmdc_module = defaultdict(list)
for r in redefined:
    by_nmdc_module[r['nmdc_schema']].append(r)

for module in sorted(by_nmdc_module.keys()):
    elements = by_nmdc_module[module]
    conflicts = sum(1 for e in elements if not e['type_match'])
    print(f"\n{module}: {len(elements)} redefinitions ({conflicts} conflicts)")
    for e in elements:
        conflict_marker = " ⚠️ CONFLICT" if not e['type_match'] else ""
        print(f"  - {e['name']} ({e['nmdc_type']} from {e['linkml_schema']}){conflict_marker}")

