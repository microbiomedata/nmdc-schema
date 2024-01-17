from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "9.3"
    _to_version = "9.4"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(
            "extraction_set", [self.move_extraction_qc_status]
        )

    def move_extraction_qc_status(self, extraction: dict) -> dict:
        r"""
        Move quality_control_report.status to qc_status

        >>> m = Migrator()
        >>> m.move_extraction_qc_status({'id': 123, 'quality_control_report': {'status': 'pass'}})
        {'id': 123, 'qc_status': 'pass'}
        >>> m.move_extraction_qc_status({'id': 123, 'quality_control_report': {'status': 'fail'}})
        {'id': 123, 'qc_status': 'fail'}
        >>> m.move_extraction_qc_status({'id': 123, 'quality_control_report': {'name': 'qcr', 'status': 'pass'}})  # discards name
        {'id': 123, 'qc_status': 'pass'}
        >>> m.move_extraction_qc_status({'id': 123, 'quality_control_report': {}})  # no change
        {'id': 123, 'quality_control_report': {}}
        """
        self.logger.info(f"Starting migration of {extraction['id']}")
        if "quality_control_report" in extraction:
            if "status" in extraction["quality_control_report"]:
                extraction["qc_status"] = extraction["quality_control_report"]["status"]
                del extraction["quality_control_report"]["status"]
                del extraction["quality_control_report"]
        return extraction
