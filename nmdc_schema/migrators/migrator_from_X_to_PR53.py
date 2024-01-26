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

        # compare the values in the part_of slot with the newly moved values in the associated_studies slot and remove
        # from the part_of slot if it exist in the associated_studies slot. If part_of it empty, delete slot entirely.
        doc["part_of"] = [item for item in doc["part_of"] if item not in doc["associated_studies"]]
        if not doc["part_of"]:
            doc.pop("part_of")
        
        return doc