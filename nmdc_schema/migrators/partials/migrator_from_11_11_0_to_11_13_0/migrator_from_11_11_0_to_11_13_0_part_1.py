import sys
from pathlib import Path

from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

class Migrator(MigratorBase):
    r'''
    Migrates a database between two schemas.
    '''

    _from_version = '11.11.0'
    _to_version = '11.13.0.part_1'

    def upgrade(self, commit_changes: bool = False) -> None:
        r'''
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        '''

        if isinstance(self.adapter, MongoAdapter):
            try:
                self.adapter.execute_in_transaction(
                    operations_callback=self.perform_all_migration_operations,
                    commit_changes=commit_changes
                )

                if commit_changes:
                    self.logger.info("Transaction committed (changes have been saved)")
                else:
                    self.logger.info("Transaction rolled back (no changes were committed)")

            except Exception as e:
                self.logger.error(f"Migration failed: {e}")
                raise
        else:
            raise NotImplementedError("This migrator currently only supports MongoAdapter.")


    def perform_all_migration_operations(self, _, __) -> None:
        self.logger.info("Moving problematic QuantityValue entries to misc_param")
        self.adapter.process_each_document("biosample_set", [
            self.migrate_misc_param_to_PropertyAssertion_range,
            self.move_problematic_values_to_misc_param,
        ])


    def migrate_misc_param_to_PropertyAssertion_range(self, biosample: dict) -> dict:
        r"""The misc_param slot on Biosample used to have range TextValue, but now has range
        PropertyAssertion. This migrator changes misc_param values to conform to the new range.

        >>> m = Migrator()

        # Test: Biosample with no misc_param
        >>> biosample_no_misc = {
        ...     "id": "test1",
        ...     "type": "nmdc:Biosample"
        ... }
        >>> m.migrate_misc_param_to_PropertyAssertion_range(biosample_no_misc)
        {'id': 'test1', 'type': 'nmdc:Biosample'}

        # Test: Biosample with misc_param as TextValue
        >>> biosample_with_misc = {
        ...     "id": "test2",
        ...     "type": "nmdc:Biosample",
        ...     "misc_param": [{"type": "nmdc:TextValue", "has_raw_value": "biomass_yield;2.565699 Mg/ha"}]
        ... }
        >>> m.migrate_misc_param_to_PropertyAssertion_range(biosample_with_misc)
        {'id': 'test2', 'type': 'nmdc:Biosample', 'misc_param': [{'type': 'nmdc:PropertyAssertion', 'has_raw_value': 'biomass_yield;2.565699 Mg/ha', 'has_attribute_label': 'biomass_yield', 'has_numeric_value': 2.565699, 'has_unit': 'Mg/ha'}]}
        """
        misc_param = biosample.get("misc_param")
        if not misc_param:
            return biosample

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
        return biosample


    def move_problematic_values_to_misc_param(self, biosample: dict) -> dict:
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
        {'id': 'test1', 'type': 'nmdc:Biosample', 'abs_air_humidity': {'type': 'nmdc:QuantityValue', 'has_unit': 'kg/kg', 'has_numeric_value': 75.0}, 'diss_oxygen': {'type': 'nmdc:QuantityValue', 'has_unit': 'umol/L', 'has_numeric_value': 8.0}, 'solar_irradiance': {'type': 'nmdc:QuantityValue', 'has_unit': 'kW/m2/d', 'has_numeric_value': 200.0}}

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
        {'id': 'test2', 'type': 'nmdc:Biosample', 'misc_param': [{'type': 'nmdc:PropertyAssertion', 'has_attribute_label': 'abs_air_humidity', 'has_attribute_id': 'MIXS:0000122', 'has_numeric_value': 75.0, 'has_unit': 'kPa'}, {'type': 'nmdc:PropertyAssertion', 'has_attribute_label': 'diss_oxygen', 'has_attribute_id': 'MIXS:0000119', 'has_numeric_value': 8.0, 'has_unit': 'mL/L'}, {'type': 'nmdc:PropertyAssertion', 'has_attribute_label': 'solar_irradiance', 'has_attribute_id': 'MIXS:0000112', 'has_numeric_value': 200.0, 'has_unit': 'W/m2'}]}
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
        return biosample
