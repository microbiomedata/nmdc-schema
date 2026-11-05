from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas.

    No migration is needed between 11.25.0 and 11.26.0.
    """

    _from_version = "11.25.0"
    _to_version = "11.26.0"

    def upgrade(self) -> None:
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        pass
