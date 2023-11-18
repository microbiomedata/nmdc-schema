from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator_from_8_0_to_8_1(MigratorBase):
    """previously: Migrates data from schema 8.0.0 to 8.1.0"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.force_research_study_study_category],
        )

    def force_research_study_study_category(self, study: dict) -> dict:
        r"""
        If the study lacks a field named `study_category`, creates it and assigns it the value "research_study".

        >>> m = Migrator_from_8_0_to_8_1()
        >>> m.force_research_study_study_category({'id': 123})  # field doesn't exist yet
        {'id': 123, 'study_category': 'research_study'}
        >>> m.force_research_study_study_category({'id': 123, 'study_category': 'preserve_me'})  # field already exists
        {'id': 123, 'study_category': 'preserve_me'}
        """

        if "study_category" not in study:
            self.logger.info(f"Forcing 'study_category: research_study' on {study['id']}")
            study["study_category"] = "research_study"
        return study
