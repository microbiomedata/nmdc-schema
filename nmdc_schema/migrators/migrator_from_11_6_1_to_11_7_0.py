from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.6.1"
    _to_version = "11.7.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("data_object_set", [self.clarify_ft_data_object_type])

    def clarify_ft_data_object_type(self, data_object: dict) -> dict:
        r"""
        If the data object has the data_object_type of "FT ICR-MS Analysis Results", replace it with "Direct Infusion FT-ICR MS Analysis Results".
        If the data object has any other value for data_object_type; ignore it.

        >>> m = Migrator()
        >>> m.clarify_ft_data_object_type({"id":123, "type":"nmdc:DataObject", "data_object_type": "FT ICR-MS Analysis Results"})
        {'id': 123, 'type': 'nmdc:DataObject', 'data_object_type': 'Direct Infusion FT-ICR MS Analysis Results'}
        >>> m.clarify_ft_data_object_type({"id":123, "type":"nmdc:DataObject", "data_object_type": "Another Type"})
        {'id': 123, 'type': 'nmdc:DataObject', 'data_object_type': 'Another Type'}
        >>> m.clarify_ft_data_object_type({"id":123, "type":"nmdc:DataObject"})
        {'id': 123, 'type': 'nmdc:DataObject'}
        """

        if data_object.get("data_object_type") == "FT ICR-MS Analysis Results":
            data_object["data_object_type"] = "Direct Infusion FT-ICR MS Analysis Results"
        return data_object