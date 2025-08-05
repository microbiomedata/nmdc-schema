from nmdc_schema.migrators.migrator_base import MigratorBase
from nmdc_schema.migrators.adapters.adapter_base import AdapterBase
from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
from nmdc_schema.migrators.migration_reporter import MigrationReporter
from typing import Optional

import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

class Migrator(MigratorBase):
    """
    Migrates data between two schemas.

    TUTORIAL: This is an example of a "migrator" class.
              It was designed for use during developer training and
              to serve as a template for production "migrator" classes.
    """

    """
    TUTORIAL: These two strings tell people the versions of the schema this
              "migrator" class was designed to migrate data between.
              
              -->  As part of creating a new "migrator" class, you will
                   populate its `_from_version` and `_to_version` strings.
    """
    _from_version = "1.0.0"  # https://github.com/microbiomedata/nmdc-schema/blob/1.0.0/
    _to_version = "EXAMPLE"  # in practice, this would be a real schema version; e.g., "7.8.0"

    def __init__(self, adapter: Optional[AdapterBase] = None, logger=None):
        """
        TUTORIAL: The __init__ function (constructor) initializes a new migrator instance.
                  This function runs automatically when you create a new migrator object.
                  
                  It accepts two optional parameters:
                  - adapter: The data store adapter (e.g., MongoAdapter, DictionaryAdapter)
                  - logger: A Python logger for outputting messages during migration
                  
                  If you don't provide these, the migrator will use default values.
                  
                  --> As part of creating a new migrator class, you typically won't need
                      to modify this function unless you need to initialize additional
                      instance variables specific to your migration logic.
        """
        super().__init__(adapter, logger)
        self.reporter = None

    def upgrade(self, commit_changes: bool = False):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        TUTORIAL: This is the `upgrade` function. You can think of it as the "main" function or
                  "entry point" of the migrator. Its job is to transform the database from
                  conforming to the original schema to conforming to the new schema.

                  The `upgrade` function accesses the database via an "adapter", instead of
                  accessing the database directly. That allows the same migrator to be used
                  with different types of data stores (e.g. MongoDB database, Python dictionary).

              --> As part of creating a new "migrator" class, you will implement an `upgrade` function.
              
        TUTORIAL: The `commit_changes` parameter controls whether changes are saved to the database:
                  - commit_changes=False (default): Changes are rolled back (dry run mode)
                  - commit_changes=True: Changes are committed and saved permanently
                  
                  This allows safe testing of migrations before applying them to production data.
              
        TUTORIAL: Example showing complete migration workflow with reporting:
        
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {
        ...     "study_set": [
        ...         {"id": "study1", "name": "Research Project"},
        ...         {"id": "study2"}  # study without name
        ...     ]
        ... }
        >>> m = Migrator(DictionaryAdapter(database))
        >>> result = m.upgrade()
        Processing collection: study_set
        >>> # Check transformation results
        >>> database["study_set"][0]["names"]
        ['Research Project']
        >>> "name" in database["study_set"][0]
        False
        >>> database["study_set"][1]["names"]
        []
        >>> # Check new collections were created
        >>> len(database["comment_set"])
        2
        >>> len(database["report_set"])
        2
        
        TUTORIAL: For MongoDB-based migrations, the commit_changes parameter controls transactions:
        
        Args:
            commit_changes (bool): If True, commits changes to database. If False (default), 
                                   rolls back changes for safe testing.
        """
        self.logger.setLevel(logging.INFO)
        # TUTORIAL: Initialize the migration reporter to track changes during migration
        self.reporter = MigrationReporter(self.logger)
        
        # TUTORIAL: Transaction handling for MongoDB migrations
        #           When using MongoDB, migrations run within a transaction for safety
        if isinstance(self.adapter, MongoAdapter):
            # MongoDB adapter - use a single transaction for all operations
            try:
                # TUTORIAL: Use the unified transaction method that gives full control
                self.adapter.execute_in_transaction(
                    operations_callback=self._perform_all_migration_operations,
                    commit_changes=commit_changes
                )
                
                if commit_changes:
                    self.logger.info("Transaction committed (changes have been saved)")
                else:
                    self.logger.info("Transaction rolled back (no changes were committed)")
                    
            except Exception as e:
                self.logger.error(f"Migration failed: {e}")
                raise
        else:
            # For non-MongoDB adapters (like DictionaryAdapter), just perform all operations
            # TUTORIAL: Dictionary adapter doesn't support transactions, so changes apply immediately
            self._perform_migration_operations()
            if not commit_changes:
                self.logger.info("Note: Dictionary adapter doesn't support rollback - changes are applied immediately")
        
        # TUTORIAL: Generate final migration report showing what was changed
        #           
        #           IMPORTANT LIMITATIONS: The migration reporter only tracks changes that you
        #           explicitly tell it about by calling its tracking methods. It does NOT
        #           automatically detect or report:
        #           
        #           - Collection creation/deletion (e.g., create_collection, drop_collection)
        #           - Document insertion/deletion (e.g., insert_document, delete_document)  
        #           - Schema changes (e.g., renaming fields, changing data types)
        #           - Index creation/modification
        #           - Database configuration changes
        #           - Any other structural changes to the database
        #           
        #           The reporter ONLY tracks what you manually report by calling methods like:
        #           - self.reporter.track_record_updated() for field value changes
        #           - self.reporter.track_record_processed() for processed records
        #           - self.reporter.track_missing_value() for missing data
        #           - self.reporter.track_unmapped_value() for unmappable data
        #           
        #           --> As part of implementing a migrator, you should call the appropriate
        #               reporter tracking methods throughout your transformation functions
        #               to ensure comprehensive reporting of the changes you make.
        #               
        #           --> The migration reporting system probably needs additional functions
        #               to track other types of changes (collections, indexes, etc.).
        if self.reporter:
            self.reporter.generate_final_report()
    
    def _perform_all_migration_operations(self, adapter, session):
        """
        TUTORIAL: This method performs ALL migration operations within a single transaction.
                  It receives the adapter and session from execute_in_transaction(), ensuring
                  proper session management and atomic operations.
                  
                  The callback signature (adapter, session) is required by execute_in_transaction().
                  While adapter is technically the same as self.adapter, both parameters are provided
                  for clean API design and to make the callback function self-contained.
                  
        Args:
            adapter: The MongoAdapter instance - provides access to database operations
                    (Note: This is the same instance as self.adapter, but passed for API clarity)
            session: The MongoDB session for transaction control - required for transactional operations
                    (Methods like insert_document, process_each_document need this for atomicity)
        """
        # TUTORIAL: Process existing documents (transactional)
        print("Processing collection: study_set")
        adapter.process_each_document("study_set", [self.allow_multiple_names], session)
        
        # TUTORIAL: Create collections (not transactional in MongoDB - happens immediately)
        adapter.create_collection("comment_set")
        adapter.create_collection("report_set")
        
        # TUTORIAL: Insert new documents (transactional)
        adapter.insert_document("comment_set", {"id": 1, "text": "Hello"}, session)
        adapter.insert_document("comment_set", {"id": 2, "text": "Goodbye"}, session)
        
        # TUTORIAL: Process documents to create reports (transactional)
        adapter.do_for_each_document("comment_set", self.create_report_based_upon_comment, session)


    def _perform_migration_operations(self):
        """
        TUTORIAL: Separated migration logic to support transaction handling.
                  This method contains all the actual data transformation operations.
        """
        # TUTORIAL: In this example, we will pass each document in the `study_set` collection through
        #           a processing pipeline that consists of a single function: `self.allow_multiple_names`.
        #
        print("Processing collection: study_set")
        self.adapter.process_each_document("study_set", [self.allow_multiple_names])

        # TUTORIAL: Create and populate a collection that doesn't exist in the `_from_version` schema.
        self.adapter.create_collection("comment_set")
        self.adapter.insert_document("comment_set", {"id": 1, "text": "Hello"})
        self.adapter.insert_document("comment_set", {"id": 2, "text": "Goodbye"})

        # TUTORIAL: Advanced: Create and populate another new collection; based upon the documents in a _different_ collection.
        self.adapter.create_collection("report_set")
        self.adapter.do_for_each_document("comment_set", self.create_report_based_upon_comment)

    def allow_multiple_names(self, study: dict) -> dict:
        """
        TUTORIAL: This is an example "transformation" function within the class.
                  Its job is to transform a dictionary that conforms to the
                  initial schema (in this case, version "1.0.0"), into one
                  that conforms to the target schema (in this case,
                  version "EXAMPLE"). That might involve adding a field,
                  converting a string into a list of strings, etc.

                  When this "transformation" function runs, it does three things:
                  1. It accepts a single dictionary as a parameter.
                  2. It transforms that dictionary.
                  3. It returns the transformed dictionary.

              --> As part of creating a new "migrator" class, you will
                  typically implement one or more "transformation" functions.

        TUTORIAL: The remaining part of this comment consists of several "doctests".
                  You can read more about doctests in the official Python documentation:
                  https://docs.python.org/3/library/doctest.html

                  Each doctest consists of (a) a snippet of Python code that calls this
                  function, followed on the next line by (b) whatever the author of the
                  test expects this function to return, if anything.

                  People can then read and run those doctests in order to learn about
                  what this function does / how this function behaves.

              --> As part of implementing a "transformation" function, you will
                  typically write a few doctests in the docstring of that function.

        >>> m = Migrator()  # creates a class instance on which we can call this function (i.e. this method)
        >>> m.allow_multiple_names({'id': 123})  # test: creates an empty `names` list
        {'id': 123, 'names': []}
        >>> m.allow_multiple_names({'id': 123, 'name': 'My project'})  # test: transfers existing name to `names` list
        {'id': 123, 'names': ['My project']}
        >>> m.allow_multiple_names({'id': 123, 'name': 'My project', 'foo': 'bar'})  # test: preserves other keys
        {'id': 123, 'foo': 'bar', 'names': ['My project']}
        >>> # Test edge cases
        >>> m.allow_multiple_names({'id': 456, 'name': ''})  # test: handles empty name
        {'id': 456, 'names': ['']}
        >>> m.allow_multiple_names({'id': 789, 'names': ['existing']})  # test: overwrites existing names
        {'id': 789, 'names': []}
        """

        # optional log message
        self.logger.info(f"Transforming study having id: {study['id']}")

        # Transform the dictionary.
        #
        # TUTORIAL: In this example, I am creating a new field named `names`, whose value is an empty list;
        #           then, if the original study has a `name` value, I'm storing that in the list and then
        #           deleting the `name` field.
        #
        study["names"] = []
        if "name" in study:
            original_name = study["name"]
            study["names"].append(original_name)
            del study["name"]
            
            # TUTORIAL: Track that we updated this record (converted single name to names list)
            if self.reporter:
                self.reporter.track_record_updated(
                    class_name="nmdc:Study",
                    slot_name="name", 
                    subclass_type="nmdc:Study",
                    source_value=original_name,
                    target_value=f"[{original_name}]"
                )
        else:
            # TUTORIAL: Track that we processed this record, but it had no name to convert
            if self.reporter:
                self.reporter.track_record_processed(
                    class_name="nmdc:Study",
                    slot_name="names",
                    subclass_type="nmdc:Study", 
                    value="[empty_list]"
                )

        # Return the transformed dictionary.
        return study

    def create_report_based_upon_comment(self, comment: dict) -> None:
        """
        Creates a report based upon the comment passed in.

        Note: Although this function will be passed a document from the `comment_set` collection,
              the function will actually modify a *different* collection instead.
              
        TUTORIAL: This demonstrates how to process documents from one collection and create
                  new documents in a different collection during migration.
                  
        >>> from nmdc_schema.migrators.adapters.dictionary_adapter import DictionaryAdapter
        >>> database = {"comment_set": [], "report_set": []}
        >>> m = Migrator(DictionaryAdapter(database))
        >>> comment = {"id": 1, "text": "Hello world"}
        >>> m.create_report_based_upon_comment(comment)
        >>> len(database["report_set"])
        1
        >>> database["report_set"][0]["body"]
        'Someone wrote Hello world'
        >>> # Test with empty text
        >>> comment_empty = {"id": 2, "text": ""}
        >>> m.create_report_based_upon_comment(comment_empty)
        >>> database["report_set"][1]["body"]
        'Someone wrote '
        """
        report = {"body": f"Someone wrote {comment['text']}"}
        self.adapter.insert_document(collection_name="report_set", document=report)
