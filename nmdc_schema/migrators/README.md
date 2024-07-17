# Migrators

## Overview

This directory (i.e. Python [package](https://docs.python.org/3/tutorial/modules.html#packages)) contains
files (i.e. Python [modules](https://docs.python.org/3/tutorial/modules.html#modules)) which, themselves, contain
the definitions of Python [classes](https://docs.python.org/3/tutorial/classes.html) related to the migration of
databases between schemas.

In this document, I'll refer to those Python classes as "migrators."

## Contents

This directory contains the following things:

- `adapters/adapter_base.py` - definition of the `AdapterBase` class
- `adapters/dictionary_adapter.py` - definition of the `DictionaryAdapter` class
    - That class can be used by a `Migrator` instance to manipulate a database represented as a Python dictionary
- `adapters/mongo_adapter.py` - definition of the `MongoAdapter` class
    - That class can be used by a `Migrator` instance to manipulate a MongoDB database
- `assets/` - data files (not Python code) used by the classes
- `cli/` - CLI scripts/commands related to the classes
- `helpers.py` - general-purpose functions used by the classes
- `migrator_base.py` - definition of the `MigratorBase` class
    - That class is agnostic to schema versions
- `migrator_from_1_0_0_to_EXAMPLE.py` - definition of an example `Migrator` class
    - That class is specific to a pair of schema versions
      (i.e. it migrates databases from schema version `1.0.0` to schema version `EXAMPLE`)
- Other `migrator_*.py` modules (they are analogous to `migrator_from_1_0_0_to_EXAMPLE.py`)

## Creating a migrator

Here's how you can create a new migrator:

1. Run `make migrator`.
    ```shell
    make migrator
    ```
    > Alternatively, you can run `$ poetry run python nmdc_schema/migrators/cli/create_migrator.py`.
   
    When prompted, enter the [version numbers of the schemas](../../CHANGELOG.md) the migrator will migrate
    data _from_ and _to_. For example, if the original schema version is `1.1.3` and the new schema version is `1.2.7`:
    > ```yaml
    > From schema version: 1.1
    > To schema version: 1.2
    > ```

    By default, **the generated migrator is a "no-op,"** meaning that it performs **no** **op**erations (i.e. doesn't do
    anything).

    > **The existence of a "no-op" migrator indicates that no migration is necessary.**

    **Checkpoint:** If _all_ databases that conform to the original schema also conform to the new schema,
    then no migration is necessary. In that situation, you can leave the migrator as is (i.e. skip the steps below).
2. Customize the newly-generated migrator.
    - Populate the `upgrade` function.
        - The job of this function is to transform the database from conforming to the original schema to conforming to
          the new schema. You can think of this as the migrator's "main" function.
    - Whenever you want the migrator to interact with a database, use `self.adapter` to do so.
        - `self.adapter` is a database adapter (i.e. it is an instance of a class that inherits from `AdapterBase`).
          It allows the same migrator to be used with different kinds of databases.

   > You can refer to the example migrator (i.e. `migrator_from_1_0_0_to_EXAMPLE.py`) and other migrators for reference.
3. Done.
