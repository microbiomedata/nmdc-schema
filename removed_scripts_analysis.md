# Analysis of Removed Validation Scripts

## Summary

### `units/scripts/production_validate_units.py`

**What it does:**
- Validates production MongoDB data (YAML dumps) against `storage_units` constraints in the schema
- Scans through all QuantityValue objects in production data to find units violations
- Generates comprehensive CSV reports showing unit usage patterns

**Problems it finds:**
1. Missing `has_unit` property on QuantityValue objects
2. Units not in UnitEnum (enum violations)
3. Units that don't match the slot's `storage_units` annotation constraint
4. Statistical analysis of unit usage by slot

**Inputs:**
- `--input`: MongoDB production data YAML file (e.g., `local/mongo_via_api_as_unvalidated_nmdc_database.yaml`)
- `--schema-file`: Schema file (defaults to `nmdc_materialized_patterns.yaml`)
- `--output`: Output file for validation report (TSV/CSV format)

**Standalone invocation:**
```bash
python units/scripts/production_validate_units.py \
  --input local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
  --output validation_report.tsv \
  --schema-file nmdc_schema/nmdc_materialized_patterns.yaml
```

---

### `tests/test_has_unit_validation.py`

**What it does:**
- Validates example YAML files in `src/data/valid/` against UnitEnum and storage_units
- Runs as a unit test to ensure test data is valid

**Problems it finds:**
1. QuantityValue objects missing `has_unit` property (in test data)
2. Units not in UnitEnum (in test data)
3. Units inappropriate for their slots based on `storage_units` (in test data)

**Inputs:**
- Automatically scans all `*.yaml` files in `src/data/valid/`
- Uses schema from `tests.SCHEMA_FILE`

**Standalone invocation:**
```bash
pytest tests/test_has_unit_validation.py -v
# or
python -m pytest tests/test_has_unit_validation.py
# or
python tests/test_has_unit_validation.py
```

---

### What replaces them?

Both scripts were replaced by the **LinkML Validation Plugin** system in the new branch (PR #2648):

**New Files:**
- `nmdc_schema/nmdc_schema_validation_plugin.py` - The plugin implementation
- `tests/test_nmdc_schema_validation_plugin.py` - The plugin tests

**Key differences:**
1. **Integration**: Plugin integrates with LinkML's official validation framework rather than custom scripts
2. **Same logic**: Performs identical validation (checks `has_unit` against UnitEnum and `storage_units`)
3. **Better architecture**: Works as part of LinkML's standard validation pipeline
4. **Test coverage**: `test_all_valid_examples()` replaces `test_has_unit_validation.py` by validating all example files

The production validation script's functionality for analyzing large MongoDB dumps is absorbed into the plugin, which can be invoked via LinkML's standard validation commands.

---

## Related Commits

- `cd933e10ee` - Add LinkML validation plugin for NMDC-specific rules
- `ab8bf75d38` - Remove script which is redundant with NMDC validation plugin
- `1937ba8045` - Remove test which is redundant with NMDC validation plugin test