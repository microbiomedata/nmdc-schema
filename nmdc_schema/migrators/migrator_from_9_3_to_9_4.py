from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates data between two schema versions."""

    _from_version = "9.3"
    _to_version = "9.4"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._agenda = dict(
            extraction_set=[self.move_extraction_qc_status],
        )

    def move_extraction_qc_status(self, extraction: dict) -> dict:
        r"""
        Move quality_control_report.status to qc_status

        >>> m = Migrator()
        >>> m.move_extraction_qc_status({'id': 123, 'quality_control_report': {'status': 'pass'}})
        {'id': 123, 'qc_status': 'pass'}
        """
        self.logger.info(f"Starting migration of {extraction['id']}")
        if "quality_control_report" in extraction:
            if "status" in extraction["quality_control_report"]:
                extraction["qc_status"] = extraction["quality_control_report"]["status"]
                del extraction["quality_control_report"]["status"]
                del extraction["quality_control_report"]
        return extraction
