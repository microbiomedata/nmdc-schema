from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: This is a "no op" migrator. Its existence serves as documentation that no
          database migration is necessary between the specified schema versions.
    """

    _from_version = "11.0.3"
    _to_version = "11.1.0"

    def upgrade(self) -> None:
        r"""Do nothing."""
        pass