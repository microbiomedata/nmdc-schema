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

To add runtime reporting to a new migrator:

1. **Import the reporter**:
   ```python
   from migration_reporter import MigrationReporter
   import logging
   ```

2. **Initialize in upgrade() method**:
   ```python
   def upgrade(self):
       logging.basicConfig(level=logging.INFO, format='%(message)s')
       self.logger.setLevel(logging.INFO)
       self.reporter = MigrationReporter(self.logger)
   ```

3. **Track record changes**:
   ```python
   # Track records that were updated/processed
   self.reporter.track_record_updated(
       class_name="nmdc:Biosample",           # MongoDB collection class
       slot_name="field_name",                # Field or path that was updated
       subclass_type="nmdc:Biosample",        # Most specific class (may be nested)
       source_value="old_value",              # Original value
       target_value="new_value"               # Updated value
   )
   
   # Track records that were already conformant (no changes needed)
   self.reporter.track_record_processed(
       class_name="nmdc:Biosample",
       slot_name="field_name", 
       subclass_type="nmdc:Biosample",
       value="existing_value"
   )
   ```

4. **Track unmapped or missing values**:
   ```python
   # Track values that couldn't be mapped/processed
   self.reporter.track_unmapped_value(
       class_name="nmdc:Biosample",
       slot_name="field_name",
       value="unmappable_value"
   )
   
   # Track fields that were missing expected values
   self.reporter.track_missing_value(
       class_name="nmdc:Biosample", 
       slot_name="field_name"
   )
   ```

5. **Generate final report**:
   ```python
   self.reporter.generate_final_report()
   ```

The reporter generates three tables:
- **Records Updated**: Shows what was changed (Class, SubClassType, Slot, Source Value, Conformant, Not Conformant, Updated, Target Value)
- **Unmapped Values**: Shows values that couldn't be processed
- **Missing Values**: Shows fields that were missing expected values 

## Adding Transaction Support

To add MongoDB transaction support with commit/rollback functionality to your migrator:

1. **Update the upgrade() method signature**:
   ```python
   def upgrade(self, commit_changes: bool = False):
       """
       Migrates the database with optional commit/rollback support.
       
       Args:
           commit_changes: If True, commits changes. If False (default), rolls back.
       """
   ```

2. **Import MongoAdapter for type checking**:
   ```python
   from nmdc_schema.migrators.adapters.mongo_adapter import MongoAdapter
   ```

3. **Add the transaction detection pattern** (use one of these approaches):

   **Option A: Using execute_in_transaction() (Recommended for complex migrations)**:
   ```python
   def upgrade(self, commit_changes: bool = False):
       # Initialize your components (reporter, schema, etc.)
       self.reporter = MigrationReporter(self.logger)
       
       # Check for MongoDB adapter and use unified transaction control
       if isinstance(self.adapter, MongoAdapter):
           # MongoDB adapter - use single transaction for all operations
           try:
               self.adapter.execute_in_transaction(
                   operations_callback=self._perform_all_migration_operations,
                   commit_changes=commit_changes
               )
               
               if commit_changes:
                   self.logger.info("Transaction committed (changes have been saved)")
               else:
                   self.logger.info("Transaction rolled back (no changes were saved)")
                   
           except Exception as e:
               self.logger.error(f"Migration failed: {e}")
               raise
       else:
           # Dictionary adapter or other - no transactions available
           self._perform_migration_operations()
           if not commit_changes:
               self.logger.info("Note: Non-MongoDB adapter doesn't support rollback")
   
   def _perform_all_migration_operations(self, adapter, session):
       """
       Callback method that receives adapter and session from execute_in_transaction().
       All operations here use the same MongoDB session for atomic transactions.
       """
       # Document processing (transactional)
       adapter.process_each_document("collection_name", [self.transform_function], session)
       
       # Collection creation (not transactional in MongoDB)
       adapter.create_collection("new_collection")
       
       # Document insertion (transactional)
       adapter.insert_document("new_collection", {"data": "value"}, session)
       
       # Generate report
       if self.reporter:
           self.reporter.generate_final_report()
   ```

   **Option B: Using process_collections_in_transaction() (For document-focused migrations)**:
   ```python
   def upgrade(self, commit_changes: bool = False):
       # Initialize your components (reporter, schema, etc.)
       self.reporter = MigrationReporter(self.logger)
       
       if isinstance(self.adapter, MongoAdapter):
           # MongoDB adapter - use transaction support for document processing
           try:
               self.adapter.process_collections_in_transaction(
                   collection_names=["collection1", "collection2"],
                   document_processor=self.transform_function,
                   commit_changes=commit_changes
               )
               
               self.reporter.generate_final_report()
               
               if commit_changes:
                   self.logger.info("Transaction committed (changes have been saved)")
               else:
                   self.logger.info("Transaction rolled back (no changes were committed)")
                   
           except Exception as e:
               self.logger.error(f"Migration failed: {e}")
               raise
       else:
           # Non-MongoDB adapter - process collections directly
           for collection_name in ["collection1", "collection2"]:
               self.adapter.process_each_document(collection_name, [self.transform_function])
           
           self.reporter.generate_final_report()
           
           if not commit_changes:
               self.logger.info("Note: Non-MongoDB adapter doesn't support rollback")
   ```

**Examples:**
- See `migrator_from_1_0_0_to_EXAMPLE.py` for unified transaction pattern with `execute_in_transaction()`
- See `migrator_from_11_9_1_to_11_10_0.py` for document-focused pattern with `process_collections_in_transaction()`

## Testing the migrator

##### Summary of steps to test a migrator:

1. Create a local copy of the MongoDB database with a schema that conforms to the release from which you are migrating.
2. Check that the database has been loaded correctly.
3. Run the migrator against the test database.
4. Run validation checks against the migrated database.

##### Running a migrator step-by-step:

1. **Set up Docker environment and MongoDB database**

First, create a local environment configuration:

```bash
# Copy the environment template
cp nmdc_schema/migrators/.docker/.env.example nmdc_schema/migrators/.docker/.env
# Edit .env with your actual MongoDB connection settings if needed
```

Then, spin up a MongoDB container using the docker-compose in this repo:

```bash
# From the migrators directory
# make sure mongo_init/mongoKeyFile has 600 permissions
cd nmdc_schema/migrators/.docker
docker-compose up -d mongo mongo-init  # or
docker compose up -d mongo mongo-init
```

Once the containers are running, check the ports. The default ports are:
- 27017 (internal docker port)  
- 27022 (external connection to mongo) for MongoDB

*Note:* This will most often be a production database. For a release with many migrators, all migrators should be 
applied in order, to the copy of the production database.

2. **Load production data into MongoDB**

```bash
# Get the mongo container id for later steps
docker ps -a

# Find the most recent docker dump
ssh your-user-name@dtn01.nersc.gov
ls /global/cfs/projectdirs/m3408/nmdc-mongodumps/  

# Download the dump (replace with actual dump name)
rsync -av --exclude='_*' --exclude='fs\.*' -e "ssh " \
  your-user-name@dtn01.nersc.gov:/global/cfs/projectdirs/m3408/nmdc-mongodumps/dump_nmdc-prod_2025-02-10_20-12-02 \
  /tmp/remote-mongodump/nmdc

# Copy the dump to the mongo container
docker cp /tmp/remote-mongodump [mongo_container_id]:/tmp/

# Access the mongo container to load the dump
docker exec -it [mongo_container_id] bash

# Inside the container, restore the database
mongorestore -v -u admin -p root --authenticationDatabase=admin --drop \
  --nsInclude='nmdc.*' --gzip \
  --dir /tmp/remote-mongodump/nmdc/dump_nmdc-prod_2025-02-10_20-12-02/ 
```

3. **Verify database loading**

```bash
# Access the MongoDB container
docker exec -it nmdc-schema-migrator-dev-mongo-1 bash
```

```bash
# Connect to MongoDB
mongosh mongodb://admin:root@mongo:27017/nmdc?authSource=admin

# Check the database has records
db.biosample_set.find({}).pretty()

# Count records per collection
db.runCommand("listCollections").cursor.firstBatch
  .filter(function(collection) { return !collection.name.startsWith("system.") })
  .sort(function(a, b) { return a.name.localeCompare(b.name) })
  .forEach(function(collection) { 
    print(collection.name + ": " + db.getCollection(collection.name).count()) 
  })
```

4. **Run the migrator**

```bash
# Rollback (Default - Safe Mode)
# These all do the same thing - rollback by default
% make run-migrator MIGRATOR=migrator_from_1_0_0_to_EXAMPLE
% make run-migrator MIGRATOR=migrator_from_1_0_0_to_EXAMPLE ACTION=rollback

# Commit (Save Changes)
# This commits the changes to the database
% make run-migrator MIGRATOR=migrator_from_1_0_0_to_EXAMPLE ACTION=commit
```
