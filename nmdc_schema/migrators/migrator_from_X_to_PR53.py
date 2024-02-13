from nmdc_schema.migrators.migrator_base import MigratorBase
import re


class Migrator(MigratorBase):
    """Migrates data from schema X to PR53"""

    _from_version = "X"
    _to_version = "PR53"
    
    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document(collection_name="omics_processing_set",
                                           pipeline=[self.move_part_of_to_associated_studies])
        self.adapter.process_each_document(collection_name="biosample_set",
                                           pipeline=[self.move_part_of_to_associated_studies])

    def move_part_of_to_associated_studies(self, doc: dict):
        r"""
        Moves `part_of` values that are studies and moves them into a new slot called `associated_studies`
        
        >>> m = Migrator()
        >>> m.move_part_of_to_associated_studies({'id': 123, 'part_of': ['gold:Gs0114663', 'nmdc:sty-55-xxx']})
        {'id': 123, 'associated_studies': ['gold:Gs0114663', 'nmdc:sty-55-xxx']}
        >>> m.move_part_of_to_associated_studies({'id': 123})  # lacks `part_of` key
        {'id': 123, 'associated_studies': []}
        """

        # Create and initialize the "associated_studies" field on the document.
        doc["associated_studies"] = []

        # If the document has a "part_of" field, move its studies to the "associated_studies" field,
        # then delete the "part_of" field.
        if "part_of" in doc:
            studies = doc["part_of"]
            for study in studies:
                doc["associated_studies"].append(study)
            del doc["part_of"]

        return doc
