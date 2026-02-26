# makefiles/migrators.Makefile — Migration framework targets
#
# This Makefile contains targets for running migration doctests,
# creating new migrator skeletons, and running migrators against MongoDB.
#
# Included by the top-level Makefile.
# RUN is inherited from the top-level Makefile.

.PHONY: migration-doctests migrator

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

# Generates a migrator skeleton for the specified schema versions.
# Note: `create-migrator` is a Poetry script registered in `pyproject.toml`.
migrator:
	$(RUN) create-migrator

# Runs a specific migrator against MongoDB
# Usage: make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 [ACTION=rollback|commit]
# The migrator now resides in: nmdc_schema/migrators/partials/migrator_from_11_9_1_to_11_10_0/
# MongoDB connection details are read from .env file or environment variables
MIGRATOR ?= migrator_from_11_9_1_to_11_10_0
ACTION ?=
.PHONY: run-migrator
run-migrator:
	@if [ -z "$(MIGRATOR)" ]; then \
		echo "Error: MIGRATOR parameter is required"; \
		echo "Usage: make run-migrator MIGRATOR=migrator_from_11_9_1_to_11_10_0 [ACTION=rollback|commit]"; \
		echo "MongoDB connection details are read from .env file or environment variables"; \
		exit 1; \
	fi
	$(RUN) run-migrator $(MIGRATOR) $(if $(ACTION),$(ACTION))
