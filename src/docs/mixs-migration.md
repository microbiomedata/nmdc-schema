# MIxS Migration Documentation

This document describes the migration of NMDC schema's MIxS import from the old `pre-2024-05-15` tag to `v6.2.0-nmdc.1`, which mirrors GSC MIxS commit `0368da846b197bef1c0dd27a9cf337a8aeea17f2`.

## Overview

The migration maintains backward compatibility with existing NMDC MongoDB data while adopting the latest GSC MIxS standard. This is achieved through yq transformations in `assets/yq-for-mixs_subset_modified.txt` that modify the imported MIxS schema.

## Source Repository

- **Repository**: `microbiomedata/mixs` (NMDC fork of GSC MIxS)
- **Tag**: `v6.2.0-nmdc.1`
- **GSC Commit**: `0368da846b197bef1c0dd27a9cf337a8aeea17f2`
- **URL**: `https://raw.githubusercontent.com/microbiomedata/mixs/v6.2.0-nmdc.1/src/mixs/schema/mixs.yaml`

## Required Customizations

### 1. Slot Renames (2 slots)

GSC renamed these slots, but NMDC MongoDB uses the old names:

| NMDC Name | GSC Name |
|-----------|----------|
| `samp_collec_device` | `samp_collect_device` |
| `samp_collec_method` | `samp_collect_method` |

Structured aliases are added to document the GSC canonical names.

### 2. QuantityValue Range Overrides (158 slots)

GSC MIxS commit `0368da8` changed ~158 measurement slots from `quantity value` to `string` range. NMDC maintains `QuantityValue` range because:

- Production data uses QuantityValue objects (`{type: "nmdc:QuantityValue", has_numeric_value: ..., has_unit: ...}`)
- QuantityValue provides better structure than pattern-matched strings
- Enables numeric queries and unit validation

**Affected slots include**: `abs_air_humidity`, `air_temp`, `al_sat`, `alkalinity`, `alt`, `ammonium`, `depth`, `temp`, `salinity`, and 149 others.

### 3. Required Field Deletions (30 slots)

GSC MIxS commit `0368da8` made 35 slots required. NMDC deletes `required: true` from 30 slots because existing biosamples don't have these fields:

`abs_air_humidity`, `add_recov_method`, `api`, `basin`, `build_occup_type`, `building_setting`, `collection_date`, `env_broad_scale`, `env_local_scale`, `env_medium`, `filter_type`, `geo_loc_name`, `hc_produced`, `hcr`, `heat_cool_type`, `indoor_space`, `iwf`, `lat_lon`, `light_type`, `occup_density_samp`, `occup_samp`, `rel_air_humidity`, `samp_collect_point`, `samp_name`, `samp_taxon_id`, `samp_type`, `seq_meth`, `space_typ_state`, `typ_occup_density`, `water_cut`

The 5 required slots we DO NOT override (`IFSAC_category`, `coll_site_geo_feat`, `host_dependence`, `project_name`, `sym_life_cycle_type`) are for specialized environmental packages that NMDC doesn't use.

### 4. Multivalued Overrides (5 slots)

GSC changed these slots to `multivalued: true`, but NMDC has single values:

| Slot | Reason |
|------|--------|
| `biotic_regm` | NMDC has single TextValue objects |
| `experimental_factor` | NMDC has single ControlledTermValue objects |
| `solar_irradiance` | NMDC has single QuantityValue objects |
| `source_mat_id` | NMDC has single TextValue objects |
| `ventilation_type` | NMDC has single TextValue objects |

### 5. Structured Pattern Deletions (7 slots)

GSC MIxS commit `0368da8` has `structured_pattern: ^{PMID}|{DOI}|{URL}$` on method slots, but NMDC production data contains free-text values:

| Slot | Sample Data | Count |
|------|-------------|-------|
| `micro_biomass_meth` | "Chloroform fumigation direct extraction" | varies |
| `samp_collec_method` | "Seawater", "Kit 1", "Kit 2" | varies |
| `soil_texture_meth` | "Textural Analysis Test (hydrometer)" | 30 |
| `soil_type_meth` | "Textural Analysis Test (hydrometer)" | 30 |
| `ph_meth` | "measured in 1:1 w/vol slurry (10.2136/...)" | 250 |
| `water_cont_soil_meth` | "volumetric soil water content; ..." | varies |

### 6. TextValue Range for Enum Slots (6 slots)

GSC MIxS commit `0368da8` changed these slots to enum ranges, but NMDC has TextValue objects:

| Slot | GSC Range | NMDC Data |
|------|-----------|-----------|
| `crop_rotation` | `CropRotationEnum` | TextValue objects |
| `cult_root_med` | `CultRootMedEnum` | TextValue objects |
| `gravidity` | `GravidityEnum` | TextValue objects |
| `perturbation` | `PerturbationEnum` | TextValue objects |
| `soil_type` | `FaoClassEnum` | TextValue objects |
| `store_cond` | `StoreCondEnum` | TextValue objects |

See [Future Migration: TextValue to Enum](#future-migration-textvalue-to-enum) for migration plan.

### 7. Enum Customizations

#### host_sex_enum

NMDC replaces GSC's `host_sex_enum` values with:
- `female`, `male`, `hermaphrodite`, `non-binary`, `transgender`, `transgender (female to male)`, `transgender (male to female)`, `undeclared`

#### SoilHorizonEnum

NMDC adds `M horizon` which is not in GSC MIxS commit `0368da8`.

## Settings for Pattern Interpolation

MIxS `structured_pattern` syntax uses placeholders like `{scientific_float}`, `{text}`, `{URL}` that require settings for interpolation. These settings are defined in `src/schema/nmdc.yaml` (not imported from MIxS) because:

1. The `sheets-and-friends` `do_shuttle` tool does not import settings from source schemas
2. The MIxS import pipeline explicitly deletes settings

When updating MIxS imports, these settings must be manually synced if the source changes.

## Slots with Non-Conforming Production Data

Some production data doesn't match GSC patterns but validates because we use TextValue/QuantityValue ranges:

| Slot | Pattern Expected | Actual Data | Count |
|------|------------------|-------------|-------|
| `agrochem_addition` | `{name};{amount} {unit};{timestamp}` | "Fertilized" | 2,676 |
| `store_cond` | `{type};{duration}` | "frozen" | 3,910 |

## Future Migration: TextValue to Enum

The following slots have TextValue data that should eventually be migrated to enum values:

- `crop_rotation` → `CropRotationEnum`
- `cult_root_med` → `CultRootMedEnum`
- `gravidity` → `GravidityEnum`
- `perturbation` → `PerturbationEnum`
- `soil_type` → `FaoClassEnum`
- `store_cond` → `StoreCondEnum`

**Migration approach**:
1. Analyze existing `has_raw_value` data for each slot
2. Map values to appropriate enum permissible values
3. Create migration script to transform TextValue → enum string
4. Update yq to remove TextValue range override
5. Run migration on MongoDB

## Validation Results

After migration, all 13,847 production biosamples validate successfully against the updated schema.

## Files Modified

- `project.Makefile` - Updated MIxS import URL and added documentation
- `assets/yq-for-mixs_subset_modified.txt` - All yq transformations
- `src/schema/nmdc.yaml` - Added MIxS settings for pattern interpolation
- `src/schema/core.yaml` - Removed retired slot references
- `src/data/valid/*.yaml` - Updated test data for new constraints

## Related Issues

- [#1368](https://github.com/microbiomedata/nmdc-schema/issues/1368) - Original MIxS migration tracking issue
