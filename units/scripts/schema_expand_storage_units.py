#!/usr/bin/env python3
"""
Script to expand pipe-concatenated storage_units annotations into separate rows.
"""

import click
import csv
import yaml
from pathlib import Path


@click.command()
@click.option('--schema-file', type=click.Path(exists=True, path_type=Path), 
              default='../nmdc_schema/nmdc_materialized_patterns.yaml',
              help='NMDC schema YAML file')
@click.option('--output', 'output_file', default='output/schema_storage_units_expanded.tsv',
              type=click.Path(path_type=Path),
              help='Output TSV file with expanded storage_units')
def main(schema_file, output_file):
    """
    Extract QuantityValue slots with storage_units and expand pipe-separated values.
    """
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(schema_file, 'r') as f:
        schema = yaml.safe_load(f)
    
    expanded_units = []
    
    # Extract slots with QuantityValue range and storage_units annotations
    slots = schema.get('slots', {})
    for slot_name, slot_def in slots.items():
        if (slot_def.get('range') == 'QuantityValue' and 
            'annotations' in slot_def and 
            'storage_units' in slot_def['annotations']):
            
            storage_units = slot_def['annotations']['storage_units']
            # Handle both string and dict annotation formats
            if isinstance(storage_units, dict):
                units_value = storage_units.get('value', '')
            else:
                units_value = str(storage_units)
            
            # Split pipe-separated units and create separate rows
            for unit in units_value.split('|'):
                unit = unit.strip()
                if unit:  # Skip empty units
                    expanded_units.append({
                        'slot': slot_name,
                        'storage_unit': unit
                    })
    
    # Write to TSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['slot', 'storage_unit'], delimiter='\t')
        writer.writeheader()
        writer.writerows(expanded_units)
    
    click.echo(f"Expanded {len(expanded_units)} slot-unit combinations to {output_file}")


if __name__ == '__main__':
    main()