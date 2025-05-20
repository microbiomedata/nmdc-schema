from nmdc_schema.migrators.migrator_base import MigratorBase

class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.7.0"
    _to_version = "11.8.0.part_1"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        self.adapter.do_for_each_document("data_object_set", self.validate_data_object_type)

    def validate_data_object_type(self, data_object: dict) -> None:
        r"""
        Raises an exception if the document lacks a `data_object_type` field.

        >>> m = Migrator()
        >>> m.validate_data_object_type({"id": 123, "type": "nmdc:DataObject", "data_object_type": "Type"})
        >>> m.validate_data_object_type({"id": 123, "type": "nmdc:DataObject"})
        Traceback (most recent call last):
        ...
        ValueError: data_object_type is required and is not present in the data object 123
        """
        if "data_object_type" not in data_object:
            raise ValueError(f"data_object_type is required and is not present in the data object {data_object.get('id')}")