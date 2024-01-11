from copy import deepcopy
from typing import Optional, Callable, List
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase


class DictionaryAdapter(AdapterBase):
    r"""
    Class containing methods related to manipulating a "database" represented by
    a Python dictionary.
    """

    def __init__(self, database: dict) -> None:
        r"""
        Initializes the reference to the database this instance will be used to manipulate.
        """
        self._db = database

    def create_collection(self, collection_name: str) -> None:
        r"""
        Creates an empty collection having the specified name, if no collection by that name exists.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.create_collection("thing_set")
        >>> "thing_set" in database
        True
        >>> len(database["thing_set"])  # existing collection will retain existing contents
        3
        >>> da.create_collection("item_set")
        >>> "item_set" in database
        True
        >>> len(database["item_set"])  # new collection will be empty
        0
        """
        if collection_name not in self._db:
            self._db[collection_name] = []

    def rename_collection(self, current_name: str, new_name: str) -> None:
        r"""
        Renames the specified collection so that it has the specified name.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.rename_collection("thing_set", "item_set")
        >>> "thing_set" in database
        False
        >>> "item_set" in database
        True
        """
        self._db[new_name] = self._db.pop(current_name)

    def delete_collection(self, collection_name: str) -> None:
        r"""
        Deletes the collection having the specified name.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.delete_collection("thing_set")
        >>> "thing_set" in database
        False
        """
        del self._db[collection_name]

    def get_document_having_value_in_field(
        self, collection_name: str, field_name: str, value: str
    ) -> Optional[dict]:
        r"""
        Retrieves the document from the specified collection, having the specified value in the specified field.

        Note: This only support top-level fields (e.g. `_id`), not nested fields (e.g. `area.height`).

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.get_document_having_value_in_field("thing_set", "id", "222")
        {'id': '222', 'foo': 'baz'}
        >>> da.get_document_having_value_in_field("thing_set", "foo", "baz")
        {'id': '222', 'foo': 'baz'}
        >>> da.get_document_having_value_in_field("thing_set", "id", "444") is None
        True
        >>> da.get_document_having_value_in_field("thing_set", "missing", "111") is None
        True
        """
        try:
            # Create a "generator expression" over which we can iterate via `next`.
            #
            # Note: You can think of a "generator expression" as a list comprehension that doesn't
            #       create the entire list in memory.
            #
            # Reference: https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
            #
            document_generator = (
                d for d in self._db[collection_name] if d.get(field_name) == value
            )

            # Return the first document yielded by the generator (or `None` if the generator doesn't yield one).
            document = next(document_generator, None)
        except KeyError:
            document = None

        return document

    def delete_document_by_nmdc_id(self, collection_name: str, nmdc_id: str) -> int:
        r"""
        Deletes all documents having the specified `id` value, from the collection having the specified name,
        and returns the number of documents deleted.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "222", "foo": "blue"},  # same id, so that we can...
        ...     {"id": "222", "foo": "blue"},  # ...test deleting multiple.
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> len(database["thing_set"])
        5
        >>> da.delete_document_by_nmdc_id("thing_set", "no_such_id")
        0
        >>> len(database["thing_set"])
        5
        >>> da.delete_document_by_nmdc_id("thing_set", "222")  # deletes 3 documents
        3
        >>> len(database["thing_set"])  # 2 documents remain
        2
        """
        # Filter out the matching documents.
        # Reference: https://docs.python.org/3/library/functions.html#filter
        documents_initial = self._db[collection_name]
        document_generator = filter(lambda d: d.get("id") != nmdc_id, documents_initial)
        documents_remaining = list(document_generator)

        # Update the collection so that it consists of the filtered result.
        self._db[collection_name] = documents_remaining

        # Return the number of documents that were deleted.
        num_documents_deleted = len(documents_initial) - len(documents_remaining)
        return num_documents_deleted

    def insert_document(self, collection_name: str, document: dict) -> None:
        r"""
        Inserts the specified document into the collection having the specified name.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.insert_document("thing_set", {"id": "444", "foo": "dee"})
        >>> database["thing_set"][-1]  # gets last item in list
        {'id': '444', 'foo': 'dee'}
        """
        self._db[collection_name].append(document)

    def process_each_document(
        self, collection_name: str, pipeline: List[Callable[[dict], dict]]
    ) -> None:
        r"""
        Passes each document in the specified collection through the specified processing pipeline—in which
        the output of any given function is the input to the function after it—and stores the final output
        back in the collection, replacing the original document.

        Reference: https://docs.python.org/3/library/copy.html#copy.deepcopy

        >>> def capitalize_foo_value(document: dict) -> dict:
        ...     document["foo"] = document["foo"].upper()
        ...     return document
        >>>
        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.process_each_document("thing_set", [capitalize_foo_value])
        >>> database["thing_set"][0]
        {'id': '111', 'foo': 'BAR'}
        >>> database["thing_set"][1]
        {'id': '222', 'foo': 'BAZ'}
        """

        # Iterate over every document in the collection.
        for index, original_document in enumerate(self._db[collection_name]):
            # Make a copy of the original document.
            #
            # Note: This isn't technically necessary (we could modify the original document in place
            #       while it resides in the Python array), but this keeps the algorithm analogous to
            #       what I expect its "real database" (e.g. MongoDB) counterparts to be.
            #
            processed_document = deepcopy(original_document)

            # "Pass" the document through the functions (i.e. "stages") that make up the pipeline,
            # such that the output from one stage becomes the input to the next stage.
            for function in pipeline:
                processed_document = function(processed_document)

            # Overwrite the original document with the processed one.
            self._db[collection_name][index] = processed_document
