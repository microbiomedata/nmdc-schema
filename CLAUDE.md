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
- Check schema patterns: `poetry run python src/scripts/schema_pattern_linting.py --schema-file src/schema/nmdc.yaml`
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
