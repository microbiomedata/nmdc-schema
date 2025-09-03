import unittest

from linkml_runtime import SchemaView

from tests import SCHEMA_FILE

# Define approved excuse values at module level
APPROVED_UNITS_ALIGNMENT_EXCUSES = {
    "not measurement like",
    "MIxS internally inconsistent", 
    "UCUM unaware of MIxS unit"
}


class TestUnitsAlignment(unittest.TestCase):

    def test_slots_with_preferred_unit_have_storage_units_or_excuse(self):
        """Test that all slots with preferred_unit annotation have either storage_units or units_alignment_excuse.
        
        Based on the yq command:
        yq '.slots | to_entries | map(select(.value.annotations.preferred_unit and (.value.annotations.storage_units == null) and (.value.annotations.units_alignment_excuse == null))) | map(.key)'
        """
        schema_view = SchemaView(SCHEMA_FILE)
        problematic_slots = []
        
        for slot_name in schema_view.all_slots():
            slot = schema_view.get_slot(slot_name)
            if not slot or not slot.annotations:
                continue
                
            annotations = slot.annotations
            
            # Check if slot has preferred_unit
            has_preferred_unit = 'preferred_unit' in annotations
            has_storage_units = 'storage_units' in annotations
            has_units_excuse = 'units_alignment_excuse' in annotations
            
            # If it has preferred_unit but neither storage_units nor units_alignment_excuse
            if has_preferred_unit and not has_storage_units and not has_units_excuse:
                problematic_slots.append(slot_name)
        
        # Sort for consistent output
        problematic_slots.sort()
        
        self.assertEqual([], problematic_slots,
                        msg=f"Found {len(problematic_slots)} slots with preferred_unit but missing storage_units and units_alignment_excuse annotations: " + str(problematic_slots))
    
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
                if hasattr(excuse_annotation, 'value'):
                    excuse_value = excuse_annotation.value
                else:
                    excuse_value = str(excuse_annotation)
                
                if excuse_value not in APPROVED_UNITS_ALIGNMENT_EXCUSES:
                    invalid_excuses.append((slot_name, excuse_value))
        
        self.assertEqual([], invalid_excuses,
                        msg=f"Found slots with invalid units_alignment_excuse values. Approved values are: {sorted(APPROVED_UNITS_ALIGNMENT_EXCUSES)}. Invalid: " + str(invalid_excuses))
    