#!/usr/bin/env python3
"""
Iterate through all elements in a LinkML schema and print their names.

Uses SchemaView.all_elements() to access all elements at once.
"""

import click
import json
import sys
from pathlib import Path
from linkml_runtime.utils.schemaview import SchemaView


@click.command()
@click.option('--schema', '-s', required=True, help='Path or URL to schema file')
@click.option('--format', '-f', type=click.Choice(['tsv', 'json'], case_sensitive=False),
              default='tsv', help='Output format (default: tsv)')
@click.option('--output', '-o', type=click.File('w'), default=sys.stdout,
              help='Output file (default: stdout)')
def list_schema_elements(schema: str, format: str, output):
    """Print all element names in a schema."""

    sv = SchemaView(schema)

    elements = []
    for element_name in sorted(sv.all_elements()):
        element = sv.get_element(element_name)
        element_type = type(element).__name__

        # Get is_a parent if it exists
        is_a = getattr(element, 'is_a', None)

        # Get abstract flag if it exists
        abstract = getattr(element, 'abstract', None)

        # Get from_schema if it exists
        from_schema = getattr(element, 'from_schema', None)

        elements.append({
            'name': element_name,
            'type': element_type,
            'is_a': is_a if is_a else '',
            'abstract': abstract if abstract is not None else '',
            'from_schema': from_schema if from_schema else ''
        })

    if format == 'tsv':
        output.write("name\ttype\tis_a\tabstract\tfrom_schema\n")
        for elem in elements:
            output.write(f"{elem['name']}\t{elem['type']}\t{elem['is_a']}\t{elem['abstract']}\t{elem['from_schema']}\n")
    elif format == 'json':
        json.dump(elements, output, indent=2)
        output.write('\n')


if __name__ == '__main__':
    list_schema_elements()
