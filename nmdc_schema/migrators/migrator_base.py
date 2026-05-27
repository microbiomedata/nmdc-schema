from abc import ABC, abstractmethod
from typing import Dict, List
from logging import getLogger
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase


class MigratorBase(ABC):
    """Base class containing properties and methods related to migrating data between two schema versions."""

    # The schema version from which this class migrates data.
    #
    # Note: This string is empty here. It will be populated within the migration-specific classes.
    #
    _from_version: str = ""

    # The schema version to which this class migrates data.
    #
    # Note: This string is empty here. It will be populated within the migration-specific classes.
    #
    _to_version: str = ""

    def __init__(self, adapter: AdapterBase = None, logger = None):
        """
        Initializes the migrator with an adapter and a logger.

        """
        # Store a reference to the specified adapter. Migrator methods can use it to manipulate the database.
        self.adapter = adapter

        # If a logger was specified, use it; otherwise, initialize one and use that.
        self.logger = getLogger(__name__) if logger is None else logger

        if self.adapter is None:
            self.logger.warning("No adapter was specified. Migration capability will be limited.")
    
    def _warn_if_commit_ignored(self, commit_changes: bool) -> None:
        """Warn if commit_changes=True but adapter doesn't support transactions.
        
        Examples:
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> import logging
        >>> logging.basicConfig(level=logging.WARNING, format='%(levelname)s:%(message)s')
        >>> 
        >>> # Create a test migrator with dictionary adapter
        >>> class TestMigrator(MigratorBase):
        ...     _from_version = "test.1"
        ...     _to_version = "test.2"
        ...     def upgrade(self, commit_changes: bool = False) -> None:
        ...         self._warn_if_commit_ignored(commit_changes)
        >>> 
        >>> database = {"test_set": []}
        >>> adapter = DictionaryAdapter(database)
        >>> migrator = TestMigrator(adapter=adapter)
        >>> 
        >>> # Test with commit_changes=False (no warning)
        >>> migrator._warn_if_commit_ignored(False)
        >>> 
        >>> # Test with commit_changes=True (should warn) - output will be captured
        >>> migrator._warn_if_commit_ignored(True)  # doctest: +SKIP
        """
        if commit_changes:
            from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
            if not isinstance(self.adapter, MongoAdapter):
                self.logger.warning(
                    "commit_changes=True was specified, but the current adapter does not support transactions. "
                    "All changes will be applied immediately and cannot be rolled back. "
                    "Use MongoAdapter for transaction support."
                )

    @abstractmethod
    def upgrade(self, commit_changes: bool = False):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema.
        
        Args:
            commit_changes: If True, commits the changes. If False (default), performs a dry run or rollback.
        """
        pass

    @classmethod
    def get_origin_version(cls) -> str:
        """Returns the schema version this class migrates data from."""
        return cls._from_version

    @classmethod
    def get_destination_version(cls) -> str:
        """Returns the schema version this class migrates data to."""
        return cls._to_version

