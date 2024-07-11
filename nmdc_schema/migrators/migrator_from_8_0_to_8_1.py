from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "8.0"
    _to_version = "8.1"

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("study_set", [self.force_research_study_study_category])

    def force_research_study_study_category(self, study: dict) -> dict:
        r"""
        If the study lacks a field named `study_category`, creates it and assigns it the value "research_study".

        >>> m = Migrator()
        >>> m.force_research_study_study_category({'id': 123})  # field doesn't exist yet
        {'id': 123, 'study_category': 'research_study'}
        >>> m.force_research_study_study_category({'id': 123, 'study_category': 'preserve_me'})  # field already exists
        {'id': 123, 'study_category': 'preserve_me'}
        """

        if "study_category" not in study:
            self.logger.info(f"Forcing 'study_category: research_study' on {study['id']}")
            study["study_category"] = "research_study"
        return study
