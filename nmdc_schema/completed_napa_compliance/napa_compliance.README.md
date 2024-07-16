# Napa Compliance

This code has been executed, the results were accepted, and it should not need to be run again. It is being included as
documentation. The Python files have been moved from `nmdc_schema/` to `nmdc_schema/completed_napa_compliance/` and they
shouldn't be expected to work from that location.

One shouldn't assume that the installation notes below are intended for any other nmdc-schema development.

## Installing Python packages

```shell
# So Python scripts can read `.env` files.
pip install python-dotenv

# So Python scripts can access Mongo databases.
pip install pymongo

# So Python code is formatted in a standard way.
pip install black
```

## Formatting source code

You can use [`black`](https://black.readthedocs.io/en/stable/) to format the Python code you write, by running:

```shell
python -m black /path/to/python/code.py
```

For example:

```shell
python -m black nmdc_schema/connect_napa_mongo.py
python -m black nmdc_schema/metab_id_refactor.py
python -m black nmdc_schema/napa_study_biosample_omics_migration.py
python -m black nmdc_schema/runtime_api_operations.py
```
