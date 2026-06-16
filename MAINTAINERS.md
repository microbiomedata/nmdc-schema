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

Changes are recorded through GitHub's auto-generated release notes rather than a manually curated change log. Write commit and pull-request messages with this in mind: they are the source those notes are built from. See [Release notes](#release-notes) below for details.

When the pull request is merged into the `main` branch, new documentation will be generated for the changed schema.

The changes can be cecked locally with `make all test`

## Making a PyPI release of the NMDC Schema

> The authoritative, step-by-step release procedure is the
> [infra-admin release runbook](https://github.com/microbiomedata/infra-admin/blob/main/releases/nmdc-schema.md).
> Pre-release (release candidate) mechanics and the `poetry-dynamic-versioning` setup
> are documented in the *Pre-release Process* section of
> [`CLAUDE.md`](CLAUDE.md). This section keeps only the version-numbering guidelines
> and the release notes convention; follow the runbook for the current steps.

The package is published to [PyPI](https://pypi.org/project/nmdc-schema/) by the
[pypi-publish](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/pypi-publish.yaml)
GitHub Action, which fires on the GitHub release `created` event. The package version is
derived from the git tag by `poetry-dynamic-versioning`; there is no `version` field to
hand-edit before a release.

### Guidelines for updating semantic version

The release tag uses the semantic-versioning format `<major>.<minor>.<patch>`, prefixed
with `v` (e.g. `v11.20.0`). Pre-release tags add a `-rc.N` suffix (e.g. `v11.20.0-rc.1`).

* If the change **breaks** backward compatibility, update the **major** number.
  Examples:
  - Removing a class, slot, or enum
* If functionality is added and the change **does not** break backward compatibility,
  update the **minor** number. Examples:
  - Adding a class, slot, or enum
  - Deprecating a class, slot, or enum
* If the change neither adds functionality nor breaks backward compatibility, update the
  **patch** number. Examples:
  - Fixing typos
  - Adding comments or annotations

**Note:** Changes can be made to the Python package (e.g. CLI functionality) that do not
affect the schema. The version still advances because it tracks the git tag; such a change
is a patch-level release.

### Release notes

Release notes are GitHub's **auto-generated** notes (the *Generate release notes* button
on the release form), built from merged pull-request titles plus a compare link. Write PR
titles so they read as change-log entries. Larger releases may add a short hand-written
**Highlights** section above the generated list; see the
[v11.20.0 notes](https://github.com/microbiomedata/nmdc-schema/releases/tag/v11.20.0) for
an example.

This repository previously kept a manually curated `CHANGELOG.md`. It was retired on
2024-06-14 in commit
[010ef75d2](https://github.com/microbiomedata/nmdc-schema/commit/010ef75d22c50d6b7cfa7eed825d0b99bbd74789)
in favor of the auto-generated notes. Do not reintroduce a `CHANGELOG.md` without first
documenting the decision in
[Audit versioning guidelines and compliance](https://github.com/microbiomedata/nmdc-schema/issues/2876).

### Notify NMDC Schema users
After the new version is on PyPI, notify [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime) and the `metadata` channel on the NMDC Slack that `nmdc-schema` has been updated.

## Maintaining the Documentation
Do **not** git add the files in `docs`. Custom documentation is added to (or edited in) the `src/docs/` directory.

The new documentation is deployed when changes are pushed to the main branch via the [build-deploy-documentation](https://github.com/microbiomedata/nmdc-schema/blob/main/.github/workflows/build-deploy-documentation.yaml) workflow.


After the GitHub action completes, the documentation will be available from a URL [https://microbiomedata.github.io/nmdc-schema](https://microbiomedata.github.io/nmdc-schema/)

## Troubleshooting Documentation Deployment

If https://microbiomedata.github.io/nmdc-schema/ returns 404:

1. Check if GitHub Pages is enabled: `gh api repos/microbiomedata/nmdc-schema/pages`
2. If it returns 404, go to Settings → Pages → Source → select "gh-pages" branch
3. Manually trigger deployment at https://github.com/microbiomedata/nmdc-schema/actions/workflows/deploy-docs.yaml

**Note:** Deleting the `gh-pages` branch disables GitHub Pages. You must re-enable it in Settings.
