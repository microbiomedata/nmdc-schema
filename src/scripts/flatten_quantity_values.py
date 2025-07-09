#!/usr/bin/env python3
"""
Script to flatten nmdc:QuantityValue structures from Biosample-possibly-exhaustive.yaml
to TSV format with specified columns.
"""

import yaml
import csv
import sys
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

def main():
    input_file = '../data/valid/Biosample-possibly-exhaustive.yaml'
    output_file = '../../quantity_values.tsv'
    
    # Read YAML file
    try:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)
    
    # Extract QuantityValue structures
    quantity_values = extract_quantity_values(data)
    
    if not quantity_values:
        print("No QuantityValue structures found in the file")
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
        
        print(f"Successfully extracted {len(quantity_values)} QuantityValue structures to {output_file}")
        
        # Print summary
        print("\nSummary:")
        print(f"Total QuantityValue fields found: {len(quantity_values)}")
        print(f"Fields with has_numeric_value: {sum(1 for qv in quantity_values if qv['has_numeric_value'])}")
        print(f"Fields with has_unit: {sum(1 for qv in quantity_values if qv['has_unit'])}")
        print(f"Fields with has_raw_value: {sum(1 for qv in quantity_values if qv['has_raw_value'])}")
        print(f"Fields with has_maximum_numeric_value: {sum(1 for qv in quantity_values if qv['has_maximum_numeric_value'])}")
        print(f"Fields with has_minimum_numeric_value: {sum(1 for qv in quantity_values if qv['has_minimum_numeric_value'])}")
        
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()