# Maintaining the NMDC Schema
## Dependencies
To make new release of the schema, you must have the following installed on your system:
- [poetry](https://python-poetry.org/docs/#installation/)
- [pandoc](https://pandoc.org/installing.html)
- [yq](https://github.com/mikefarah/yq)
  - Specifically, [Mike Farah's Go-based yq](https://github.com/mikefarah/yq)
- (Optional) [ROBOT](http://robot.obolibrary.org/)
  - Editor's note: We may eventually switch to using [Apache Jena<sup>1</sup>  ARQ](https://jena.apache.org/documentation/query/) instead
- (Optional) [Apache Jena<sup>1</sup> RIOT](https://jena.apache.org/documentation/io/)
  - This is only necessary for dumping, repairing, and validating MongoDB data; which occurs when generating and validating RDF/TTL

<sup>1</sup> The lead maintainer of this repository uses Apache Jena version `4.8.0`, which you can [download here](https://archive.apache.org/dist/jena/binaries/).

## Making changes to the NMDC Schema
To track changes made to the NMDC Schema, it is best maintained by following these steps:
1. Submit an [issue](https://github.com/microbiomedata/nmdc-schema/issues) detailing problem.
2. Create a branch to address this issue that uses the same number as the issue tracker. For example, if the issue is `#50` in the issue tracker, name the branch `issue-50`. This allows other developers to easily know which branch needs to be checked out in order to contribute.
3. Create a pull request that fixes the issue. If possible, create a draft (or WIP) branch early in the process.
4. Merge pull request once all the necessary changes have been made. If needed, tag other developers to review pull request. 
5. Delete the issue branch (e.g., branch `issue-50`).

This project previously used a manually curated [**Change log**](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md). More recently, we have decided that GitHub's auto-generated release notes are sufficient. Commit and pull messages should be written with this in mind: they will become part of the repo's documentation. 

When the pull request is merged into the `main` branch, new documentation will be generated for the changed schema.

The changes can be cecked locally with `make all test`

## Making a PyPI release of the NMDC Schema

The NMDC Schema is deployed to [PyPI](https://pypi.org/project/nmdc-schema/) using the [pypi-publish](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/pypi-publish.yml) github action.

### Steps for making a release
1. Generate the set of artifacts by running `make clean` followed by `make all`.

2. If **#1** succeeds and changes have been made to the schema, update the `version` [nmdc.yaml](https://github.com/microbiomedata/nmdc-schema/blob/main/src/schema/nmdc.yaml) using semantic versioning (i.e., `<major number>`**.** `<minor number>`**.**`<patch number>`). 
  
    #### Guidelines for updating semantic version
    * If the change **breaks** backward compatibility, update the **major** number.
      Examples:
      - Removing a class, slot, or enum
    * If functionality is added and the change **does not** break backward compatibility, update the **minor** number.
      Examples:
      - Adding a class, slot, or enum
      - Deprecating a class, slot, or enum
    * If the change neither adds functionality nor breaks backward compatibility, update the **patch** number.
      Examples:
      - Fixing typos
      - Adding comments or annotations
      
**Note:** Changes can be made to the Python package (e.g., functionality added to the CLI) that do not affect the schema. In these cases, the schema version does not need to be changed, only the PyPI version needs to be updated.

3. If **#1** succeeds:
  * Make the sure the sections of the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) (discussed above) have been updated appropriately.
  * Change the `Current (update before releasing)` section of the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) into a hyperlink that matches the tag you assign to the release in step **#4** below.  
  For example, if the tag assigned for the release is `1.0.0`, change the section to:  
  ```
  [2021.07.01rc1](https://github.com/microbiomedata/nmdc-schema/releases/tag/1.0.0)
  ```
4. Create a GitHub release of the schema using the `Releases -> Draft new release` links. The tag of the release must conform to the semantic versioning format `<major number>.<minor number>.<patch number>` (see semantic versioning guidelines above). The value of this tag needs to match the value you assigned to the `Current (update before releasing)` section in the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md) (discussed above).

5. Give the release the same name as the semantic version tag you created in **#4**.

6. Fill in the changes made for this release. This is most easily done by copying the information you recorded in the [Change log](https://github.com/microbiomedata/nmdc-schema/blob/main/CHANGELOG.md).

7. Click `Publish release` button. This fires the action to update the [PyPI package](https://pypi.org/project/nmdc-schema/).

### Notify NMDC Schema users
After the new version has been released on PyPI, notify the [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime) and the `metadata` channel on the NMDC slack group that the `nmdc-schema` has been updated.

## Maintaining the Documentation
Do **not** git add the files in `docs`. Custom documentation is added to (or edited in) the `src/docs/` directory.

The new documentation is deployed when changes are pushed to the main branch via the [build-deploy-documentation](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/build-deploy-documentation.yaml) workflow.


After the GitHub action completes, the documentation will be available from a URL [https://microbiomedata.github.io/nmdc-schema](https://microbiomedata.github.io/nmdc-schema/)

