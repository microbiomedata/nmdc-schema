# NMDC-Schema Development Guide

## Build/Lint/Test Commands
- Install: `poetry install`
- Build: `make all` or `make site`
- Clean: `make squeaky-clean`
- All tests: `make test`
- Python tests: `make test-python`
- Schema tests: `make test-schema`
- Run single test: `poetry run pytest tests/test_file.py -v`
- Run doctest: `poetry run python -m doctest -v path/to/file.py`
- Lint: `make linkml-lint` or `make linkml-lint-all` (outputs to local/linkml-lint-all.log)
- Check schema patterns: `poetry run schema-pattern-linting --schema-file src/schema/nmdc.yaml`
- View docs locally: `make serve` (in Docker: `poetry run mkdocs serve --dev-addr 0.0.0.0:8000`)

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
