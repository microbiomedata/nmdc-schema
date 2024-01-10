from abc import ABC, abstractmethod
from typing import Optional


class AdapterBase(ABC):
    r"""
    Abstract base class containing method stubs related to manipulating a "database" represented by either
    a Python data dictionary or a MongoDB database.
    """

    @abstractmethod
    def rename_collection(
        self, current_collection_name: str, new_collection_name: str
    ) -> None:
        r"""
        Renames the specified collection so that it has the specified name.
        """
        pass

    @abstractmethod
    def get_document_by_nmdc_id(
        self, collection_name: str, nmdc_id: str
    ) -> Optional[dict]:
        r"""
        Retrieves the document having the specified `id` value, from the collection having the specified name.
        """
        pass

    @abstractmethod
    def insert_document(self, collection_name: str, document: dict) -> None:
        r"""
        Inserts the specified document into the collection having the specified name.
        """
        pass
