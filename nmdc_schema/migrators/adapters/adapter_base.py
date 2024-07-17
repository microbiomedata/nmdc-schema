from abc import ABC, abstractmethod
from typing import Optional, Callable, List, Any, Union


class AdapterBase(ABC):
    r"""
    Abstract base class containing method stubs related to manipulating a "database" represented by either
    a Python data dictionary or a MongoDB database.
    """

    def __init__(
        self,
        on_collection_created: Optional[Callable[[str], Any]] = None,
        on_collection_renamed: Optional[Callable[[str, str], Any]] = None,
        on_collection_deleted: Optional[Callable[[str], Any]] = None,
    ):
        r"""
        Binds callback functions to the class instance.

        Note: This is a "concrete" method within an "abstract" class.

        :param on_collection_created: Callback function that will be invoked after a collection is created.
                                      It will be passed the name of the collection.
        :param on_collection_renamed: Callback function that will be invoked after a collection is renamed.
                                      It will be passed the original name and new name of the collection.
        :param on_collection_deleted: Callback function that will be invoked after a collection is deleted.
                                      It will be passed the name of the collection.
        """
        self.on_collection_created = on_collection_created
        self.on_collection_renamed = on_collection_renamed
        self.on_collection_deleted = on_collection_deleted

    @abstractmethod
    def create_collection(self, collection_name: str) -> None:
        r"""
        Creates an empty collection having the specified name, if no collection by that name exists.
        Also invokes `self.on_collection_created`, if defined, passing to it the name of the collection.
        """
        pass

    @abstractmethod
    def rename_collection(self, current_name: str, new_name: str) -> None:
        r"""
        Renames the specified collection, if it exists, so that it has the specified new name.
        Also invokes `self.on_collection_renamed`, if defined, passing to it the old and new names of the collection.
        """
        pass

    @abstractmethod
    def delete_collection(self, collection_name: str) -> None:
        r"""
        Deletes the collection having the specified name, if such a collection exists.
        Also invokes `self.on_collection_deleted`, if defined, passing to it the name of the collection.
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

    @abstractmethod
    def set_field_of_each_document(
        self, collection_name: str, field_name: str, value: Union[None, str, int, float, bool],
    ) -> None:
        r"""
        Assigns the specified value to the specified field of each document in the collection.
        This method is a specialized alternative to the `process_each_document` method.
        """
        pass

    @abstractmethod
    def do_for_each_document(
        self, collection_name: str, action: Callable[[dict], None]
    ) -> None:
        r"""
        Passes each document in the specified collection to the specified function. This method was designed
        to facilitate iterating over all documents in a collection without actually modifying them.
        """
        pass
