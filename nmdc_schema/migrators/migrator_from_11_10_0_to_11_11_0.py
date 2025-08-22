from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.10.0"
    _to_version = "11.11.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "data_object_set", [self.confirm_permissible_values_are_absent]
        )

    def confirm_permissible_values_are_absent(self, data_object: dict) -> dict:
        r"""
        If the data object has the data_object_type of "Metagenome Bins" or "Centrifuge Classification Report" raise an exception.

        >>> m = Migrator()
 
        # Test: data_object_type of "Metagenome Bins"
        >>> m.confirm_permissible_values_are_absent({"id": 1, "type": "nmdc:DataObject", "data_object_type": "Metagenome Bins"})
        Traceback (most recent call last):
            ...
        ValueError: DataObject 1 has value: Metagenome Bins

        # Test: data_object_type of "Centrifuge Classification Report"
        >>> m.confirm_permissible_values_are_absent({"id": 2, "type": "nmdc:DataObject", "data_object_type": "Centrifuge Classification Report"})
        Traceback (most recent call last):
            ...
        ValueError: DataObject 2 has value: Centrifuge Classification Report

        # Test: valid data_object_type
        >>> m.confirm_permissible_values_are_absent({"id": 3, "type": "nmdc:DataObject", "data_object_type": "Virus Summary"})
        {'id': 3, 'type': 'nmdc:DataObject', 'data_object_type': 'Virus Summary'}
        """

        data_object_type_value = data_object.get("data_object_type")
        data_object_id = data_object.get("id")
        if (
            data_object.get("data_object_type") == "Metagenome Bins"
            or data_object.get("data_object_type") == "Centrifuge Classification Report"
        ):
            raise ValueError(
                 f"DataObject {data_object_id} has value: {data_object_type_value}"
            )
        return data_object
