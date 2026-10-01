from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    No migration is necessary. Every database valid under 11.24.0 is valid under 11.24.1, because
    the only schema changes add a permissible value or change text (descriptions and titles), and
    none of them changes what data is valid:

    - Adds the ``SeqCenter`` permissible value to ``ProcessingInstitutionEnum`` (nmdc-schema#3436).
    - Rewrites the description of the ``badges`` slot (nmdc-schema#3442). It drops the claim that
      badges are recalculated when ``ProvenanceMetadata.mod_date`` changes and records the metadata
      quality squad's 2026-09-16 decision that awarding is additive (microbiomedata/issues#1820).
    - Adds titles to the ``MetadataBadgeEnum`` permissible values (nmdc-schema#3456).
    - Adds titles to 35 slots used by ``Biosample`` (nmdc-schema#3451). Titles are display text only.

    Nothing was removed, renamed, narrowed, or made required.
    """

    _from_version = "11.24.0"
    _to_version = "11.24.1"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""No upgrade needed."""
        pass
