from nmdc_schema.migrators.migrator_base import MigratorBase
import re

class Migrator_from_X_to_PR53(MigratorBase):
    """Migrates data from schema X to PR53"""

    def __init__(self, *args, **kwargs) -> None:
        """Invokes parent constructor and populates collection-to-transformations map."""

        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            omics_processing_set=[self.move_part_of_to_associated_studies],
            biosample_set=[self.move_part_of_to_associated_studies],
        )

    def move_part_of_to_associated_studies(self, doc: dict):
        r"""
        Moves `part_of` values that are studies and moves them into a new slot called `associated_studies`
        
        >>> m = Migrator_from_X_to_PR53()
        >>> m.move_part_of_to_associated_studies({'id': 123, 'part_of': ['gold:Gs0114663', 'nmdc:sty-55-xxx']})
        {'id': 123, 'associated_studies': ['gold:Gs0114663', 'nmdc:sty-55-xxx']}
        """

        studies = doc["part_of"]
        doc["associated_studies"] = []
        for study in studies:
            doc["associated_studies"].append(study)
        
        doc.pop("part_of")
        
        return doc