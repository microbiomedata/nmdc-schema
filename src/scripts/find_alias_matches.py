#!/usr/bin/env python3
"""
Script to find schema elements where the name matches one of their aliases.
"""

import click
from linkml_runtime import SchemaView


@click.command()
@click.option('--schema-file', default='src/schema/nmdc.yaml', help='Schema file path.')
def find_alias_matches(schema_file):
    """
    Find schema elements where the name matches one of their aliases.
    """
    schema_view = SchemaView(schema_file)
    
    click.echo("Checking for elements where name matches aliases...")
    click.echo("=" * 60)
    
    matches_found = False
    
    # Check all elements using all_elements method
    for element_name in schema_view.all_elements():
        element_def = schema_view.get_element(element_name)
        
        # Skip elements from mixs.yaml
        if (hasattr(element_def, 'from_schema') and 
            element_def.from_schema == 'https://raw.githubusercontent.com/microbiomedata/nmdc-schema/main/src/schema/mixs.yaml'):
            continue
            
        if element_def.aliases:
            if element_name in element_def.aliases:
                print(f"{element_name} (aliases: {element_def.aliases})")
                matches_found = True
    
    print("\n" + "=" * 60)
    if not matches_found:
        print("No elements found where name matches an alias.")
    else:
        print("Found elements where name matches an alias (listed above).")


if __name__ == '__main__':
    find_alias_matches()