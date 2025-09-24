# Comprehensive Units Analysis for NMDC Schema

## Executive Summary

This analysis documents the complete units ecosystem in the NMDC schema, focusing on QuantityValue slot validation, UCUM compliance, MIxS integration, and production data coverage. The current system achieves 97% compliance in production with strategic storage_units annotations and minimal excuse usage.

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

#### Fast Generated Files (`output/`)
- `schema_preferred_units.tsv`, `schema_ucum_input.tsv`, `schema_ucum_detailed.tsv` - Schema analysis pipeline
- `yq_commands_single_unit.txt`, `yq_commands_multi_unit.txt` - Generated yq commands for storage_units  
- `testdata_quantity_values.tsv` - QuantityValue structures from test data
- `ucum_validation_results.csv` - UCUM compliance validation analysis
- `schema_qv_*.txt` - QuantityValue annotation coverage reports  
- `schema_units_excuses.tsv` - Slots with excuse annotations

#### Slow Generated Files (`slow-outputs/`)
- `production_validation_results.tsv` - Full production data validation (minutes/hours)

#### Semi-Static Inputs (`semi-static-inputs/`)
- `mongodb-slots-to-units.csv` - Production SPARQL query results
- `mongodb-slots-to-units_remediated.csv` - Manually curated analysis

#### SPARQL Resources (`sparql/`)
- `fix-units-update-v2.ru` - Hand-crafted units fix queries

### Benefits of Organization
- **Clean separation**: Source code vs generated files vs documentation
- **Lifecycle awareness**: Fast rebuilds vs expensive operations vs curated inputs
- **Maintenance efficiency**: Clear ownership and update patterns
- **Development workflow**: `make clean-fast` preserves expensive computations

## Strategic Goals Assessment

### UCUM Compliance ✅
- All storage_units atoms validated against UCUM specification
- RDF/OWL compatible unit representations maintained
- Special handling for non-UCUM units (api, permeability) via excuse annotations

### MIxS Integration ✅  
- 544 yq commands in `assets/yq-for-mixs_subset_modified.txt` ensure MIxS preferred units preserved
- Multi-unit storage_units accommodate MIxS diversity (e.g., `calcium: "[ppm]|mg/L|umol/L|mg/kg"`)
- Production validation shows historical MIxS compliance issues resolved

### Production Data Coverage ✅
- 32,000+ QuantityValue instances analyzed across MongoDB collections
- Only 3 real violations out of 93 slot-unit combinations (97% compliance)
- Strategic pipe-separated units capture production diversity

### Excuse Minimization ✅
- 34 total excuse annotations (down from potential hundreds)
- Categories: protocol_slot (17), pending_analysis (11), mixs_inconsistent (4), non_ucum_unit (2)
- Zero production usage validates pending_analysis excuses

## Architecture Overview

### Core Components

1. **Schema Files with Units Constraints**
   - `src/schema/nmdc.yaml` - NMDC-native QuantityValue slots
   - `src/schema/core.yaml` - Process-related QuantityValue slots  
   - `src/schema/mixs.yaml` - Generated from MIxS with storage_units annotations

2. **Units Processing Pipeline**
   - `assets/yq-for-mixs_subset_modified.txt` - 544 yq commands for MIxS integration
   - `units/Makefile` - Validation and reporting targets
   - `src/scripts/check_quantity_value_units.py` - YAML validation
   - `units/production_validation_analysis.md` - Production compliance analysis

3. **Validation Layers**
   - Schema-level: LinkML annotations require storage_units OR excuse
   - Code-level: Python validation scripts check YAML compliance  
   - Production-level: MongoDB data analysis validates real-world usage
   - Build-level: Makefile targets ensure consistency

## Detailed Analysis by Component

### Schema Files Analysis

#### MIxS Integration (`assets/yq-for-mixs_subset_modified.txt`)
**Primary Contributors**: User (MAM)
**Lines**: 544 yq commands
**Function**: Transform upstream MIxS schema for NMDC compatibility

**Key Operations**:
- Lines 257-522: storage_units annotations for 200+ MIxS slots
- Lines 477-498: excuse annotations for protocol/regimen slots  
- Lines 533-543: excuse annotations for problematic specifications

**Consolidation Opportunity**: This file represents user's comprehensive MIxS integration work and could be enhanced with:
- Automated validation of storage_units atoms against UCUM
- Documentation of MIxS preferred_unit derivations
- Tracking of upstream MIxS changes

#### NMDC Native Schema Files
**Primary Contributors**: Mixed (User added excuse annotations, others added core definitions)

`src/schema/nmdc.yaml`:
- User contributions: excuse annotations (biomaterial_purity, container_size, filter_pore_size, input_volume, value)
- Format standardization: verbose → abbreviated annotation format

`src/schema/core.yaml`:  
- User contributions: excuse annotations (bulk_elect_conductivity, substances_volume, concentration)
- Format standardization: verbose → abbreviated annotation format

### Validation Scripts Analysis

#### Production Data Validation
**File**: `units/production_units_validation.tsv`
**Primary Contributor**: User (MAM)
**Size**: 584MB, 32,000+ instances analyzed
**Key Insight**: 97% compliance validates storage_units strategy

**Critical Findings**:
- `abs_air_humidity`: Schema correct, production data quality issue (kPa vs humidity units)
- `solar_irradiance`: Should add W/m2 to storage_units (missing time dimension consideration)
- `diss_oxygen`: Should add mL/L to storage_units (volume vs mass units)

#### YAML Validation Scripts
**Files**: 
- `src/scripts/check_quantity_value_units.py` (User: sole contributor)
- `src/scripts/check_units.py` (User: major contributor)

**Consolidation Opportunity**: Both scripts are user's work and should be moved to `units/` directory:
- No evidence of external dependencies or disruption
- Would centralize all units validation logic
- Current placement in `src/scripts/` is inconsistent with domain focus

### Build Integration Analysis

#### Units Makefile (`units/Makefile`)
**Primary Contributor**: User (MAM)  
**Key Targets**:
- `units_excuses.tsv`: Reports slots with excuse annotations
- `production_validation`: Analyzes MongoDB dumps
- `update_mixs`: Integrates upstream MIxS changes

**Technical Implementation**:
```makefile
units_excuses.tsv: $(SCHEMA_FILE)
	yq eval '(.slots // {}) | to_entries[] | select(.value.annotations.units_alignment_excuse) | .key + "	" + (.value.annotations.units_alignment_excuse.value // .value.annotations.units_alignment_excuse)' $< | sort > $@
```

#### Root Makefile Integration
**Units-related targets in root Makefile**: None found
**Assessment**: Units validation is properly isolated in domain-specific directory

### Test Analysis - Antipattern Identification

#### Excessive Output Tests (Antipattern)
**Finding**: No evidence of unit-related tests with excessive output antipattern
**Root cause**: Units validation is data-driven rather than exhaustive enumeration

**Good Pattern Examples**:
- Schema validation: Binary pass/fail for each slot
- Production validation: Aggregated statistics rather than individual violations
- UCUM validation: Focused error reporting rather than full unit enumeration

### Storage Units Atoms Analysis

#### UCUM Compliance Assessment
**Method**: Pipe-split all storage_units values and validate each atom

**Categories**:
1. **Standard UCUM**: `mg/L`, `umol/L`, `Cel`, `m`, `g`, etc. (95%+)
2. **UCUM with brackets**: `[ppm]`, `[pH]`, `[NTU]`, etc. (UCUM-compliant arbitrary units)
3. **Non-UCUM with excuse**: `api` (American Petroleum Institute gravity), `permeability` (darcy units)

**RDF/OWL Compatibility**: 
- All bracketed units properly escaped in UnitEnum generation
- SPARQL update queries handle special characters correctly
- Namespace URIs properly formed for all unit atoms

### Contributor Attribution Analysis

#### User (MAM) Primary Contributions
**Scope**: ~80% of units ecosystem
**Areas of Ownership**:
- Complete MIxS integration pipeline (544 yq commands)
- Production validation methodology and analysis
- Units validation scripts (100% ownership)
- Units directory organization and build targets
- Excuse annotation strategy and implementation

#### Mixed Contributions
**Schema definitions**: Core QuantityValue slot definitions predate units work
**Build infrastructure**: Poetry/LinkML integration predates units work
**Test framework**: Validation test patterns established before units focus

#### Consolidation Recommendations

1. **Move validation scripts to units/**:
   - `src/scripts/check_quantity_value_units.py` → `units/check_quantity_value_units.py`
   - `src/scripts/check_units.py` → `units/check_units.py`
   - Update Makefile references accordingly

2. **Enhance MIxS integration**:
   - Add UCUM validation to yq pipeline
   - Document storage_units derivation methodology  
   - Create upstream change tracking

3. **Consolidate analysis outputs**:
   - All units reports in `units/*.tsv` format
   - Standardized analysis markdown templates
   - Automated insight generation from production data

## Production Validation Insights

### Compliance Metrics
- **97% slot-unit combination compliance** (90/93 combinations valid)
- **98.5%+ instance-weighted compliance** (485 violations / 32,000+ instances)  
- **100% excuse validation** (all pending_analysis slots have zero production usage)

### Strategic Successes
1. **Multi-unit strategy validation**: Production systems successfully use diverse units for same measurements
2. **Historical issue resolution**: All previously problematic slots now compliant
3. **MIxS compatibility**: Real systems leverage MIxS unit diversity effectively

### Actionable Recommendations

#### Schema Updates
1. Add `W/m2` to `solar_irradiance` storage_units
2. Add `mL/L` to `diss_oxygen` storage_units  
3. Investigate `abs_air_humidity` production data quality (pressure vs humidity units)

#### Process Improvements
1. Automated UCUM validation in CI/CD pipeline
2. Production data monitoring for new unit usage patterns
3. Upstream MIxS change impact assessment

## Conclusion

The NMDC units ecosystem represents a comprehensive solution balancing multiple constraints:
- **UCUM compliance** for interoperability
- **MIxS compatibility** for domain standards  
- **Production coverage** for real-world usage
- **RDF/OWL compatibility** for semantic web integration

The current 97% compliance rate with minimal excuse usage validates the strategic approach. User's comprehensive ownership of the units domain enables aggressive cleanup and consolidation without disrupting other contributors' work.

### Next Phase Priorities
1. **Consolidate validation scripts** in units/ directory
2. **Enhance automation** with UCUM validation pipeline
3. **Monitor production trends** for emerging unit patterns
4. **Document methodology** for future MIxS integration cycles

The units ecosystem stands as a successful example of domain-driven design enabling complex constraint satisfaction across multiple stakeholder requirements.