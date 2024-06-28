from typing import List
from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    """
    Migrates data from X to PR192, makes the existing extraction_target slot multivalued and change its name to extraction_targets

    Should be run after migrator_from_10_2_0_to_11_0_0_part_09.py.
    """

    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""

        self.adapter.process_each_document("extraction_set", [self.rename_extraction_target])

    def rename_extraction_target(self, extraction: dict) -> dict:
        r"""
        Renames the `extraction_target` field to `extraction_targets` and makes it multivalued.

        >>> m = Migrator()
        >>> m.rename_extraction_target({'id': 123})  # no `extraction_target` field
        {'id': 123}
        >>> m.rename_extraction_target({'id': 123, 'extraction_target': 'DNA'})  # test: renames field and casts it as a list value
        {'id': 123, 'extraction_targets': ['DNA']}
        """

        self.logger.info(f"Starting migration of {extraction['id']}")
        if "extraction_target" in extraction:
            extraction["extraction_targets"] = [extraction.pop("extraction_target")]
        return extraction