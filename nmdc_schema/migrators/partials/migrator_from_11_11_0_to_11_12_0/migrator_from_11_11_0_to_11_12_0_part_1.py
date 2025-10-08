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

        self.adapter.do_for_each_document("biosample_set", self.move_problematic_values_to_misc_param)

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


    def move_problematic_values_to_misc_param(self, biosample: dict) -> None:
        r"""Move QuantityValue entries with invalid units to misc_param as PropertyAssertion.

        >>> m = Migrator()

        # Test: Biosample with valid QuantityValue entries
        >>> biosample_valid = {
        ...     "id": "test1",
        ...     "type": "nmdc:Biosample",
        ...     "abs_air_humidity": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "kg/kg",
        ...         "has_numeric_value": 75.0
        ...     },
        ...     "diss_oxygen": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "umol/L",
        ...         "has_numeric_value": 8.0
        ...     },
        ...     "solar_irradiance": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "kW/m2/d",
        ...         "has_numeric_value": 200.0
        ...     }
        ... }
        >>> m.move_problematic_values_to_misc_param(biosample_valid)
        >>> biosample_valid.get("misc_param") is None
        True

        # Test: Biosample with problematic QuantityValue entries
        >>> biosample_problematic = {
        ...     "id": "test2",
        ...     "type": "nmdc:Biosample",
        ...     "abs_air_humidity": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "kPa",
        ...         "has_numeric_value": 75.0
        ...     },
        ...     "diss_oxygen": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "mL/L",
        ...         "has_numeric_value": 8.0
        ...     },
        ...     "solar_irradiance": {
        ...         "type": "nmdc:QuantityValue",
        ...         "has_unit": "W/m2",
        ...         "has_numeric_value": 200.0
        ...     }
        ... }
        >>> m.move_problematic_values_to_misc_param(biosample_problematic)
        >>> biosample_problematic.get("misc_param") == [
        ... {
        ...     "type": "nmdc:PropertyAssertion",
        ...     "has_attribute_label": "abs_air_humidity",
        ...     "has_attribute_id": "MIXS:0000122",
        ...     "has_numeric_value": 75.0,
        ...     "has_unit": "kPa"
        ... },
        ... {
        ...     "type": "nmdc:PropertyAssertion",
        ...     "has_attribute_label": "diss_oxygen",
        ...     "has_attribute_id": "MIXS:0000119",
        ...     "has_numeric_value": 8.0,
        ...     "has_unit": "mL/L"
        ... },
        ... {
        ...     "type": "nmdc:PropertyAssertion",
        ...     "has_attribute_label": "solar_irradiance",
        ...     "has_attribute_id": "MIXS:0000112",
        ...     "has_numeric_value": 200.0,
        ...     "has_unit": "W/m2"
        ... }]
        True
        >>> biosample_problematic.get("abs_air_humidity") is None
        True
        >>> biosample_problematic.get("diss_oxygen") is None
        True
        >>> biosample_problematic.get("solar_irradiance") is None
        True
        """
        problematic_units = (
            ("abs_air_humidity", "MIXS:0000122", "kPa"),
            ("diss_oxygen", "MIXS:0000119", "mL/L"),
            ("solar_irradiance", "MIXS:0000112", "W/m2"),
        )
        for slot_name, slot_uri, bad_unit in problematic_units:
            qv = biosample.get(slot_name)
            if isinstance(qv, dict) and qv.get("type") == "nmdc:QuantityValue":
                if qv.get("has_unit") == bad_unit:
                    # Move to misc_param as PropertyAssertion
                    pa = {
                        "type": "nmdc:PropertyAssertion",
                        "has_attribute_label": slot_name,
                        "has_attribute_id": slot_uri,
                    }
                    if "has_numeric_value" in qv:
                        pa["has_numeric_value"] = qv["has_numeric_value"]
                    if "has_unit" in qv:
                        pa["has_unit"] = qv["has_unit"]
                    if "has_raw_value" in qv:
                        pa["has_raw_value"] = qv["has_raw_value"]

                    # Ensure misc_param is a list and append the new PropertyAssertion
                    if "misc_param" not in biosample or not isinstance(biosample["misc_param"], list):
                        biosample["misc_param"] = []
                    biosample["misc_param"].append(pa)
                    # Remove the problematic QuantityValue from its original slot
                    del biosample[slot_name]


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