from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_10_0_to_11_11_0 import (
    get_migrator_classes,
)


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.
    """

    _from_version = "11.10.0"
    _to_version = "11.11.0"

    def upgrade(self, commit_changes: bool = False) -> None:
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        This migrator uses partial migrators. It runs them in the order in which they are returned by
        the `get_migrator_classes` function.
        
        Args:
            commit_changes: If True, commits the changes. If False (default), performs a dry run or rollback.
        """

        migrator_classes = get_migrator_classes()
        num_migrators = len(migrator_classes)
        for idx, migrator_class in enumerate(migrator_classes):
            self.logger.info(f"Running migrator {idx + 1} of {num_migrators}")
            self.logger.debug(
                f"Migrating from {migrator_class.get_origin_version()} "
                f"to {migrator_class.get_destination_version()}"
            )
            migrator = migrator_class(adapter=self.adapter, logger=self.logger)
            migrator.upgrade(commit_changes=commit_changes)
