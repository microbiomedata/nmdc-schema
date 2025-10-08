from nmdc_schema.migrators.migrator_base import MigratorBase
import sys
from pathlib import Path
from nmdc_schema.migrators.helpers import create_schema_view

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from units.scripts.production_validate_units import ProductionUnitsValidator
from migrators.partials.migrator_from_11_9_1_to_11_10_0.migrator_from_11_9_1_to_11_10_0_part_1 import get_collection_names_with_qv_slots_from_schema

class Migrator(MigratorBase):
    r'''
    Migrates a database between two schemas.
    TWO NOTES: 
    - If there is no storage_unit on the slot, the only test is whether the value for `has_unit` is in the UnitEnum
    - This assumes that all storage_unit restrictions are applied on the global level, it does not validate any changes made on slot_useage (same as python tests, example: does not test if temp on biosample has to be celsius but temp on conversion process is kelvin)
    '''

    _from_version = '11.11.0'
    _to_version = '11.12.0.part_1'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize the validator with the schema file
        schema_file = Path('nmdc_schema/nmdc_materialized_patterns.yaml')
        self.validator = ProductionUnitsValidator(schema_file)

        

    def upgrade(self,commit_changes: bool = False) -> None:
        r'''
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        '''
        
        # Get schema view to find all classes and their slots with QuantityValue range
        self._schema_view = create_schema_view()

        self.adapter.do_for_each_document("biosample_set", self.migrate_misc_param_to_PropertyAssertion_range)

        # Get the actual collection names from the Database class slots
        real_collection_names = get_collection_names_with_qv_slots_from_schema()

        # Apply migrator through collections
        for collection_name in real_collection_names:
            print(f'processing collection {collection_name}')
            self.adapter.do_for_each_document(collection_name, self.confirm_units_fit_unitenum_and_storage_units)


    def migrate_misc_param_to_PropertyAssertion_range(self, biosample: dict) -> None:
        r"""The misc_param slot on Biosample used to have range TextValue, but now has range
        PropertyAssertion. This migrator changes misc_param values to conform to the new range.

        >>> m = Migrator()

        # Test: Biosample with no misc_param
        >>> biosample_no_misc = {
        ...     "id": "test1",
        ...     "type": "nmdc:Biosample"
        ... }
        >>> m.migrate_misc_param_to_PropertyAssertion_range(biosample_no_misc)
        >>> biosample_no_misc.get("misc_param") is None
        True

        # Test: Biosample with misc_param as TextValue
        >>> biosample_with_misc = {
        ...     "id": "test2",
        ...     "type": "nmdc:Biosample",
        ...     "misc_param": [{"type": "nmdc:TextValue", "has_raw_value": "biomass_yield;2.565699 Mg/ha"}]
        ... }
        >>> m.migrate_misc_param_to_PropertyAssertion_range(biosample_with_misc)
        >>> misc_params = biosample_with_misc.get("misc_param")
        >>> isinstance(misc_params, list) and len(misc_params) == 1
        True
        >>> pa = misc_params[0]
        >>> pa["type"]
        'nmdc:PropertyAssertion'
        >>> pa["has_raw_value"]
        'biomass_yield;2.565699 Mg/ha'
        >>> pa["has_attribute_label"]
        'biomass_yield'
        >>> pa["has_numeric_value"]
        2.565699
        >>> pa["has_unit"]
        'Mg/ha'
        """
        misc_param = biosample.get("misc_param")
        if not misc_param:
            return

        property_assertions = []
        for item in misc_param:
            if isinstance(item, dict) and item.get("type") == "nmdc:TextValue":
                # Convert TextValue to PropertyAssertion
                raw_value = item.get("has_raw_value")
                if not raw_value:
                    continue
                pa = {
                    "type": "nmdc:PropertyAssertion",
                    "has_raw_value": raw_value
                }
                if ";" in raw_value:
                    [label, _, value] = item.get("has_raw_value", "").partition(";")
                    pa["has_attribute_label"] = label.strip()
                    if " " in value:
                        num_str, _, unit = value.strip().partition(" ")
                        try:
                            pa["has_numeric_value"] = float(num_str)
                        except ValueError:
                            pass  # If conversion fails, skip adding has_numeric_value
                        if unit:
                            pa["has_unit"] = unit.strip()
                property_assertions.append(pa)
            else:
                raise ValueError(
                    f"Biosample {biosample.get('id')} has misc_param item that is not a TextValue: {item}"
                )
        biosample["misc_param"] = property_assertions

    def confirm_units_fit_unitenum_and_storage_units(self, document: dict) -> None:
        r'''
        Raise an exception if the QuantityValue's has_unit slot is not valid against slot's storage_unit or UnitEnum constraints.

        >>> m = Migrator()
        
        # Test: valid QuantityValue with proper units in biosample
        >>> valid_biosample = {
        ...     "id": "test1", 
        ...     "type": "nmdc:Biosample",
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "Cel",
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(valid_biosample)  # Should not raise
        
        # Test: invalid unit not in UnitEnum
        >>> invalid_biosample_enum = {
        ...     "id": "test2", 
        ...     "type": "nmdc:Biosample",
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue", 
        ...         "has_unit": "invalid_unit",
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(invalid_biosample_enum)
        Traceback (most recent call last):
            ...
        ValueError: Document test2 has invalid unit 'invalid_unit' for slot 'temp': Unit not in UnitEnum
        
        # Test: unit not allowed for specific slot's storage_units
        >>> invalid_biosample_storage = {
        ...     "id": "test3",
        ...     "type": "nmdc:Biosample", 
        ...     "temp": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "m",  # Wrong unit type for temperature
        ...         "has_numeric_value": 25.0
        ...     }
        ... }
        >>> m.confirm_units_fit_unitenum_and_storage_units(invalid_biosample_storage)
        Traceback (most recent call last):
            ...
        ValueError: Document test3 has invalid unit 'm' for slot 'temp': Unit 'm' not in allowed storage_units ['Cel'] for slot 'temp'

        '''
        
        document_id = document.get("id")
        
        # Find all QuantityValue objects in this document using the imported validator
        for path, qv_data in self.validator.iter_quantity_values(document):
            has_unit = qv_data.get('has_unit')
            if not has_unit:
                continue
                
            # Extract slot name from path using the imported method
            slot_name = path[-1]
            
            # First validate against UnitEnum using the imported method
            if not self.validator.validate_has_unit_against_enum(has_unit):
                raise ValueError(
                    f"Document {document_id} has invalid unit '{has_unit}' for slot '{slot_name}': Unit not in UnitEnum"
                )
            
            # Then validate against storage_units constraints using the imported method
            is_valid, message = self.validator.validate_has_unit_against_slot(has_unit, slot_name)
            if not is_valid:
                raise ValueError(
                    f"Document {document_id} has invalid unit '{has_unit}' for slot '{slot_name}': {message}"
                )