#!/usr/bin/env python3
"""
List NMDC elements that redefine LinkML element names.
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
    
    if linkml_from.startswith('https://w3id.org/linkml/') and \
       nmdc_from.startswith('https://w3id.org/nmdc/'):
        redefined.append(name)

print("NMDC elements that redefine LinkML element names:")
print()
for name in redefined:
    print(name)
print()
print(f"Total: {len(redefined)} elements")
