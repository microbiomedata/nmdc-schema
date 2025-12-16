# NMDC Schema Development Guide

## Build Instructions

**Do not run make targets directly** - most are long-running (10+ minutes). Instead:
- Inform the user when make targets are needed: "This change requires running `make all` to regenerate artifacts."
- Let the user run make targets, or let GitHub Actions handle it on PR submission
- Exception: Quick targets like `make squeaky-clean` or `make help` are safe to run

**Full rebuild command** (for users to run, includes MIxS regeneration and units reports):
```bash
clear && make squeaky-clean mixs-yaml-clean && make src/schema/mixs.yaml && make squeaky-clean all test && make -C units fast
```

## Schema Structure

- **Main schema**: `src/schema/nmdc.yaml` (imports other schema files)
- **Schema modules**: `src/schema/*.yaml` (core.yaml, mixs.yaml, etc.)
- **MIxS import**: `src/schema/mixs.yaml` is generated from GSC MIxS via yq transformations
- **Generated artifacts**: `nmdc_schema/` directory (JSON Schema, Pydantic, etc.)

## MIxS Customizations

NMDC imports GSC MIxS and applies customizations:
- **Import mapping**: `assets/import_mixs_slots_regardless.tsv`
- **yq transformations**: `assets/yq-for-mixs-customizations.txt`
- **Documentation**: `src/docs/mixs-v6.2.2-customizations.md`

## Validation and Testing

Quick validation commands (safe to run):
```bash
poetry run linkml-validate -s src/schema/nmdc.yaml src/data/valid/SomeFile.yaml
poetry run linkml-lint --config .linkmllint.yaml src/schema/nmdc.yaml
```

For full test suite, ask the user to run `make test` or let CI handle it.

## Test Data

- **Valid examples**: `src/data/valid/*.yaml`
- **Invalid examples**: `src/data/invalid/*.yaml`
- **Database-interleaved.yaml**: Large test file with production-like data

## Poetry Environment

If `poetry run <command>` fails with "Command not found":
1. Check installation: `poetry show | grep <package-name>`
2. Force reinstall: `poetry run pip uninstall <package> -y && poetry install`
3. Last resort: `poetry env remove && poetry install`
