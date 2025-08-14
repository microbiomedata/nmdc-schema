"""Test that all annotation keys are in the allowed whitelist."""
import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

# Allowed annotation keys based on the provided whitelist
ALLOWED_ANNOTATION_KEYS = {
    'expected_value',
    'file_name_pattern', 
    'occurrence',
    'originally',
    'preferred_unit',
    'source',
    'storage_units',
    'tooltip'
}


class TestAnnotationKeysWhitelist(unittest.TestCase):
    """Test that all annotation keys are in the allowed whitelist."""

    def test_annotation_keys_whitelist(self):
        """Check all annotations in schema against whitelist."""
        view = SchemaView(SCHEMA_FILE)
        
        found_annotation_keys = set()
        violations = []
        
        # Check all elements for annotations
        all_elements = view.all_elements()
        for element_name, element in all_elements.items():
            element_type = type(element).__name__
            
            # Check element-level annotations
            if element.annotations and element.annotations not in ["", []]:
                # Handle dict-style annotations (like in core.yaml)
                if isinstance(element.annotations, dict):
                    for key, annotation_obj in element.annotations.items():
                        found_annotation_keys.add(key)
                        if key not in ALLOWED_ANNOTATION_KEYS:
                            violations.append(f"{element_type}.{element_name}: annotation key '{key}' not in whitelist")
                else:
                    # Handle list-style annotations
                    for annotation in element.annotations:
                        # Handle different annotation formats
                        if hasattr(annotation, 'tag'):
                            key = annotation.tag
                        elif isinstance(annotation, str):
                            key = annotation  # Sometimes annotations are just strings
                        else:
                            continue  # Skip malformed annotations
                        
                        found_annotation_keys.add(key)
                        if key not in ALLOWED_ANNOTATION_KEYS:
                            violations.append(f"{element_type}.{element_name}: annotation key '{key}' not in whitelist")
            
            # Check class slot_usage annotations
            if hasattr(element, 'slot_usage') and element.slot_usage:
                for slot_name, slot_usage in element.slot_usage.items():
                    if slot_usage.annotations and slot_usage.annotations not in ["", []]:
                        for annotation in slot_usage.annotations:
                            # Handle different annotation formats
                            if hasattr(annotation, 'tag'):
                                key = annotation.tag
                            elif isinstance(annotation, str):
                                key = annotation
                            else:
                                continue
                            
                            found_annotation_keys.add(key)
                            if key not in ALLOWED_ANNOTATION_KEYS:
                                violations.append(f"{element_type}.{element_name}.slot_usage.{slot_name}: annotation key '{key}' not in whitelist")
            
            # Check enum permissible value annotations
            if hasattr(element, 'permissible_values') and element.permissible_values:
                for pv_name, pv_def in element.permissible_values.items():
                    if pv_def.annotations and pv_def.annotations not in ["", []]:
                        for annotation in pv_def.annotations:
                            # Handle different annotation formats
                            if hasattr(annotation, 'tag'):
                                key = annotation.tag
                            elif isinstance(annotation, str):
                                key = annotation
                            else:
                                continue
                                
                            found_annotation_keys.add(key)
                            if key not in ALLOWED_ANNOTATION_KEYS:
                                violations.append(f"{element_type}.{element_name}.permissible_values.{pv_name}: annotation key '{key}' not in whitelist")

        # Print found annotation keys for debugging
        print(f"\nFound annotation keys: {sorted(found_annotation_keys)}")
        print(f"Allowed annotation keys: {sorted(ALLOWED_ANNOTATION_KEYS)}")
        
        if violations:
            print(f"\nAnnotation key violations found:")
            for violation in sorted(violations):
                print(f"  {violation}")
        
        self.assertEqual(len(violations), 0, f"Found {len(violations)} annotation key violations")

    def test_storage_units_from_unit_enum(self):
        """Check that all storage_units annotation values come from UnitEnum."""
        view = SchemaView(SCHEMA_FILE)
        
        # Get allowed units from UnitEnum
        unit_enum = view.get_enum('UnitEnum')
        if not unit_enum or not unit_enum.permissible_values:
            self.fail("UnitEnum not found or has no permissible values")
        
        allowed_units = set(unit_enum.permissible_values.keys())
        
        violations = []
        found_storage_units = set()
        
        # Check all elements for storage_units annotations
        all_elements = view.all_elements()
        for element_name, element in all_elements.items():
            element_type = type(element).__name__
            
            # Check element-level storage_units annotations
            if element.annotations and element.annotations not in ["", []]:
                # Handle dict-style annotations (like in core.yaml)
                if isinstance(element.annotations, dict):
                    if 'storage_units' in element.annotations:
                        annotation_obj = element.annotations['storage_units']
                        if annotation_obj and hasattr(annotation_obj, 'value'):
                            value = annotation_obj.value
                            if value:
                                # Split on pipes and check each unit
                                units = [unit.strip() for unit in str(value).split('|')]
                                found_storage_units.update(units)
                                
                                for unit in units:
                                    if unit not in allowed_units:
                                        violations.append(f"{element_type}.{element_name}: storage_units value '{unit}' not in UnitEnum")
                else:
                    # Handle list-style annotations
                    for annotation in element.annotations:
                        # Handle different annotation formats
                        if hasattr(annotation, 'tag'):
                            key = annotation.tag
                            value = annotation.value if hasattr(annotation, 'value') else None
                        elif isinstance(annotation, str):
                            continue  # String annotations don't have storage_units
                        else:
                            continue
                        
                        if key == 'storage_units' and value:
                            # Split on pipes and check each unit
                            units = [unit.strip() for unit in value.split('|')]
                            found_storage_units.update(units)
                            
                            for unit in units:
                                if unit not in allowed_units:
                                    violations.append(f"{element_type}.{element_name}: storage_units value '{unit}' not in UnitEnum")
            
            # Check class slot_usage storage_units annotations
            if hasattr(element, 'slot_usage') and element.slot_usage:
                for slot_name, slot_usage in element.slot_usage.items():
                    if slot_usage.annotations and slot_usage.annotations not in ["", []]:
                        for annotation in slot_usage.annotations:
                            # Handle different annotation formats
                            if hasattr(annotation, 'tag'):
                                key = annotation.tag
                                value = annotation.value if hasattr(annotation, 'value') else None
                            elif isinstance(annotation, str):
                                continue
                            else:
                                continue
                            
                            if key == 'storage_units' and value:
                                # Split on pipes and check each unit
                                units = [unit.strip() for unit in value.split('|')]
                                found_storage_units.update(units)
                                
                                for unit in units:
                                    if unit not in allowed_units:
                                        violations.append(f"{element_type}.{element_name}.slot_usage.{slot_name}: storage_units value '{unit}' not in UnitEnum")

        print(f"\nFound {len(found_storage_units)} unique storage_units values")
        print(f"UnitEnum has {len(allowed_units)} permissible values")
        
        if violations:
            print(f"\nStorage units violations found:")
            for violation in sorted(violations):
                print(f"  {violation}")
        
        self.assertEqual(len(violations), 0, f"Found {len(violations)} storage_units violations")


if __name__ == '__main__':
    unittest.main()