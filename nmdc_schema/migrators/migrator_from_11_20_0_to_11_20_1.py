from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: Since this migrator was created retroactively, we can include a link to the release notes as evidence that
          no migration is necessary. Release notes: https://github.com/microbiomedata/nmdc-schema/releases/tag/v11.20.1
    """

    _from_version = "11.20.0"
    _to_version = "11.20.1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""No upgrade needed."""
        pass
