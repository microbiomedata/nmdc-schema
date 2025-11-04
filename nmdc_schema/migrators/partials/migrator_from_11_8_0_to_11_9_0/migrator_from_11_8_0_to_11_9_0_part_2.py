from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.9.0.part_1"
    _to_version = "11.9.0.part_2"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        # Update each document in the `workflow_execution_set` collection so its `was_informed_by` value is a list.
        self.adapter.process_each_document(
            "workflow_execution_set", [self.update_was_informed_by]
        )

    def update_was_informed_by(self, workflow_execution: dict) -> dict:
        r"""
        Update the document's `was_informed_by` value to be a list (since the schema says the slot is now multivalued).

        >>> m = Migrator()
        >>> m.update_was_informed_by({'id': 1, 'was_informed_by': 'nmdc:dgns-11-000001'})
        {'id': 1, 'was_informed_by': ['nmdc:dgns-11-000001']}
        """
        self.logger.info(f"Processing WorkflowExecution: {workflow_execution['id']}")

        original_was_informed_by_value = workflow_execution["was_informed_by"]
        workflow_execution["was_informed_by"] = [original_was_informed_by_value]
        return workflow_execution
