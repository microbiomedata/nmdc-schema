# Units

This document provides a comprehensive overview of the unit analysis, validation, and storage_units annotation workflow for the NMDC schema. It documents all data transformations, scripts, and automation opportunities for managing unit-related schema components.

## Table of Contents

1. [Maintainer Guide](#maintainer-guide) **← START HERE**
2. [Documentation Navigation](#documentation-navigation)
3. [Overview](#overview)
4. [Data Flow Pipeline](#data-flow-pipeline)
5. [Core Scripts & Transformations](#core-scripts--transformations)
6. [UCUM Validation System](#ucum-validation-system)
7. [Schema Transformation Outputs](#schema-transformation-outputs)
8. [Automation Recommendations](#automation-recommendations)
9. [Troubleshooting](#troubleshooting)
10. [File Management](#file-management)

## Documentation Navigation

### Primary Documents

- **`units-problems-definitive.md`** - **DEFINITIVE SOURCE** for all units problems (excuse problems and production data issues)
- **`README.md`** - This file: workflow overview, scripts, and automation guidance

### Specialized Analysis

- **`units-ecosystem-overview.md`** - Strategic architecture and contributor analysis

### Contributor Support

- **`migration-guide.md`** - Workflow migration guidance for existing contributors  
- **`legacy-data-strategy.md`** - Proposed strategy for non-standard units

## Maintainer Guide

### For Schema Maintainers: When Do I Touch This Directory?

**Short Answer**: You don't. These scripts are specialist tools for units work.

#### **Normal Schema Maintenance**

- ✅ **Adding new classes/slots**: No action needed
- ✅ **Changing slot ranges**: No action needed  
- ✅ **General schema updates**: No action needed
- ✅ **Tests passing**: Units constraints enforced automatically

#### **When Units Work Is Needed**

- ❌ **Test failure**: QuantityValue slot validation
- **Who handles it**: UCUM Squad (@turbomam)
- **Process**: Add to weekly UCUM Squad meeting agenda
- **Your role**: Review and merge the resulting PR

#### **What Gets Changed**

- **Files modified**: Schema YAML files (`src/schema/*.yaml`)
- **Changes**: Addition of required slot annotations
- **Review needed**: Standard schema change review (no special units knowledge required)

#### **Emergency Override**

See `units-problems-definitive.md` for emergency procedures.

### For UCUM Squad: Script Usage

The scripts in this directory are for specialized units analysis and should only be run by someone familiar with UCUM, MIxS, and units validation concepts.

**For all units problems:** See `units-problems-definitive.md` - the definitive source for both excuse problems and production data issues.

### Implementation Status and Project Coordination

**Primary Issue:** [#2598](https://github.com/microbiomedata/nmdc-schema/issues/2598) - Add `storage_units` annotations to QuantityValue slots

**✅ Phase 1: COMPLETED** (Under review in [PR #2599](https://github.com/microbiomedata/nmdc-schema/pull/2599))

- Added `storage_units` annotations to 159 QuantityValue slots with clear MIxS → UCUM mappings
- Lead: @turbomam

**🔄 Phase 2: NEXT TASK**

- Add `storage_units` annotations to remaining QuantityValue slots without MIxS `preferred_unit` annotations

**Contributors:**

- **@turbomam:** Schema annotation implementation (#2598, PR #2599)
- **samobermiller:** Validation and migration support (#2637, PR #2641)

**Current analysis:** Run `make fast` to generate current QuantityValue slot analysis including storage_units status.

### Future Migration Note

The data validation scripts in `units/` (like `validate_production_units.py`) will be replaced with validation code in the `nmdc-runtime` repository (handled by @pkalita-lbl). The schema annotation scripts will remain here.

### User-Friendly Unit Titles

**Issue from PR #2599**: "storage_units that may not be intuitive and might require a title assertion, to be used as the display value"

**Solution**: ✅ Complete - Added `title` annotations to cryptic UCUM units in the schema.

**Current mappings**: Run `make output/user_friendly_units.tsv` to generate current table.

**For new units**: Add `title`, `aliases`, and `description` fields to ensure meaningful display names.

### Legacy Data and Non-Standard Units

For data with units that cannot be converted to UCUM or don't conform to storage_units specifications, see:

- **units/docs/legacy-data-strategy.md** - Proposed approach using misc_param key-value structure (⚠️ speculative)
- **units/docs/units-problems-definitive.md** - Definitive source for all units problems

## Overview

The unit analysis workflow addresses Issue #2598: adding `storage_units` annotations to QuantityValue slots that have clear MIxS-UCUM mappings.

### Schema-Only Approach (Current Implementation)

**Key Breakthrough:** The workflow can now be implemented using only NMDC schema data, eliminating external dependencies:

**This schema-only workflow replaces:**

1. MongoDB data extraction + SPARQL queries
2. MIxS external data download
3. LLM processing for UCUM conversion
4. Chain of 4 individual scripts

**New workflow uses only:**

1. NMDC schema preferred_unit annotations
2. Deterministic UCUM conversion rules
3. Single consolidated script

### Legacy Workflow Components

The original workflow involved:

- **MongoDB data analysis** - Understanding actual vs. acceptable units in production data
- **MIxS mapping** - Correlating schema slots with MIxS preferred units
- **UCUM validation** - Ensuring units comply with standardized notation
- **Schema annotation** - Generating `storage_units` annotations for LinkML slots
- **Schema transformation** - Converting between RDF/TTL formats with unit fixes

## Data Flow Pipeline

### MongoDB Production Data Analysis

**Core Workflow**: Dump MongoDB → migrate data → validate against schema

**Two approaches for slot/unit analysis:**

#### **Approach A: RDF/Triplestore Analysis**

```
mongodb-slots-to-units.csv --[analyze_units.py]--> mongodb-slots-to-units_analyzed.csv --[manual]--> mongodb-slots-to-units_remediated.csv
```

**File**: `assets/sparql/mongodb-slots-to-units.rq`  
**Pipeline**: MongoDB dump → RDF conversion (w/ workarounds) → schema→OWL (w/ workarounds) → SPARQL query → downstream Python analysis  
**Advantage**: Rich triplestore discovery capabilities

**SPARQL Output:** `mongodb-slots-to-units.csv`

- CSV format: `sc,p,l,su,u,count` (schema class, property, label, acceptable units, actual unit, count)
- Contains production MongoDB data showing actual units used vs. schema-acceptable units
- Example: `https://w3id.org/nmdc/Biosample,https://w3id.org/mixs/0000110,samp_store_temp,Cel,Cel,4219`

#### **Approach B: Direct Python Analysis**

**File**: `units/validate_production_units.py`  
**Pipeline**: MongoDB dump → direct YAML processing → slot/unit compliance analysis  
**Advantage**: Same slot/unit analysis without RDF/OWL conversion workarounds

**SPARQL Query Used:**
Saved as `assets/sparql/mongodb-slots-to-units.rq`:

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX nmdc: <https://w3id.org/nmdc/>
select 
?sc ?p ?l ?su ?u (count(?s) as ?count)
where {
    ?s a ?sc ;
    ?p ?qv .
    ?qv a nmdc:QuantityValue ;
    nmdc:has_unit ?u .
    optional {
        ?p rdfs:label ?l
    }
    optional {
        ?p nmdc:storage_units ?su
    }
}
group by ?sc ?p ?l ?su ?u
```

**Query Logic:**

- **Finds instances** (`?s`) with QuantityValue properties containing actual units (`nmdc:has_unit ?u`)
- **Gets schema-acceptable units** via `nmdc:storage_units ?su` 
- **Aggregates by class, property, label, acceptable units, and actual unit**
- **Optional patterns** handle missing labels and storage_units (explains empty CSV values)

**Script:** `analyze_units.py`

- Adds `valid` column indicating whether actual unit (u) is in acceptable units (su)
- Values: validation status indicators
- Provides summary statistics

**Output:** `mongodb-slots-to-units_analyzed.csv`

- Same as input plus `valid` column
- Shows validation status for each slot-unit combination

**LLM Processing:** Creates `mongodb-slots-to-units_remediated.csv`

- **Method**: `mongodb-slots-to-units_analyzed.csv` processed through LLM 
- Adds `remediation` column with systematic fix recommendations
- **LLM generates**: Specific conversion factors, schema additions, or "none required"
- Example outputs: `"add m to schema acceptable units"`, `"convert data from ug/L to mg/L (multiply by 0.001)"`

### 2. Current Schema-Only Pipeline

The pipeline processes schema YAML files through three stages to generate storage_units annotations. See the Makefile for the complete workflow definition.

### 3. Schema Annotation Application

The pipeline generates yq commands that are applied to update schema files with `storage_units` annotations. See the Makefile targets for implementation details.

## Core Scripts & Transformations

### Current Implementation

**Quick Start:** Run `make help` for available targets.

**Files:**

- `units/scripts/schema_extract_preferred_units.py` - Extract preferred units from schema
- `units/scripts/schema_convert_to_ucum.py` - Convert to UCUM with problem detection  
- `units/scripts/schema_generate_yq_commands.py` - Generate yq commands for storage_units
- `Makefile` - Build automation
- `output/schema_preferred_units.tsv` - Preferred units extracted from schema
- `output/schema_ucum_input.tsv` - Minimal data for processing (slot, ucum_notation, problem)
- `output/schema_ucum_detailed.tsv` - Full metadata with context and descriptions
- `output/yq_commands_single_unit.txt` - yq commands for slots with one unit
- `output/yq_commands_multi_unit.txt` - yq commands for slots with multiple units

### Script Usage

Run any script with `--help` for detailed usage information:

```bash
poetry run units-schema-extract --help
poetry run units-schema-convert --help  
poetry run units-schema-generate --help
```

## Unit Sanitization & Validation

### The Sanitization Problem

The round-trip testing with ROBOT tool revealed that **special characters in UnitEnum permissible values break ontology processing**. The log file `robot.txt` (now deleted) showed extensive parsing failures when processing units with:

- **Bracket characters**: `[NTU]`, `[FNU]`, `[pH]`, `[ppm]`, etc.
- **Special symbols**: `%`, `mm[Hg]`, compound units
- **URI encoding conflicts** that cause OWL serialization problems

### Current Sanitization Approach

**SPARQL-based**: Uses `fix-units-update-v2.ru` to transform units:

```sparql
# Remove brackets and fix special characters
DELETE { <https://w3id.org/nmdc/UnitEnum#%> ?p ?o } 
INSERT { <https://w3id.org/nmdc/UnitEnum#percent> ?p ?o }

DELETE { <https://w3id.org/nmdc/UnitEnum#[NTU]> ?p ?o } 
INSERT { <https://w3id.org/nmdc/UnitEnum#NTU> ?p ?o }

DELETE { <https://w3id.org/nmdc/UnitEnum#mm[Hg]> ?p ?o } 
INSERT { <https://w3id.org/nmdc/UnitEnum#mmHg> ?p ?o }
```

### Missing: Python-based Sanitization

**Gap identified**: No Python scripts currently sanitize permissible values. The root directory scripts only:

- **Analyze** units (`analyze_units.py`) - validates but doesn't clean
- **Generate** yq commands using existing clean units
- **Flag** slots requiring attention

**Current Risk**: Square brackets in UCUM units like `[NTU]` break OWL generation, causing failures in OntoText GraphDB and `robot convert`. (See [issue #2614](https://github.com/microbiomedata/nmdc-schema/issues/2614))

**Short-term workaround**: Manual bracket removal script:

- Remove brackets: `[NTU]` → `NTU`  
- Convert special chars: `%` → `percent`, `mm[Hg]` → `mmHg`
- Validate URI safety before RDF generation

**Long-term solution**: LinkML PR #2869 (merged to main, awaiting release) implements proper URI encoding for special characters in permissible values, eliminating manual sanitization needs.

### Testing Tools for Unit Issues

#### 1. ROBOT Round-Trip Testing

```bash
# Test ontology parsing robustness
robot convert --input schema.owl.ttl --output schema-rt.owl.ttl --debug > robot-log.txt
```

**Purpose**: Identifies which units cause RDF/OWL parsing failures

#### 2. Manual URI Validation

Check units for characters that break URIs:

- Brackets: `[`, `]`
- Spaces, special chars that need encoding
- Characters requiring encoding in RDF fragment identifiers

#### 3. Schema Analysis Tools

For comprehensive class/slot analysis, use **LinkML SchemaView** instead of RDF extraction:

```python
from linkml_runtime.utils.schemaview import SchemaView

view = SchemaView("nmdc_materialized_patterns.yaml")
biosample_class = view.get_class("Biosample")
all_slots = view.class_slots("Biosample")  # Gets ALL usable slots
```

**Advantage over RDF extraction**: Captures optional/compatible slots, not just axiomatically required ones.

#### 4. UCUM Validation (Not Currently Available)

**Status**: JavaScript UCUM validation automation is not currently implemented

**If implemented, would provide**:

- Validation against UCUM standard
- Identification of non-standard unit expressions
- Recommendations for UCUM-compliant alternatives

### Recommended Sanitization Workflow

```
src/schema/attribute_values.yaml --[Python sanitizer]--> cleaned units --[schema build]--> validated schema
                                                                           |
                                                                           v
                                                                   [ROBOT round-trip test]
                                                                           |
                                                                           v
                                                                   [Pass/Fail assessment]
```

**Benefits of Python approach**:

- **Preventive**: Fix issues before RDF generation
- **Automated**: Can be integrated into Makefile
- **Reversible**: Can maintain mapping of original → sanitized units
- **Testable**: Can validate changes before applying

## Schema Transformation Outputs

### RDF/TTL Transformations

The workflow generates several RDF transformation artifacts:

```
nmdc-non-native-uris.owl.ttl --[robot + SPARQL]--> nmdc-non-native-uris-rt.owl.ttl
nmdc-non-native-uris.owl.ttl --[fix-units-update-v2.ru]--> nmdc-fixed.ttl --> nmdc-fixed2.ttl
```

**Key Files:**

- `fix-units-update-v2.ru` - SPARQL UPDATE queries for unit URI fixes

**Note on RDF Extraction Limitations:**
Attempts to extract individual classes (like `biosample.ttl`) from OWL files typically only capture axiomatically required properties, missing optional/compatible slots. Use LinkML SchemaView for comprehensive class analysis instead.

**Transformations Applied:**

- Remove brackets from bracketed units: `[NTU]` → `NTU`
- Standardize unit URIs: `%` → `percent`
- Fix mercury unit syntax: `mm[Hg]` → `mmHg`

## Automation Recommendations

### Current Makefile

See the `Makefile` in this directory for the complete workflow definition and available targets.

### Alternative Approaches

The current schema-only workflow replaced earlier MongoDB-based approaches that required external data dependencies.

### Potential Additional Automation

**Unit Sanitization** (recommended addition):

```makefile
# Sanitize units before schema build
src/schema/attribute_values_clean.yaml: src/schema/attribute_values.yaml sanitize_units.py
    $(RUN) python sanitize_units.py $< > $@

# Round-trip test for unit issues
test-units-roundtrip: nmdc_schema/nmdc_materialized_patterns.yaml
    robot convert --input project/owl/nmdc.owl.ttl --output local/nmdc-rt.owl.ttl --debug > local/robot-test.log
    @echo "Check local/robot-test.log for unit parsing issues"
```

**UCUM Validation** (not currently available):

```makefile
# This automation could be implemented in the future
# local/validation_results.txt: validation target (not yet available)
```

## Data Validation Against storage_units Constraints

### SPARQL-based Production Validation (Recommended)

The MongoDB SPARQL approach provides comprehensive validation of production data against storage_units constraints:

```sparql
# Find all instances where:
?instance a ?class ;           # some instance of some class  
    ?slot ?qv .                # uses some slot to connect to a quantity value
?qv a nmdc:QuantityValue ;     # the quantity value
    nmdc:has_unit ?actual_unit . # has an actual unit

# Get the constraint:
?slot nmdc:storage_units ?allowed_units . # storage_units of the slot

# Validation: check if ?actual_unit is in pipe-separated ?allowed_units
```

**Advantages of SPARQL approach:**

- **Comprehensive coverage** - Analyzes ALL QuantityValue patterns in production MongoDB data
- **Production scale** - Handles large datasets efficiently vs limited test files
- **Flexible querying** - Can filter by class, slot, unit patterns ("show all Biosample temperature readings with non-Celsius units")
- **Statistical analysis** - Count compliance, group by slot/class, find patterns
- **Pattern discovery** - Identify usage patterns for storage_units constraints

### MongoDB YAML Dump Validation (Implemented)

The `validate_production_units.py` script provides SPARQL-like comprehensive analysis without RDF complexity:

```bash
# First generate MongoDB production data dump (from project root)
make local/mongo_via_api_as_unvalidated_nmdc_database.yaml           # Uses prod API + dev schema (hardcoded)
make local/mongo_via_api_as_unvalidated_nmdc_database.yaml ENV=dev   # Uses dev API + dev schema (hardcoded)

# Then validate units in the dump (from units/ directory)
cd units && make validate-production                    # Uses dev schema (flexible)
cd units && make validate-production ENV=prod           # Uses release schema (flexible)
```

**Current Flexibility Status:**

- **MongoDB dump (project.Makefile)**: ✅ API flexible, ⚠️ schema hardcoded to dev
- **Units validation (units/Makefile)**: ✅ API inherited, ✅ schema flexible

**MongoDB dump process:**

- **Collections analyzed**: 16 default collections including `biosample_set`, `processed_sample_set`, `data_object_set`, etc.
- **Data source**: Live NMDC API (`https://api.microbiomedata.org`)
- **Scope**: Up to 200,000 documents per collection
- **Output format**: Single YAML file with all collections

**Validation features:**

- **UnitEnum compliance** - Checks all `has_unit` values exist in schema's UnitEnum
- **storage_units constraints** - Validates units against slot-specific storage_units annotations
- **Comprehensive reporting** - TSV output with compliance details, statistics, and summaries
- **Production scale** - Handles full MongoDB dataset efficiently

**Usage:**

```bash
# Validate against current development schema (default)
python validate_production_units.py \
    --input ../local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
    --output production_validation_report.tsv

# Validate against latest release schema
python validate_production_units.py \
    --input ../local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
    --output production_validation_report.tsv \
    --schema-file ../local/nmdc_schema_last_release.yaml

# Or use Makefile with ENV variable
make validate-production                    # Uses dev schema
make validate-production ENV=prod           # Uses release schema
```

### Test-based Validation (Limited Scope)

The existing `tests/test_has_unit_validation.py` validates example data files:

- **Scope**: Only `src/data/valid/*.yaml` files (curated examples)
- **Purpose**: Ensures example data complies with storage_units constraints
- **Limitations**: Small dataset, no production coverage, limited aggregation capabilities

**When to use each approach:**

- **SPARQL**: Production compliance analysis, schema validation assessment, identifying real-world unit issues
- **Tests**: CI/CD validation of example data, ensuring curated examples remain compliant

The SPARQL approach provides the comprehensive production analysis needed to assess how well actual data complies with storage_units constraints generated by this workflow.

## Production Data Dump Troubleshooting

### MongoDB Dump Issues and Workarounds

**Problem 1: Makefile target broken due to contributor modifications**

```
Error: No such option: --psize Did you mean --page-size?
```

**Root Cause:** The `project.Makefile` target for `local/mongo_via_api_as_unvalidated_nmdc_database.yaml` has been modified by another contributor and now produces malformed command lines.

**Diagnostic:** The `--page-size 200000` parameter gets mangled into `--psize 200 200000` during Make processing.

**Workaround:** Call `pure-export` directly instead of using the Makefile target:

```bash
poetry run pure-export \
    --max-docs-per-coll 200000 \
    --output-yaml local/mongo_via_api_as_unvalidated_nmdc_database.yaml \
    --schema-source nmdc_schema/nmdc_materialized_patterns.yaml \
    [... all --selected-collections flags ...] \
    dump-from-api \
    --client-base-url "https://api-dev.microbiomedata.org" \
    --endpoint-prefix nmdcschema \
    --page-size 200000
```

**Problem 2: Incorrect dev API URL in project.Makefile**

```
Failed to resolve 'dev-api.microbiomedata.org' ([Errno 8] nodename nor servname provided, or not known)
```

**Root Cause:** Makefile uses incorrect URL `dev-api.microbiomedata.org` instead of correct `api-dev.microbiomedata.org`.

**Problem 3: Collection coverage gaps**

```
Database slots only: ['functional_annotation_agg']
```

**Observation:** The `DEFAULT_COLLECTIONS` list in `project.Makefile` includes 16 collections but misses `functional_annotation_agg` which:

- ✅ Exists in schema (17 total collections)
- ✅ Exists in database (41.3M documents - largest collection!)
- ❌ Not included in default dump

**Impact Assessment:** For units validation, this may miss QuantityValue objects in `functional_annotation_agg`. Consider adding it to collection list if it contains unit data.

**Problem 4: Dev API endpoint availability**

**Issue:** Development APIs often have intermittent availability or require special network access.

### Data Collection Statistics (Dev API)

**Data collection overview:**

- **biosample_set**: Environmental measurements  
- **data_object_set**: Large collection
- **workflow_execution_set**: Analysis results
- **functional_annotation_agg**: Very large collection - **Not included in default dump**
- **Other collections**: Various sizes, some empty

**Collections with substantial QuantityValue potential:**

- `biosample_set` - Environmental measurements
- `material_processing_set` - Processing metadata
- `study_set` - Study-level metadata
- `workflow_execution_set` - Analysis results

### Document Limit Analysis (200k max per collection)

**Collections approaching document limits:**

- **data_object_set**: Approaching collection limit, risk of truncation
- **functional_annotation_agg**: Far exceeds limits, excluded from default dump

**Collections within limits:**

- **workflow_execution_set**: Well below limit
- **biosample_set**: Well below limit  
- **material_processing_set**: Well below limit
- **Other collections**: Small numbers

**Recommendations:**

1. **Monitor data_object_set growth** - Consider increasing limit or adding alerts
2. **Investigate functional_annotation_agg** - Determine if it contains QuantityValue objects
3. **Collection-specific limits** - Large collections may need higher limits than 200k
4. **Validation completeness** - Document which collections are truncated vs complete

## Troubleshooting

### Common Issues

#### Script not found

Ensure you're running from the `units/` directory.

#### Missing dependencies

All scripts require `click`, `pandas`, and `yaml` packages.

#### Schema file not found

The default schema path is `../nmdc_schema/nmdc_materialized_patterns.yaml`. Use `--schema-file` to specify different path.

#### Empty outputs

Check that schema contains `preferred_unit` annotations. Run with verbose output.

## File Management

### Current Files (Keep)

- **Core Scripts:** `units/scripts/schema_extract_preferred_units.py`, `units/scripts/schema_convert_to_ucum.py`, `units/scripts/schema_generate_yq_commands.py` - Current implementation
- **Build System:** `Makefile` - Clean artifact-based automation
- **Documentation:** `README.md` - This comprehensive documentation
- **Transformation Queries:** `fix-units-update-v2.ru` - SPARQL unit URI fixes

### Generated Files (Cleaned by `make clean`)

- **Intermediate Data:** `output/schema_preferred_units.tsv`, `output/schema_ucum_input.tsv`, `output/schema_ucum_detailed.tsv`
- **Final Outputs:** `output/yq_commands_single_unit.txt`, `output/yq_commands_multi_unit.txt` - yq command files for applying storage_units annotations

**When to regenerate:** The yq command files should be regenerated when:

- New slots receive preferred_unit annotations
- UCUM conversion logic improvements are made 
- Preferred_unit values change in the schema
- Historical unit issues are resolved

### Legacy Files Analysis

#### Files Deleted During Cleanup

- **Documentation stubs:** `TURBIDITY_UNIT_FIX_STATUS.md` - ✅ **Status: Deleted**
- **ROBOT logs:** `robot.txt` - ✅ **Status: Deleted** 
- **Context Files:** `UnitEnum-context.txt` - ✅ **Status: Deleted**
- **Legacy Validation Files:** Various validation outputs - ✅ **Status: Deleted**
- **RDF Transformation Files:** `nmdc-non-native-uris*.owl.ttl` - ✅ **Status: Deleted**
- **Generated RDF Outputs:** `nmdc-fixed.ttl`, `nmdc-fixed2.ttl` - ✅ **Status: Deleted**
- **Incomplete Extractions:** `biosample.ttl` - ✅ **Status: Deleted**
- **IRI Mapping Files:** `nmdc-iri-map*.tsv` - ✅ **Status: Deleted**

#### MongoDB Production Data Analysis Files

- **`mongodb-slots-to-units.csv`** - **Status: Can delete** - Regenerable via SPARQL query (documented above)
- **`mongodb-slots-to-units_analyzed.csv`** - **Status: Can delete** - Regenerable via `analyze_units.py`
- **`mongodb-slots-to-units_remediated.csv`** - **Status: Keep** - LLM-generated remediation with specific conversion factors

**Keep Only:** The remediated file contains the most valuable insights - systematic LLM-generated conversion factors and remediation strategies that would be time-consuming to recreate:

- **Specific conversion factors**: "convert data from ug/L to mg/L (multiply by 0.001)"
- **Schema recommendations**: "add m to schema acceptable units"  
- **Production data analysis**: Based on real MongoDB usage patterns with thousands of records

#### Current Script Architecture

- **`units/scripts/schema_extract_preferred_units.py`** - Extract preferred_unit annotations from schema
- **`units/scripts/schema_convert_to_ucum.py`** - Convert units to UCUM notation with problem detection
- **`units/scripts/schema_generate_yq_commands.py`** - Generate yq commands for storage_units annotations

Use `poetry run <script-name> --help` for detailed CLI options.

#### File Evolution Notes

Several files and approaches have been replaced or consolidated:

- **Reference data**: Now fetched from GitHub URLs for reproducibility
- **Derived exports**: Generated on-demand from materialized schema
- **Redundant scripts**: Consolidated into current pipeline

This workflow documentation centralizes all unit-related analysis and provides clear automation pathways for future maintenance while preserving the complete history and rationale of our development process.