from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: No migration is necessary.
    """

    _from_version = "11.21.0"
    _to_version = "11.22.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""No upgrade needed."""
        pass
