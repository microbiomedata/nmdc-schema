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
- `cli/` - CLI scripts/commands related to the classes
- `helpers.py` - general-purpose functions used by the classes
- `migrator_base.py` - definition of the `MigratorBase` class
    - That class is agnostic to schema versions
- `migrator_from_A_B_C_to_X_Y_Z.py` - definition of an example `Migrator` class
    - That class is specific to a pair of schema versions (i.e. it migrates data from schema version `A.B.C` to schema version `X.Y.Z`)
- Other `migrator_*.py` modules (they are analogous to `migrator_from_A_B_C_to_X_Y_Z.py`)

## Creating a migrator

Here's how you can create a new migrator:

1. Run `make migrator`.
    ```shell
    make migrator
    ```
    > Alternatively, you can run `$ poetry run python nmdc_schema/migrators/cli/create_migrator.py`.
   
    When prompted, enter the [schema version numbers](../../CHANGELOG.md) the migrator will migrate data _from_ and _to_. For example:
    > ```yaml
    > From schema version: 1.1
    > To schema version: 1.2
    > ```

    By default, the generated migrator is a "no-op," meaning that it performs **no** **op**erations (i.e. doesn't do
    anything).

    > If the corresponding schema changes don't require that any data be migrated, you can skip the steps
    below. The existence of a "no-op" migrator indicates that no migration is necessary.
2. Customize the newly-generated migrator.
    - Define the "transformation" function(s) that are part of this migration. Ensure each "transformation" function:
        - **Accepts** a Python `dict`; for example:
            ```diff
            + def add_name(self, person: dict) -> dict:
            ```
        - Has a **docstring** that summarizes what the function does (optional); for example:
            ```diff
                  """
            +     Adds a `name` key and sets its value to "Anonymous".
            ```
        - Has at least one **[doctest](https://docs.python.org/3/library/doctest.html)** that demonstrates what the function does (optional); for example:
            ```diff
            +     >>> migrator = Migrator()
            +     >>> migrator.add_name({'id': 123})
            +     {'id': 123, 'name': 'Anonymous'}
                  """
            ```
        - **Returns** a Python `dict`; for example:
            ```diff
            +     return person
            ```
    - Add the "transformation" function(s) to the agenda:
        - For example:
          ```diff
            self._agenda = dict(
          +     person_set=[self.add_name],
            )
          ```
    You can refer to the example migrator (i.e. `migrator_from_A_B_C_to_X_Y_Z.py`) as a guide.
3. Done.
