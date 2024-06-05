import unittest
from typing import Optional

from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter


class TestDictionaryAdapter(unittest.TestCase):
    r"""
    Tests targeting the `DictionaryAdapter` class.

    You can run these tests like this:
    $ poetry run python -m unittest -v nmdc_schema/migrators/adapters/test_dictionary_adapter.py

    References:
    - https://docs.python.org/3/library/unittest.html#basic-example
    - https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    """

    db: Optional[dict] = None

    def setUp(self) -> None:
        r"""
        Gets a reference to the database.

        Note: This function runs before each test starts.
        """
        self.db = dict()

    def tearDown(self) -> None:
        r"""
        Relinquishes the reference to the database.

        Note: This function runs after each test finishes.
        """
        self.db = None

    def test_create_collection(self):
        # Set up:
        collection_name = "my_collection"

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.create_collection(collection_name)

        # Validate result:
        assert len(self.db.keys()) == 1
        assert collection_name in self.db

    def test_rename_collection(self):
        # Set up:
        collection_name_original = "my_collection"
        collection_name_target = "your_collection"
        self.db[collection_name_original] = []
        assert len(self.db.keys()) == 1

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.rename_collection(collection_name_original, collection_name_target)

        # Validate result:
        assert len(self.db.keys()) == 1
        assert collection_name_target in self.db

    def test_delete_collection(self):
        # Set up:
        collection_name = "my_collection"
        self.db[collection_name] = []
        assert len(self.db.keys()) == 1

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.delete_collection(collection_name)

        # Validate result:
        assert len(self.db.keys()) == 0

    def test_insert_document(self):
        # Set up:
        collection_name = "my_collection"
        document = dict(id=123, foo="bar")
        self.db[collection_name] = []
        assert len(self.db[collection_name]) == 0

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.insert_document(collection_name, document)

        # Validate result:
        assert len(self.db[collection_name]) == 1
        document_actual = self.db[collection_name][0]
        for k, v in document.items():
            assert v == document_actual[k]

    def test_get_document_having_value_in_field(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(id=1, x="a")
        document_2 = dict(id=2, x="b")
        document_3 = dict(id=3, x="c")
        self.db[collection_name] = []
        self.db[collection_name].extend([document_1, document_2, document_3])
        assert len(self.db[collection_name]) == 3

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        document_actual = adapter.get_document_having_value_in_field(
            collection_name, "x", "b"
        )

        # Validate result:
        for k, v in document_2.items():
            assert v == document_actual[k]

    def test_get_document_having_one_of_values_in_field(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(id=1, x="a")
        document_2 = dict(id=2, x="b")
        document_3 = dict(id=3, x="c")
        self.db[collection_name] = []
        self.db[collection_name].extend([document_1, document_2, document_3])
        assert len(self.db[collection_name]) == 3

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        document_actual = adapter.get_document_having_one_of_values_in_field(
            collection_name, "x", ["n", "b", "m"]
        )

        # Validate result:
        for k, v in document_2.items():
            assert v == document_actual[k]

    def test_delete_documents_having_value_in_field(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(id=1, x="a")
        document_2 = dict(id=2, x="b")
        document_3 = dict(id=3, x="c")
        document_4 = dict(id=4, x="b")  # note: x="b" here also
        self.db[collection_name] = []
        self.db[collection_name].extend(
            [document_1, document_2, document_3, document_4]
        )
        assert len(self.db[collection_name]) == 4

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        num_documents_deleted = adapter.delete_documents_having_value_in_field(
            collection_name, "x", "b"
        )

        # Validate result:
        collection = self.db[collection_name]
        assert num_documents_deleted == 2
        assert len(self.db[collection_name]) == 2
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "a"]) == 1
        assert len([doc for doc in collection if doc["id"] == 2 and doc["x"] == "b"]) == 0
        assert len([doc for doc in collection if doc["id"] == 3 and doc["x"] == "c"]) == 1
        assert len([doc for doc in collection if doc["id"] == 4 and doc["x"] == "b"]) == 0

    def test_process_each_document(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(_id=1, id=1, x="a")
        document_2 = dict(_id=2, id=2, x="b")
        document_3 = dict(_id=3, id=3, x="c")
        self.db[collection_name] = []
        self.db[collection_name].extend(
            [document_1, document_2, document_3]
        )
        assert len(self.db[collection_name]) == 3

        def capitalize_x(doc: dict) -> dict:
            r"""Example pipeline stage that capitalizes the first letter of the `x` value."""
            doc["x"] = doc["x"].capitalize()
            return doc

        def append_z_to_x_value(doc: dict) -> dict:
            r"""Example pipeline stage that appends "z" to the `x` value."""
            doc["x"] = doc["x"] + "z"
            return doc

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.process_each_document(
            collection_name, [capitalize_x, append_z_to_x_value]
        )

        # Validate result:
        collection = self.db[collection_name]
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "a"]) == 0  # pre-pipeline
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "b"]) == 0
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "c"]) == 0
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "A"]) == 0  # mid-pipeline
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "B"]) == 0
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "C"]) == 0
        assert len([doc for doc in collection if doc["id"] == 1 and doc["x"] == "Az"]) == 1  # post-pipeline
        assert len([doc for doc in collection if doc["id"] == 2 and doc["x"] == "Bz"]) == 1
        assert len([doc for doc in collection if doc["id"] == 3 and doc["x"] == "Cz"]) == 1

    def test_set_field_of_each_document(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(_id=1, id=1, x="original")
        document_2 = dict(_id=2, id=2)
        document_3 = dict(_id=3, id=3, x=None)
        self.db[collection_name] = []
        self.db[collection_name].extend(
            [document_1, document_2, document_3]
        )
        assert len(self.db[collection_name]) == 3

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.set_field_of_each_document(
            collection_name, "x", "new"
        )

        # Validate result:
        collection = self.db[collection_name]
        assert len([doc for doc in collection if doc["x"] == "original"]) == 0
        assert len([doc for doc in collection if "x" not in doc]) == 0
        assert len([doc for doc in collection if doc["x"] is None]) == 0
        assert len([doc for doc in collection if doc["_id"] == 1 and doc["id"] == 1 and doc["x"] == "new"]) == 1
        assert len([doc for doc in collection if doc["_id"] == 2 and doc["id"] == 2 and doc["x"] == "new"]) == 1
        assert len([doc for doc in collection if doc["_id"] == 3 and doc["id"] == 3 and doc["x"] == "new"]) == 1

    def test_do_for_each_document(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(_id=1, id=1, x="a")
        document_2 = dict(_id=2, id=2, x="b")
        document_3 = dict(_id=3, id=3, x="c")
        self.db[collection_name] = [document_1, document_2, document_3]
        assert len(self.db[collection_name]) == 3
        # Temporarily add an attribute to this class instance so that
        # this test has something persistent it can modify and examine.
        self._characters = []

        def append_x_to_sequence(doc: dict) -> None:
            r"""Example pipeline stage that appends the `x` value to some list."""
            self._characters.append(doc["x"])

        # Invoke function-under-test:
        adapter = DictionaryAdapter(database=self.db)
        adapter.do_for_each_document(
            collection_name, append_x_to_sequence
        )

        # Validate result:
        # - The list consists of the `x` values from the documents in the collection.
        assert len(self._characters) == 3
        assert self._characters[0] == "a"
        assert self._characters[1] == "b"
        assert self._characters[2] == "c"
        # - The collection was not modified.
        collection = self.db[collection_name]
        assert len([doc for doc in collection if doc["_id"] == 1 and doc["id"] == 1 and doc["x"] == "a"]) == 1
        assert len([doc for doc in collection if doc["_id"] == 2 and doc["id"] == 2 and doc["x"] == "b"]) == 1
        assert len([doc for doc in collection if doc["_id"] == 3 and doc["id"] == 3 and doc["x"] == "c"]) == 1

        # Clean up:
        delattr(self, "_characters")

    def test_callbacks(self):
        # Set up:
        collection_name = "my_collection"
        new_collection_name = "my_new_collection"
        event_log: list[str] = []
        adapter = DictionaryAdapter(
            database=self.db,
            on_collection_created=lambda name: event_log.append(f"Created {name}"),
            on_collection_renamed=lambda old_name, name: event_log.append(f"Renamed {old_name} to {name}"),
            on_collection_deleted=lambda name: event_log.append(f"Deleted {name}"),
        )
        assert len(event_log) == 0

        # Trigger callback and validate latest message in event log:
        adapter.create_collection(collection_name)
        assert len(event_log) == 1
        assert event_log[0] == f"Created {collection_name}"

        # Trigger callback and validate latest message in event log:
        adapter.rename_collection(collection_name, new_collection_name)
        assert len(event_log) == 2
        assert event_log[1] == f"Renamed {collection_name} to {new_collection_name}"

        # Trigger callback and validate latest message in event log:
        adapter.delete_collection(new_collection_name)
        assert len(event_log) == 3
        assert event_log[2] == f"Deleted {new_collection_name}"


if __name__ == "__main__":
    unittest.main()
