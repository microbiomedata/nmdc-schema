from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Note: No migration is necessary. The 11.20.2 to 11.20.3 schema changes are purely additive: new
          library-preparation slots and enums, plus a DataObject rule whose precondition is a new
          data_object_type value, so no data valid under 11.20.2 becomes invalid under 11.20.3.
          Release notes: https://github.com/microbiomedata/nmdc-schema/releases/tag/v11.20.3
    """

    _from_version = "11.20.2"
    _to_version = "11.20.3"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""No upgrade needed."""
        pass
