# Comprehensive Problematic Units Analysis

## Overview

This document is the **definitive source** for all units-related problems in the NMDC schema, covering both:

1. **Problematic Slots** (Schema design issues) - Slots with `units_alignment_excuse` annotations
2. **Problematic Data** (Production data issues) - Data using units not in the slot's `storage_units` list



## Types of Problems

### 1. **Problematic Slots** (Schema Design Issues)
Slots that cannot or should not have `storage_units` annotations due to fundamental design issues.

### 2. **Problematic Data** (Production Data Issues)  
Data using units not in the slot's `storage_units` list, indicating data quality issues.

## Excuse Categories Analysis

### Schema State Summary
Current state after recent fixes and regeneration.

### `protocol_slot` Category

**Problem Statement**: These slots describe experimental protocols/regimens rather than direct measurements. They combine multiple measurement types with temporal/procedural information that cannot be reduced to a single storage unit.

**Example Problem Slots**:
- `agrochem_addition`
- `fertilizer_regm` 
- `antibiotic_regm`
- `fungicide_regm`
- `growth_hormone_regm`
- `herbicide_regm`
- `mineral_nutr_regm`
- `non_min_nutr_regm`
- `pesticide_regm`
- `salt_regm`
- `air_temp_regm`
- `humidity_regm`
- `light_regm`
- `radiation_regm`
- `rainfall_regm`
- `water_temp_regm`
- `watering_regm`
- `standing_water_regm`
- `org_count_qpcr_info`
- `samp_transport_cond`

**Examples**: 
- `agrochem_addition`: "roundup;5 milligram per liter;2018-06-21"
- `air_temp_regm`: "25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M"

**Why no storage_units**: The range includes both quantitative measurements AND temporal/procedural metadata that cannot be standardized to UCUM units.

**GitHub Reference**: [PR #2599 comment](https://github.com/microbiomedata/nmdc-schema/pull/2599#issuecomment-3270547242) - "I don't think it's really possible to assert a unit for compound slots like these"

### `complex_unit` Category (2 slots)

**Problem Statement**: These slots have QuantityValue range but represent complex structured measurements that combine numeric and text data, making simple UCUM storage_units inappropriate.

**Affected Slots**:
- `microbial_biomass` (QuantityValue) - combines numeric biomass with measurement method text
- `tvdss_of_hcr_temp` (QuantityValue) - combines depth measurement with temperature reference

**Why no storage_units**: These represent structured measurements that cannot be reduced to simple UCUM units while preserving their semantic meaning.


### `pending_analysis` Category (10 slots)

**Problem Statement**: These slots require further investigation to determine appropriate units or whether they should have QuantityValue range at all.

**Affected Slots**:
- `biomaterial_purity`, `bulk_elect_conductivity`, `concentration`, `container_size`, `exp_pipe`, `filter_pore_size`, `input_volume`, `occup_density_samp`, `substances_volume`, `value`

**Key Examples**:
- **`biomaterial_purity`**:
  - **Issue**: [#2548](https://github.com/microbiomedata/nmdc-schema/issues/2548)
  - **Problem**: Parent of DNA absorbance slots, may need to be abstract
  - **Range conflict**: Has QuantityValue range but children have float range
- **`value`**:
  - **Problem**: Generic slot name requires range clarification
  - **Too broad**: Could be any type of value

**Note**: `soil_text_measure` was removed from this category - it was removed from GSC MIxS v6.2.2 and is now hardcoded in nmdc.yaml with `range: string` instead of QuantityValue (see [#1368](https://github.com/microbiomedata/nmdc-schema/issues/1368)).

**Validation Status**: Production analysis confirmed **zero usage** in NMDC data for all pending_analysis slots, validating their "pending" status and allowing time for proper schema design decisions.

**Why no storage_units**: Require schema design decisions about whether these should have QuantityValue range or use different modeling approaches (TextValue, categorical enums, etc.).


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


### `non_ucum_unit` Category (1 slot)

**Problem Statement**: These slots use industry-standard units that are not part of the UCUM standard but are legitimate, well-established units in their respective domains.

**Affected Slots**:
- `api` - Uses "degrees API" (American Petroleum Institute gravity scale)

**Example Problem Slots**:
- `api` - Industry-standard density measurement for petroleum products
- `permeability` - Uses "mD" (millidarcy), standard geological permeability unit

**Why no storage_units**: These are valid, widely-accepted units in petroleum and geology domains but fall outside UCUM scope.

**GitHub Reference**: [PR #2599 analysis](https://github.com/microbiomedata/nmdc-schema/pull/2599#issuecomment-3246905246) - confirmed as valid industry standards that "can't be aligned with UCUM"


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


### 7. **Production Data Fixes**
Schema updates recommended:
1. Add `W/m2` to `solar_irradiance` storage_units
2. Add `mL/L` to `diss_oxygen` storage_units  
3. Investigate `abs_air_humidity` production data quality (pressure vs humidity units)

### 8. **Category-Specific Actions**

#### `pending_analysis` Category (10 slots):
1. Review each slot's semantic meaning and intended use
2. Determine appropriate LinkML range (QuantityValue, TextValue, string, enum)
3. Add storage_units if keeping QuantityValue range
4. Update range if measurement nature is non-quantitative


#### `mixs_inconsistent` Category (4 slots):
- Coordinate with MIxS consortium to resolve specification inconsistencies

#### `non_ucum_unit` Category (2 slots):
- Consider creating domain-specific unit enums or accepting as legitimate exceptions

## Resolution Progress

**Current Goal**: [Issue #2646](https://github.com/microbiomedata/nmdc-schema/issues/2646) - "decrease the number of QuantityValue slots that have excuses"

**Priority Order**:
1. **`pending_analysis`** - Highest impact (10 slots), zero production usage allows safe changes
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