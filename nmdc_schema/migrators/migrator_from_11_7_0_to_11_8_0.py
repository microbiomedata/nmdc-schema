from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.7.0"
    _to_version = "11.8.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.process_each_document("data_object_set", [self.validate_data_object_type])

    def validate_data_object_type(self, data_object: dict) -> dict:
        r"""
        Raises an exception if the document either lacks a `data_object_type`
        field or it has a `data_object_type` field whose value is falsey.

        >>> m = Migrator()
        >>> m.validate_data_object_type({"id": 123, "type": "nmdc:DataObject", "data_object_type": "Type"})
        {'id': 123, 'type': 'nmdc:DataObject', 'data_object_type': 'Type'}
        >>> m.validate_data_object_type({"id": 123, "type": "nmdc:DataObject"})
        Traceback (most recent call last):
        ...
        ValueError: data_object_type is required and is not present in the data object 123
        """
        if not data_object.get("data_object_type"):
            raise ValueError(f"data_object_type is required and is not present in the data object {data_object.get('id')}")
        return data_object