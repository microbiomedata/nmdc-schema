import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

# Define approved excuse values at module level
APPROVED_UNITS_ALIGNMENT_EXCUSES = {
    "protocol_slot",           # For protocol/regimen slots (not measurement-like)
    "mixs_inconsistent",       # For MIxS specification errors
    "non_ucum_unit",          # For units not recognized by UCUM
    "complex_unit",           # For multi-dimensional or complex units
    "pending_analysis"        # Temporary excuse during development
}


class TestUnitsAlignment(unittest.TestCase):

    def test_quantityvalue_slots_have_storage_units_or_excuse(self):
        """Test that ALL QuantityValue slots have either storage_units or units_alignment_excuse.
        
        Expanded constraint: All QuantityValue slots must have storage_units OR units_alignment_excuse.
        This ensures complete coverage of unit constraints for data validation.
        
        Consumer behavior: units_alignment_excuse means "skip storage_units validation for documented reason".
        """
        schema_view = SchemaView(SCHEMA_FILE)
        problematic_slots = []
        
        for slot_name in schema_view.all_slots():
            slot = schema_view.get_slot(slot_name)
            if not slot:
                continue
                
            # Check if slot has QuantityValue range
            if slot.range != 'QuantityValue':
                continue
                
            annotations = slot.annotations or {}
            has_storage_units = 'storage_units' in annotations
            has_units_excuse = 'units_alignment_excuse' in annotations
            
            # All QuantityValue slots must have either storage_units or excuse
            if not has_storage_units and not has_units_excuse:
                problematic_slots.append(slot_name)
        
        # Sort for consistent output
        problematic_slots.sort()
        
        self.assertEqual([], problematic_slots,
                        msg=f"Found {len(problematic_slots)} QuantityValue slots missing both storage_units and units_alignment_excuse annotations")
    
    def test_units_alignment_excuse_values_are_valid(self):
        """Test that units_alignment_excuse annotations use approved excuse values."""
        schema_view = SchemaView(SCHEMA_FILE)
        invalid_excuses = []
        
        for slot_name in schema_view.all_slots():
            slot = schema_view.get_slot(slot_name)
            if not slot or not slot.annotations:
                continue
                
            annotations = slot.annotations
            
            if 'units_alignment_excuse' in annotations:
                excuse_annotation = annotations['units_alignment_excuse']
                excuse_value = excuse_annotation.value
                
                if excuse_value not in APPROVED_UNITS_ALIGNMENT_EXCUSES:
                    invalid_excuses.append((slot_name, excuse_value))
        
        self.assertEqual([], invalid_excuses,
                        msg=f"Found slots with invalid units_alignment_excuse values. Approved values are: {sorted(APPROVED_UNITS_ALIGNMENT_EXCUSES)}")
    