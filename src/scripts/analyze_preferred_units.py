#!/usr/bin/env python3
"""
Script to analyze NMDC schema for slots with preferred_unit annotations.

This script examines nmdc_materialized_patterns.yaml to find:
1. Global slot definitions with preferred_unit annotations
2. Slot usage within classes that have preferred_unit annotations

Generates a TSV report with slot name, context (global or class-specific), 
class name (if applicable), and preferred unit value.
"""

import yaml
import csv
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

def extract_examples_values(slot_data: Dict[str, Any]) -> str:
    """Extract examples values from slot data."""
    examples = slot_data.get('examples', [])
    if not examples:
        return ''
    
    example_values = []
    for example in examples:
        if isinstance(example, dict):
            value = example.get('value', '')
            if value:
                example_values.append(str(value))
        elif isinstance(example, str):
            example_values.append(example)
    
    return '; '.join(example_values)

def extract_preferred_units_from_slots(slots_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """Extract preferred_unit annotations from global slot definitions."""
    results = []
    
    for slot_name, slot_data in slots_data.items():
        if isinstance(slot_data, dict):
            annotations = slot_data.get('annotations', {})
            if 'preferred_unit' in annotations:
                preferred_unit_info = annotations['preferred_unit']
                unit_value = preferred_unit_info.get('value', '') if isinstance(preferred_unit_info, dict) else ''
                
                results.append({
                    'slot_name': slot_name,
                    'context': 'global',
                    'class_name': '',
                    'preferred_unit': unit_value,
                    'description': slot_data.get('description', ''),
                    'range': slot_data.get('range', ''),
                    'examples': extract_examples_values(slot_data)
                })
    
    return results

def extract_preferred_units_from_classes(classes_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """Extract preferred_unit annotations from slot_usage within classes."""
    results = []
    
    for class_name, class_data in classes_data.items():
        if isinstance(class_data, dict):
            slot_usage = class_data.get('slot_usage', {})
            if slot_usage:
                for slot_name, slot_usage_data in slot_usage.items():
                    if isinstance(slot_usage_data, dict):
                        annotations = slot_usage_data.get('annotations', {})
                        if 'preferred_unit' in annotations:
                            preferred_unit_info = annotations['preferred_unit']
                            unit_value = preferred_unit_info.get('value', '') if isinstance(preferred_unit_info, dict) else ''
                            
                            results.append({
                                'slot_name': slot_name,
                                'context': 'class_usage',
                                'class_name': class_name,
                                'preferred_unit': unit_value,
                                'description': slot_usage_data.get('description', ''),
                                'range': slot_usage_data.get('range', ''),
                                'examples': extract_examples_values(slot_usage_data)
                            })
    
    return results

def main():
    # File paths
    schema_file = Path('../../nmdc_schema/nmdc_materialized_patterns.yaml')
    output_file = Path('../../preferred_units_report.tsv')
    
    print(f"Analyzing schema file: {schema_file}")
    
    # Read YAML file
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Schema file {schema_file} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)
    
    # Extract preferred unit annotations
    print("Extracting preferred unit annotations...")
    
    # From global slots
    slots_data = schema_data.get('slots', {})
    global_units = extract_preferred_units_from_slots(slots_data)
    print(f"Found {len(global_units)} global slots with preferred_unit annotations")
    
    # From class slot_usage
    classes_data = schema_data.get('classes', {})
    class_usage_units = extract_preferred_units_from_classes(classes_data)
    print(f"Found {len(class_usage_units)} class slot_usage entries with preferred_unit annotations")
    
    # Combine results
    all_results = global_units + class_usage_units
    
    if not all_results:
        print("No preferred_unit annotations found in the schema")
        sys.exit(0)
    
    # Sort by slot name, then by context
    all_results.sort(key=lambda x: (x['slot_name'], x['context'], x['class_name']))
    
    # Define column headers
    headers = [
        'slot_name',
        'context',
        'class_name', 
        'preferred_unit',
        'description',
        'range',
        'examples'
    ]
    
    # Write to TSV file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(all_results)
        
        print(f"\\nSuccessfully wrote {len(all_results)} preferred unit annotations to {output_file}")
        
        # Print summary
        print("\\nSummary:")
        print(f"Total preferred_unit annotations found: {len(all_results)}")
        print(f"Global slot definitions: {len(global_units)}")
        print(f"Class slot_usage definitions: {len(class_usage_units)}")
        
        # Show unique units
        unique_units = set(result['preferred_unit'] for result in all_results if result['preferred_unit'])
        print(f"Unique preferred units found: {len(unique_units)}")
        
        # Show breakdown by context
        context_counts = {}
        for result in all_results:
            context = result['context']
            context_counts[context] = context_counts.get(context, 0) + 1
        
        print("\\nBreakdown by context:")
        for context, count in sorted(context_counts.items()):
            print(f"  {context}: {count}")
        
        # Show most common units
        unit_counts = {}
        for result in all_results:
            unit = result['preferred_unit']
            if unit:
                unit_counts[unit] = unit_counts.get(unit, 0) + 1
        
        print("\\nMost common preferred units:")
        sorted_units = sorted(unit_counts.items(), key=lambda x: x[1], reverse=True)
        for unit, count in sorted_units[:10]:  # Top 10
            print(f"  '{unit}': {count}")
        
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()