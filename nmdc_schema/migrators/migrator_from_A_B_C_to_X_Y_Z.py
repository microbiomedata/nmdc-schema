from nmdc_schema.migrators.migrator_base import MigratorBase


class Migrator_from_A_B_C_to_X_Y_Z(MigratorBase):
    """
    Migrates data from schema A.B.C to X.Y.Z

    TUTORIAL: This is an example of a "migrator" class.
              It was designed for use during developer training and
              to serve as a template for production "migrator" classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        TUTORIAL: This is the "constructor" function of the class.
                  As is true about the "constructor" function of any class,
                  it runs whenever that class is instantiated, and its job
                  is to initialize the newly-created instance of that class.

                  When this "constructor" function runs, it does two things:
                  1. It invokes the base class's "constructor" function; and
                  2. It populates a dictionary that keeps track of which
                     transformation functions will be applied to objects
                     from which collections. You can think of this as the
                     "agenda", "itinerary", "plan", or "registry" of
                     transformations that make up this migration. As
                     security guards at marathons say, "If it ain't
                     part of the plan, it ain't gonna be ran."

             -->  As part of creating a new "migration" class, you will
                  populate its "agenda."
        """

        # Invoke the base class's "constructor" function, passing/forwarding to it
        # all arguments that were passed to the current function.
        super().__init__(*args, **kwargs)

        # Populate the "collection-to-transformers" map for this specific migration.
        self.agenda = dict(
            study_set=[self.allow_multiple_names],
        )

    def allow_multiple_names(self, study: dict) -> dict:
        """
        TUTORIAL: This is an example "transformation" function within the class.
                  Its job is to transform a dictionary that conforms to the
                  initial schema version (in this case, version "A.B.C"), into one
                  that conforms to the target schema version (in this case,
                  version "X.Y.Z"). That might involve adding a field,
                  converting a string into a list of strings, etc.

                  When this "transformation" function runs, it does three things:
                  1. It accepts a single dictionary as a parameter.
                  2. It transforms that dictionary.
                  3. It returns the transformed dictionary.

              --> As part of creating a new "migration" class, you will
                  typically implement one or more "transformation" functions.
                  You will also add them to the "agenda" of the class.

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

        >>> mig = Migrator_from_A_B_C_to_X_Y_Z()  # creates a class instance on which we can call this function (method)
        >>> mig.allow_multiple_names({'id': 123, 'name': 'My project'})  # test: transfers existing name to `names` list
        {'id': 123, 'names': ['My project']}
        >>> mig.allow_multiple_names({'id': 123, 'name': 'My project', 'foo': 'bar'})  # test: preserves other keys
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
