# Maintaining the NMDC Schema
## Making changes to the NMDC Schema
In order to track changes made to the NMDC Schema, it is best maintained by following these steps:
1. Submit an [issue](https://github.com/microbiomedata/nmdc-schema/issues) detailing problem.
2. Create a branch to address this issue that uses the same number as the issue tracker. For example, if the issue is `#50` in the issue tracker, name the branch `issue-50`. This allows other developers to easily know which branch needs to be checked out in order to contribute.
3. Create a pull request that fixes the issue. If possible, create a draft (or WIP) branch early in the process.
4. Merge pull request once all the necessary changes have been made. If needed, tag other developers to review pull request. 
5. Delete the issue branch (e.g., branch `issue-50`).

As you make you make changes to the NMDC Schema, it is **HIGHLY** recomended that you update the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) in order to easily document the changes when a release is made. In the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md), the set of changes that have **not** been released appear under the section titled `Current (update before releasing)`. As you update the schema, add information to the following sections:
#### Added
  - Add information about new classes, slots, enums, etc. added to the schema.
#### Fixed
  - Add information about changes made to the schema that **fixes** a problem.
#### Changed 
  - Add information about changes made to the schema that were not made to fix a problem.
#### Removed
  - Add information about classes, slot, enums etc. removed from the schema


## Making a release of the NMDC Schema

The NMDC Schema is deployed to PyPI via the [pypi-publish](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/pypi-publish.yml) github action.

The steps for making a release are:


See the instructions at the top of [Makefile](Makefile)

First install the linkml python package and mkdocs:

```bash
. environment.sh
pip install -r requirements.txt
```

Then every time you change the source schema, run:

```bash
make all
```

This will generate files in:

 * [docs]
 * [jsonschema]
 * [shex]
 * [owl]
 * [rdf]

## Documentation
Do **not** git add the files in `docs`. Custom documentation is added to (or edited in) the `src/docs/` directory.

The new documentation is deployed when changes are pushed to the main branch via the [build-deploy-documentation](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/build-deploy-documentation.yaml) workflow.


After the github action completes, the documentation will be available from a URL [https://microbiomedata.github.io/nmdc-schema](https://microbiomedata.github.io/nmdc-schema/)

