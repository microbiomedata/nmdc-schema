from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.partials.migrator_from_11_24_1_to_11_25_0 import (
    get_migrator_classes,
)


class Migrator(MigratorBase):
    r"""
    Migrates a database between two schemas.

    Partial 1 raises if any Biosample still has ``collection_time_inc``, which was removed in
    nmdc-schema#3470. It changes nothing (nmdc-schema#3489).
    """

    _from_version = "11.24.1"
    _to_version = "11.25.0"

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
