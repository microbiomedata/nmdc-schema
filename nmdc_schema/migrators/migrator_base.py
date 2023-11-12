from typing import Dict, List
from logging import getLogger


class MigratorBase:
    """Base class containing properties and methods related to migrating data between schema versions."""

    def __init__(self, logger=None):
        # If a logger was specified, use it; otherwise, initialize one and use that.
        self.logger = getLogger(__name__) if logger is None else logger

        # Define the "agenda" of transformations that constitute this migration.
        #
        # Note: This is a dictionary that maps a given collection to a list of "transformation" functions.
        #       Each key is a collection name, and each value is a list. Each element of the list is a
        #       so-called "transformation" function. A "transformation" function is a function that
        #       transforms something from one schema version to another. In this case, the "something"
        #       is a dictionary representing a single document from the specified collection.
        #
        # Note: This dictionary is empty here. It will be populated within the "constructor" functions
        #       of the migration-specific classes (i.e. the classes that inherit from this base class).
        #
        self.agenda: Dict[str, List[callable]] = dict()

    def get_transformers_for(self, collection_name: str) -> List[callable]:
        """Returns the list of transformers defined for the specified collection."""
        return self.agenda.get(collection_name, [])
