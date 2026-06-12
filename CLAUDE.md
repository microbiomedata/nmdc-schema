# NMDC-Schema Development Guide

## Authoritative conventions (see also)

The repository's committed contributor docs are the canonical source for schema-modeling and process conventions. This file does not duplicate them; consult them and keep them authoritative:

- `CONTRIBUTING.md`: Modeling Best Practice (naming, documentation, examples and counter-examples, enums for categorical values, PV `is_a`, reuse, placing classes under upper-level classes, ID patterning), the Current Policy vs Legacy Guidance table, and the ADR log pointer for recording decisions.
- `DEVELOPMENT.md`: prerequisites and local development environment.
- `MAINTAINERS.md` and the [infra-admin release runbook](https://github.com/microbiomedata/infra-admin/blob/main/releases/nmdc-schema.md) (in the separate `microbiomedata/infra-admin` repo): release procedure.
- `nmdc_schema/migrators/README.md`: migrator authoring and testing.

This guide adds the operational details and gotchas that are not (yet) captured in those files.

## Build/Lint/Test Commands
- Install: `poetry install --with dev,deps`
- Build: `make all` or `make site`
- Clean: `make squeaky-clean`
- All tests: `make test`
- Python tests: `make test-python`
- Schema tests: `make test-schema`
- Run single test: `poetry run pytest tests/test_file.py -v`
- Run doctest: `poetry run python -m doctest -v path/to/file.py`
- Lint: `make linkml-lint` or `make linkml-lint-all` (outputs to local/linkml-lint-all.log)
- Check schema patterns: `poetry run python src/scripts/schema_pattern_linting.py --schema-file src/schema/nmdc.yaml`
- View docs locally: `make serve` (in Docker: `poetry run mkdocs serve --dev-addr 0.0.0.0:8000`)

Build prerequisites and gotchas:
- `make all` needs `yq` (mikefarah/yq) on PATH (`brew install yq`); it is used to strip readonly metaslots and apply MIxS customizations. Java/ROBOT is NOT needed: the OWL artifact is produced by `linkml generate owl`.
- `squeaky-clean` runs `clean examples-clean shuttle-clean site-clean`; it deliberately leaves `src/schema/mixs.yaml` in place. Removing that file is a separate fast target (`mixs-yaml-clean`, just an `rm`); regenerating it (`make src/schema/mixs.yaml`) is the slow, network-dependent step. For a full-from-scratch rebuild including a fresh MIxS pull: `make squeaky-clean mixs-yaml-clean && make src/schema/mixs.yaml && make squeaky-clean all test`.
- CI tests only Python 3.10 and 3.13 (other workflows pin 3.12). `requires-python` is `>=3.10,<4.0`, so a too-new system Python (e.g. 3.14) is out of range and will break installs. Build and test against a supported interpreter.
- `local/.env` is optional. Its credential blocks (BioPortal key, NCBI BioSample Postgres, source MongoDB) are only consumed by specific scripts; `make all` and `make test` run without any of them.

## Script Entry Point Policy
- Keep `[project.scripts]` limited to package-backed, stable CLIs intended for default installs.
- Do not add ad-hoc aliases for `src/scripts/*` into `[project.scripts]`.
- For repo-local automation scripts, call them explicitly from Makefiles, e.g. `poetry run python src/scripts/<name>.py`.
- Do not add new modules under `nmdc_schema/` (the published package) without a client-facing purpose; experimental and developer-only scripts go under `src/scripts/`.

## Dependency Management

This is a Poetry repo. Sibling `submission-schema` migrated to `uv`; do not confuse the two.

- **Use poetry 2.4.1** (pinned in every CI workflow via `pipx install poetry==2.4.1`). The `poetry.lock` content-hash is poetry-version-sensitive: a different poetry version can report the lock as "out of sync with pyproject.toml" even when the dependencies are unchanged. Align dev/container poetry to the pinned version. CI runs `poetry check` (in `main.yaml`) to catch real pyproject/lock drift in PRs rather than on a teammate's fresh install. To sync after editing pyproject: `poetry lock` (no `--regenerate` unless you intend to bump versions).

- Never create a `uv.lock` here, and never run `uv add`, `uv sync`, or `uv lock`. If a stray `uv.lock` appears, delete it before committing.
- Before tightening any pin in `pyproject.toml` (especially `linkml`), check that `submission-schema` still resolves. nmdc-schema is a library, so a tighter pin propagates to consumers even when nmdc-schema itself does not exercise the feature. `linkml` and `linkml-runtime` versions must be paired (a runtime release can drop something the matching `linkml` references).
- `pyproject.toml` conventions: upper-bound policy (packages at 1.0 or above cap at the next major, pre-1.0 cap at the next minor); PEP 508 form (`"pkg>=min,<max"`, not the Poetry caret); alphabetical ordering within each dependency group; runtime deps in `[project.dependencies]`, dev tools in `[dependency-groups] dev`, `deptry` in its own `deps` group; transitive packages pinned for security are also added to `[tool.deptry] per_rule_ignores.DEP002`; comments cite the issue number that motivated a pin.

## Released migrators

Migrator partials under `nmdc_schema/migrators/partials/migrator_from_X_to_Y/` are versioned snapshots of migrations that have already run against the production database. Do not make functional changes to them; they are the authoritative record of what ran. Explanatory comments are fine. New breaking schema changes get a new migrator, not an edit to an old one (and a breaking change with no production data may legitimately ship no migrator, with the reason noted in the PR).

Whether a release needs a migrator at all is a conformance question, not a version-number question: if every database valid under the old schema is still valid under the new one, no migration is needed, and you record that fact with a no-op migrator rather than shipping nothing. Deletions are handled outside migrators. The authoritative explanation and the `make migrator` workflow are in [`nmdc_schema/migrators/README.md`](nmdc_schema/migrators/README.md) (which this section does not duplicate); backfilling no-op migrators for past releases that lack them is tracked in [#3180](https://github.com/microbiomedata/nmdc-schema/issues/3180).

## Workflow security and linting (actionlint + zizmor)

The GitHub Actions workflows in `.github/workflows/` are security-sensitive: they carry permissions, secrets, and the PyPI release path. Two static tools audit them:

- `actionlint`: workflow syntax, deprecated action references, and shell bugs in `run:` steps. It only lints shell in `run:` blocks when `shellcheck` is on PATH, and inline Python when `pyflakes` is on PATH; without those it silently skips its strictest checks. For a full-strength run install both (`brew install actionlint shellcheck`, `pipx install pyflakes`).
- `zizmor`: workflow security audit (credential persistence, cache poisoning, template injection, and more). Its default (`regular`) persona is what CI reports to code scanning; `--persona pedantic` surfaces extra lower-signal audits (excessive-permissions, undocumented-permissions, concurrency-limits, anonymous-definition) that the default hides.

When developing in this repo, if these tools are available in the active environment, run them against the workflows as a routine self-check. Do this whenever a workflow is edited, and opportunistically on any substantive session even when no workflow changed:

```bash
actionlint                                       # with shellcheck + pyflakes on PATH
uvx zizmor .github/workflows/                    # default persona (what CI reports)
uvx zizmor --persona pedantic .github/workflows/ # stricter, optional
```

Do not install the tools just to run this, and do not treat their absence as a failure; skip the check when they are not present. `actionlint` is a Go binary (`brew install actionlint`). `zizmor` runs with no install via `uvx zizmor` or `pipx run zizmor`.

As of June 2026 the workflows pass both `actionlint` (with shellcheck + pyflakes) and `zizmor` at default and `--persona pedantic`, with two deliberate exceptions. Act on new findings, but do not re-report these known, triaged ones:

- The credential-persistence (`artipacked`) findings on `deploy-docs.yaml` and `test-pages-build.yaml` are intentional, because those workflows push to gh-pages with the persisted token. They are suppressed inline with `# zizmor: ignore[artipacked]` and a reason. Proper token-scoped hardening stays open in #3147.
- The `pypi-publish.yaml` cache-poisoning and credential-persistence findings were fixed in #3160 (removed the release-trigger dependency cache; set `persist-credentials: false`). The `persist-credentials: false` change is validated by analysis, not a live run; confirm it with a pre-release before relying on it. Closed #3148.
- The pedantic-persona findings (excessive-permissions, concurrency-limits, undocumented-permissions, anonymous-definition) were fixed in #3162 by scoping permissions to the job with a top-level `permissions: {}` deny-all, adding concurrency groups (the publish job uses `cancel-in-progress: false`), documenting each elevated scope, and naming jobs. Closed #3161.

When editing permissions, keep the established pattern: top-level `permissions: {}`, and grant the minimum at the job level with an inline comment saying why. Do not edit `pypi-publish.yaml` casually; it is the release path and only fully exercises at publish time.

CI also runs zizmor in a non-blocking job that reports to code scanning (the Security tab), added in #3149. The local check is for faster, in-development feedback.

## Python linting and tooling

`ruff` is the single linter and formatter. It replaced black/autopep8 (formatting), flake8 (E/F/W), isort (I), bandit (the `S` security rules), and pydocstyle (D); those packages were removed from the dev group. `mypy` (types), `pylint`, `vulture`, and `pyroma` are kept because ruff does not fully cover them. `deptry` checks for unused/missing dependencies.

- Config lives in `[tool.ruff]` in `pyproject.toml`. Generated artifacts (`nmdc.py`, `nmdc_pydantic.py`, `nmdc_materialized_patterns.yaml`), `notebooks/`, and the frozen `migrators/partials/` are excluded.
- `make lint` runs `ruff check .` (the blocking CI gate, currently the `F`/pyflakes rules). `make format` runs `ruff format` + `ruff check --fix`.
- CI: `.github/workflows/lint.yaml` runs `ruff check` (blocking) plus a non-blocking `ruff check --select S` security scan. Formatting is not yet gated (the code is not uniformly format-clean); the one-time sweep is tracked in #3166. The security backlog (timeouts, hardcoded /tmp in `src/scripts`) is #3164; once cleared, add `"S"` to `select` and drop the separate step. mypy typing cleanup is #3165.
- ruff `S` reproduces bandit's findings, so bandit is redundant here. The in-repo `ruff` + `zizmor` (workflows) pair covers what CodeQL was doing for this repo (CodeQL had 0 open Python alerts), if a move away from CodeQL is wanted.

**YAML safety:** always use `yaml.safe_load` and `yaml.safe_dump` in authored code, never `yaml.load`/`yaml.dump` (even with `FullLoader`). The repo is uniformly on the safe variants as of #3163; keep it that way. linkml's own `yaml_dumper` is separate and fine.

Dependabot security updates and alerts are on; `.github/dependabot.yml` adds grouped weekly version updates for the `github-actions` and `pip` ecosystems. Secret scanning is on.

## Code Style Guidelines
- Follow PEP8 conventions; format with `ruff format` (black-compatible)
- Use snake_case for variables/functions, PascalCase for classes
- Type annotations required for all parameters and returns
- Imports: stdlib first, third-party next, local modules last
- Docstrings use triple double quotes with examples
- Prefer specific exception handling with descriptive messages
- Use pathlib for file operations instead of os.path
- Write verbose, descriptive variable and function names
- Use None return values to indicate absence of a result

## LinkML Mapping Metaslots — Conventions

Use typed subtypes (`exact_mappings`, `close_mappings`, `broad_mappings`,
`narrow_mappings`, `related_mappings`) in preference to generic `mappings`.

**Exception — keep `mappings` (generic) for:** schema.org properties
(`schema:QuantityValue`, `schema:latitude`, etc.), QUDT (`qud:unit`,
`qud:quantityValue`), and `prov:wasGeneratedBy`. These are
*property-to-property* alignments where SKOS directional semantics
(broader/narrower) don't apply. Do not "fix" these to `exact_mappings`.

**`see_also`** is for human-readable documentation pointers only: URLs,
GitHub issue links, specification documents. Ontology CURIEs belong in a
`*_mappings` slot. See #3031 for an open cleanup of MIXS CURIEs currently
in `see_also` in `portal_mixs_inspired.yaml`.

**`structured_aliases`** requires `literal_form`, a SKOS predicate
(`EXACT_SYNONYM`, `NARROW_SYNONYM`, `BROAD_SYNONYM`, `RELATED_SYNONYM`),
and `source` (a real, publicly resolvable URL identifying where the alias
comes from). Use `source`, not `contexts`: `source` means "where the alias
comes from" (StructuredAlias metamodel), which is what we record; `contexts`
means "the context in which the alias applies," which is different. When the
authoritative source is access-restricted (e.g. the JGI Isolate form
template), put the best public URL in `source` and a one-line caveat in
`notes`. Per-alias rationale (e.g. why a predicate is NARROW rather than
EXACT) also goes in `notes`, not in a YAML `#` comment. Plain `aliases` is
for unattributed synonym strings.

## LinkML Readonly Metaslots — Do Not Assert
The LinkML metamodel defines 12 slots that are **readonly** — populated
automatically by the schema loader or generators. Never add these to
hand-edited schema YAML files under `src/schema/`. If they appear in
generated files (like `mixs.yaml`), the build pipeline in
`makefiles/mixs.Makefile` strips them via `yq eval`.

The 12 readonly slots: `definition_uri`, `domain_of`, `from_schema`,
`generation_date`, `imported_from`, `is_usage_slot`, `metamodel_version`,
`owner`, `source_file`, `source_file_date`, `source_file_size`,
`usage_slot_name`.

Context: PR #2696 (dematerialize mixs.yaml), issue #2663.

## Permissible-value hierarchies (`is_a`)

Permissible values may declare `is_a: <other-pv-name>` (the name/key of another
PV in the same enum) to record that one value is a more specific kind of
another (e.g. `sequel_IIe is_a sequel_II`, `hiseq_2500 is_a hiseq`). Most enums
are flat; `is_a` is an optional, deliberate addition for the cases where a real
specialization holds, and is read downstream for grouping, rollup, and
querying. Assert it only where the relationship genuinely holds. Decision
guidance: `CONTRIBUTING.md` (Modeling Best Practice).

It does not currently change JSON-Schema validation or require migration (enums
still compile to a flat value list), so it is non-breaking to merge.

**OWL is deprioritized; do not enable `--enum-inherits-as-subclass-of`.**
LinkML 1.10.0's `linkml generate owl --enum-inherits-as-subclass-of` would
emit PV `is_a` as OWL `subClassOf` (the only way the hierarchy reaches a
machine-actionable artifact). The OWL build does **not** set this flag
(checked `Makefile`, `project.Makefile`, `gen-project-config.yaml`), and we
are intentionally leaving it off for now. Revisit only as part of a
deliberate OWL re-prioritization.

Context: issue #3120.

## Architectural Changes (Oct 2025 – Feb 2026)
Reviewers and contributors should be aware of these changes (Oct 2025
through Feb 2026) that affect the build system and project layout:

- **Makefile reorganization** (PR #2848, 2026-02-26): `project.Makefile`
  was split. MIxS pipeline moved to `makefiles/mixs.Makefile`, migrator
  targets to `makefiles/migrators.Makefile`. RDF conversion tooling and
  related Python scripts were removed. The main `Makefile` includes all
  three via `include` directives.
- **Unified LinkML CLI** (PR #2839, 2026-02-20): Build commands switched
  from legacy `gen-owl`, `gen-json-schema`, etc. to `linkml generate owl`,
  `linkml generate json-schema`, etc. Old `gen-*` entry points still exist
  in linkml but are no longer used here.
- **LinkML 1.10.0 upgrade** (PR #2849, 2026-02-26): Adds new OWL flags
  like `--enum-inherits-as-subclass-of`. Drops Python 3.9.
- **Dead code removal** (PR #2846, 2026-02-26): Removed `about.yaml` and
  experimental scripts that were no longer referenced.
- **Downloads page** (PR #2302, 2026-02-21): Schema-derived JSON and YAML
  files are now downloadable via the docs website.

## Example Data Guidelines

### Invalid examples: single point of failure
Each file in `src/data/invalid/` must be invalid for **exactly one
reason**. When modifying the schema (moving, removing, or renaming
slots), check whether any invalid example files use those slots
incidentally. If so, remove or update those fields so each file
continues to fail for only its originally intended reason.

To find affected files:
```bash
grep -rl 'slot_name' src/data/invalid/
```

### Valid examples: handling derived files in PRs
Do not manually edit generated/derived files like `nmdc_schema/nmdc.py`
or `nmdc_schema/nmdc_materialized_patterns.yaml`. These are regenerated
by `make all` and are part of the packaged artifacts.

- **Do not commit generated `nmdc_schema/` files during feature
  development.** These artifacts are updated immediately before merge
  or release, not in development PRs. If they show up in your diff,
  restore them from `main`:
  `git checkout origin/main -- nmdc_schema/nmdc.py nmdc_schema/nmdc_materialized_patterns.yaml nmdc_schema/nmdc_pydantic.py nmdc_schema/nmdc.schema.json nmdc_schema/nmdc_materialized_patterns.json nmdc_schema/nmdc_materialized_patterns.schema.json`
- You should still run `make all` locally to verify your schema changes
  build correctly, but do not stage or commit the resulting generated
  files.

### QuantityValue slot names — `has_numeric_value`, not `has_value`
The `QuantityValue` class in this schema has these slots:
`has_numeric_value`, `has_unit`, `has_minimum_numeric_value`,
`has_maximum_numeric_value`, `has_raw_value`. There is **no `has_value`**
on QuantityValue. Example data (and test fixtures) must use
`has_numeric_value`:

```yaml
# Right
gc_content:
  type: nmdc:QuantityValue
  has_numeric_value: 54.0
  has_unit: "%"

# Wrong — `has_value` is not a slot on QuantityValue
gc_content:
  type: nmdc:QuantityValue
  has_value: 54.0
  has_unit: "%"
```

The `linkml examples` runner (validating against the materialized
artifact in closed mode) rejects the wrong form with
`Additional properties are not allowed ('has_value' was unexpected)`.
The pytest validation plugin can be more permissive, so this can pass
unit tests and still fail the build at the examples step.

### Don't put scalar constraints on wrapper-class-ranged slots
`minimum_value`, `maximum_value`, and `pattern` are scalar constraints.
On a slot whose range is a wrapper class (`QuantityValue`, `TextValue`,
`ControlledIdentifiedTermValue`, etc.), they generate JSON Schema
keywords (`minimum`/`maximum`/`pattern`) that sit alongside the `$ref`
to the wrapper class. JSON Schema's numeric/string keywords only apply
to numeric/string instances — when the value is an object, those
keywords are silently ignored. The build passes, but no enforcement
happens.

Verified 2026-05-01: `gc_content` with `range: QuantityValue` +
`minimum_value: 0` + `maximum_value: 100` accepts a value of
`has_numeric_value: 123` without complaint. The same constraints on
`completeness` (`range: float`) correctly reject a value of -50.
See https://github.com/microbiomedata/nmdc-schema/issues/3007 for the
parallel `structured_pattern` case (silent ignore on wrapper slots).

If you need real bounds on a wrapper-class-ranged slot, write a
LinkML rule against the inner scalar slot (e.g. `has_numeric_value`),
not a slot-level `minimum_value` on the outer slot.

### YAML implicit type pitfalls in example data
YAML parses bare `yes`, `no`, `true`, `false` as booleans and bare
dates like `2023-06-15` as `datetime.date` objects. When these values
are meant as strings (e.g. `YesNoEnum` permissible values,
`has_raw_value` on `TimestampValue`), they must be quoted:

```yaml
# Wrong — parses as boolean True
single_colony_isolation: yes

# Right — stays as string "yes"
single_colony_isolation: "yes"

# Wrong — parses as datetime.date(2023, 6, 15)
has_raw_value: 2023-06-15

# Right — stays as string "2023-06-15"
has_raw_value: "2023-06-15"
```

## Pre-release Process

Use pre-releases to test schema changes on PyPI before a full release.
The authoritative publish workflow is `.github/workflows/pypi-publish.yaml`.
See also `MAINTAINERS.md` for general release guidance (note: some details
there may be outdated).

### Tag format

Use **`v{major}.{minor}.{patch}-rc.{N}`**, e.g. `v11.17.0-rc.1`.

Historical tags used inconsistent formats (`rc1`, `-rc2`, `-rc.1`).
The hyphen-dot format (`-rc.N`) is the current standard — use it for
all new pre-releases.

### Steps

Follow the authoritative checklist at
[`infra-admin/releases/nmdc-schema.md`](https://github.com/microbiomedata/infra-admin/blob/main/releases/nmdc-schema.md).
The key steps are:

1. Create a release-prep branch (e.g. `release/v11.17.0-rc.3`).
2. Run `make squeaky-clean all test` locally.
3. **Commit the regenerated artifacts** on the branch. The build produces
   files like JSON Schema, OWL, and `nmdc_schema/nmdc_pydantic.py` that
   must be checked in before tagging — otherwise the published package
   will be missing them.
4. Open a PR into `main` and get it merged. **Never push release-prep
   commits directly to `main`**, even if you have admin access to bypass
   branch protection.
5. Go to **Releases → Draft a new release** on GitHub.
6. Create a new tag matching the format above (e.g. `v11.17.0-rc.3`),
   targeting `main`.
7. Check the **"Set as a pre-release"** box (for pre-releases only).
8. Click **Publish release**.

The existing `pypi-publish.yaml` workflow triggers on any release
(including pre-releases) and publishes to PyPI via trusted publishing.

### Dynamic versioning

The build uses `poetry-dynamic-versioning` to derive the package version
from the git tag. This requires specific `pyproject.toml` structure:

- `[project]` must have `dynamic = ["version"]` and **no** hardcoded
  `version` field.
- `[tool.poetry]` must have `version = "0.0.0"` as a placeholder.
- `[build-system]` uses `poetry_dynamic_versioning.backend`.

If `version = "0.0.0"` is in `[project]` instead of `[tool.poetry]`,
the plugin cannot substitute the version and the package builds as
`nmdc_schema-0.0.0`, which PyPI will reject. See PR #2869 for context.

### PyPI behavior

The git tag `v11.17.0-rc.1` is normalized to PEP 440 version `11.17.0rc1`
on PyPI (the `v` prefix and `-rc.` punctuation are stripped/collapsed by
`poetry-dynamic-versioning`).

Pre-release versions are **not installed by default**. Users must opt in:
```bash
pip install nmdc-schema==11.17.0rc1   # specific version
pip install --pre nmdc-schema          # latest including pre-releases
```

### When to pre-release

- Schema changes that affect downstream consumers (nmdc-runtime,
  nmdc-server) and need integration testing before committing to a
  full release.
- Large structural changes (new classes, slot migrations) where you
  want reviewers to `pip install` and test before merging follow-up PRs.

## Docker Development
- Start env: `docker compose up --detach`
- Connect: `docker compose exec app bash`
- Working dir: `/nmdc-schema`

## Troubleshooting

### Poetry Entry Points
If `poetry run <command>` fails with "Command not found":
1. Force reinstall: `poetry run pip uninstall <package> -y && poetry install`
2. Rebuild environment: `poetry env remove && poetry install`

Essential commands that should work:
- `poetry run do_shuttle --help` (from sheets-and-friends)
- `poetry run gen-linkml --help` (from linkml)
- `poetry run gen-pydantic --help` (from linkml)
