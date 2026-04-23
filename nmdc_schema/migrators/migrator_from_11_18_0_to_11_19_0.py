import re
from typing import Dict, List

from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator(MigratorBase):
    r"""Migrates a database between two schemas."""

    _from_version = "11.18.0"
    _to_version = "11.19.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.
        """

        # List of collection names that we want the migration orchestration notebook to validate.
        self._collection_names = [
            "workflow_execution_set",
        ]

        # Note: This migrator does not perform any transformations. It also doesn't perform any
        #       validation (or "checks"), itself.
        # 
        #       However, it does contain the above list of the names of collections whose
        #       documents we want the migration orchestration notebook to validate during the
        #       migration process.
        # 
        #       This is a stopgap solution for while the following issue is unresolved:
        #       https://github.com/microbiomedata/nmdc-schema/issues/2674
        pass
