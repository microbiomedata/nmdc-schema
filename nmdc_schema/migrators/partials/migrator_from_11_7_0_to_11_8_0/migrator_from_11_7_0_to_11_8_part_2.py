from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.helpers import load_yaml_asset

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.7.0"
    _to_version = "11.8.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.process_each_document("data_object_set", [self.clarify_ft_data_category])

    def clarify_ft_data_category(self, data_object: dict) -> dict:
        r"""
        If the data object does not have data_category field, add a value based on the data_object_type.
        If the data object has any other value for data_object_type; ignore it.

        >>> m = Migrator()
        >>> m.clarify_ft_data_category({"id":123, "type":"nmdc:DataObject", "data_object_type":"Metagenome Raw Reads"})
        {'id': 123, 'type': 'nmdc:DataObject', 'data_object_type': 'Metagenome Raw Reads', 'data_category': 'instrument_data'}
        >>> m.clarify_ft_data_category({"id":123, "type":"nmdc:DataObject", "data_category": "instrument_data"})
        {'id': 123, 'type': 'nmdc:DataObject', 'data_category': 'instrument_data'}
        """
        data_category_map = load_yaml_asset('migrator_from_11_7_to_11_8/data_category_map.yaml')

        if not data_object.get("data_category"):
            try:
                data_object["data_category"] = data_category_map[data_object.get("data_object_type")]
            except KeyError:
                data_object["data_category"] = ""
        return data_object