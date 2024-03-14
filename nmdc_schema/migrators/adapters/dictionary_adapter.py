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
        Initializes the reference to the database this adapter instance will be used to manipulate.
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

    def get_document_having_value_in_field(
            self, collection_name: str, field_name: str, value: str
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having the specified value in the specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

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
        >>> da.get_document_having_value_in_field("thing_set", "id", "no_such_value") is None
        True
        >>> da.get_document_having_value_in_field("thing_set", "no_such_field", "111") is None
        True
        """
        try:
            # Create a generator over which we can iterate via `next`.
            #
            # Note: A generator is a special type of iterator. We create it here via a so-called "generator expression".
            #       You can think of a "generator expression" as a list comprehension that doesn't involve loading the
            #       entire sequence into memory.
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

    def get_document_having_one_of_values_in_field(
            self, collection_name: str, field_name: str, values: List[str]
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having any one of the specified values in the
        specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.get_document_having_one_of_values_in_field("thing_set", "id", ["221", "222", "223"])
        {'id': '222', 'foo': 'baz'}
        >>> da.get_document_having_one_of_values_in_field("thing_set", "foo", ["baa", "baz", "bab"])
        {'id': '222', 'foo': 'baz'}
        >>> da.get_document_having_one_of_values_in_field("thing_set", "id", ["no_such_value"]) is None
        True
        >>> da.get_document_having_one_of_values_in_field("thing_set", "foo", []) is None  # no values to match with
        True
        """
        try:
            # Create a generator over which we can iterate via `next`.
            document_generator = (
                d for d in self._db[collection_name] if d.get(field_name) in values
            )

            # Return the first document yielded by the generator (or `None` if the generator doesn't yield one).
            document = next(document_generator, None)
        except KeyError:
            document = None

        return document

    def delete_documents_having_value_in_field(self, collection_name: str, field_name: str, value: str) -> int:
        r"""
        Deletes all documents from the specified collection, having the specified value in the specified field;
        and returns the number of documents that were deleted.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

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
        >>> da.delete_documents_having_value_in_field("thing_set", "id", "no_such_value")
        0
        >>> da.delete_documents_having_value_in_field("thing_set", "no_such_field", "111")
        0
        >>> len(database["thing_set"])
        5
        >>> da.delete_documents_having_value_in_field("thing_set", "id", "222")  # deletes 3 documents
        3
        >>> len(database["thing_set"])
        2
        >>> da.delete_documents_having_value_in_field("thing_set", "foo", "qux")
        1
        >>> len(database["thing_set"])
        1
        """
        # Filter out the documents having the specified value in the specified field.
        # Reference: https://docs.python.org/3/library/functions.html#filter
        documents_initial = self._db[collection_name]
        document_generator = filter(lambda d: field_name not in d or d.get(field_name) != value, documents_initial)
        documents_remaining = list(document_generator)

        # Update the collection so that it consists of the filtered result.
        self._db[collection_name] = documents_remaining

        # Return the number of documents that were deleted.
        num_documents_deleted = len(documents_initial) - len(documents_remaining)
        return num_documents_deleted

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
        >>> da.process_each_document("missing_set", [capitalize_foo_value])  # non-existent collection does not trigger an exception
        """

        # Iterate over every document in the collection, if the collection exists.
        if collection_name in self._db:
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
