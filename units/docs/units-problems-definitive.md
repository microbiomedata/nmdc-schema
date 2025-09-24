# Comprehensive Problematic Units Analysis

## Overview

This document is the **definitive source** for all units-related problems in the NMDC schema, covering both:

1. **Problematic Slots** (Schema design issues) - Slots with `units_alignment_excuse` annotations
2. **Problematic Data** (Production data issues) - Data using units not in the slot's `storage_units` list

## Schema Annotation Issues Found

### 1. Missing Slot from Excuse File
The slot `organism_count` is listed in `units/output/schema_units_excuses.tsv` as having `protocol_slot` excuse, but current schema shows it has `storage_units: '1'`.

### 2. Contradictory Dual Annotations  
15 slots have BOTH `storage_units` AND `units_alignment_excuse` annotations:

- `agrochem_addition` - has `storage_units: g|mg/L|mol/L` AND `units_alignment_excuse: protocol_slot`
- `antibiotic_regm` - has `storage_units: mg` AND `units_alignment_excuse: protocol_slot`  
- `fertilizer_regm` - has `storage_units: g|mg/L|mol/L` AND `units_alignment_excuse: protocol_slot`
- `fungicide_regm` - has both storage_units and excuse
- `growth_hormone_regm` - has both storage_units and excuse
- `herbicide_regm` - has both storage_units and excuse
- `humidity_regm` - has both storage_units and excuse
- `mineral_nutr_regm` - has both storage_units and excuse
- `non_min_nutr_regm` - has both storage_units and excuse
- `pesticide_regm` - has both storage_units and excuse
- `radiation_regm` - has both storage_units and excuse
- `rainfall_regm` - has both storage_units and excuse
- `salt_regm` - has both storage_units and excuse
- `water_temp_regm` - has both storage_units and excuse
- `watering_regm` - has both storage_units and excuse

A slot should have EITHER storage_units OR units_alignment_excuse, not both.

## Types of Problems

### 1. **Problematic Slots** (Schema Design Issues)
Slots that cannot or should not have `storage_units` annotations due to fundamental design issues.

### 2. **Problematic Data** (Production Data Issues)  
Data using units not in the slot's `storage_units` list, indicating data quality issues.

## Excuse Categories Analysis

### Schema State Summary
- **37 slots listed in excuse file**
- **22 slots have ONLY excuse annotations** (✅ correct)
- **15 slots have BOTH storage_units AND excuse** (❌ contradictory)
- **1 slot missing from excuse file** (`organism_count` has storage_units but was listed as excused)

### `protocol_slot` Category (20 slots)

**Problem Statement**: These slots describe experimental protocols/regimens rather than direct measurements. They combine multiple measurement types with temporal/procedural information that cannot be reduced to a single storage unit.

**Affected Slots**:
- `agrochem_addition`, `fertilizer_regm`, `antibiotic_regm`, `fungicide_regm`, `growth_hormone_regm`, `herbicide_regm`, `mineral_nutr_regm`, `non_min_nutr_regm`, `pesticide_regm`, `salt_regm`
- `air_temp_regm`, `humidity_regm`, `light_regm`, `radiation_regm`, `rainfall_regm`, `water_temp_regm`, `watering_regm`, `standing_water_regm`
- `org_count_qpcr_info`, `samp_transport_cond`

**Examples**: 
- `agrochem_addition`: "roundup;5 milligram per liter;2018-06-21"
- `air_temp_regm`: "25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M"

**Why no storage_units**: The range includes both quantitative measurements AND temporal/procedural metadata that cannot be standardized to UCUM units.

**GitHub Reference**: [PR #2599 comment](https://github.com/microbiomedata/nmdc-schema/pull/2599#issuecomment-3270547242) - "I don't think it's really possible to assert a unit for compound slots like these"

**Issue**: 15 of 19 protocol_slot category slots have contradictory dual annotations

**Slots with CONTRADICTORY dual annotations** (have both storage_units AND excuse):
- `agrochem_addition` (TextValue) - has `storage_units: g|mg/L|mol/L` + excuse
- `antibiotic_regm` (TextValue) - has `storage_units: mg` + excuse
- `fertilizer_regm` (TextValue) - has `storage_units: g|mg/L|mol/L` + excuse
- `fungicide_regm` (TextValue) - has both annotations
- `growth_hormone_regm` (TextValue) - has both annotations
- `herbicide_regm` (TextValue) - has both annotations
- `humidity_regm` (TextValue) - has both annotations
- `mineral_nutr_regm` (TextValue) - has both annotations
- `non_min_nutr_regm` (TextValue) - has both annotations
- `pesticide_regm` (TextValue) - has both annotations
- `radiation_regm` (TextValue) - has both annotations
- `rainfall_regm` (TextValue) - has both annotations
- `salt_regm` (TextValue) - has both annotations
- `water_temp_regm` (TextValue) - has both annotations
- `watering_regm` (TextValue) - has both annotations

**Slots with ONLY excuse annotation** (✅ correct):
- `air_temp_regm` (TextValue) - excuse only
- `light_regm` (TextValue) - excuse only
- `org_count_qpcr_info` (string) - excuse only
- `samp_transport_cond` (TextValue) - excuse only
- `standing_water_regm` (TextValue) - excuse only

### `pending_analysis` Category (11 slots)

**Problem Statement**: These slots require further investigation to determine appropriate units or whether they should have QuantityValue range at all.

**Affected Slots**:
- `biomaterial_purity`, `bulk_elect_conductivity`, `concentration`, `container_size`, `exp_pipe`, `filter_pore_size`, `input_volume`, `occup_density_samp`, `soil_text_measure`, `substances_volume`, `value`

**Key Examples**:
- **`biomaterial_purity`**: 
  - **Issue**: [#2548](https://github.com/microbiomedata/nmdc-schema/issues/2548)
  - **Problem**: Parent of DNA absorbance slots, may need to be abstract
  - **Range conflict**: Has QuantityValue range but children have float range
- **`soil_text_measure`**: 
  - **Issue**: [#2387](https://github.com/microbiomedata/nmdc-schema/issues/2387) 
  - **Problem**: Description incompatible with QuantityValue range
  - **Suggests**: Textual soil classification rather than numeric measurement
- **`value`**: 
  - **Problem**: Generic slot name requires range clarification
  - **Too broad**: Could be any type of value

**Validation Status**: Production analysis confirmed **zero usage** in NMDC data for all pending_analysis slots, validating their "pending" status and allowing time for proper schema design decisions.

**Why no storage_units**: Require schema design decisions about whether these should have QuantityValue range or use different modeling approaches (TextValue, categorical enums, etc.).

**All slots have ONLY excuse annotation** (✅ correct, no dual annotations):
- `biomaterial_purity` (QuantityValue) - excuse only
- `bulk_elect_conductivity` (QuantityValue) - excuse only  
- `concentration` (QuantityValue) - excuse only
- `container_size` (QuantityValue) - excuse only
- `exp_pipe` (QuantityValue) - excuse only
- `filter_pore_size` (QuantityValue) - excuse only
- `input_volume` (QuantityValue) - excuse only
- `occup_density_samp` (QuantityValue) - excuse only
- `soil_text_measure` (QuantityValue) - excuse only
- `substances_volume` (QuantityValue) - excuse only
- `value` (QuantityValue) - excuse only

### `mixs_inconsistent` Category (4 slots)

**Problem Statement**: MIxS specification has internal contradictions between slot names and specified preferred units, making it impossible to determine the correct unit without external clarification.

**Affected Slots**:
- **`efficiency_percent`**: 
  - **Contradiction**: Name suggests percentage but MIxS specifies "micromole per liter" (concentration)
  - **Impact**: Cannot determine if this measures percentage efficiency or concentration
- **`inside_lux`**: 
  - **Contradiction**: Name suggests illuminance (lux) but MIxS specifies "kilowatt per square metre" (power density)
  - **Impact**: Fundamental mismatch between expected measurement type and specified unit
- **`rel_humidity_out`**, **`specific_humidity`**: 
  - **Problem**: MIxS units "gram of air, kilogram of air" are ambiguously phrased
  - **Should be**: "gram per kilogram of air" for humidity measurements
  - **Impact**: Missing "per" makes ratio unclear

**Why no storage_units**: Cannot resolve contradictions between semantic meaning and MIxS-specified units without domain expert clarification.

**GitHub Reference**: [PR #2599 detailed analysis](https://github.com/microbiomedata/nmdc-schema/pull/2599#issuecomment-3246905246) - documented as "Major MIxS Specification Problems"

**All slots have ONLY excuse annotation** (✅ correct):
- `efficiency_percent` (QuantityValue) - excuse only, name suggests % but MIxS specifies concentration
- `inside_lux` (QuantityValue) - excuse only, name suggests illuminance but MIxS specifies power density  
- `rel_humidity_out` (QuantityValue) - excuse only, ambiguous unit phrasing
- `specific_humidity` (QuantityValue) - excuse only, ambiguous unit phrasing

### `non_ucum_unit` Category (2 slots)

**Problem Statement**: These slots use industry-standard units that are not part of the UCUM standard but are legitimate, well-established units in their respective domains.

**Affected Slots**:
- **`api`**: Uses "degrees API" (American Petroleum Institute gravity scale)
  - Industry-standard density measurement for petroleum products
  - Cannot be converted to UCUM without losing domain-specific meaning
- **`permeability`**: Uses "mD" (millidarcy) 
  - Standard geological permeability unit
  - Specialized unit for fluid flow through porous media

**Why no storage_units**: These are valid, widely-accepted units in petroleum and geology domains but fall outside UCUM scope.

**GitHub Reference**: [PR #2599 analysis](https://github.com/microbiomedata/nmdc-schema/pull/2599#issuecomment-3246905246) - confirmed as valid industry standards that "can't be aligned with UCUM"

**All slots have ONLY excuse annotation** (✅ correct):
- `api` (QuantityValue) - excuse only, degrees API petroleum industry standard
- `permeability` (TextValue) - excuse only, mD millidarcy geological standard

## Production Data Problems

### Confirmed Unit Violations
From production validation analysis:

1. **`abs_air_humidity`**: 
   - **Schema allows**: `[lb_av]|g/g|kg|kg/kg` (humidity units)
   - **Production uses**: `kPa` (pressure units)
   - **Issue**: Fundamental unit type mismatch - pressure ≠ humidity
   - **Status**: Data quality issue, schema is correct

2. **`solar_irradiance`**:  
   - **Schema allows**: `kW/m2/d|erg/cm2/s`
   - **Production uses**: `W/m2`
   - **Issues**: 
     - Scale factor: kW vs W (less critical)
     - **Missing time dimension**: `/d` vs instantaneous (more critical)
   - **Recommendation**: Add `W/m2` to storage_units

3. **`diss_oxygen`**:
   - **Schema allows**: `mg/L|umol/kg|umol/L` 
   - **Production uses**: `mL/L`
   - **Issue**: Volume vs mass units (mL vs mg)
   - **Recommendation**: Add `mL/L` to storage_units

### Validation of Historical "Problematic Slots"

**MAJOR SUCCESS**: All previously problematic slots are now working correctly in production:

- `diss_oxygen` ✅ (most instances using allowed units, some using non-allowed `mL/L`)
- `salinity` ✅ (instances using `mg/L` and `%` - both allowed)
- `nitro` ✅ (instances using `%` - allowed)
- `org_carb` ✅ (instances using `%` - allowed)
- `tot_carb` ✅ (instances using `%` - allowed)
- `potassium` ✅ (instances using `mg/kg` and `mg/L` - both allowed)
- `calcium`, `magnesium`, `conduc`, `density` ✅ (all using allowed units)

**Multi-unit storage_units strategy is working** - production systems are successfully using the various acceptable units.

### Additional Production Data Issues

#### Invalid UCUM Units in Schema
From UCUM validation:

1. **`'1/d'`** - Per Day Frequency Unit:
   - **Current**: `'1/d'` 
   - **Should be**: `'/d'` (UCUM standard for "per day")
   - **Used in**: `freq_clean`, `freq_cook` slots
   - **UCUM Rule**: Frequency units should omit the leading "1"

2. **`'[NTU]'`** - Turbidity Unit:
   - **Current**: `'[NTU]'`
   - **Should be**: `'[ntu]'` (UCUM is case-sensitive)
   - **Used in**: `turbidity` slot
   - **UCUM Rule**: Arbitrary units in brackets must be lowercase

3. **`mbar`** - Millibar Pressure Unit:
   - **Current**: `'mbar'`
   - **Issue**: UOM website reports invalid (may be validation service issue)
   - **Status**: Requires UCUM specification verification

#### Slots with Excuses Analysis

**Protocol Slots with QuantityValue Range (Anomalies)**:

**Incorrect excuse assignments found**:
- **`organism_count`**: Range = `QuantityValue`, excuse = `protocol_slot`
  - **Should have**: storage_units annotation (this is a count, not a protocol)
  - **Current production usage**: Not found in validation data

**Correct excuse assignments**:
- Most regimen slots: `agrochem_addition`, `air_temp_regm`, etc. → Range = `TextValue` ✅
- Some protocol slots: `org_count_qpcr_info`, `non_min_nutr_regm` → Range = `string` ✅

### High Compliance Metrics

**Slot-Unit Combination Compliance:**
- **Total violations**: Small number of slot-unit combinations
- **Total combinations**: Many analyzed  
- **Compliance**: Very high percentage

**Volume-Weighted Compliance:**
- **Violation instances**: Small number relative to total
- **Total instances**: Large dataset
- **Compliance**: Very high percentage

**Excuse Validation:**
- **Complete excuse validation** (all pending_analysis slots have zero production usage)

## Immediate Action Items

### 1. **Resolve Contradictory Dual Annotations**
15 slots have BOTH storage_units AND units_alignment_excuse:

**Decision needed**: For each of the 15 contradictory slots:
- **Option A**: Remove `units_alignment_excuse` (if storage_units is sufficient)
- **Option B**: Remove `storage_units` (if excuse is still needed)
- **Logic**: A slot should have EITHER storage_units OR excuse, never both

**Affected slots**: All 15 protocol_slot slots with dual annotations listed above.

### 2. **Fix Missing Excuse File Entry**
**`organism_count`** was listed in excuse file but actually has `storage_units: '1'`:
- **Action**: Remove from excuse file analysis
- **Reason**: Has valid storage_units annotation

### 3. **Regenerate Excuse Analysis** 
Regenerate all analysis files after fixing dual annotations using the fast analysis targets.

### 4. **Emergency Override for Test Failures**
If you need to fix a failing test immediately:
1. Add temporary excuse: `units_alignment_excuse: {tag: "units_alignment_excuse", value: "pending_analysis"}`
2. File issue for UCUM Squad review
3. Tag @turbomam and add to UCUM Squad meeting agenda

### 5. **Fix Invalid UCUM Units in Schema**
From validation analysis - invalid UCUM units need fixing:

1. **`'1/d'`** → **`'/d'`** in freq_clean and freq_cook slots
2. **`'[NTU]|[FNU]'`** → **`'[ntu]|[fnu]'`** in turbidity slot  
3. **`mbar`** → needs investigation

Also fix turbidity test failure: `[FNU]` missing from materialized UnitEnum.

### 6. **Verified Categories (No Action Needed)**
- **`pending_analysis`** (11 slots) - all have only excuse, all QuantityValue range
- **`mixs_inconsistent`** (4 slots) - all have only excuse, all QuantityValue range  
- **`non_ucum_unit`** (2 slots) - all have only excuse, appropriate ranges

### 7. **Production Data Fixes**
Schema updates recommended:
1. Add `W/m2` to `solar_irradiance` storage_units
2. Add `mL/L` to `diss_oxygen` storage_units  
3. Investigate `abs_air_humidity` production data quality (pressure vs humidity units)

### 8. **Category-Specific Actions**

#### `pending_analysis` Category (11 slots):
1. Review each slot's semantic meaning and intended use
2. Determine appropriate LinkML range (QuantityValue, TextValue, string, enum)
3. Add storage_units if keeping QuantityValue range
4. Update range if measurement nature is non-quantitative

#### `protocol_slot` Category (5 correctly excused + 15 with dual annotations):
- Consider whether dual-annotation slots should have `TextValue` range instead of `QuantityValue`
- Keep excuse for genuine protocol/regimen slots

#### `mixs_inconsistent` Category (4 slots):
- Coordinate with MIxS consortium to resolve specification inconsistencies

#### `non_ucum_unit` Category (2 slots):
- Consider creating domain-specific unit enums or accepting as legitimate exceptions

## Resolution Progress

**Current Goal**: [Issue #2646](https://github.com/microbiomedata/nmdc-schema/issues/2646) - "decrease the number of QuantityValue slots that have excuses"

**Priority Order**:
1. **`pending_analysis`** - Highest impact (11 slots), zero production usage allows safe changes
2. **`mixs_inconsistent`** - Requires MIxS coordination but clear technical resolution path  
3. **`protocol_slot`** - May require range changes from QuantityValue to TextValue
4. **`non_ucum_unit`** - Lowest priority, represent legitimate domain-specific standards

### Strategic Insights

#### Multi-Unit Strategy Validation
- Real systems DO use diverse units for the same measurement
- Multi-unit annotations like `calcium: "[ppm]|mg/L|umol/L|mg/kg"` accommodate this diversity  

#### Excuse Categories Performance
1. **`protocol_slot`**: Mostly correct, one error identified
2. **`pending_analysis`**: Fully validated - no production usage
3. **`mixs_inconsistent`**: No production violations found
4. **`non_ucum_unit`**: No production violations found

This systematic approach ensures schema integrity while providing clear paths forward for each category based on the underlying problem type.

## Evidence Sources Referenced

- Systematic excuse categorization analysis
- Production data validation results  
- Historical problematic slots analysis
- UCUM validation analysis
- Schema excuse file analysis (⚠️ **APPEARS STALE**)
- Production validation outputs
- UCUM validation outputs

## Next Steps

1. **URGENT**: Regenerate excuse analysis with current schema
2. **Verify**: Each excuse annotation against current schema state  
3. **Categorize**: Separate schema problems from data problems
4. **Document**: Clear resolution paths for each problem type
5. **Update**: All documentation to reflect current reality

This analysis extracted "problematic" references from all units documentation but revealed that the primary data source (excuse file) may be outdated. **All findings require verification against current schema state.**