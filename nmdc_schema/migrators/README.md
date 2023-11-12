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
   version `1.2.4`.
   ```shell
   # Run from the same directory as this `README.md` file:
   cp migrator_from_A_B_C_to_X_Y_Z.py migrator_from_1_2_3_to_1_2_4.py
   ```
2. Customize the migrator module according to the instructions in the example migrator module.
   - Update the class name (to `Migrator_from_1_2_3_to_1_2_4`)
   - Implement the transformation functions (ensure each one accepts and returns a Python dictionary)
   - Add the transformation functions to the agenda
   > TODO: Replace this step with more detailed instructions; possibly enough that we can replace the current example
   > migrator module with one that lacks tutorial comments and is more ready-to-populate.
3. Add the migrator module to the list of modules in the `import` statement in `nmdc_schema/migrators.py`.
