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
    def insert_document(self, collection_name: str, document: dict) -> None:
        r"""
        Inserts the specified document into the collection having the specified name.
        """
        pass

    @abstractmethod
    def get_document_having_value_in_field(
        self, collection_name: str, field_name: str, value: str
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having the specified value in the specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).
        """
        pass

    @abstractmethod
    def get_document_having_one_of_values_in_field(
        self, collection_name: str, field_name: str, values: List[str]
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having any one of the specified values in the
        specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).
        """
        pass

    @abstractmethod
    def delete_documents_having_value_in_field(
        self, collection_name: str, field_name: str, value: str
    ) -> int:
        r"""
        Deletes all documents from the specified collection, having the specified value in the specified field;
        and returns the number of documents that were deleted.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).
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
