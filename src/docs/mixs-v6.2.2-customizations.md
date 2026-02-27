# MIxS v6.2.2 NMDC Customizations

This document describes the migration of NMDC schema's MIxS import from the old `pre-2024-05-15` tag to GSC MIxS release `v6.2.2` (commit `1243e22a7565f36f0955cb9c6806e80efe41cc28`).

## Overview

The migration maintains backward compatibility with existing NMDC MongoDB data while adopting the latest GSC MIxS standard. This is achieved through yq transformations in `assets/yq-for-mixs-customizations.txt` that modify the imported MIxS schema.

**Source Repository:**
- **Repository**: `GenomicsStandardsConsortium/mixs` (official GSC MIxS)
- **Release**: `v6.2.2`
- **Commit**: `1243e22a7565f36f0955cb9c6806e80efe41cc28`
- **URL**: `https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/v6.2.2/src/mixs/schema/mixs.yaml`

**Validation:** After migration, all 13,847 production biosamples validate successfully against the updated schema.

## Slot and Enum Inventory Changes

This section summarizes all inventory differences between main branch (old NMDC MIxS fork) and this branch (GSC MIxS v6.2.2).

### Summary

| Metric | Main Branch | This Branch | Change |
|--------|-------------|-------------|--------|
| Slots in mixs.yaml | 489 | 486 | -3 (moved to hardcoded) |
| Enums in mixs.yaml | 102 | 93 | -24 dropped, +15 added |
| Slots explicitly set to string | 22 | 31 | +10 added, -1 removed |

### Slot Changes

#### Slots No Longer Imported, Hardcoded Instead (3 slots)

These slots were removed from GSC MIxS v6.2.2 and cannot be imported. They are hardcoded in `src/schema/nmdc.yaml` for backward compatibility with `submission-schema`:

| Slot | Range | Production Data | Why Retained |
|------|-------|-----------------|--------------|
| `host_family_relation` | `string` (multivalued) | None | `submission-schema` compatibility |
| `salinity_meth` | `string` with `structured_pattern` | None | `submission-schema` compatibility |
| `soil_text_measure` | `string` | None | `submission-schema` compatibility |

#### Slots Imported and Renamed for MongoDB Compatibility (2 slots)

These slots are imported from GSC MIxS v6.2.2 but renamed by yq to stay compliant with existing MongoDB data:

| GSC MIxS v6.2.2 Name | NMDC Name After Rename | Reason |
|---------------------|------------------------|--------|
| `samp_collect_device` | `samp_collec_device` | MongoDB uses `samp_collec_device` |
| `samp_collect_method` | `samp_collec_method` | MongoDB uses `samp_collec_method` |

Structured aliases are added to document the GSC canonical names.

#### Slots Changed from TextValue to String (10 slots)

These slots had explicit `range: string` in both the old fork and GSC v6.2.2, but the old yq did not override them, so they were converted to TextValue. The new yq explicitly keeps them as string:

| Slot | Has `structured_pattern` | Reason for Change |
|------|-------------------------|-------------------|
| `al_sat_meth` | Yes | Enable pattern validation |
| `alkalinity_method` | No | Consistency with other method slots |
| `biocide_admin_method` | No | Prevent future conversion |
| `cur_vegetation_meth` | Yes | Enable pattern validation |
| `heavy_metals_meth` | Yes | Enable pattern validation |
| `horizon_meth` | Yes | Enable pattern validation |
| `local_class_meth` | Yes | Enable pattern validation |
| `samp_sort_meth` | No | Consistency with other method slots |
| `seq_meth` | Yes | Enable pattern validation |
| `tot_org_c_meth` | Yes | Enable pattern validation |

**Impact:** If production MongoDB has TextValue objects (`{type: "nmdc:TextValue", has_raw_value: ...}`) for any of these slots, a data migration will be required. Check MongoDB before deploying.

### Enum Changes

#### Enums Dropped (accepted removal) (24 enums)

These enums existed in main branch but are not in GSC MIxS v6.2.2:

`ceil_cond_enum`, `ceil_texture_enum`, `door_cond_enum`, `door_loc_enum`, `door_type_wood_enum`, `ext_wall_orient_enum`, `ext_window_orient_enum`, `floor_cond_enum`, `floor_finish_mat_enum`, `hcr_geol_age_enum`, `heat_deliv_loc_enum`, `int_wall_cond_enum`, `organism_count_enum`, `plant_growth_med_enum`, `room_type_enum`, `samp_floor_enum`, `samp_md_enum`, `shading_device_cond_enum`, `sr_geol_age_enum`, `vis_media_enum`, `wall_loc_enum`, `wall_texture_enum`, `window_cond_enum`, `window_loc_enum`

#### Enums Added in GSC MIxS v6.2.2 (15 enums)

`AeroStrucEnum`, `BuiltStrucSetEnum`, `CeilingWallTextureEnum`, `CeilStrucEnum`, `DamagedEnum`, `DamagedRupturedEnum`, `FireplaceTypeEnum`, `GeolAgeEnum`, `HeatSysDelivMethEnum`, `MoldVisibilityEnum`, `SeasonEnum`, `SeqQualityCheckEnum`, `ShadingDeviceLocEnum`, `SpaceTypStateEnum`, `WindowStatusEnum`

#### Enums Renamed for Consistency (1 enum)

GSC MIxS v6.2.2 uses `host_sex_enum` (snake_case). NMDC renames it to `HostSexEnum` for consistency with other GSC v6.2.2 enums (PascalCase).

#### Enums Customized

| Enum | Customization |
|------|---------------|
| `HostSexEnum` | Permissible values replaced with: `female`, `male`, `hermaphrodite`, `non-binary`, `transgender`, `transgender (female to male)`, `transgender (male to female)`, `undeclared` |
| `CurLandUseEnum` | NMDC-defined enum in `assets/other_mixs_yaml_files/CurLandUseEnum.yaml` with restructured permissible values including examples and annotations |
| `SoilHorizonEnum` | Added `M horizon` (not in GSC MIxS v6.2.2) |

## Required Customizations

This section documents how NMDC handles differences between GSC MIxS v6.2.2 and NMDC requirements.

### QuantityValue Range Overrides (158 slots)

GSC MIxS v6.2.2 changed ~158 measurement slots from `quantity value` to `string` range. NMDC maintains `QuantityValue` range because:

- Production data uses QuantityValue objects (`{type: "nmdc:QuantityValue", has_numeric_value: ..., has_unit: ...}`)
- QuantityValue provides better structure than pattern-matched strings
- Enables numeric queries and unit validation

**Affected slots include**: `abs_air_humidity`, `air_temp`, `al_sat`, `alkalinity`, `alt`, `ammonium`, `depth`, `temp`, `salinity`, and 149 others.

### Required Field Deletions (30 slots)

GSC MIxS v6.2.2 made 35 slots required. NMDC deletes `required: true` from 30 slots because existing biosamples don't have these fields:

`abs_air_humidity`, `add_recov_method`, `api`, `basin`, `build_occup_type`, `building_setting`, `collection_date`, `env_broad_scale`, `env_local_scale`, `env_medium`, `filter_type`, `geo_loc_name`, `hc_produced`, `hcr`, `heat_cool_type`, `indoor_space`, `iwf`, `lat_lon`, `light_type`, `occup_density_samp`, `occup_samp`, `rel_air_humidity`, `samp_collect_point`, `samp_name`, `samp_taxon_id`, `samp_type`, `seq_meth`, `space_typ_state`, `typ_occup_density`, `water_cut`

The 5 required slots we DO NOT override (`IFSAC_category`, `coll_site_geo_feat`, `host_dependence`, `project_name`, `sym_life_cycle_type`) are for specialized environmental packages that NMDC doesn't use.

### Multivalued Overrides (5 slots)

GSC changed these slots to `multivalued: true`, but NMDC has single values:

| Slot | Reason |
|------|--------|
| `biotic_regm` | NMDC has single TextValue objects |
| `experimental_factor` | NMDC has single ControlledTermValue objects |
| `solar_irradiance` | NMDC has single QuantityValue objects |
| `source_mat_id` | NMDC has single TextValue objects |
| `ventilation_type` | NMDC has single TextValue objects |

### Slots Kept as String Range (31 slots)

The yq pipeline sets explicit `range: string` for 31 slots. Without this, slots with explicit `range: string` in GSC MIxS would be converted to TextValue by the range transformation rules.

| Category | Count | Slots |
|----------|-------|-------|
| Slots with `structured_pattern` | 13 | `al_sat_meth`, `cur_vegetation_meth`, `heavy_metals_meth`, `horizon_meth`, `local_class_meth`, `micro_biomass_meth`, `prev_land_use_meth`, `seq_meth`, `soil_texture_meth`, `tot_nitro_cont_meth`, `tot_org_c_meth`, `water_cont_soil_meth`, `water_content` |
| GSC datetime → NMDC string | 3 | `extreme_event`, `fire`, `flooding` |
| GSC enum → NMDC string | 2 | `heat_sys_deliv_meth`, `shad_dev_water_mold` |
| GSC default_range → explicit string | 7 | `biocide_admin_method`, `chem_treat_method`, `host_subspecf_genlin`, `org_count_qpcr_info`, `pres_animal_insect`, `samp_collec_device`, `samp_collec_method` |
| Other string slots | 6 | `alkalinity_method`, `host_symbiont`, `non_min_nutr_regm`, `room_architec_elem`, `samp_name`, `samp_sort_meth` |

**Note:** `structured_pattern` is deleted from 6 slots due to non-conforming production data (see [Non-Conforming Production Data](#non-conforming-production-data)).

**Exception:** `ph_meth` and `soil_type_meth` are kept as TextValue because production data uses TextValue objects. See [#2774](https://github.com/microbiomedata/nmdc-schema/issues/2774).

### TextValue Range for Enum Slots (6 slots)

GSC MIxS v6.2.2 changed these slots to enum ranges, but NMDC has TextValue objects:

| Slot | GSC Range |
|------|-----------|
| `crop_rotation` | `CropRotationEnum` |
| `cult_root_med` | `CultRootMedEnum` |
| `gravidity` | `GravidityEnum` |
| `perturbation` | `PerturbationEnum` |
| `soil_type` | `FaoClassEnum` |
| `store_cond` | `StoreCondEnum` |

## Technical Reference

### Range Transformation Pipeline

The yq transformation pipeline in `assets/yq-for-mixs-customizations.txt` processes MIxS slots as follows:

1. **Slots with explicit `range: string`** in GSC MIxS:
   - Default behavior: Converted to `TextValue` or `QuantityValue` (based on slot semantics)
   - Override behavior: If explicitly set to `range: string` in yq, remains as string

2. **Slots with implicit string** (no `range` declared, inheriting from `default_range: string`):
   - These are **NOT transformed** - they remain as string
   - The yq pipeline only matches slots with explicit range declarations

This distinction is critical: the 21 slots in NMDC's derived mixs.yaml that have implicit string range were never transformed because they lacked explicit `range` declarations in the source.

### GSC MIxS v6.2.2 Slot Range Statistics

GSC MIxS v6.2.2 defines 1,059 slots with the following range distribution:

| Range Type | Count | Notes |
|------------|-------|-------|
| string (explicit) | 385 | Slots with `range: string` declared |
| string (implicit) | 177 | Slots inheriting from `default_range: string` |
| **string (total)** | **562** | 53% of all slots |
| integer | 21 | |
| float | 19 | |
| datetime | 17 | |
| boolean | 6 | |
| enums | 147 | 127 distinct enum types |
| classes | 287 | Combination classes (MigsBa*, MigsEu*, etc.) |

**Note:** The 177 slots without explicit range declarations rely on `default_range: string`. See [GenomicsStandardsConsortium/mixs#1091](https://github.com/GenomicsStandardsConsortium/mixs/issues/1091) and [linkml/linkml discussion #3043](https://github.com/orgs/linkml/discussions/3043).

### NMDC-Derived mixs.yaml Slot Range Statistics

After NMDC's yq transformations, the derived `src/schema/mixs.yaml` contains 487 slots:

| Range Type | Count | Notes |
|------------|-------|-------|
| QuantityValue | 166 | Measurement slots (GSC `string` → NMDC `QuantityValue`) |
| TextValue | 137 | Free-text slots (GSC `string` → NMDC `TextValue`) |
| string (explicit) | 31 | Slots with explicit `range: string` |
| string (implicit) | 21 | Slots inheriting from `default_range: string` |
| **string (total)** | **52** | 11% of all slots |
| enums | 104 | 94 distinct enum types |
| ControlledTermValue | 9 | Ontology-backed slots |
| ControlledIdentifiedTermValue | 6 | Ontology slots with identifiers |
| TimestampValue | 5 | Date/time slots |
| GeolocationValue | 1 | `lat_lon` slot |
| PropertyAssertion | 1 | `env_package` slot |

### Settings for Pattern Interpolation

MIxS `structured_pattern` syntax uses placeholders like `{scientific_float}`, `{text}`, `{URL}` that require settings for interpolation. These settings are defined in `src/schema/nmdc.yaml` (not imported from MIxS) because:

1. The `sheets-and-friends` `do_shuttle` tool does not import settings from source schemas
2. The MIxS import pipeline explicitly deletes settings

When updating MIxS imports, these settings must be manually synced if the source changes.

### Non-Conforming Production Data

Some production data doesn't match GSC patterns. We handle this by using TextValue/QuantityValue ranges or deleting structured patterns:

| Slot | Issue | Resolution |
|------|-------|------------|
| `agrochem_addition` | Data is "Fertilized" instead of `{name};{amount} {unit};{timestamp}` | TextValue range |
| `store_cond` | Data is "frozen" instead of `{type};{duration}` | TextValue range |
| `micro_biomass_meth` | Data is "Chloroform fumigation direct extraction" | Delete `structured_pattern` |
| `samp_collec_method` | Data is "Seawater", "Kit 1", "Kit 2" | Delete `structured_pattern` |
| `soil_texture_meth` | Data is "Textural Analysis Test (hydrometer)" | Delete `structured_pattern` |
| `soil_type_meth` | Data is "Textural Analysis Test (hydrometer)" | Delete `structured_pattern` |
| `ph_meth` | Data is "measured in 1:1 w/vol slurry (10.2136/...)" | Delete `structured_pattern` |
| `water_cont_soil_meth` | Data is "volumetric soil water content; ..." | Delete `structured_pattern` |

## Future Work

### TextValue to Enum Migrations

The following slots have TextValue data that should eventually be migrated to enum values:

| Slot | Target Enum |
|------|-------------|
| `crop_rotation` | `CropRotationEnum` |
| `cult_root_med` | `CultRootMedEnum` |
| `gravidity` | `GravidityEnum` |
| `perturbation` | `PerturbationEnum` |
| `soil_type` | `FaoClassEnum` |
| `store_cond` | `StoreCondEnum` |

**Migration approach:**
1. Analyze existing `has_raw_value` data for each slot
2. Map values to appropriate enum permissible values
3. Create migration script to transform TextValue → enum string
4. Update yq to remove TextValue range override
5. Run migration on MongoDB

See [#2772](https://github.com/microbiomedata/nmdc-schema/issues/2772).

### Other Pending Migrations

- [#2774](https://github.com/microbiomedata/nmdc-schema/issues/2774) - Migrate `ph_meth` and `soil_type_meth` from TextValue to string

## Files Modified

- `project.Makefile` - Updated MIxS import URL and added documentation
- `assets/yq-for-mixs-customizations.txt` - All yq transformations
- `src/schema/nmdc.yaml` - Added MIxS settings for pattern interpolation and legacy slots
- `src/schema/core.yaml` - Removed retired slot references
- `src/data/valid/*.yaml` - Updated test data for new constraints

## Related Issues

- [#1368](https://github.com/microbiomedata/nmdc-schema/issues/1368) - Original MIxS migration tracking issue
- [#2772](https://github.com/microbiomedata/nmdc-schema/issues/2772) - TextValue to enum migration task
- [#2774](https://github.com/microbiomedata/nmdc-schema/issues/2774) - Migrate ph_meth and soil_type_meth from TextValue to string
- [#2777](https://github.com/microbiomedata/nmdc-schema/issues/2777) - 85 NMDC schema slots lack explicit range declarations
- [GenomicsStandardsConsortium/mixs#1091](https://github.com/GenomicsStandardsConsortium/mixs/issues/1091) - GSC MIxS slots without explicit range
- [linkml/linkml discussion #3043](https://github.com/orgs/linkml/discussions/3043) - Request for `--materialize-default-range` option
