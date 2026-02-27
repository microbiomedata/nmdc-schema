from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.14.0"
    _to_version = "11.15.1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""No upgrade needed."""
        pass
