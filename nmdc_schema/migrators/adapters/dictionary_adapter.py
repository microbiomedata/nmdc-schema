from typing import Optional
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

    def rename_collection(
        self, current_collection_name: str, new_collection_name: str
    ) -> None:
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
        self._db[new_collection_name] = self._db.pop(current_collection_name)

    def get_document_by_nmdc_id(
        self, collection_name: str, nmdc_id: str
    ) -> Optional[dict]:
        r"""
        Retrieves the document having the specified `id` value, from the collection having the specified name.

        >>> database = {
        ...   "thing_set": [
        ...     {"id": "111", "foo": "bar"},
        ...     {"id": "222", "foo": "baz"},
        ...     {"id": "333", "foo": "qux"}
        ...   ]
        ... }
        >>> da = DictionaryAdapter(database)
        >>> da.get_document_by_nmdc_id("thing_set", "222")
        {'id': '222', 'foo': 'baz'}
        >>> da.get_document_by_nmdc_id("thing_set", "444") is None
        True
        """
        # Create a "generator expression" over which we can iterate via `next`.
        #
        # Note: You can think of a "generator expression" as a list comprehension that doesn't
        #       create the entire list in memory.
        #
        # Reference: https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
        #
        document_generator = (
            d for d in self._db[collection_name] if d.get("id") == nmdc_id
        )

        # Return the first document yielded by the generator (or `None` if the generator doesn't yield one).
        document = next(document_generator, None)
        return document

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
