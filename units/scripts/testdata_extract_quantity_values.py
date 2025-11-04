#!/usr/bin/env python3
"""
Script to flatten nmdc:QuantityValue structures from YAML files
to TSV format with specified columns.
"""

import yaml
import csv
import sys
import click
from pathlib import Path
from typing import Dict, Any, List

def extract_quantity_values(data: Dict[str, Any], parent_key: str = '') -> List[Dict[str, str]]:
    """Extract all QuantityValue structures from nested YAML data."""
    results = []
    
    for key, value in data.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        
        if isinstance(value, dict):
            if value.get('type') == 'nmdc:QuantityValue':
                # Extract QuantityValue fields
                qv_data = {
                    'field_name': current_key,
                    'has_maximum_numeric_value': str(value.get('has_maximum_numeric_value', '')),
                    'has_minimum_numeric_value': str(value.get('has_minimum_numeric_value', '')),
                    'has_numeric_value': str(value.get('has_numeric_value', '')),
                    'has_unit': str(value.get('has_unit', '')),
                    'has_raw_value': str(value.get('has_raw_value', '')),
                    'type': str(value.get('type', ''))
                }
                results.append(qv_data)
            else:
                # Recursively search nested dictionaries
                results.extend(extract_quantity_values(value, current_key))
        elif isinstance(value, list):
            # Handle lists of objects
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    if item.get('type') == 'nmdc:QuantityValue':
                        qv_data = {
                            'field_name': f"{current_key}[{i}]",
                            'has_maximum_numeric_value': str(item.get('has_maximum_numeric_value', '')),
                            'has_minimum_numeric_value': str(item.get('has_minimum_numeric_value', '')),
                            'has_numeric_value': str(item.get('has_numeric_value', '')),
                            'has_unit': str(item.get('has_unit', '')),
                            'has_raw_value': str(item.get('has_raw_value', '')),
                            'type': str(item.get('type', ''))
                        }
                        results.append(qv_data)
                    else:
                        results.extend(extract_quantity_values(item, f"{current_key}[{i}]"))
    
    return results

@click.command()
@click.option('--input', 'input_file', default='../src/data/valid/Biosample-possibly-exhaustive.yaml', 
              type=click.Path(exists=True, path_type=Path), 
              help='Input YAML file containing QuantityValue structures')
@click.option('--output', 'output_file', default='quantity_values.tsv',
              type=click.Path(path_type=Path),
              help='Output TSV file path')
def main(input_file, output_file):
    """Extract QuantityValue structures from YAML file to TSV format."""
    
    # Read YAML file
    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        click.echo(f"Error: File {input_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        click.echo(f"Error parsing YAML: {e}")
        sys.exit(1)
    
    # Extract QuantityValue structures
    quantity_values = extract_quantity_values(data)
    
    if not quantity_values:
        click.echo("No QuantityValue structures found in the file")
        sys.exit(0)
    
    # Define column headers
    headers = [
        'field_name',
        'has_maximum_numeric_value',
        'has_minimum_numeric_value',
        'has_numeric_value',
        'has_unit',
        'has_raw_value',
        'type'
    ]
    
    # Write to TSV file
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(quantity_values)
        
        click.echo(f"Extracted {len(quantity_values)} QuantityValue structures to {output_file}")
        
    except IOError as e:
        click.echo(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()