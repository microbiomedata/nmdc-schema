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
- `partials/` - migrators that _partially_ migrate a database between two schema versions
    - More information is available in [`partials/README.md`](./partials/README.md)
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
    > From schema version: 1.1.3
    > To schema version: 1.2.7
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

## Adding Migration Reporting

To add consistent reporting to a new migrator:

1. **Import the reporter**:
   ```python
   from nmdc_schema.migrators.utils.migration_reporter import create_immediate_reporter
   import logging
   ```

2. **Initialize in upgrade() method**:
   ```python
   def upgrade(self):
       logging.basicConfig(level=logging.INFO, format='%(message)s')
       self.logger.setLevel(logging.INFO)
       reporter = create_immediate_reporter(self.logger)
   ```

3. **Wrap collection processing**:
   ```python
   reporter.start_collection(collection_name)
   
   # Process documents...
   docs_updated = 0
   for document in collection.find():
       # Do migration work...
       if modified:
           docs_updated += 1
   
   reporter.end_collection(collection_name, total_docs, docs_updated)
   ```

4. **Track operations**:
   ```python
   # Count operations: reporter.track_operation(type, key, count)
   reporter.track_operation('fields_added', 'names', 1)
   
   # Track unique items: reporter.track_item(type, item)
   reporter.track_item('collections_modified', 'study_set')
   
   # Track nested values: reporter.track_value_set(type, key, value)  
   reporter.track_value_set('errors_by_collection', 'study_set', 'missing_id')
   ```

5. **Generate final report**:
   ```python
   reporter.generate_final_report()
   ```

See `migrator_from_1_0_0_to_EXAMPLE.py` for a complete example. 

## Testing the migrator

1. Create a local copy of the MongoDB database with a schema that conforms to the release from which you are migrating.

*Note:* This will most often be a production database.  For a release with many migrators, all migrators should be 
applied in order, to the copy of the production database. 

```bash
% git clone github.com/microbiomedata/nmdc-runtime 
% cd nmdc-runtime
% make up-test # creates a basic mongodb docker container for you with prod-ish configuration but no data. 
```
Once up, check the ports.  The default ports this comes with are 27017 (internal docker port), 
27018 (external connection to mongo) for MongoDB.

```bash
% docker ps -a # get the mongo container id for later steps below

# find the most recent docker dump
% ssh your-user-name@dtn01.nersc.gov
% ls global/cfs/projectdirs/m3408/nmdc-mongodumps/  
% rsync -av --exclude='_*' --exclude='fs\.*' -e "ssh " your-user-name@dtn01.nersc.gov:/global/cfs/projectdirs/m3408/nmdc-mongodumps/dump_nmdc-prod_2025-02-10_20-12-02 /tmp/remote-mongodump/nmdc

# Copy the dump to the mongo container
% docker cp /tmp/remote-mongodump [mongo_container_id]:/tmp/

# invade the running mongo docker container to load the dump
% docker exec -it [mongo_container_id] bash

# inside the container, run the following to load the dump
% mongorestore -v -u admin -p root --authenticationDatabase=admin --drop --nsInclude='nmdc.*' --gzip --dir /tmp/remote-mongodump/nmdc/dump_nmdc-prod_2025-02-10_20-12-02/ 
```

3. Run the migrator against the test database. 
4. Verify that the test database conforms to the new schema.
5. Run validation checks against the migrated database.
