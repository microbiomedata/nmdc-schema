# Downstream schema compatibility

A schema change can pass this repository's tests while breaking a consumer's
generated artifacts, Python constructors, or persisted-data readers. A pinned
consumer dependency makes its build reproducible; it does not establish
compatibility with a candidate schema or with data migrated by another service.

The [coordination umbrella](https://github.com/microbiomedata/nmdc-schema/issues/3427)
tracks the immediate rollout and the automation work. The machine-readable
[consumer registry](https://github.com/microbiomedata/nmdc-schema/blob/main/assets/schema-consumers.yaml)
records repository ownership, dependency declaration paths, and implementation
issues. It is an inventory, not a lockfile or an enabled workflow configuration.
Read current versions from each consumer's dependency files.

`planned_integration` means that a consumer's required checks are identified but
its runnable integration has not been established here. `discovery` means that
the package dependency is known and the relevant check/owner still needs to be
confirmed. Neither status means that a consumer has passed a compatibility run.
Named maintainers and exact integration entry points must be confirmed during
implementation. Keep the registry current when a consumer adopts a new package,
adds an integration check, or retires a dependency.

## Responsibilities

`nmdc-schema` owns candidate/release identity and cross-repository coordination.
Each consumer repository owns its tests, dependency pins, lockfile, generated
artifacts, and update PR. The first automation targets are `submission-schema`
and `nmdc-lakehouse-schema`, which derive products from the source schema.

Runtime, portal, and metadata-producer checks should follow their actual data
paths: construct records, validate or ingest them, serialize them, and verify
that required information survives. Successful imports alone are insufficient.

For the lakehouse, the dependency chain is:

```text
nmdc-schema -> nmdc-lakehouse-schema -> nmdc-lakehouse
       \------------------------------^
```

The lakehouse needs a source schema compatible with the released flat artifact.
Use the artifact's recorded source provenance when selecting that pair. If a
source release arrives first, wait for a compatible flat product and expose that
waiting state in the update workflow.

Production GOLD translation belongs to `nmdc-runtime`. The historical
`sample-annotator` pipeline still contains old model references, but
[the ownership record](https://github.com/microbiomedata/sample-annotator/issues/106#issuecomment-2590703062)
states that production conversion moved to runtime. Confirm operational use
before treating other historical code as an additional release dependency.

## Candidate checks to implement

The [orchestration issue](https://github.com/microbiomedata/nmdc-schema/issues/3428)
defines the work; this guide does not claim that the matrix is already enabled.

For each run, record the exact source commit, freshly built wheel identity and
digest, consumer commit, installed candidate identity, check entry point, and
result. Verify that imports resolve to the candidate wheel instead of an older
locked release or an editable sibling checkout.

Use isolated consumer environments and retain their normal pinned CI. A
candidate source is expected to change generated artifacts, so generate into a
temporary destination and report a diff. Keep baseline reproducibility checks
separate from candidate compatibility checks.

Consumer results should distinguish pass, failure, and unavailable integration.
Include a passing baseline and a known incompatible case to show that each
check can detect the failure it is intended to prevent. Candidate code runs in
unprivileged jobs; credentials for creating update PRs belong to the separate
release workflow.

The Agent change in [PR #3385](https://github.com/microbiomedata/nmdc-schema/pull/3385)
provides a concrete negative control. For Person and Organization credit
associations, test the containing Study/DataGeneration records and side tables,
and compare emitted row keys with generated columns. Verify that email, ORCID,
and ROR survive through the output projection. The
[generator fix](https://github.com/microbiomedata/nmdc-lakehouse-schema/issues/11)
and [candidate coverage](https://github.com/microbiomedata/nmdc-lakehouse-schema/issues/12)
are tracked separately.

## Release and migration coordination

[Release orchestration](https://github.com/microbiomedata/nmdc-schema/issues/3429)
will provide a version-discovery or release-event contract. Consumer workflows
will open or update one PR per target release, with pin/lock changes, regenerated
artifacts, schema differences, test results, and links to required code changes.
Inspect the built distribution's actual artifact as well as the repository copy.

Before adopting a breaking persisted-data change:

1. Link affected consumer issues from the source PR and the coordination issue.
2. Implement and test producers, readers, and derived artifacts against the
   candidate. Include index paths and frontend/API models where applicable.
3. Record the compatible consumer versions and the chosen transition or cutover
   sequence. Test any period in which old and new representations coexist.
4. Follow the existing maintainer release process for publishing, deploying,
   and migrating data. Merging a source PR or opening a dependency-update PR
   does not perform or authorize those operations.

The umbrella contains the #3385 rollout links, including the separate
[mass-spectrometry generator update](https://github.com/microbiomedata/nmdc_mass_spectrometry_metadata_generation/issues/280).
The two derived-schema repositories have their own candidate-check and
release-update issues in the registry. Broader repository dependency policy
remains tracked in [#2216](https://github.com/microbiomedata/nmdc-schema/issues/2216).
