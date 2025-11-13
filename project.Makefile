###########################################################
# project.Makefile - DEPRECATED
###########################################################
#
# This file has been reorganized into three specialized makefiles
# for better separation of concerns:
#
# 1. Makefile - Core schema development, building, testing, documentation
#    - Schema generation (gen-project, prefixmaps, pydantic)
#    - Documentation (gendoc, mkdocs targets)
#    - Testing (test, test-python, linkml-lint)
#    - Example validation (examples/output)
#    - Schema analysis and reporting
#    - Asset generation
#    - Release tracking
#
# 2. mixs.Makefile - MIxS schema import and regeneration
#    - MIxS slot extraction (do_shuttle)
#    - Transformations and modifications
#    - Enum and annotation injection
#    - src/schema/mixs.yaml generation
#    - Targets: mixs-yaml-clean, shuttle-clean, src/schema/mixs.yaml
#
# 3. data-validation.Makefile - Production data validation
#    - MongoDB export and RDF conversion
#    - SPARQL validation workflows
#    - Migration framework (migration-doctests, migrator, run-migrator)
#    - API-based validation (test-migrator-on-database)
#    - Targets: make-rdf, pure-export-and-validate, migration-doctests
#
# This file is kept only for backwards compatibility and will be
# removed in a future release. All new development should use the
# specialized makefiles.
#
###########################################################

# Placeholder to prevent errors if project.Makefile is included
.PHONY: deprecated-project-makefile-warning

deprecated-project-makefile-warning:
	@echo "WARNING: project.Makefile is deprecated."
	@echo "Targets have been reorganized into:"
	@echo "  - Makefile (schema development)"
	@echo "  - mixs.Makefile (MIxS import)"
	@echo "  - data-validation.Makefile (data validation)"
