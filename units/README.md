# Units

This document provides a comprehensive overview of the unit analysis, validation, and storage_units annotation workflow for the NMDC schema. It documents all data transformations, scripts, and automation opportunities for managing unit-related schema components.

## Table of Contents

1. [Overview](#overview)
2. [Data Flow Pipeline](#data-flow-pipeline)
3. [Core Scripts & Transformations](#core-scripts--transformations)
4. [UCUM Validation System](#ucum-validation-system)
5. [Schema Transformation Outputs](#schema-transformation-outputs)
6. [Automation Recommendations](#automation-recommendations)
7. [Troubleshooting](#troubleshooting)
8. [File Management](#file-management)

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

### 1. MongoDB Unit Analysis Pipeline

```
mongodb-slots-to-units.csv --[analyze_units.py]--> mongodb-slots-to-units_analyzed.csv --[manual]--> mongodb-slots-to-units_remediated.csv
```

**Input:** `mongodb-slots-to-units.csv`
- **Source**: Generated via SPARQL query over RDF-converted MongoDB production data
- **Infrastructure**: Uses Makefile targets for MongoDB→RDF conversion + custom SPARQL query
- CSV format: `sc,p,l,su,u,count` (schema class, property, label, acceptable units, actual unit, count)
- Contains production MongoDB data showing actual units used vs. schema-acceptable units
- Example: `https://w3id.org/nmdc/Biosample,https://w3id.org/mixs/0000110,samp_store_temp,Cel,Cel,4219`

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
- Values: `valid`, `invalid`, `no_spec`
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

```
../nmdc_schema/nmdc_materialized_patterns.yaml
    ↓ [analyze.py]
schema.tsv 
    ↓ [extract.py] 
input.tsv + detailed.tsv
    ↓ [process.py]
single.txt + multi.txt
```

**Script 1:** `analyze.py` (formerly `analyze_preferred_units.py`)
- Extracts preferred_unit annotations from schema YAML
- Now uses Click CLI with configurable schema path
- Moved from `src/scripts/` to local `units/` directory

**Script 2:** `extract.py` (formerly `generate_mixs_input_from_schema.py`)
- Converts preferred units to UCUM notation deterministically
- Detects problem patterns (brackets, imperial units, complex expressions)
- Handles multi-unit slots (comma/pipe separated)
- **Key Innovation**: No external dependencies - pure schema-based

**Script 3:** `process.py` (formerly `process_mixs_units.py`)
- Consolidated replacement for 4 individual scripts:
  - `add_has_problem.py`
  - `add_slot_count.py` 
  - `find_storage_units.py`
  - `generate_multi_unit_storage_units.py`
- Complete processing pipeline in single script
- Proper error handling and Click CLI interface

### 3. Storage Units Annotation Generation

#### Single-Unit Slots
```
input.tsv --[process.py]--> single.txt (yq commands)
```

**Logic:**
- Filters: `problem != 1` AND `slot_row_count == 1`
- Generates yq commands for single UCUM-compatible units
- Output format: `'.slots.{slot_name}.annotations.storage_units.tag |= "storage_units"'`

#### Multi-Unit Slots
```
input.tsv --[process.py]--> multi.txt (yq commands)
```

**Logic:**
- Filters: `problem != 1` AND `slot_row_count > 1`
- Groups by slot, creates pipe-separated UCUM notation lists
- Output format: `'.slots.{slot_name}.annotations.storage_units = {"tag": "storage_units", "value": "unit1|unit2"}'`

### 4. Schema Annotation Application

```
single.txt + multi.txt --[yq]--> src/schema/*.yaml (updated with storage_units annotations)
```

The generated yq commands are applied to update schema files with `storage_units` annotations.

## Core Scripts & Transformations

### Current Implementation

**Quick Start:**
```bash
make all         # Build all outputs
make rebuild     # Clean then build
make clean       # Remove generated files
```

**Files:**
- `analyze.py` - Extract preferred units from schema
- `extract.py` - Convert to UCUM with problem detection  
- `process.py` - Generate yq commands for storage_units
- `Makefile` - Build automation
- `schema.tsv` - Preferred units extracted from schema
- `input.tsv` - Minimal data for processing (slot, ucum_notation, problem)
- `detailed.tsv` - Full metadata with context and descriptions
- `single.txt` - yq commands for slots with one unit
- `multi.txt` - yq commands for slots with multiple units

### `analyze.py`
**Purpose:** Extract preferred_unit annotations from NMDC schema

**Usage:**
```bash
python analyze.py [--schema-file PATH] OUTPUT_FILE
```

**Features:**
- Converted to Click CLI (was hardcoded paths)
- Moved from `src/scripts/` to local directory
- Configurable schema file path
- Comprehensive summary statistics

### `extract.py`
**Purpose:** Schema-only UCUM conversion with problem detection

**Usage:**
```bash
python extract.py INPUT_FILE OUTPUT_FILE [--detailed DETAILED_FILE] [--quiet]
```

**Key Innovation:** Replaces external MIxS data + LLM processing with deterministic rules:

**Direct UCUM mappings:**
```python
direct_mappings = {
    'degree Celsius': 'Cel',
    'meter': 'm',
    'millimeter': 'mm',
    'gram': 'g',
    'liter': 'L',
    'percent': '%',
    # ... etc
}
```

**Problem pattern detection:**
```python
problem_patterns = [
    r'.*,.*',           # Multiple units separated by commas
    r'.*\\|.*',         # Multiple units separated by pipes  
    r'.*\\[.*\\].*',    # Bracketed units like [NTU], [pH]
    r'.*\\bper\\b.*\\bper\\b.*',  # Complex ratios
    r'.*formazin.*',    # Turbidity units
    # ... etc
]
```

### `process.py`
**Purpose:** Consolidated pipeline generating yq commands

**Usage:**
```bash
python process.py INPUT_FILE [--output-dir DIR]
```

**Replaces 4 scripts:**
- Adds slot-level problem flags
- Counts units per slot
- Generates single-unit yq commands
- Generates multi-unit yq commands

## Unit Sanitization & Validation

### The Sanitization Problem

The round-trip testing with ROBOT tool revealed that **special characters in UnitEnum permissible values break ontology processing**. The log file `robot.txt` (now deleted) showed extensive parsing failures when processing units with:

- **Bracket characters**: `[NTU]`, `[FNU]`, `[pH]`, `[ppm]`, etc.
- **Special symbols**: `%`, `mm[Hg]`, compound units
- **URI encoding conflicts** that cause OWL serialization problems

### Current Sanitization Approach

**SPARQL-based**: Uses `fix-units-update-v2.ru` to transform problematic units:
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
- **Flag** problematic slots without fixing them

**Needed**: A Python script that could:
- Remove brackets: `[NTU]` → `NTU`
- Convert special chars: `%` → `percent`, `mm[Hg]` → `mmHg`
- Validate URI safety of unit values
- Bulk sanitize YAML files before RDF generation

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
- Characters invalid in RDF fragment identifiers

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
**Status**: Referenced automation doesn't exist
- ❌ Makefile target `make local/invalid_unitenum_units.txt` - **missing**
- ❌ Script `src/scripts/check_unitenum_ucum_compliance.js` - **missing** 
- ❌ Node.js UCUM validation integration - **not implemented**

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
- `fix-units-update-v2.ru` - SPARQL UPDATE queries for unit URI fixes (6.4KB, kept)
- `nmdc-iri-map*.tsv` - Entity-to-replacement mappings for ROBOT tool (deleted)
- `robot.txt` - ROBOT tool execution logs (deleted)
- `nmdc-fixed.ttl`, `nmdc-fixed2.ttl` - Generated RDF outputs (deleted)

**Generated RDF Analysis (now deleted):**
The sequential transformation workflow `nmdc-fixed.ttl` → `nmdc-fixed2.ttl` successfully demonstrated SPARQL-based unit sanitization:
- **nmdc-fixed.ttl** (2.2MB) - First-pass SPARQL transformation, partially cleaned units
- **nmdc-fixed2.ttl** (2.7MB) - Final cleaned output with more complete processing
- **Proof of concept** - Showed that `%` → `percent`, `[NTU]` → `NTU`, `mm[Hg]` → `mmHg` transformations work

**IRI Mapping Analysis (now deleted):**
The IRI mapping files demonstrated an alternative ROBOT-based approach to unit cleaning:
- **nmdc-iri-map.tsv** (969B) - Original entity-to-replacement mappings
- **nmdc-iri-map-robot.tsv** (966B) - ROBOT tool compatible format (`Old IRI | New IRI`)
- **nmdc-iri-map-robot-v2.tsv** (966B) - Duplicate of robot version
- **Dual approach strategy** - Explored both SPARQL (`fix-units-update-v2.ru`) and ROBOT (`replace-iris`) methods

**Note on RDF Extraction Limitations:**
Attempts to extract individual classes (like `biosample.ttl`) from OWL files typically only capture axiomatically required properties, missing optional/compatible slots. Use LinkML SchemaView for comprehensive class analysis instead.

**Transformations Applied:**
- Remove brackets from bracketed units: `[NTU]` → `NTU`
- Standardize unit URIs: `%` → `percent`
- Fix mercury unit syntax: `mm[Hg]` → `mmHg`

## Automation Recommendations

### Current Makefile

```makefile
# Current simplified workflow
all: single.txt multi.txt

schema.tsv: analyze.py
	python analyze.py schema.tsv

input.tsv detailed.tsv: schema.tsv extract.py
	python extract.py $< $@ --detailed detailed.tsv

single.txt multi.txt: input.tsv process.py
	python process.py input.tsv

clean:
	rm -f schema.tsv input.tsv detailed.tsv single.txt multi.txt

rebuild: clean all
```

### Legacy Automation (Replaced)

**MongoDB unit analysis pipeline:**
```makefile
# This was the old approach - now replaced
mongodb-slots-to-units_analyzed.csv: mongodb-slots-to-units.csv analyze_units.py
	$(RUN) python analyze_units.py $<

# Storage units yq command generation  
storage-units-single.txt: find_storage_units.py pref-unit-slots-final.tsv
	$(RUN) python find_storage_units.py > $@
```

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
# This automation doesn't exist but could be implemented
local/invalid_unitenum_units.txt: src/schema/attribute_values.yaml src/scripts/check_unitenum_ucum_compliance.js
	cd src/scripts && npm ci && node check_unitenum_ucum_compliance.js ../../$< > ../../$@
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
- **Statistical analysis** - Count violations, group by slot/class, find most common issues
- **Pattern discovery** - Identify which slots have the most storage_units constraint violations

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
- **Comprehensive reporting** - TSV output with violation details, statistics, and summaries
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

**Root Cause:** The `project.Makefile` defines:
```makefile
API_DEV_URL = https://dev-api.microbiomedata.org  # INCORRECT
```

**Correct URL:** `https://api-dev.microbiomedata.org` (confirmed working at `/docs` endpoint)

**Diagnostic:** DNS lookup shows `NXDOMAIN` for `dev-api.microbiomedata.org` but `api-dev.microbiomedata.org` resolves correctly.

**Impact:** This affects the `ENV=dev` functionality in `project.Makefile` but not our units validation since we use the correct URL directly.

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

**Diagnostic Steps:**
1. Test DNS resolution: `nslookup api-dev.microbiomedata.org`
2. Check endpoint health: `curl https://api-dev.microbiomedata.org/docs`
3. Verify API compatibility with expected endpoints

**Fallback Strategy:** Use production API (`https://api.microbiomedata.org`) for testing validation workflow if dev is unavailable.

### Current API Infrastructure Status

**Production API**: ✅ `https://api.microbiomedata.org` - Stable, publicly accessible
**Development API**: ✅ `https://api-dev.microbiomedata.org` - Working (as of validation)
**Incorrect URL in Makefile**: ⚠️ `https://dev-api.microbiomedata.org` - Does not exist

### Data Collection Statistics (Dev API)

**Successful dump from api-dev.microbiomedata.org:**
- **biosample_set**: 13,248 documents (25.4MB)
- **data_object_set**: 184,356 documents (94.6MB) 
- **workflow_execution_set**: 19,522 documents (524MB)
- **functional_annotation_agg**: 41.3M documents (6.8GB) - **Not included in default dump**
- **Other collections**: Various sizes, some empty
- **Total collections available**: 17 in schema, 16 in default dump

**Collections with substantial QuantityValue potential:**
- `biosample_set` - Environmental measurements
- `material_processing_set` - 9,372 documents
- `study_set` - Study-level metadata
- `workflow_execution_set` - Analysis results

### Document Limit Analysis (200k max per collection)

**🚨 Critical Risk - Collections approaching limit:**
- **data_object_set**: 184,356 documents (92% of 200k limit)
  - Only 15,644 documents below limit
  - High risk of truncation with normal data growth
  - May miss recent data objects in validation

**⚠️ Extreme Risk - Collections exceeding limit:**
- **functional_annotation_agg**: 41,305,297 documents (206x the limit!)
  - Would be truncated to only 0.5% of actual data
  - Fortunately excluded from default dump
  - Unclear if contains QuantityValue objects for units validation

**✅ Safe Collections (well below limit):**
- workflow_execution_set: 19,522 docs (10% of limit)
- biosample_set: 13,248 docs (7% of limit) 
- material_processing_set: 9,372 docs (5% of limit)
- All other collections: <1,000 docs each

**Recommendations:**
1. **Monitor data_object_set growth** - Consider increasing limit or adding alerts
2. **Investigate functional_annotation_agg** - Determine if it contains QuantityValue objects
3. **Collection-specific limits** - Large collections may need higher limits than 200k
4. **Validation completeness** - Document which collections are truncated vs complete

## Troubleshooting

### Turbidity Unit Fix Status

**Issue:** Test `tests/test_annotations.py::TestAnnotations::test_storage_units_from_unit_enum` fails with:
```
"SlotDefinition.turbidity: storage_units value '[FNU]' not in UnitEnum"
```

**Root Cause:** [FNU] is defined in `src/schema/attribute_values.yaml` but not appearing in the materialized UnitEnum.

**Resolution Steps:**
1. **Debug [FNU] missing from UnitEnum:**
   ```bash
   grep -n "\[FNU\]" nmdc_schema/nmdc_materialized_patterns.yaml
   ```

2. **Verify UnitEnum generation:**
   - Check how `src/schema/attribute_values.yaml` gets converted to materialized UnitEnum
   - Look for filtering steps that might exclude [FNU]

3. **Test the fix:**
   ```bash
   python -m pytest tests/test_annotations.py::TestAnnotations::test_storage_units_from_unit_enum -v
   ```

**Completed Tasks:**
- ✅ Added `not_measurement_like` to annotation whitelist in `tests/test_annotations.py`
- ✅ Updated test data files to use proper turbidity units (`[NTU]`)
- ✅ Confirmed [FNU] exists in `src/schema/attribute_values.yaml:1936-1938`
- ✅ Rebuilt schema with `make squeaky-clean all`

### Common Issues

#### Script not found
Ensure you're running from the `units/` directory.

#### Missing dependencies
All scripts require `click`, `pandas`, and `yaml` packages.

#### Schema file not found
The default schema path is `../nmdc_schema/nmdc_materialized_patterns.yaml`. Use `--schema-file` to specify different path.

#### Empty outputs
Check that schema contains `preferred_unit` annotations. Run with verbose output.

#### "npm: command not found"
Install Node.js and npm for UCUM validation (if implemented).

#### Network errors during npm ci
Check internet connection for package downloads.

## File Management

### Current Files (Keep)
- **Core Scripts:** `analyze.py`, `extract.py`, `process.py` - Current implementation
- **Build System:** `Makefile` - Clean artifact-based automation
- **Documentation:** `README.md` - This comprehensive documentation
- **Transformation Queries:** `fix-units-update-v2.ru` - SPARQL unit URI fixes

### Generated Files (Cleaned by `make clean`)
- **Intermediate Data:** `schema.tsv`, `input.tsv`, `detailed.tsv`
- **Final Outputs:** `single.txt`, `multi.txt` - yq command files for applying storage_units annotations

**When to regenerate:** The yq command files should be regenerated when:
- New slots receive preferred_unit annotations
- UCUM conversion logic improvements are made 
- Preferred_unit values change in the schema
- Previously problematic units are resolved

### Legacy Files Analysis

#### Files Deleted During Cleanup
- **Documentation stubs:** `TURBIDITY_UNIT_FIX_STATUS.md` - ✅ **Status: Deleted**
- **ROBOT logs:** `robot.txt` (1830 lines) - ✅ **Status: Deleted** 
- **Context Files:** `UnitEnum-context.txt` - ✅ **Status: Deleted**
- **Invalid Validation Files:** `local/invalid_unitenum_units.txt`, `UnitEnum_UCUM_Validation.md` - ✅ **Status: Deleted**
- **RDF Transformation Files:** `nmdc-non-native-uris*.owl.ttl` - ✅ **Status: Deleted**
- **Generated RDF Outputs:** `nmdc-fixed.ttl`, `nmdc-fixed2.ttl` (5MB+ total) - ✅ **Status: Deleted**
- **Incomplete Extractions:** `biosample.ttl` (34KB) - ✅ **Status: Deleted**
- **IRI Mapping Files:** `nmdc-iri-map*.tsv` (2.9KB total) - ✅ **Status: Deleted**

#### MongoDB Production Data Analysis Files 
- **`mongodb-slots-to-units.csv`** (89 lines) - **Status: Can delete** - Regenerable via SPARQL query (documented above)
- **`mongodb-slots-to-units_analyzed.csv`** (89 lines) - **Status: Can delete** - Regenerable via `analyze_units.py`
- **`mongodb-slots-to-units_remediated.csv`** (88 lines) - **Status: Keep** - LLM-generated remediation with specific conversion factors

**Keep Only:** The remediated file contains the most valuable insights - systematic LLM-generated conversion factors and remediation strategies that would be time-consuming to recreate:
- **Specific conversion factors**: "convert data from ug/L to mg/L (multiply by 0.001)"
- **Schema recommendations**: "add m to schema acceptable units"  
- **Production data analysis**: Based on real MongoDB usage patterns with thousands of records

#### Individual Scripts (Consolidated)
- **`add_has_problem.py`, `add_slot_count.py`, `find_storage_units.py`, `generate_multi_unit_storage_units.py`** - ✅ **Status: Deleted** - Individual scripts in broken MIxS pipeline, replaced by consolidated `process.py`

#### Script Consolidation Summary
- **`process.py`** - ✅ **New** - Consolidated MIxS processing pipeline with proper error handling and Click CLI interface
  - **Replaces**: 4 individual scripts with hardcoded paths and no error handling
  - **Usage**: `python process.py INPUT_FILE [--output-dir DIR]`
  - **Required input columns**: `slot`, `ucum_notation`, `problem`
  - **Outputs**: `single.txt`, `multi.txt`
  - **Benefits**: Single script, proper error handling, consistent paths, Click CLI interface

#### Schema-Only Input Generation
- **`extract.py`** - ✅ **New** - **Schema-only workflow** that eliminates external dependencies
  - **Key Innovation**: Generates input for `process.py` using **only schema data** - no MongoDB, no external MIxS downloads, no LLM
  - **Data sources**: 
    1. **NMDC schema preferred_unit annotations** - via `analyze.py`
    2. **Deterministic UCUM conversion** - pattern-based rules, fully reproducible
    3. **Problem detection** - regex patterns for brackets, complex expressions, imperial units
  - **Creates**: `input.tsv` (minimal) + `detailed.tsv` (full metadata)
  - **Results**: 369 slot-unit combinations from 224 unique slots, 144 clean UCUM units
  - **Workflow**: `make all` (complete automation)
  - **Advantages**: Faster, simpler, no external dependencies, fully deterministic

#### Files That Were Archived/Replaced
- **Large Reference Data:** `mixs_source.tsv` - ✅ **Status: Deleted** - Use GitHub URL instead for reproducibility
  - **Replace with**: `curl "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs6.2_release_candidate/refs/heads/main/GSC-excel-harmonized-repaired/mixs_v6.xlsx.harmonized.tsv" > mixs_source.tsv`
  - **Benefits**: Always uses latest MIxS 6.2 data, publicly reproducible workflow
- **Schema Annotation Export:** `annotations.tsv` - ✅ **Status: Deleted** - Regenerable from materialized schema
  - **Replace with**: 
    ```bash
    yq eval '
      ((.slots // {}) | to_entries[] | 
      select(.value.annotations) |
      (.key as $slot | .value.annotations | to_entries[] | 
      "slots." + $slot + "\t" + .value.tag + "\t" + .value.value)),
      
      ((.classes // {}) | to_entries[] |
      select(.value.slot_usage) |
      (.key as $class | .value.slot_usage | to_entries[] |
      select(.value.annotations) |
      (.key as $slot | .value.annotations | to_entries[] |
      "classes." + $class + ".slot_usage." + $slot + "\t" + .value.tag + "\t" + .value.value)))
    ' nmdc_schema/nmdc_materialized_patterns.yaml > annotations.tsv
    ```
  - **Benefits**: Always current with schema, eliminates maintenance of derived files
- **Redundant Script:** `generate_fixed_storage_units.py` - ✅ **Status: Deleted** - Duplicate functionality, replaced by `process.py`
- **Obsoleted Prototype:** `create_mixs_input_prototype.py` - ✅ **Status: Deleted** - External dependency prototype, replaced by schema-only `extract.py`
- **One-time Fix Script:** `fix_biosample_entry.py` - ✅ **Status: Deleted** - Fixed corrupted biosample entry `nmdc:bsm-99-4444444` in `Database-interleaved.yaml` (work complete)

This workflow documentation centralizes all unit-related analysis and provides clear automation pathways for future maintenance while preserving the complete history and rationale of our development process.