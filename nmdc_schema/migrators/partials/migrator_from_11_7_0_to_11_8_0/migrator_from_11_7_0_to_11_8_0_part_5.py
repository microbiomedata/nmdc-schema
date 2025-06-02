from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0.part_4"
    _to_version = "11.8.0.part_5"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.process_each_document("biosample_set", [self.standardize_unit_celsius])
        self.adapter.process_each_document("material_processing_set", [self.standardize_unit_celsius])
        self.adapter.process_each_document("configuration_set", [self.standardize_unit_celsius])
        self.adapter.process_each_document("storage_process_set", [self.standardize_unit_celsius])

    def standardize_unit_celsius(self, record: dict) -> dict:
        r"""
        If the record has one of the indicated fields and has the has_unit slot, replace the string using the yaml.
        If the record has none of the indicated fields, do nothing.
        A mapping is loaded from a YAML file. The mapping is a dictionary where the keys are strings presently in Mongo that all indicate Celsius
        and the values are the agreed upon new string for Celsius 'Cel'.
        If the `has_unit` string is not in the mapping, raise a ValueError.

        >>> m = Migrator()
        >>> m.standardize_unit_celsius({"id": 123, "type": "nmdc:Biosample", "temp": {"has_numeric_value": 6.6, "has_unit": "Celsius", "type": "nmdc:QuantityValue"}})
        {'id': 123, 'type': 'nmdc:Biosample', 'temp': {'has_numeric_value': 6.6, 'has_unit': 'Cel', 'type': 'nmdc:QuantityValueCelsius'}}
        >>> m.standardize_unit_celsius({"id": 123, "type": "nmdc:Biosample", "temp": {"has_numeric_value": 6.6, "has_unit": "Cel", "type": "nmdc:QuantityValue"}})
        {'id': 123, 'type': 'nmdc:Biosample', 'temp': {'has_numeric_value': 6.6, 'has_unit': 'Cel', 'type': 'nmdc:QuantityValueCelsius'}}
        >>> m.standardize_unit_celsius({"id": 123, "type": "nmdc:Biosample", "temp": {"has_numeric_value": 6.6, "type": "nmdc:QuantityValue"}})
        Traceback (most recent call last):
        ...
        ValueError: record 123 and field temp populated but missing `has_unit` value.
        >>> m.standardize_unit_celsius({"id": 123, "type": "nmdc:Biosample", "temp": {"has_numeric_value": 6.6, "has_unit": "F", "type": "nmdc:QuantityValue"}})
        Traceback (most recent call last):
        ...
        ValueError: `has_unit` string F is not found in the mapping. Cannot assign 'Cel'.
        """
        celsius_map = load_yaml_asset('migrator_from_11_7_to_11_8/celsius_map.yaml')

        fields = ['air_temp', 'annual_temp', 'avg_temp', 'host_body_temp', 'samp_store_temp', 'season_temp', 'surf_temp', 'temp', 'temp_out', 'temperature']
        
        for field in fields:
            if record.get(field):
                if record[field].get('has_unit'):
                    try:
                        record[field]["has_unit"] = celsius_map[record[field].get('has_unit')]
                        record[field]["type"] = "nmdc:QuantityValueCelsius"
                    except KeyError:
                        raise ValueError(
                            f"`has_unit` string {record[field].get('has_unit')} is not found in the mapping. Cannot assign 'Cel'."
                        )
                else:
                    raise ValueError(
                            f"record {record['id']} and field {field} populated but missing `has_unit` value."
                        )
        return record
    