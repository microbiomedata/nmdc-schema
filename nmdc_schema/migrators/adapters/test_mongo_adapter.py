import unittest
from typing import Optional

# TODO: pymongo is used here, but it is not listed as a production dependency of nmdc-schema (only as a dev-dependency).
from pymongo import MongoClient, timeout
from pymongo.database import Database

from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter


# Define constants used by the test.
# TODO: Move these to an environment configuration file (is there a standard one; e.g. "local/.env")?
MONGO_HOST: str = "host.docker.internal"
MONGO_PORT: int = 27017
MONGO_USER: Optional[str] = None
MONGO_PASS: Optional[str] = None
MONGO_DATABASE_NAME: str = "test-nmdc-schema"
MONGO_TIMEOUT_DURATION: int = 3  # seconds


class TestMongoAdapter(unittest.TestCase):
    r"""
    Tests targeting the `MongoAdapter` class.

    You can start up a containerized MongoDB server like this:
    $ docker run --rm --detach --name mongo-test-nmdc-schema -p 27017:27017 mongo

    One that's running, other containers will be able to access it via:
    - host.docker.internal:27017

    You can run these tests like this:
    $ poetry run python -m unittest -v nmdc_schema/migrators/adapters/test_mongo_adapter.py

    References:
    - https://docs.python.org/3/library/unittest.html#basic-example
    - https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
    """

    mongo_client: Optional[MongoClient] = None
    db: Optional[Database] = None

    def setUp(self) -> None:
        r"""
        Connects to the MongoDB server and gets a reference to the database.

        Note: This function runs before each test starts.
        """

        # Connect to the MongoDB server and store a reference to the connection.
        self.mongo_client = MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT,
            username=MONGO_USER,
            password=MONGO_PASS,
            authSource="admin",
        )
        with timeout(MONGO_TIMEOUT_DURATION):
            # Try connecting to the database server.
            _ = self.mongo_client.server_info()
            db = self.mongo_client[MONGO_DATABASE_NAME]

            # Ensure the database contains no collections.
            if len(db.list_collection_names()):
                raise KeyError(f"Database is not empty: {MONGO_DATABASE_NAME}")

        # Store a reference to the database.
        self.db = db

    def tearDown(self) -> None:
        r"""
        Drops all collections in the database and closes the connection to the MongoDB server.

        Note: This function runs after each test finishes.
        """

        # Drop all collections in the database.
        for collection_name in self.db.list_collection_names():
            self.db.drop_collection(collection_name)

        # Close the connection to the server.
        self.mongo_client.close()

    def test_create_collection(self):
        # Set up:
        collection_name = "my_collection"

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
        adapter.create_collection(collection_name)

        # Validate result:
        collection_names_after = self.db.list_collection_names()
        assert len(collection_names_after) == 1
        assert collection_name in collection_names_after

    def test_rename_collection(self):
        # Set up:
        collection_name_original = "my_collection"
        collection_name_target = "your_collection"
        self.db.create_collection(collection_name_original)
        assert len(self.db.list_collection_names()) == 1

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
        adapter.rename_collection(collection_name_original, collection_name_target)

        # Validate result:
        collection_names_after = self.db.list_collection_names()
        assert len(collection_names_after) == 1
        assert collection_name_target == collection_names_after[0]

    def test_delete_collection(self):
        # Set up:
        collection_name = "my_collection"
        self.db.create_collection(collection_name)
        assert len(self.db.list_collection_names()) == 1

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
        adapter.delete_collection(collection_name)

        # Validate result:
        assert len(self.db.list_collection_names()) == 0

    def test_insert_document(self):
        # Set up:
        collection_name = "my_collection"
        document = dict(id=123, foo="bar")
        self.db.create_collection(collection_name)
        assert self.db.get_collection(collection_name).count_documents({}) == 0

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
        adapter.insert_document(collection_name, document)

        # Validate result:
        assert self.db.get_collection(collection_name).count_documents({}) == 1
        document_actual = self.db.get_collection(collection_name).find_one({})
        for k, v in document.items():
            assert v == document_actual[k]

    def test_get_document_having_value_in_field(self):
        # Set up:
        collection_name = "my_collection"
        document_1 = dict(id=1, x="a")
        document_2 = dict(id=2, x="b")
        document_3 = dict(id=3, x="c")
        self.db.create_collection(collection_name)
        self.db.get_collection(collection_name).insert_many(
            [document_1, document_2, document_3]
        )
        assert self.db.get_collection(collection_name).count_documents({}) == 3

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
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
        self.db.create_collection(collection_name)
        self.db.get_collection(collection_name).insert_many(
            [document_1, document_2, document_3]
        )
        assert self.db.get_collection(collection_name).count_documents({}) == 3

        # Invoke function-under-test:
        adapter = MongoAdapter(database=self.db)
        document_actual = adapter.get_document_having_one_of_values_in_field(
            collection_name, "x", ["n", "b", "m"]
        )

        # Validate result:
        for k, v in document_2.items():
            assert v == document_actual[k]

    def test_delete_documents_having_value_in_field(self):
        raise NotImplementedError()

    def test_process_each_document(self):
        raise NotImplementedError()


if __name__ == "__main__":
    unittest.main()
