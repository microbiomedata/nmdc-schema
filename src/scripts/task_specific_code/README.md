# Napa Compliance

This code has been executed, the results were accepted, and it should not need to be run again. It is being included as
documentation. The Python files have been moved from `nmdc_schema/` to `src/scripts/task_specific_code/` and they
shouldn't be expected to work from that location. These scripts demonstrate many good design principles, but may not
meet all of nmdc-schema's current code quality standards.

* insert_many_pymongo.py
* metap_records_delete.py
* misc_reid_code.py

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
python -m black src/scripts/task_specific_code/metap_records_delete.py
```
