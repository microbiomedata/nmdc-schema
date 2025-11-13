###########################################################
# Migration Framework
###########################################################
#
# Purpose: Tools for developing, testing, and running schema migrations
#
# Who needs this: Schema maintainers creating or testing migrations
# Who doesn't: Contributors working on schema definitions only
#
# Key targets:
#   migration-doctests: Run all doctests in migrator modules
#   migrator: Generate a new migrator skeleton for schema version migration
#   run-migrator: Execute a specific migrator against MongoDB
#
# Typical workflows:
#   1. Develop new migration:
#      make migrator  # Creates skeleton
#      # Edit nmdc_schema/migrators/partials/migrator_from_X_to_Y/
#      make migration-doctests  # Test your migration logic
#
#   2. Test migration against database:
#      make run-migrator MIGRATOR=migrator_from_X_to_Y
#      make run-migrator MIGRATOR=migrator_from_X_to_Y ACTION=rollback
#      make run-migrator MIGRATOR=migrator_from_X_to_Y ACTION=commit
#
###########################################################

RUN=poetry run

.PHONY: migration-doctests migrator run-migrator

###########################################################
# Doctest Validation
###########################################################

# Runs all doctests defined within the migrator modules, adapters, and CLI scripts.
#
# To run in non-verbose mode:
# ```
# $ make migration-doctests DOCTEST_OPT=''
# ```
DOCTEST_OPT ?= -v
migration-doctests: nmdc_schema/nmdc_materialized_patterns.yaml
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/partials/**/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/adapters/*.py
	$(RUN) python -m doctest $(DOCTEST_OPT) nmdc_schema/migrators/cli/*.py

###########################################################
# Migrator Generation
###########################################################

# Generates a migrator skeleton for the specified schema versions.
# Note: `create-migrator` is a Poetry script registered in `pyproject.toml`.
#
# Interactive usage: prompts for from/to schema versions
# Example: Creates nmdc_schema/migrators/partials/migrator_from_11_9_1_to_11_10_0/
migrator:
	$(RUN) create-migrator

###########################################################
# Migrator Execution
###########################################################

# Runs a specific migrator against MongoDB
#
# Usage:
#   make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0         # Show plan
#   make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 ACTION=rollback
#   make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 ACTION=commit
#
# The migrator resides in: nmdc_schema/migrators/partials/$(MIGRATOR)/
# MongoDB connection details are read from .env file or environment variables
MIGRATOR ?= migrator_from_11_9_1_to_11_10_0
ACTION ?=
run-migrator:
	@if [ -z "$(MIGRATOR)" ]; then \
		echo "Error: MIGRATOR parameter is required"; \
		echo "Usage: make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 [ACTION=rollback|commit]"; \
		echo "MongoDB connection details are read from .env file or environment variables"; \
		exit 1; \
	fi
	$(RUN) run-migrator $(MIGRATOR) $(if $(ACTION),$(ACTION))
