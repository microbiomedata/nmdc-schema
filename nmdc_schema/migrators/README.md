# Migrators

## Overview

This directory (i.e. Python [package](https://docs.python.org/3/tutorial/modules.html#packages)) contains
files (i.e. Python [modules](https://docs.python.org/3/tutorial/modules.html#modules)) which, themselves, contain
the definitions of Python [classes](https://docs.python.org/3/tutorial/classes.html) related to the migration of data
between schema versions.

In this document, I'll refer to those Python classes as "migrators."

## Contents

This directory contains the following things:

- `assets/` - data files (not Python code) used by the classes
- `helpers.py` - general-purpose functions used by the classes
- `migrator_base.py` - definition of the `MigratorBase` class
    - That class is agnostic to schema versions
- `migrator_from_A_B_C_to_X_Y_Z.py` - definition of the `Migrator_from_A_B_C_to_X_Y_Z` class
    - That class is used to migrate data from schema version `A.B.C` to schema version `X.Y.Z`
- Other `migrator_*.py` modules (they are analogous to `migrator_from_A_B_C_to_X_Y_Z.py`)

## Creating a migrator

Here's how you can create a new migrator:

1. Create a new migrator module based upon the example one.
   > In this example, I'll create a migrator that can be used to migrate data from schema version `1.2.3` to schema
   > version `1.2.4`.
   ```shell
   # Run from the same directory as this `README.md` file:
   cp migrator_from_A_B_C_to_X_Y_Z.py migrator_from_1_2_3_to_1_2_4.py
   ```
2. Customize the migrator module according to the instructions in the example migrator module.
    - Update the class name:
      ```diff
      - class Migrator_from_A_B_C_to_X_Y_Z(MigratorBase):
      + class Migrator_from_1_2_3_to_1_2_4(MigratorBase):
      ```
    - Remove the definition of the _example_ "transformation" function:
      ```diff
      - def allow_multiple_names(self, study: dict) -> dict:
      -     ...
      -
      -     # Return the transformed dictionary.
      -     return study
      ```
    - Remove the _example_ "transformation" function from the agenda:
      ```diff
        self.agenda = dict(
      -     study_set=[self.allow_multiple_names],
        )      
      ```
    - Define the "transformation" function(s) that are part of this migration. Ensure each "transformation" function:
        - **Accepts** a Python `dict`
            - For example:
                ```diff
                + def add_name(self, person: dict) -> dict:
                ```
        - Has a **docstring** that summarizes what the function does (optional)
            - For example:
              ```diff
                """
              + Adds a `name` key and sets its value to "Anonymous".
              ```
        - Has at least one **[doctest](https://docs.python.org/3/library/doctest.html)** that demonstrates what the function does (optional)
            - For example:
              ```diff
              + >>> migrator = Migrator_from_1_2_3_to_1_2_4()
              + >>> migrator.add_name({'id': 123})
              + {'id': 123, 'name': 'Anonymous'}
                """
              ```
        - **Returns** a Python `dict`
            - For example:
              ```diff
              + return person
              ```
    - Add the "transformation" function(s) to the agenda:
        - For example:
          ```diff
            self.agenda = dict(
          +     person_set=[self.add_name],
            )
          ```
3. Done.
