#!/usr/bin/env python3
"""
Production Units Validation

This script validates production MongoDB data against storage_units constraints.
It provides comprehensive analysis similar to SPARQL queries but using simple YAML processing.

Input: MongoDB production data dump (local/mongo_via_api_as_unvalidated_nmdc_database.yaml)
Output: Validation report showing compliance with storage_units annotations

Usage:
    python validate_production_units.py --input ../local/mongo_via_api_as_unvalidated_nmdc_database.yaml --output validation_report.tsv

This combines:
- Production data coverage (like SPARQL approach)
- Simple YAML processing (like test framework)
- No RDF conversion complexity
- Comprehensive statistical analysis
"""

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import yaml
import click
import csv
from collections import defaultdict, Counter

from linkml_runtime import SchemaView


class ProductionUnitsValidator:
    """Validates production QuantityValue units against storage_units constraints."""
    
    def __init__(self, schema_file: Path):
        """Initialize validator with schema."""
        self.schema_view = SchemaView(schema_file)
        self._slot_storage_units_cache = {}
        self._allowed_units = None
        
    @property
    def allowed_units(self) -> set:
        """Get all allowed units from UnitEnum."""
        if self._allowed_units is None:
            unit_enum = self.schema_view.get_enum("UnitEnum")
            if unit_enum and unit_enum.permissible_values:
                self._allowed_units = set(unit_enum.permissible_values.keys())
            else:
                self._allowed_units = set()
        return self._allowed_units
    
    def get_slot_storage_units(self, slot_name: str) -> Optional[List[str]]:
        """Get storage_units for a slot, handling pipe-separated multiple units."""
        if slot_name in self._slot_storage_units_cache:
            return self._slot_storage_units_cache[slot_name]

        slot = self.schema_view.get_slot(slot_name)
        if not slot or not slot.annotations:
            self._slot_storage_units_cache[slot_name] = None
            return None

        storage_units = None
        if "storage_units" in slot.annotations:
            annotation_obj = slot.annotations["storage_units"]
            if annotation_obj and hasattr(annotation_obj, "value"):
                # Split on pipes for multiple units
                storage_units = str(annotation_obj.value).split("|")

        self._slot_storage_units_cache[slot_name] = storage_units
        return storage_units

    def validate_has_unit_against_enum(self, has_unit: str) -> bool:
        """Check if a has_unit value exists in UnitEnum."""
        return has_unit in self.allowed_units

    def validate_has_unit_against_slot(
        self, has_unit: str, slot_name: str
    ) -> Tuple[bool, str]:
        """
        Check if a has_unit value is appropriate for the given slot.
        Returns (is_valid, message).
        """
        storage_units = self.get_slot_storage_units(slot_name)

        if storage_units is None:
            # No storage_units constraint, any valid unit is acceptable
            return True, f"No storage_units constraint for slot '{slot_name}'"

        if has_unit in storage_units:
            return True, f"Unit matches storage_units for slot '{slot_name}'"
        else:
            return (
                False,
                f"Unit '{has_unit}' not in allowed storage_units {storage_units} for slot '{slot_name}'",
            )

    def iter_quantity_values(self, data: Any, path: Optional[List[str]] = None):
        """Recursively yield QuantityValue objects from production data."""
        if path is None:
            path = []
        
        if isinstance(data, dict):
            if data.get("type") == "nmdc:QuantityValue":
                yield path, data
            else:
                # Recursively search nested dictionaries
                for key, value in data.items():
                    yield from self.iter_quantity_values(value, path + [key])
        elif isinstance(data, list):
            # Recursively search list items
            for i, item in enumerate(data):
                yield from self.iter_quantity_values(item, path + [str(i)])

    def extract_slot_from_path(self, path: List[str]) -> Optional[str]:
        """Extract slot name from the path to QuantityValue."""
        # The slot is typically the second-to-last element in the path
        # e.g., ['biosample_set', '0', 'temp', 'has_numeric_value'] -> 'temp'
        if len(path) >= 2:
            return path[-2]
        return None

    def analyze_production_data(self, yaml_file: Path) -> Dict[str, Any]:
        """Analyze production data and return validation results."""
        click.echo(f"Loading production data from {yaml_file}...")
        
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except Exception as e:
            click.echo(f"Error loading YAML file: {e}", err=True)
            sys.exit(1)
        
        results = {
            'total_quantity_values': 0,
            'enum_violations': [],
            'storage_units_violations': [],
            'valid_units': [],
            'slots_analyzed': Counter(),
            'units_by_slot': defaultdict(Counter),
            'collections_processed': []
        }
        
        # Process each collection in the MongoDB dump
        if isinstance(data, dict):
            for collection_name, collection_data in data.items():
                if collection_name.endswith('_set') and isinstance(collection_data, list):
                    results['collections_processed'].append(collection_name)
                    click.echo(f"  Processing {collection_name}: {len(collection_data)} documents")
                    
                    for path, qv_data in self.iter_quantity_values(collection_data):
                        results['total_quantity_values'] += 1
                        
                        # Extract has_unit
                        has_unit = qv_data.get('has_unit')
                        if not has_unit:
                            continue
                            
                        # Extract slot name from path
                        slot_name = self.extract_slot_from_path(path)
                        if not slot_name:
                            continue
                            
                        results['slots_analyzed'][slot_name] += 1
                        results['units_by_slot'][slot_name][has_unit] += 1
                        
                        # Validate against UnitEnum
                        if not self.validate_has_unit_against_enum(has_unit):
                            results['enum_violations'].append({
                                'collection': collection_name,
                                'path': '.'.join(path),
                                'slot': slot_name,
                                'has_unit': has_unit,
                                'issue': 'Unit not in UnitEnum'
                            })
                            continue
                        
                        # Validate against storage_units
                        is_valid, message = self.validate_has_unit_against_slot(has_unit, slot_name)
                        if not is_valid:
                            results['storage_units_violations'].append({
                                'collection': collection_name,
                                'path': '.'.join(path),
                                'slot': slot_name,
                                'has_unit': has_unit,
                                'storage_units': self.get_slot_storage_units(slot_name),
                                'issue': 'Unit not in storage_units constraint'
                            })
                        else:
                            results['valid_units'].append({
                                'collection': collection_name,
                                'slot': slot_name,
                                'has_unit': has_unit
                            })
        
        return results

    def generate_report(self, results: Dict[str, Any], output_file: Path):
        """Generate CSV report in mongodb-slots-to-units.csv format."""
        click.echo(f"Generating validation report: {output_file}")
        
        # Aggregate data in mongodb format: class, slot, label, storage_units, actual_unit, count
        aggregated_data = defaultdict(int)
        
        # Process all valid units
        for item in results['valid_units']:
            collection = item['collection']
            slot_name = item['slot']
            has_unit = item['has_unit']
            
            # Get storage_units for this slot
            storage_units = self.get_slot_storage_units(slot_name)
            storage_units_str = '|'.join(storage_units) if storage_units else ''
            
            # Map collection to schema class (simplified mapping)
            schema_class = f"https://w3id.org/nmdc/{collection.replace('_set', '').title()}"
            
            # Use slot name as property and label (simplified)
            property_uri = f"https://w3id.org/mixs/{slot_name}"
            label = slot_name
            
            # Create key for aggregation
            key = (schema_class, property_uri, label, storage_units_str, has_unit)
            aggregated_data[key] += 1
        
        # Process violations too (with empty storage_units)
        for violation in results['storage_units_violations']:
            collection = violation['collection']
            slot_name = violation['slot']
            has_unit = violation['has_unit']
            storage_units = violation['storage_units']
            
            schema_class = f"https://w3id.org/nmdc/{collection.replace('_set', '').title()}"
            property_uri = f"https://w3id.org/mixs/{slot_name}"
            label = slot_name
            storage_units_str = '|'.join(storage_units) if storage_units else ''
            
            key = (schema_class, property_uri, label, storage_units_str, has_unit)
            aggregated_data[key] += 1
        
        # Write CSV in mongodb format
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Header matching mongodb-slots-to-units.csv
            writer.writerow(['sc', 'p', 'l', 'su', 'u', 'count'])
            
            # Write aggregated data sorted by count (descending)
            for (sc, p, l, su, u), count in sorted(aggregated_data.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([sc, p, l, su, u, count])
        
        # Print summary to console
        click.echo(f"\nSummary:")
        click.echo(f"  Total unique slot-unit combinations: {len(aggregated_data)}")
        click.echo(f"  Total QuantityValue instances: {sum(aggregated_data.values())}")
        click.echo(f"  UnitEnum violations: {len(results['enum_violations'])}")
        click.echo(f"  storage_units violations: {len(results['storage_units_violations'])}")
        if results['enum_violations'] or results['storage_units_violations']:
            click.echo(f"  ⚠️  Found violations - check detailed output")
        else:
            click.echo(f"  ✅ All units valid")


@click.command()
@click.option('--input', type=click.Path(exists=True, path_type=Path), required=True,
              help='MongoDB production data YAML file (from project.Makefile)')
@click.option('--output', type=click.Path(path_type=Path), required=True,
              help='Output TSV file for validation report')
@click.option('--schema-file', type=click.Path(exists=True, path_type=Path),
              default=Path('../nmdc_schema/nmdc_materialized_patterns.yaml'),
              help='Schema file for validation')
def main(input: Path, output: Path, schema_file: Path):
    """Validate production MongoDB data against storage_units constraints.
    
    This provides comprehensive production analysis without SPARQL complexity.
    Use the MongoDB dump from: make local/mongo_via_api_as_unvalidated_nmdc_database.yaml
    """
    
    click.echo("Production Units Validation")
    click.echo("=" * 50)
    
    # Initialize validator
    validator = ProductionUnitsValidator(schema_file)
    
    # Analyze production data
    results = validator.analyze_production_data(input)
    
    # Generate report
    validator.generate_report(results, output)
    
    # Print summary
    click.echo("\nValidation Summary:")
    click.echo(f"  Total QuantityValues: {results['total_quantity_values']}")
    click.echo(f"  Collections processed: {len(results['collections_processed'])}")
    click.echo(f"  Unique slots: {len(results['slots_analyzed'])}")
    click.echo(f"  UnitEnum violations: {len(results['enum_violations'])}")
    click.echo(f"  storage_units violations: {len(results['storage_units_violations'])}")
    click.echo(f"  Valid units: {len(results['valid_units'])}")
    
    if results['enum_violations'] or results['storage_units_violations']:
        click.echo(f"\n⚠️  Issues found - see detailed report: {output}")
    else:
        click.echo(f"\n✅ All units valid - see full report: {output}")


if __name__ == "__main__":
    main()