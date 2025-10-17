#!/usr/bin/env python3
"""
Compare LinkML schemas for metaslot usage.

Usage:
  # Compare two schemas
  poetry run python compare_linkml_schemas.py schema_a.yaml schema_b.yaml
  
  # Compare schema against directory of sources
  poetry run python compare_linkml_schemas.py materialized.yaml src/schema/
"""
import yaml
import sys
from pathlib import Path
from typing import Set
from linkml_runtime.utils.schemaview import SchemaView

def extract_all_keys(obj, keys_set: Set[str]):
    """Recursively extract all dictionary keys from a YAML structure."""
    if isinstance(obj, dict):
        keys_set.update(obj.keys())
        for value in obj.values():
            extract_all_keys(value, keys_set)
    elif isinstance(obj, list):
        for item in obj:
            extract_all_keys(item, keys_set)

def get_linkml_metamodel_slots() -> Set[str]:
    """Get all slot names from the LinkML metamodel."""
    metamodel_view = SchemaView("https://w3id.org/linkml/meta.yaml")
    return set(metamodel_view.all_slots().keys())

def get_linkml_builtin_types() -> Set[str]:
    """Get LinkML built-in types to exclude."""
    return {
        'string', 'integer', 'boolean', 'float', 'double', 
        'decimal', 'time', 'date', 'datetime', 'date_or_datetime',
        'uriorcurie', 'curie', 'uri', 'ncname', 'objectidentifier',
        'nodeidentifier', 'jsonpointer', 'jsonpath', 'sparqlpath'
    }

def extract_schema_keys(schema_path: str) -> Set[str]:
    """Extract all keys from a schema file."""
    with open(schema_path, 'r') as f:
        data = yaml.safe_load(f)
    keys = set()
    extract_all_keys(data, keys)
    return keys

def extract_keys_from_directory(directory: str) -> Set[str]:
    """Extract all keys from all YAML files in a directory."""
    all_keys = set()
    yaml_files = list(Path(directory).glob("*.yaml"))
    
    print(f"Found {len(yaml_files)} YAML files in {directory}", file=sys.stderr)
    for yaml_file in yaml_files:
        keys = extract_schema_keys(str(yaml_file))
        all_keys.update(keys)
    
    return all_keys

def filter_to_metaslots(keys: Set[str], metaslots: Set[str]) -> Set[str]:
    """Filter keys to only those that are valid LinkML metaslots."""
    filtered = keys & metaslots
    builtin_types = get_linkml_builtin_types()
    return filtered - builtin_types

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare_linkml_schemas.py <schema_a> <schema_b_or_dir>")
        sys.exit(1)
    
    schema_a = sys.argv[1]
    schema_b_or_dir = sys.argv[2]
    
    print("Loading LinkML metamodel...", file=sys.stderr)
    metaslots = get_linkml_metamodel_slots()
    print(f"Found {len(metaslots)} metaslots in LinkML metamodel\n", file=sys.stderr)
    
    print(f"Extracting keys from {schema_a}...", file=sys.stderr)
    keys_a = extract_schema_keys(schema_a)
    print(f"Found {len(keys_a)} total keys\n", file=sys.stderr)
    
    # Check if schema_b_or_dir is a directory or file
    if Path(schema_b_or_dir).is_dir():
        print(f"Extracting keys from {schema_b_or_dir}/*.yaml...", file=sys.stderr)
        keys_b = extract_keys_from_directory(schema_b_or_dir)
        schema_b_label = f"{schema_b_or_dir}/*.yaml"
    else:
        print(f"Extracting keys from {schema_b_or_dir}...", file=sys.stderr)
        keys_b = extract_schema_keys(schema_b_or_dir)
        schema_b_label = schema_b_or_dir
    
    print(f"Found {len(keys_b)} total keys\n", file=sys.stderr)
    
    metaslots_a = filter_to_metaslots(keys_a, metaslots)
    metaslots_b = filter_to_metaslots(keys_b, metaslots)
    
    print(f"{len(metaslots_a)} metaslots in schema A", file=sys.stderr)
    print(f"{len(metaslots_b)} metaslots in schema B\n", file=sys.stderr)
    
    only_in_a = metaslots_a - metaslots_b
    only_in_b = metaslots_b - metaslots_a
    in_both = metaslots_a & metaslots_b
    
    print("="*70)
    print(f"METASLOTS ONLY IN {schema_a}:")
    print("="*70)
    for slot in sorted(only_in_a):
        print(f"  {slot}")
    
    print(f"\n{'='*70}")
    print(f"METASLOTS ONLY IN {schema_b_label}:")
    print("="*70)
    for slot in sorted(only_in_b):
        print(f"  {slot}")
    
    print(f"\n({len(in_both)} metaslots appear in both)")
