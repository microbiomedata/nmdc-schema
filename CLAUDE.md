# NMDC-Schema Development Guide

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

## Script Entry Point Policy
- Keep `[project.scripts]` limited to package-backed, stable CLIs intended for default installs.
- Do not add ad-hoc aliases for `src/scripts/*` into `[project.scripts]`.
- For repo-local automation scripts, call them explicitly from Makefiles, e.g. `poetry run python src/scripts/<name>.py`.

## Code Style Guidelines
- Follow PEP8 conventions and Black formatting
- Use snake_case for variables/functions, PascalCase for classes
- Type annotations required for all parameters and returns
- Imports: stdlib first, third-party next, local modules last
- Docstrings use triple double quotes with examples
- Prefer specific exception handling with descriptive messages
- Use pathlib for file operations instead of os.path
- Write verbose, descriptive variable and function names
- Use None return values to indicate absence of a result

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
