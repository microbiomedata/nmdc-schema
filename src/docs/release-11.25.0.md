# nmdc-schema 11.25.0: what consumers need to know

This page covers what changes in 11.25.0 for repositories that use nmdc-schema, what each of them has to do, what is knowingly left unfixed, and how the linkml 1.12 build could be backed out. It describes 11.25.0 as planned for rc3 and later. 11.25.0rc1 (built with linkml 1.11.1) and 11.25.0rc2 (built with linkml 1.12.1) are on PyPI.

Each claim says how it is known: "tested" with a date means it was run, "read" means it was read from source without running it. For the general process, see [Downstream schema compatibility](downstream-compatibility.md).

## Version number

11.25.0 is a minor release, but it removes one slot, `collection_time_inc` on `Biosample`. MAINTAINERS.md calls a removal a major-version change, and earlier v11 minor releases have not followed that rule either. That question is open in https://github.com/microbiomedata/nmdc-schema/issues/2876. Read the release notes before moving a pin.

## What changes

Packaging:

- The generated files are built with linkml and linkml-runtime 1.12.1.
- The published dependency ranges are unchanged: `linkml>=1.9.0,<2.0.0` and `linkml-runtime>=1.9.0,<2.0.0` (read, `pyproject.toml`). Consumers keep whatever linkml they lock.
- `requires-python` is `>=3.10,<3.15`. CI tests 3.10, 3.13 and 3.14.
- Developers build with uv instead of Poetry (https://github.com/microbiomedata/nmdc-schema/pull/3528). This does not affect installing the package.

Schema content, v11.24.1 compared with main on 2026-10-15 (tested, SchemaView):

- Removed: `collection_time_inc`. The 11.25.0 migrator changes no data; it stops with an error if a `biosample_set` document still has the slot. Production had none (checked in https://github.com/microbiomedata/nmdc-schema/pull/3495).
- Added classes for SIP (stable isotope probing): `IsotopeLabelingProcess`, `IsotopologAddition`, `IsotopologComposition`, `DensityGradientFractionationProcess`.
- `AnalysisTypeEnum` gains 10 values.
- MIxS slots are imported from MIxS v7.0.1 instead of v6.3.0 (https://github.com/microbiomedata/nmdc-schema/pull/3501). No migrator is needed: the JSON Schema differs only in descriptions, titles and examples (tested 2026-10-14).
- One title changes: `estimated_size`, used only by `Organism`, from "estimated size" to "estimated genome size". 14 descriptions change.

Generated files (linkml 1.12 build):

| change | example | how known |
|---|---|---|
| id patterns are wrapped by linkml as `^(?:...)$` | `^(?:(nmdc):sty-([0-9][a-z]{0,6}[0-9])-([A-Za-z0-9]{1,}))$` | tested 2026-10-15 with https://github.com/microbiomedata/nmdc-schema/pull/3549; rc2 had doubled anchors, `^(?:^(nmdc):sty-...$)$` |
| `type` accepts the full class URI as well as the CURIE | `https://w3id.org/nmdc/Study` and `nmdc:Study` (83 `type` enums) | tested on rc2; https://github.com/microbiomedata/nmdc-schema/issues/3537 |
| optional slots ranged on an enum or class accept `null` | 191 class-slot pairs on 125 slots | tested, rc2 compared with rc1; https://github.com/microbiomedata/nmdc-schema/issues/3424 |
| slot examples appear in the JSON Schema, including one `id` example per class | `nmdc:bsm-11-001pmq31` on `Biosample` | tested 2026-10-15; https://github.com/microbiomedata/nmdc-schema/pull/3545 |
| the OWL build logs many more "Multiple owl types" warnings | 203 with 1.12.1, 1 with 1.11.1 | observed in the build log 2026-10-15; effect on the OWL file not checked |

Code that reads pattern strings out of the JSON Schema must accept the `^(?:...)$` wrapping. `nmdc_schema.get_typecode_for_future_ids` reads both the wrapped and the older form (https://github.com/microbiomedata/nmdc-schema/pull/3511, https://github.com/microbiomedata/nmdc-schema/pull/3549).

## What each consumer has to do

Pins were read from each repository's default branch on 2026-10-15.

| consumer | current pin | what it has to do for 11.25.0 | how known | tracked in |
|---|---|---|---|---|
| nmdc-runtime | `nmdc-schema==11.24.0` (`pyproject.toml:60`) | Move the pin and merge https://github.com/microbiomedata/nmdc-runtime/pull/1659 in the same change. Without it, the minter finds no typecodes and the test setup fails to import. Run the 11.24.0 to 11.24.1 and 11.24.1 to 11.25.0 migrators. | tested with rc2: 0 typecodes on main, 40 with the PR; the PR's tests pass against the single-anchored patterns (tested 2026-10-15) | https://github.com/microbiomedata/nmdc-runtime/issues/1658 |
| nmdc-server | `nmdc-schema==11.24.0` and `nmdc-submission-schema==11.24.0` (`pyproject.toml:27-28`); web app at `v11.24.1` (`web/package.json:46`) | Nothing required for nmdc-schema 11.25.0. Keep `nmdc-submission-schema==11.24.0` until https://github.com/microbiomedata/nmdc-server/issues/2401 is fixed; that break comes from submission-schema's new titles, not from nmdc-schema. | imports tested with rc1 and rc2; tests need Postgres and were not run | https://github.com/microbiomedata/nmdc-server/issues/2401 |
| submission-schema | `nmdc-schema==11.24.0`, dev group only | Move the dev pin, rebuild, release nmdc-submission-schema 11.25.0. Its own move to linkml 1.12 is separate. | tested with rc2: `make all` and 44 tests pass | https://github.com/microbiomedata/submission-schema/issues/493 |
| nmdc_mass_spectrometry_metadata_generation | `nmdc-schema==11.24.0` (`requirements.txt:2`) | Move the pin to 11.25.0 and release. Its checks fail today because 11.24.0 cannot read linkml-runtime 1.12's id patterns. | tested with rc1 and rc2: 68 pass, 4 need credentials | https://github.com/microbiomedata/nmdc_mass_spectrometry_metadata_generation/issues/287 |
| nmdc-mass-spec-automation | nmdc_mass_spectrometry_metadata_generation `@2.12.0` (`requirements.txt:1`) | Move to the release above. | tested with rc1 and rc2: 121 unit tests pass | https://github.com/microbiomedata/nmdc-mass-spec-automation/issues/126 |
| nmdc-lakehouse | hard-coded 11.24.0 | Accept 11.25.0 as a source version. | tested with rc1 and rc2 | https://github.com/microbiomedata/nmdc-lakehouse/issues/395 |
| nmdc-lakehouse-schema | | Update the expected class count from 61 to 62. | tested with rc1 and rc2 | https://github.com/microbiomedata/nmdc-lakehouse/issues/395 |
| nmdc_automation | `nmdc-schema = "^11.24.0"` | Nothing. | tested with rc1 and rc2: same results as 11.24.1 | |
| nmdc-ingest-agent | | Nothing new; its `TargetGeneEnum` failure predates 11.25.0. | tested: same failures on 11.24.1 | https://github.com/microbiomedata/nmdc-ingest-agent/issues/62 |
| nmdc-ai-eval, nmdc-metadata-suggestor-ai-tool | no nmdc-schema dependency | Nothing; they get nmdc-schema content only through nmdc-submission-schema. | read | |
| ontology-loader | `nmdc-schema = "*"` | Nothing. | tested with rc1 and rc2: 131 pass | |

## Known gaps in 11.25.0

1. Full-URI `type` (https://github.com/microbiomedata/nmdc-schema/issues/3537). Validation accepts `"type": "https://w3id.org/nmdc/Study"`, but nmdc-runtime reads `type` as a CURIE (read: `metadata.py:168`, `alldocs.py:317`, `linked_instances.py:209`). Production has no URI `type` values (counted 2026-10-15). Each fix considered has a cost: https://github.com/microbiomedata/nmdc-schema/issues/3537#issuecomment-6194946359
2. Nulls (https://github.com/microbiomedata/nmdc-schema/issues/3424). `null` satisfies optional enum- and class-ranged slots, including some that class rules require. Production's only explicit nulls are `description` on all 22,722 `ontology_class_set` documents (counted 2026-10-15). ontology-loader stopped writing them in https://github.com/microbiomedata/ontology-loader/pull/92; the stored ones remain.
3. Typecodes are still derived from id patterns rather than declared in the schema.

Security: Dependabot alert 58 (setuptools, medium) was dismissed because oaklib caps setuptools below the fixed version. No code-scanning alerts were open on 2026-10-15.

## Backing out the linkml 1.12 build

If the 1.12 build is not acceptable, 11.25.0 (or, after release, 11.25.1) can be built with linkml 1.11.1, as rc1 was:

- Add back the dev-group caps on `linkml` and `linkml-runtime` below 1.12 that https://github.com/microbiomedata/nmdc-schema/pull/3529 removed, as https://github.com/microbiomedata/nmdc-schema/pull/3532 did before rc1, then relock and rebuild.
- Also revert https://github.com/microbiomedata/nmdc-schema/pull/3549. linkml 1.11.1 ignores `partial_match` and adds no anchors, so without our own anchors the id patterns would be unanchored (tested 2026-10-15).
- With rc1, every consumer above passed and nmdc-runtime's minter worked without https://github.com/microbiomedata/nmdc-runtime/pull/1659 (tested 2026-10-15).
- The JSON Schema would then carry none of the changes in the generated-files table, and no examples (0 with 1.11.1 compared with 655 with 1.12.1, tested 2026-10-15).
- Consumers need nothing different, since the published dependency ranges do not change.
- Not tested: a 1.11.1 build of current main.
