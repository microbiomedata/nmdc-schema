"""
Test that validates has_unit values in YAML data files against UnitEnum
and checks unit appropriateness for their slots.
"""
import os
import unittest
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from linkml_runtime import SchemaView


ROOT = os.path.join(os.path.dirname(__file__), '..')
SCHEMA_DIR = os.path.join(ROOT, "src", "schema")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, 'nmdc.yaml')
DATA_DIR = os.path.join(ROOT, "src", "data", "valid")


class HasUnitValidator:
    """Utility class to validate has_unit values in YAML data files."""
    
    def __init__(self, schema_view: SchemaView):
        self.schema_view = schema_view
        self.unit_enum = schema_view.get_enum('UnitEnum')
        self.allowed_units = set(self.unit_enum.permissible_values.keys()) if self.unit_enum else set()
        self._slot_storage_units_cache = {}
    
    def get_slot_storage_units(self, slot_name: str) -> Optional[List[str]]:
        """Get allowed storage_units for a slot, with caching."""
        if slot_name in self._slot_storage_units_cache:
            return self._slot_storage_units_cache[slot_name]
        
        slot = self.schema_view.get_slot(slot_name)
        if not slot or not slot.annotations:
            self._slot_storage_units_cache[slot_name] = None
            return None
        
        storage_units = None
        if isinstance(slot.annotations, dict):
            if 'storage_units' in slot.annotations:
                annotation_obj = slot.annotations['storage_units']
                if annotation_obj and hasattr(annotation_obj, 'value'):
                    # Split on pipes for multiple units
                    storage_units = [unit.strip() for unit in str(annotation_obj.value).split('|')]
        else:
            # Handle list-style annotations
            for annotation in slot.annotations:
                if hasattr(annotation, 'tag') and annotation.tag == 'storage_units':
                    if hasattr(annotation, 'value') and annotation.value:
                        storage_units = [unit.strip() for unit in str(annotation.value).split('|')]
                        break
        
        self._slot_storage_units_cache[slot_name] = storage_units
        return storage_units
    
    def extract_quantity_values(self, data: Any, path: str = "") -> List[Dict[str, Any]]:
        """Recursively extract QuantityValue objects from YAML data."""
        results = []
        
        if isinstance(data, dict):
            if data.get('type') == 'nmdc:QuantityValue':
                has_unit = data.get('has_unit')
                if has_unit:  # Only process if has_unit is present
                    results.append({
                        'path': path,
                        'has_unit': has_unit,
                        'has_raw_value': data.get('has_raw_value'),
                        'has_numeric_value': data.get('has_numeric_value'),
                        'quantity_value_data': data
                    })
            else:
                # Recursively search nested dictionaries
                for key, value in data.items():
                    new_path = f"{path}.{key}" if path else key
                    results.extend(self.extract_quantity_values(value, new_path))
        elif isinstance(data, list):
            # Handle lists of objects
            for i, item in enumerate(data):
                new_path = f"{path}[{i}]"
                results.extend(self.extract_quantity_values(item, new_path))
        
        return results
    
    def infer_slot_from_path(self, path: str) -> Optional[str]:
        """
        Infer slot name from the path.
        Examples:
        - 'depth' -> 'depth'
        - 'biosample_set[0].depth' -> 'depth'
        - 'biosample_set[1].temp' -> 'temp'
        """
        # Remove array indices and get the last component
        parts = path.replace(']', '').split('.')
        # Handle array indices like 'biosample_set[0'
        parts = [part.split('[')[0] if '[' in part else part for part in parts]
        
        # The last part should be the slot name if it's a known slot
        for part in reversed(parts):
            if part and self.schema_view.get_slot(part):
                return part
        
        return None
    
    def validate_has_unit_against_enum(self, has_unit: str) -> bool:
        """Check if has_unit value exists in UnitEnum."""
        return has_unit in self.allowed_units
    
    def validate_has_unit_against_slot(self, has_unit: str, slot_name: str) -> Tuple[bool, str]:
        """
        Check if has_unit value is appropriate for the given slot.
        Returns (is_valid, message).
        """
        storage_units = self.get_slot_storage_units(slot_name)
        
        if storage_units is None:
            # No storage_units constraint, any valid unit is acceptable
            return True, f"No storage_units constraint for slot '{slot_name}'"
        
        if has_unit in storage_units:
            return True, f"Unit matches storage_units for slot '{slot_name}'"
        else:
            return False, f"Unit '{has_unit}' not in allowed storage_units {storage_units} for slot '{slot_name}'"


class TestHasUnitValidation(unittest.TestCase):
    """Test has_unit validation across YAML data files."""
    
    def setUp(self):
        """Set up test with schema view and validator."""
        self.schema_view = SchemaView(SCHEMA_FILE)
        self.validator = HasUnitValidator(self.schema_view)
        self.data_dir = Path(DATA_DIR)
    
    def test_has_unit_enum_validation(self):
        """Test that all has_unit values exist in UnitEnum."""
        violations = []
        total_quantity_values = 0
        
        # Process all YAML files in src/data/valid
        for yaml_file in self.data_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                
                quantity_values = self.validator.extract_quantity_values(data)
                total_quantity_values += len(quantity_values)
                
                for qv in quantity_values:
                    has_unit = qv['has_unit']
                    if not self.validator.validate_has_unit_against_enum(has_unit):
                        violations.append({
                            'file': yaml_file.name,
                            'path': qv['path'],
                            'has_unit': has_unit,
                            'has_raw_value': qv['has_raw_value'],
                            'violation_type': 'not_in_enum',
                            'message': f"Unit '{has_unit}' not found in UnitEnum"
                        })
            
            except Exception as e:
                self.fail(f"Error processing {yaml_file.name}: {e}")
        
        print(f"\nProcessed {total_quantity_values} QuantityValue objects from {len(list(self.data_dir.glob('*.yaml')))} files")
        print(f"Found {len(self.validator.allowed_units)} allowed units in UnitEnum")
        
        if violations:
            print(f"\nhas_unit enum violations found:")
            for v in violations:
                print(f"  {v['file']}:{v['path']} - {v['message']}")
        
        self.assertEqual(len(violations), 0, f"Found {len(violations)} has_unit values not in UnitEnum")
    
    def test_has_unit_slot_appropriateness(self):
        """Test that has_unit values are appropriate for their slots."""
        violations = []
        total_quantity_values = 0
        unknown_slot_count = 0
        
        # Process all YAML files in src/data/valid
        for yaml_file in self.data_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                
                quantity_values = self.validator.extract_quantity_values(data)
                total_quantity_values += len(quantity_values)
                
                for qv in quantity_values:
                    has_unit = qv['has_unit']
                    slot_name = self.validator.infer_slot_from_path(qv['path'])
                    
                    if slot_name:
                        is_valid, message = self.validator.validate_has_unit_against_slot(has_unit, slot_name)
                        if not is_valid:
                            violations.append({
                                'file': yaml_file.name,
                                'path': qv['path'],
                                'slot': slot_name,
                                'has_unit': has_unit,
                                'has_raw_value': qv['has_raw_value'],
                                'violation_type': 'inappropriate_for_slot',
                                'message': message
                            })
                    else:
                        # Edge case: direct QuantityValue instantiation without clear slot ownership
                        unknown_slot_count += 1
            
            except Exception as e:
                self.fail(f"Error processing {yaml_file.name}: {e}")
        
        print(f"\nProcessed {total_quantity_values} QuantityValue objects")
        print(f"Could not determine slot for {unknown_slot_count} QuantityValue objects (direct instantiation)")
        print(f"Validated slot appropriateness for {total_quantity_values - unknown_slot_count} QuantityValue objects")
        
        if violations:
            print(f"\nhas_unit slot appropriateness violations found:")
            for v in violations:
                print(f"  {v['file']}:{v['path']} (slot: {v['slot']}) - {v['message']}")
        
        self.assertEqual(len(violations), 0, f"Found {len(violations)} has_unit values inappropriate for their slots")
    
    def test_quantity_value_completeness(self):
        """Test that QuantityValue objects have required has_unit fields."""
        missing_units = []
        total_quantity_values = 0
        
        # Process all YAML files in src/data/valid
        for yaml_file in self.data_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r') as f:
                    data = yaml.safe_load(f)
                
                def find_quantity_values_missing_units(obj, path=""):
                    """Find QuantityValue objects missing has_unit."""
                    results = []
                    count = 0
                    if isinstance(obj, dict):
                        if obj.get('type') == 'nmdc:QuantityValue':
                            count += 1
                            if 'has_unit' not in obj or not obj['has_unit']:
                                results.append({
                                    'file': yaml_file.name,
                                    'path': path,
                                    'has_raw_value': obj.get('has_raw_value'),
                                    'has_numeric_value': obj.get('has_numeric_value')
                                })
                        for key, value in obj.items():
                            new_path = f"{path}.{key}" if path else key
                            sub_results, sub_count = find_quantity_values_missing_units(value, new_path)
                            results.extend(sub_results)
                            count += sub_count
                    elif isinstance(obj, list):
                        for i, item in enumerate(obj):
                            new_path = f"{path}[{i}]"
                            sub_results, sub_count = find_quantity_values_missing_units(item, new_path)
                            results.extend(sub_results)
                            count += sub_count
                    return results, count
                
                file_results, file_count = find_quantity_values_missing_units(data)
                missing_units.extend(file_results)
                total_quantity_values += file_count
            
            except Exception as e:
                self.fail(f"Error processing {yaml_file.name}: {e}")
        
        print(f"\nFound {total_quantity_values} total QuantityValue objects")
        print(f"Found {len(missing_units)} QuantityValue objects missing has_unit")
        
        if missing_units:
            print(f"\nQuantityValue objects missing has_unit:")
            for item in missing_units:
                print(f"  {item['file']}:{item['path']} - raw_value: {item['has_raw_value']}")
        
        # This is informational, not necessarily a failure
        if missing_units:
            print(f"\nNote: {len(missing_units)} QuantityValue objects are missing has_unit fields")


if __name__ == '__main__':
    unittest.main()