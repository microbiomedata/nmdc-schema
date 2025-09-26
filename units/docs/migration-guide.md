# Migration Guide

## Purpose

This document helps **existing contributors** understand changes to the units analysis workflow, focusing on specific impacts for ongoing PRs and coordination needs.

**For current workflow:** See `README.md`

## What Changed

**High-level**: Units analysis codebase restructured from ad-hoc scripts to organized analysis pipeline with new CLI aliases, Makefile targets, and structured outputs.

## Contributors & PR Coordination

### Key Contributors

**Mark A. Miller** (`MAM@lbl.gov` / @turbomam):

- Units analysis infrastructure reorganization
- All original functionality preserved in new structure

**samobermiller** (`samobermiller@gmail.com`):

- Enhanced production validation
- ⚠️ **Active PR conflict**:[Add migrator assuring unit compliance with annotations and UnitEnum by samobermiller · Pull Request #2641 · microbiomedata/nmdc-schema · GitHub](https://github.com/microbiomedata/nmdc-schema/pull/2641)

## Specific Conflicts & Resolutions

### Production Validation Script Movement

- **Old location**: `units/validate_production_units.py`  
- **New location**: `units/scripts/production_validate_units.py`
- **Impact**: Sam's PR changes need to be applied to new location
- **Resolution**: Coordinate with samobermiller to migrate changes

### Breaking Changes

- **File paths**: Hardcoded references to old script locations will break
- **Import statements**: Python imports of moved modules will fail  
- **CI/Documentation**: References to old script names need updating

## Required Actions

1. **Coordinate with samobermiller**: Resolve conflicts with open PRs
2. **Update CI references**: Fix hardcoded script paths in automation  
3. **Monitor for issues**: Address workflow disruptions from reorganization

## Getting Current Info

- **Available commands**: `poetry run --help`
- **Available targets**: `make help`
- **File structure**: See `units/docs/README.md`