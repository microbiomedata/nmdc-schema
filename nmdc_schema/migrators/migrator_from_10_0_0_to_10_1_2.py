from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "10.0.0"  
    _to_version = "10.1.2"  

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        # Update each document in the `data_object_set` collection so that it uses a valid `FileTypeEnum` value.
        #
        # Note: The schema changed such that the `FileTypeEnum` value, "Metagenome Bins Compression File", is no longer
        #       valid. It was replaced with the value, "Metagenome HQMQ Bins Compression File". This migrator
        #       transforms all occurrences of the former value into the latter value, so that data that was valid with
        #       respect to the old schema is valid with respect to the new schema. According to the schema docs,
        #       the `FileTypeEnum` enum is used only by the `data_object_type` slot of the `DataObject` class.
        #
        self.adapter.process_each_document(
            "data_object_set", [self.update_data_object_type]
        )

    def update_data_object_type(self, data_object: dict) -> dict:
        r"""
        Updates a data object's `data_object_type` value to "Metagenome HQMQ Bins Compression File",
        if its value was originally "Metagenome Bins Compression File".

        >>> m = Migrator()
        >>> m.update_data_object_type({'id': 1})  # test: field not present
        {'id': 1}
        >>> m.update_data_object_type({'id': 1, 'data_object_type': 'unrelated'})  # test: value not relevant
        {'id': 1, 'data_object_type': 'unrelated'}
        >>> m.update_data_object_type({'id': 1, 'data_object_type': 'Metagenome HQMQ Bins Compression File'})
        {'id': 1, 'data_object_type': 'Metagenome HQMQ Bins Compression File'}
        >>> m.update_data_object_type({'id': 1, 'data_object_type': 'Metagenome Bins Compression File'})
        {'id': 1, 'data_object_type': 'Metagenome HQMQ Bins Compression File'}
        """
        self.logger.info(f"Processing DataObject: {data_object['id']}")

        invalid_value = "Metagenome Bins Compression File"
        valid_value = "Metagenome HQMQ Bins Compression File"

        # If this data object's `data_object_type` consists of the invalid value, replace it with the valid value.
        if "data_object_type" in data_object:
            if data_object["data_object_type"] == invalid_value:
                data_object["data_object_type"] = valid_value

        return data_object
