from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.14.0"
    _to_version = "11.16.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("workflow_execution_set", [self.make_uses_calibration_multivalued])

    def make_uses_calibration_multivalued(self, workflow_execution: dict) -> dict:
        r"""
        If a WorkflowExection record in the workflow_execution_set has a 'uses_calibration' field, convert it to a list containing the original value.

        >>> m = Migrator()
        >>> m.make_uses_calibration_multivalued({'id': 123})  # no `extraction_target` field
        {'id': 123}
        >>> m.make_uses_calibration_multivalued({'id': 123, 'uses_calibration': 'nmdc:calib-13-tester'})  # test: casts it as a list value
        {'id': 123, 'uses_calibration': ['nmdc:calib-13-tester']}
        """

        if workflow_execution.get("uses_calibration") is not None:
            workflow_execution[
                "uses_calibration"
            ] = [workflow_execution["uses_calibration"]]
        return workflow_execution