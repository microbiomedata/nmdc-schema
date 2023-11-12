import logging
from .migrator_base import MigratorBase


logger = logging.getLogger(__name__)


class Migrator_from_8_0_to_8_1(MigratorBase):
    """previously: Migrates data from schema 8.0.0 to 8.1.0"""

    def __init__(self) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__()

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.force_research_study_study_category],
        )

    def force_research_study_study_category(self, study: dict) -> dict:
        if "study_category" not in study:
            logger.info(f"Forcing 'study_category: research_study' on {study['id']}")
            study["study_category"] = "research_study"
        return study
