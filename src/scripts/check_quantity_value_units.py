#!/usr/bin/env python3
"""
Script to check QuantityValue fields for missing has_unit fields.
"""

import click
import yaml
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
def main(file_path):
    """
    Check a YAML file for QuantityValue entries missing has_unit fields.
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        click.echo(f"Error: File {file_path} does not exist")
        return
    
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    missing_units = check_quantity_value_units(data)
    
    if missing_units:
        click.echo(f"Found {len(missing_units)} QuantityValue entries missing has_unit:")
        click.echo("=" * 60)
        for entry in missing_units:
            click.echo(f"Path: {entry['path']}")
            click.echo(f"Raw value: {entry['has_raw_value']}")
            click.echo("-" * 40)
    else:
        click.echo("✅ All QuantityValue entries have has_unit fields!")


if __name__ == '__main__':
    main()