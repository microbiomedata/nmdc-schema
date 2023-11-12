# Migrators

## Overview

This directory (i.e. Python [package](https://docs.python.org/3/tutorial/modules.html#packages)) contains
files (i.e. Python [modules](https://docs.python.org/3/tutorial/modules.html#modules)) which, themselves, contain
the definitions of Python [classes](https://docs.python.org/3/tutorial/classes.html) related to the migration of data between schema versions.

## Contents

This directory contains the following things:

- `assets/` - data files (not Python code) used by the classes
- `helpers.py` - general-purpose functions used by the classes
- `migrator_base.py` - definition of the `MigratorBase` class
    - That class is agnostic to schema versions
- `migrator_from_A_B_C_to_X_Y_Z.py` - definition of the `Migrator_from_A_B_C_to_X_Y_Z` class
    - That class is used to migrate data from schema version `A.B.C` to schema version `X.Y.Z`  
- Other `migrator_*.py` modules (they are analogous to `migrator_from_A_B_C_to_X_Y_Z.py`)

## Contributing

TODO