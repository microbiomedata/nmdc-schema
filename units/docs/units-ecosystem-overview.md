# Units Ecosystem Overview

## Purpose

This document provides a **strategic overview** of the complete units ecosystem in the NMDC schema. It focuses on architecture, organization, contributor analysis, and high-level strategic goals rather than specific problems.

**For specific problems:** See `units-problems-definitive.md`  
**For operational guidance:** See `README.md`

## Executive Summary

This analysis documents the complete units ecosystem in the NMDC schema, focusing on QuantityValue slot validation, UCUM compliance, MIxS integration, and production data coverage. The current system achieves high compliance in production with strategic storage_units annotations.

## 📁 Directory Structure

The units analysis ecosystem is organized into logical directories by file purpose and lifecycle:

### Core Structure
```
units/
├── scripts/          # Python analysis tools (.py files)
├── docs/            # Documentation (.md files)
├── output/          # Generated analysis files (fast targets)
├── slow-outputs/    # Expensive computations (MongoDB analysis)
├── semi-static-inputs/  # Curated datasets for analysis
├── sparql/          # SPARQL update queries (.ru files)
└── Makefile         # Workflow orchestration
```

### File Categories by Lifecycle

- **Fast Generated Files (`output/`)** - Schema analysis and validation reports
- **Slow Generated Files (`slow-outputs/`)** - Production data validation requiring significant compute time
- **Semi-Static Inputs (`semi-static-inputs/`)** - Curated datasets for analysis
- **SPARQL Resources (`sparql/`)** - Hand-crafted transformation queries

### Benefits of Organization
- **Clean separation**: Source code vs generated files vs documentation
- **Lifecycle awareness**: Fast rebuilds vs expensive operations vs curated inputs
- **Maintenance efficiency**: Clear update patterns
- **Development workflow**: `make clean-fast` preserves expensive computations

## Strategic Goals Assessment

### UCUM Compliance ✅
- All storage_units atoms validated against UCUM specification
- RDF/OWL compatible unit representations maintained

### MIxS Integration ✅  
- Comprehensive yq commands in `assets/yq-for-mixs-customizations.txt` ensure MIxS preferred units preserved
- Multi-unit storage_units accommodate MIxS diversity (e.g., `calcium: "[ppm]|mg/L|umol/L|mg/kg"`)

### Production Data Coverage ✅
- Comprehensive QuantityValue analysis across MongoDB collections
- Strategic pipe-separated units capture production diversity

## Architecture Overview

### Core Components

1. **Schema Files with Units Constraints**
   - `src/schema/nmdc.yaml` - NMDC-native QuantityValue slots
   - `src/schema/core.yaml` - Process-related QuantityValue slots  
   - `src/schema/mixs.yaml` - Generated from MIxS with storage_units annotations

2. **Units Processing Pipeline**
   - `assets/yq-for-mixs-customizations.txt` - Comprehensive yq commands for MIxS integration
   - `units/Makefile` - Validation and reporting targets
   - `src/scripts/check_quantity_value_units.py` - YAML validation

3. **Validation Layers**
   - Schema-level: LinkML annotations require storage_units OR excuse
   - Code-level: Python validation scripts check YAML compliance  
   - Production-level: MongoDB data analysis validates real-world usage
   - Build-level: Makefile targets ensure consistency

## Detailed Analysis by Component

### Schema Files Analysis

#### MIxS Integration (`assets/yq-for-mixs-customizations.txt`)
**Contributors**: MAM
**Function**: Transform upstream MIxS schema for NMDC compatibility

**Key Operations**:
- Comprehensive storage_units annotations for MIxS slots
- Multi-unit storage_units accommodate MIxS diversity

**Consolidation Opportunity**: This file represents comprehensive MIxS integration work and could be enhanced with:
- Automated validation of storage_units atoms against UCUM
- Documentation of storage_units derivation methodology
- Tracking of upstream MIxS changes

#### NMDC Native Schema Files
**Contributors**: Mixed (annotations, core definitions)

`src/schema/nmdc.yaml`:
- Format standardization: verbose → abbreviated annotation format

`src/schema/core.yaml`:  
- Format standardization: verbose → abbreviated annotation format

### Validation Scripts Analysis

#### Production Data Validation
**File**: `units/production_units_validation.tsv`
**Contributor**: MAM
**Function**: Comprehensive analysis of production QuantityValue instances

#### YAML Validation Scripts
**Files**: 
- `src/scripts/check_quantity_value_units.py`
- `src/scripts/check_units.py`

**Consolidation Opportunity**: Both scripts should be moved to `units/` directory:
- No evidence of external dependencies or disruption
- Would centralize all units validation logic
- Current placement in `src/scripts/` is inconsistent with domain focus

### Build Integration Analysis

#### Units Makefile (`units/Makefile`)
**Contributor**: MAM  
**Key Targets**:
- Reports and validation
- Integrates upstream MIxS changes

**Technical Implementation**: See `units/Makefile` for complete workflow definitions

#### Root Makefile Integration
**Units-related targets in root Makefile**: None found
**Assessment**: Units validation is properly isolated in domain-specific directory

### Storage Units Atoms Analysis

#### UCUM Compliance Assessment
**Method**: Pipe-split all storage_units values and validate each atom

**Categories**:
1. **Standard UCUM**: `mg/L`, `umol/L`, `Cel`, `m`, `g`, etc. (vast majority)
2. **UCUM with brackets**: `[ppm]`, `[pH]`, `[NTU]`, etc. (UCUM-compliant arbitrary units)

**RDF/OWL Compatibility**: 
- All bracketed units properly escaped in UnitEnum generation
- SPARQL update queries handle special characters correctly
- Namespace URIs properly formed for all unit atoms

### Contributor Attribution Analysis

#### Contributor Analysis (MAM)
**Areas of Work**:
- MIxS integration pipeline 
- Production validation methodology and analysis
- Units validation scripts
- Units directory organization and build targets

#### Mixed Contributions
**Schema definitions**: Core QuantityValue slot definitions predate units work
**Build infrastructure**: Poetry/LinkML integration predates units work
**Test framework**: Validation test patterns established before units focus


## Conclusion

The NMDC units ecosystem represents a comprehensive solution balancing multiple constraints:
- **UCUM compliance** for interoperability
- **MIxS compatibility** for domain standards  
- **Production coverage** for real-world usage
- **RDF/OWL compatibility** for semantic web integration

The current high compliance rate validates the strategic approach. The units domain organization enables cleanup and consolidation without disrupting other contributors' work.

### Next Phase Priorities
1. **Consolidate validation scripts** in units/ directory
2. **Enhance automation** with UCUM validation pipeline
3. **Monitor production trends** for emerging unit patterns
4. **Document methodology** for future MIxS integration cycles

The units ecosystem stands as a successful example of domain-driven design enabling complex constraint satisfaction across multiple stakeholder requirements.