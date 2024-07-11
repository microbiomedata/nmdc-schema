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

    def __init__(self, adapter: AdapterBase = None, logger=None):
        # Store a reference to the specified adapter. Migrator methods can use it to manipulate the database.
        self.adapter = adapter

        # If a logger was specified, use it; otherwise, initialize one and use that.
        self.logger = getLogger(__name__) if logger is None else logger

        if self.adapter is None:
            self.logger.warning("No adapter was specified. Migration capability will be limited.")

    @abstractmethod
    def upgrade(self):
        r"""Migrates the database from conforming to the original schema, to conforming to the new schema."""
        pass

    @classmethod
    def get_origin_version(cls) -> str:
        """Returns the schema version this class migrates data from."""
        return cls._from_version

    @classmethod
    def get_destination_version(cls) -> str:
        """Returns the schema version this class migrates data to."""
        return cls._to_version

