from typing import Optional, Callable, List, Union
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase
from pymongo.database import Database
from pymongo.client_session import ClientSession


class MongoAdapter(AdapterBase):
    r"""
    Class containing methods related to manipulating a MongoDB database.
    """

    def __init__(self, database: Database, **kwargs) -> None:
        r"""
        Invokes the initialization method of the parent class, passing to it any specified keyword arguments.
        Also initializes the reference to the database this adapter instance will be used to manipulate.

        References:
        - https://pymongo.readthedocs.io/en/stable/examples/type_hints.html#typed-database
        """
        super().__init__(**kwargs)
        self._db = database

    def create_collection(self, collection_name: str) -> None:
        r"""
        Creates an empty collection having the specified name, if no collection by that name exists.
        Also invokes `self.on_collection_created`, if defined, passing to it the name of the collection.

        Note: This operation is NOT transactional in MongoDB - collections are created immediately
        regardless of any active transaction state.

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html#pymongo.database.Database.create_collection
        - https://docs.python.org/3/library/functions.html#callable
        """
        if collection_name not in self._db.list_collection_names():
            self._db.create_collection(name=collection_name)

            # If the relevant callback function exists, invoke it.
            if callable(self.on_collection_created):
                self.on_collection_created(collection_name)

    def rename_collection(self, current_name: str, new_name: str) -> None:
        r"""
        Renames the specified collection, if it exists, so that it has the specified new name.
        Also invokes `self.on_collection_renamed`, if defined, passing to it the old and new names of the collection.

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html#pymongo.database.Database.get_collection
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.rename
        """
        if current_name in self._db.list_collection_names():
            self._db.get_collection(name=current_name).rename(new_name=new_name)

            # If the relevant callback function exists, invoke it.
            if callable(self.on_collection_renamed):
                self.on_collection_renamed(current_name, new_name)

    def delete_collection(self, collection_name: str) -> None:
        r"""
        Deletes the collection having the specified name, if such a collection exists.
        Also invokes `self.on_collection_deleted`, if defined, passing to it the name of the collection.

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html#pymongo.database.Database.drop_collection
        """
        if collection_name in self._db.list_collection_names():
            self._db.drop_collection(name_or_collection=collection_name)

            # If the relevant callback function exists, invoke it.
            if callable(self.on_collection_deleted):
                self.on_collection_deleted(collection_name)

    def insert_document(self, collection_name: str, document: dict, session: ClientSession = None) -> None:
        r"""
        Inserts the specified document into the collection having the specified name.

        Args:
            collection_name: Name of the collection
            document: Document to insert
            session: Optional MongoDB session for transaction support

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
        """
        self._db.get_collection(name=collection_name).insert_one(document, session=session)

    def get_document_having_value_in_field(
        self, collection_name: str, field_name: str, value: str
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having the specified value in the specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find_one
        - https://www.mongodb.com/docs/manual/reference/operator/query/eq/#syntax
        """

        # Create the filter for the query.
        # Note: I named this variable `filter_` because `filter` is a built-in Python function.
        filter_ = dict()
        filter_[field_name] = {"$eq": value}

        # Find and return the first matching document, if any.
        document = self._db.get_collection(name=collection_name).find_one(
            filter=filter_
        )
        return document

    def get_document_having_one_of_values_in_field(
        self, collection_name: str, field_name: str, values: List[str]
    ) -> Optional[dict]:
        r"""
        Retrieves the first document from the specified collection, having any one of the specified values in the
        specified field.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

        References:
        - https://www.mongodb.com/docs/manual/reference/operator/query/in/
        - https://www.mongodb.com/docs/manual/reference/operator/query/type/
        """

        # Create the filter for the query.
        #
        # Note: The `$in` operator has a special-case behavior where, if the field is an array, the operator
        #       looks for any matching element _within_ the array. That is not what I want in this situation.
        #       I want to only compare the value of the field, itself. Since `values` is a list of strings,
        #       I will only bother checking fields of type "string" (which excludes fields of type "array").
        #
        filter_ = dict()
        filter_[field_name] = {"$type": "string", "$in": values}

        # Find and return the first matching document, if any.
        document = self._db.get_collection(name=collection_name).find_one(
            filter=filter_
        )
        return document

    def delete_documents_having_value_in_field(
        self, collection_name: str, field_name: str, value: str
    ) -> int:
        r"""
        Deletes all documents from the specified collection, having the specified value in the specified field;
        and returns the number of documents that were deleted.

        Note: This only supports top-level fields (e.g. `_id`, `depth`), not nested fields (e.g. `depth.has_unit`).

        References:
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.delete_many
        """

        # Create the filter for the query.
        # Note: I named this variable `filter_` because `filter` is a built-in Python function.
        filter_ = dict()
        filter_[field_name] = {"$eq": value}

        # Delete all matching documents.
        result = self._db.get_collection(name=collection_name).delete_many(
            filter=filter_
        )

        # Return the number of documents that were deleted.
        num_deleted = result.deleted_count
        return num_deleted

    def process_each_document(
        self, collection_name: str, pipeline: List[Callable[[dict], dict]], session: ClientSession = None
    ) -> None:
        r"""
        Passes each document in the specified collection through the specified processing pipeline—in which
        the output of any given function is the input to the function after it—and stores the final output
        back in the collection, replacing the original document.

        Args:
            collection_name: Name of the collection to process
            pipeline: List of functions to apply to each document
            session: Optional MongoDB session for transaction support

        References:
        - https://docs.python.org/3/library/copy.html#copy.deepcopy
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.replace_one
        """

        # Iterate over every document in the collection, if the collection exists.
        if collection_name in self._db.list_collection_names():
            collection = self._db.get_collection(name=collection_name)
            for document in collection.find({}, session=session):
                # Create a filter based upon this document's `_id` value, so that we can find the same document later.
                # We do this up front in case a function in the pipeline "inadvertently" tampers with the `_id` field.
                document_id = document["_id"]
                filter_ = {"_id": {"$eq": document_id}}

                # "Pass" the document through the functions (i.e. "stages") that make up the pipeline,
                # such that the output from one stage becomes the input to the next stage.
                for function in pipeline:
                    document = function(document)

                # Overwrite the original document with the processed one.
                collection.replace_one(filter=filter_, replacement=document, session=session)

    def set_field_of_each_document(
        self, collection_name: str, field_name: str, value: Union[None, str, int, float, bool],
    ) -> None:
        r"""
        Assigns the specified value to the specified field of each document in the collection.
        This method is a specialized alternative to the `process_each_document` method.
        """

        # Update every document in the collection, if the collection exists.
        if collection_name in self._db.list_collection_names():
            collection = self._db.get_collection(name=collection_name)
            collection.update_many({}, {"$set": {field_name: value}})

    def remove_field_from_each_document(
        self,
        collection_name: str,
        field_name: str,
    ) -> None:
        r"""
        Removes the specified field from each document in the collection.

        References:
        - https://www.mongodb.com/docs/manual/reference/operator/update/unset/
        """

        # Iterate over every document in the collection, if the collection exists.
        if collection_name in self._db.list_collection_names():
            collection = self._db.get_collection(name=collection_name)
            collection.update_many({}, {"$unset": {field_name: 0}})  # value is arbitrary (e.g. 0)

    def do_for_each_document(
        self, collection_name: str, action: Callable[[dict], None], session: ClientSession = None
    ) -> None:
        r"""
        Passes each document in the specified collection to the specified function. This method was designed
        to facilitate iterating over all documents in a collection without actually modifying them.
        
        Args:
            collection_name: Name of the collection to iterate over
            action: Function to call for each document
            session: Optional MongoDB session for transaction support
        """

        # Iterate over every document in the collection, if the collection exists.
        if collection_name in self._db.list_collection_names():
            collection = self._db.get_collection(name=collection_name)
            for document in collection.find({}, session=session):
                action(document)

    def copy_value_from_field_to_field_in_each_document(
        self,
        collection_name: str,
        source_field_name: str,
        destination_field_name: str,
    ) -> None:
        r"""
        For each document in the collection that has the source field, copy the value of the source field
        into the destination field, creating the destination field if it doesn't already exist.

        References:
        - https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany
        - https://www.mongodb.com/docs/manual/reference/operator/update/set/
        - https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_many
        """

        # Update every document in the collection, if the collection exists.
        if collection_name in self._db.list_collection_names():
            collection = self._db.get_collection(name=collection_name)
            collection.update_many(
                {source_field_name: {"$exists": True}},
                [{"$set": {destination_field_name: f"${source_field_name}"}}]
            )


    def process_collections_in_transaction(
        self, 
        collection_names: List[str], 
        document_processor: Callable[[dict], dict],
        commit_changes: bool = False
    ) -> None:
        r"""
        Process documents in multiple collections within a MongoDB transaction.
        This method wraps the existing process_each_document method with transaction handling.
        
        Args:
            collection_names: List of collection names to process
            document_processor: Function that takes a document and returns the modified document
            commit_changes: If True, commits the transaction. If False, rolls back.
        """
        with self._db.client.start_session() as session:
            with session.start_transaction():
                try:
                    # Use the existing process_each_document method with session support
                    for collection_name in collection_names:
                        self.process_each_document(collection_name, [document_processor], session)
                    
                    if commit_changes:
                        session.commit_transaction()
                    else:
                        session.abort_transaction()
                        
                except Exception as e:
                    session.abort_transaction()
                    raise e

    def execute_in_transaction(
        self,
        operations_callback: Callable[['MongoAdapter', ClientSession], None],
        commit_changes: bool = False
    ) -> None:
        r"""
        Execute arbitrary operations within a MongoDB transaction.
        This gives the migrator full control over what operations are performed within a single transaction.
        
        Args:
            operations_callback: Function that takes (adapter, session) and performs operations
            commit_changes: If True, commits the transaction. If False, rolls back.
            
        Example usage:
            def my_operations(adapter, session):
                adapter.create_collection("new_collection")  # Not transactional
                adapter.insert_document("new_collection", {"id": 1}, session)  # Transactional
                adapter.do_for_each_document("old_collection", some_function, session)  # Transactional
                
            adapter.execute_in_transaction(my_operations, commit_changes=True)
        """
        with self._db.client.start_session() as session:
            with session.start_transaction():
                try:
                    # Call the operations callback, passing both adapter and session
                    operations_callback(self, session)
                    
                    if commit_changes:
                        session.commit_transaction()
                    else:
                        session.abort_transaction()
                        
                except Exception as e:
                    session.abort_transaction()
                    raise e

