from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.8.0"  
    _to_version = "11.9.0"  

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
            "workflow_execution_set", [self.update_was_informed_by]
        )

    def update_was_informed_by(self, workflow_execution: dict) -> dict:
        r"""
        Update was_informed_by to be multivalued.

        >>> m = Migrator()
        >>> m.was_informed_by({'id': 1, 'was_informed_by': 'nmdc:dgns-11-abdc4'})  # test: value not relevant
        {'id': 1, 'was_informed_by': ['nmdc:dgns-11-abdc4']}
        """
        self.logger.info(f"Processing WorkflowExecution: {workflow_execution['id']}")

        workflow_execution["was_informed_by"] = [workflow_execution["was_informed_by"]]
        return data_object
