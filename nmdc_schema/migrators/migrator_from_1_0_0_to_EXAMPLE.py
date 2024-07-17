from nmdc_schema.migrators.migrator_base import MigratorBase


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

    def upgrade(self):
        r"""
        Migrates the database from conforming to the original schema, to conforming to the new schema.

        TUTORIAL: This is the `upgrade` function. You can think of it as the "main" function or
                  "entry point" of the migrator. Its job is to transform the database from
                  conforming to the original schema to conforming to the new schema.

                  The `upgrade` function accesses the database via an "adapter", instead of
                  accessing the database directly. That allows the same migrator to be used
                  with different types of data stores (e.g. MongoDB database, Python dictionary).

              --> As part of creating a new "migrator" class, you will implement an `upgrade` function.
        """

        # Process each document in the specified collection.
        #
        # Note: In this example, we will pass each document in the `study_set` collection through
        #       a processing pipeline that consists of a single function: `self.allow_multiple_names`.
        #
        self.adapter.process_each_document("study_set", [self.allow_multiple_names])

        # Create and populate a collection that doesn't exist in the `_from_version` schema.
        self.adapter.create_collection("comment_set")
        self.adapter.insert_document("comment_set", {"id": 1, "text": "Hello"})
        self.adapter.insert_document("comment_set", {"id": 2, "text": "Goodbye"})

        # Advanced: Create and populate another new collection; based upon the documents in a _different_ collection.
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

        # Return the transformed dictionary.
        return study

    def create_report_based_upon_comment(self, comment: dict) -> None:
        """
        Creates a report based upon the comment passed in.

        Note: Although this function will be passed a document from the `comment_set` collection,
              the function will actually modify a *different* collection instead.
        """
        report = {"body": f"Someone wrote {comment['text']}"}
        self.adapter.insert_document(collection_name="report_set", document=report)
