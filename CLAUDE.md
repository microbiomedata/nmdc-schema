# NMDC-Schema Development Guide

## Build/Lint/Test Commands
- Install: `poetry install`
- Build: `make all` or `make site`
- Clean: `make squeaky-clean`
- All tests: `make test`
- Python tests: `make test-python`
- Schema tests: `make test-schema`
- Run single test: `poetry run python -m unittest tests/test_file.py`
- Run doctest: `poetry run python -m doctest -v path/to/file.py`
- Lint: `make lint` (outputs to local/lint.log)
- Check schema patterns: `make schema-pattern-linting`
- View docs locally: `make serve`

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