#!/usr/bin/env python3
"""
Script to check QuantityValue fields for missing has_unit fields.
"""

import click
import yaml
import csv
from pathlib import Path


def check_quantity_value_units(data, path=""):
    """
    Recursively check for QuantityValue entries missing has_unit fields.
    """
    missing_units = []
    
    if isinstance(data, dict):
        if data.get('type') == 'nmdc:QuantityValue':
            if 'has_unit' not in data:
                missing_units.append({
                    'path': path,
                    'has_raw_value': data.get('has_raw_value', 'N/A')
                })
        
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            missing_units.extend(check_quantity_value_units(value, new_path))
    
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            missing_units.extend(check_quantity_value_units(item, new_path))
    
    return missing_units


@click.command()
@click.option('--file-path', default='src/data/valid/Biosample-possibly-exhaustive.yaml', help='Path to YAML file to check.')
@click.option('--output', 'output_file', default='output/testdata_has_unit_check.tsv', help='Output TSV file for results.')
def main(file_path, output_file):
    """
    Check a YAML file for QuantityValue entries missing has_unit fields.
    """
    file_path = Path(file_path)
    output_file = Path(output_file)
    
    if not file_path.exists():
        click.echo(f"Error: File {file_path} does not exist")
        return
    
    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    missing_units = check_quantity_value_units(data)
    
    # Write structured output
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['path', 'has_raw_value', 'status'])
        
        if missing_units:
            for entry in missing_units:
                writer.writerow([entry['path'], entry['has_raw_value'], 'missing_has_unit'])
        
        # Write summary row
        writer.writerow(['SUMMARY', f'{len(missing_units)} missing has_unit fields', 
                        'FAIL' if missing_units else 'PASS'])
    
    # Minimal console output
    if missing_units:
        click.echo(f"Found {len(missing_units)} QuantityValue entries missing has_unit - see {output_file}")
    else:
        click.echo(f"✅ All QuantityValue entries have has_unit fields - see {output_file}")


if __name__ == '__main__':
    main()