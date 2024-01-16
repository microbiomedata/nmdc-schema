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
    _from_version = "A.B.C"
    _to_version = "X.Y.Z"

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
        # Note: This works in a similar way to the "agenda-based" migrations we used to use before
        #       adapters were introduced. However, now, each collection's entry in the "agenda" is
        #       expressed as an invocation of the `self.adapter.process_each_document` function.
        #
        self.adapter.process_each_document("study_set", [self.allow_multiple_names])

        # Invoke some other adapter functions (as an example).
        self.adapter.create_collection("comment_set")
        self.adapter.insert_document("comment_set", {"id": 1, "text": "Hello"})
        self.adapter.insert_document("comment_set", {"id": 2, "text": "Goodbye"})

    def allow_multiple_names(self, study: dict) -> dict:
        """
        TUTORIAL: This is an example "transformation" function within the class.
                  Its job is to transform a dictionary that conforms to the
                  initial schema (in this case, version "A.B.C"), into one
                  that conforms to the target schema (in this case,
                  version "X.Y.Z"). That might involve adding a field,
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
        >>> m.allow_multiple_names({'id': 123, 'name': 'My project'})  # test: transfers existing name to `names` list
        {'id': 123, 'names': ['My project']}
        >>> m.allow_multiple_names({'id': 123, 'name': 'My project', 'foo': 'bar'})  # test: preserves other keys
        {'id': 123, 'foo': 'bar', 'names': ['My project']}
        """

        # optional log message
        self.logger.info(f"Transforming study having id: {study['id']}")

        # Transform the dictionary.
        #
        # TUTORIAL: In this example scenario, I am pretending that:
        #           1. In schema version "A.B.C", the `Study` class has a `name` slot,
        #              which contain a single string.
        #           2. In schema version "X.Y.Z", the `Study` class no longer has that
        #              `name` slot. Instead, it has a `names` slot, which contains
        #              a list of strings.
        #
        original_name = study["name"]  # preserve the original value
        study["names"] = []  # create a new key, whose value is an empty list of names
        study["names"].append(original_name)  # add the original value to that list
        del study["name"]  # delete the obsolete key

        # Return the transformed dictionary.
        return study
