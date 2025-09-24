# Units Directory Migration Guide

## Overview

The units analysis scripts and workflow have been reorganized to improve maintainability and provide clearer automation. This document helps existing contributors understand the changes and migrate their workflows.

## What Changed

### File Reorganization
The units analysis codebase was restructured from ad-hoc scripts to a comprehensive analysis pipeline:

**Deleted Files** (moved/renamed):
- `src/scripts/check_quantity_value_units.py` → `units/scripts/testdata_check_has_unit.py`
- `src/scripts/check_units.py` → `units/scripts/ucum_validate_units.py`  
- `src/scripts/flatten_quantity_values.py` → `units/scripts/testdata_extract_quantity_values.py`
- `units/analyze.py` → `units/scripts/schema_extract_preferred_units.py`
- `units/analyze_units.py` → `units/scripts/mongodb_analyze_units.py`
- `units/extract.py` → (functionality distributed across multiple scripts)
- `units/process.py` → `units/scripts/schema_convert_to_ucum.py`
- `units/validate_production_units.py` → `units/scripts/production_validate_units.py`

**New Structure**:
- `units/scripts/` - All Python analysis tools
- `units/docs/` - Comprehensive documentation
- `units/output/` - Generated analysis files
- `units/semi-static-inputs/` - Reference data
- `units/slow-outputs/` - Time-intensive results

### Enhanced Automation
- **New Makefile**: Provides `make fast` (comprehensive analysis) and `make all` targets
- **CLI Integration**: Poetry-managed command aliases for all scripts
- **Structured Output**: All analysis results saved to organized files

## Migration for Contributors

### Original Contributors & Their Work

**Mark A. Miller** (`MAM@lbl.gov`):
- Original author of the core units analysis infrastructure
- Created: `units/analyze.py`, `units/process.py`, `units/extract.py`, `units/validate_production_units.py`
- All original functionality preserved in new structure

**samobermiller** (`samobermiller@gmail.com`):
- Enhanced production validation (`productionunitsvalidator`)
- ⚠️ **Note**: May have an open PR affecting production validation scripts

### Command Migration Guide

| Old Command | New Command | Notes |
|-------------|-------------|-------|
| `python units/analyze.py` | `poetry run units-schema-extract` | Extract preferred_unit annotations |
| `python units/process.py` | `poetry run units-schema-convert` | Convert units to UCUM notation |
| `python units/validate_production_units.py` | `poetry run units-production-validate` | Production data validation |
| `python src/scripts/check_units.py` | `poetry run units-ucum-validate` | UCUM compliance validation |
| `python src/scripts/check_quantity_value_units.py` | `poetry run units-testdata-check` | Check test data completeness |
| `python src/scripts/flatten_quantity_values.py` | `poetry run units-testdata-extract` | Extract test QuantityValues |
| Manual script coordination | `make fast` | Comprehensive analysis pipeline |

### Workflow Migration

**Before** (ad-hoc):
```bash
python units/analyze.py
python units/process.py  
python units/validate_production_units.py
# Manual coordination of outputs
```

**After** (structured):
```bash
make fast  # Runs comprehensive analysis pipeline
# OR individual commands:
poetry run units-schema-extract
poetry run units-schema-convert
poetry run units-production-validate
```

## Potential Conflicts

### Active Development
- **samobermiller**: May have an open PR modifying production validation scripts
- **Impact**: Changes to `units/validate_production_units.py` will need to be migrated to `units/scripts/production_validate_units.py`
- **Resolution**: Coordinate with samobermiller to apply changes to new location

### Breaking Changes
- **File paths**: Any hardcoded references to old script locations will break
- **Import statements**: Python imports of moved modules will fail
- **CI/Documentation**: References to old script names need updating

## Responsibilities

**Reorganization Changes** (contributor: various):
- **File movement/renaming**: Responsibility for ensuring all functionality is preserved
- **CLI integration**: Maintenance of `pyproject.toml` aliases
- **Documentation**: Guides in `units/docs/` (extensive but may not cover all edge cases)
- **Makefile targets**: Automation of common workflows

**Required Follow-up Actions**:
1. **Coordinate with samobermiller**: Resolve any conflicts with open PRs
2. **Update CI references**: Fix any hardcoded script paths in automation
3. **Team communication**: Notify contributors of new command structure
4. **Monitor for issues**: Address any workflow disruptions

## Getting Help

- **Quick start**: Run `make fast` for comprehensive analysis
- **Individual tools**: Use `poetry run units-<domain>-<action>` pattern
- **Documentation**: See `units/docs/README.md` (comprehensive but large)
- **Issues**: File issues referencing this migration guide

## Backward Compatibility

Currently no backward compatibility shims are provided. Contributors should migrate to the new command structure. If needed, temporary compatibility scripts can be created:

```bash
# Example compatibility shim (not implemented)
echo "DEPRECATED: Use 'poetry run units-schema-extract' instead" 
poetry run units-schema-extract "$@"
```

Consider implementing if migration proves disruptive to active development.