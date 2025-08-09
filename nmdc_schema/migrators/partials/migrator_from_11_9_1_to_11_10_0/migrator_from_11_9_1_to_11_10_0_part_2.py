from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.10.0.part_1"
    _to_version = "11.10.0.part_2"

    def upgrade(self, commit_changes: bool = True) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        
        Note: The `commit_changes` parameter is not used, but must be present in the
              method signature to comply with the base class. This migrator does
              not use transactions—all changes are committed immediately.

        TODO: Address the fact that existing migrators' `upgrade` methods
              no longer comply with the base class.
        """

        self.adapter.process_each_document(
            "workflow_execution_set", [self.update_processing_metadata]
        )

    def update_processing_metadata(self, workflow_execution: dict) -> dict:
        r"""
        Update the document's processing_institution and execution_resource values.

        >>> m = Migrator()
        >>> m.update_processing_metadata({'id': 1, 'execution_resource': 'JGI'})
        {'id': 1, 'processing_institution': 'JGI'}
        >>> m.update_processing_metadata({'id': 1, 'execution_resource': 'EMSL'})
        {'id': 1, 'processing_institution': 'NMDC'}
        >>> m.update_processing_metadata({'id': 1, 'execution_resource': 'NERSC-Perlmutter'})
        {'id': 1, 'execution_resource': 'NERSC-Perlmutter', 'processing_institution': 'NMDC'}
        >>> m.update_processing_metadata({'id': 1, 'execution_resource': 'EMSL-RZR'})
        {'id': 1, 'execution_resource': 'EMSL-RZR', 'processing_institution': 'NMDC'}
        >>> m.update_processing_metadata({'id': 1, 'execution_resource': 'NERSC-Cori'})
        {'id': 1, 'execution_resource': 'NERSC-Cori', 'processing_institution': 'NMDC'}

        """
        self.logger.info(f"Processing WorkflowExecution: {workflow_execution['id']}")
        if workflow_execution["execution_resource"] == "JGI":
            workflow_execution["processing_institution"] = "JGI"
            workflow_execution.pop("execution_resource", None)
        elif workflow_execution["execution_resource"] == "EMSL":
            workflow_execution["processing_institution"] = "NMDC"
            workflow_execution.pop("execution_resource", None)
        elif workflow_execution["execution_resource"] == "NERSC-Perlmutter":
            workflow_execution["processing_institution"] = "NMDC"
        elif workflow_execution["execution_resource"] == "EMSL-RZR":
            workflow_execution["processing_institution"] = "NMDC"
        elif workflow_execution["execution_resource"] == "NERSC-Cori":
            workflow_execution["processing_institution"] = "NMDC"
        else:
             raise ValueError(
                 f"No migration action defined for {workflow_execution['id']}"
             )
        return workflow_execution
