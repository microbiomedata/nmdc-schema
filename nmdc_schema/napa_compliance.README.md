# Napa Compliance

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
