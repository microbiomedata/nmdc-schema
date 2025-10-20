#!/usr/bin/env python3
"""
Dump detailed information about a specific element from a schema.
"""
import sys
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.dumpers import yaml_dumper

if len(sys.argv) < 3:
    print("Usage: python dump_element.py <schema_path> <element_name>")
    sys.exit(1)

schema_path = sys.argv[1]
element_name = sys.argv[2]

sv = SchemaView(schema_path)
element = sv.get_element(element_name)

if element is None:
    print(f"Element '{element_name}' not found in schema")
    sys.exit(1)

print(f"Element: {element_name}")
print(f"Type: {type(element).__name__}")
print(f"From Schema: {getattr(element, 'from_schema', 'N/A')}")
print()
print("=" * 80)
print("YAML Representation:")
print("=" * 80)
print(yaml_dumper.dumps(element))
