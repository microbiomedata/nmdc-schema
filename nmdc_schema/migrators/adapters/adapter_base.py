from abc import ABC, abstractmethod
from typing import Optional, Callable, List


class AdapterBase(ABC):
    r"""
    Abstract base class containing method stubs related to manipulating a "database" represented by either
    a Python data dictionary or a MongoDB database.
    """

    @abstractmethod
    def create_collection(self, collection_name: str) -> None:
        r"""
        Creates an empty collection having the specified name, if no collection by that name exists.
        """
        pass

    @abstractmethod
    def rename_collection(self, current_name: str, new_name: str) -> None:
        r"""
        Renames the specified collection so that it has the specified name.
        """
        pass

    @abstractmethod
    def delete_collection(self, collection_name: str) -> None:
        r"""
        Deletes the collection having the specified name.
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
    def delete_document_by_nmdc_id(self, collection_name: str, nmdc_id: str) -> int:
        r"""
        Deletes all documents having the specified `id` value, from the collection having the specified name,
        and returns the number of documents deleted.
        """
        pass

    @abstractmethod
    def insert_document(self, collection_name: str, document: dict) -> None:
        r"""
        Inserts the specified document into the collection having the specified name.
        """
        pass

    @abstractmethod
    def process_each_document(
        self, collection_name: str, pipeline: List[Callable[[dict], dict]]
    ) -> None:
        r"""
        Passes each document in the specified collection through the specified processing pipeline—in which
        the output of any given function is the input to the function after it—and stores the final output
        back in the collection, replacing the original document.
        """
        pass
