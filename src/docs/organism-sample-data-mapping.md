# OrganismSample Data Mapping Guide

This guide documents how to convert organism/isolate records from three
source systems into NMDC `OrganismSample` instances. Each source uses
different field names, value formats, and structural conventions.

See also:

- [OrganismSample class definition](https://microbiomedata.github.io/nmdc-schema/OrganismSample/)
- Example data files in `src/data/valid/OrganismSample-*.yaml`
- Subset definitions in `src/schema/nmdc_subsets.yaml` (`migs_ba`, `gold_organism`, `jgi_isolate`)

## General Principles

### Range wrapping

NMDC slots have typed ranges. Plain values from source systems must be
wrapped in the appropriate type:

| NMDC Range | YAML Pattern |
|---|---|
| `string` | `slot_name: "value"` |
| `integer` | `slot_name: 42` |
| `boolean` | `slot_name: true` |
| `float` | `slot_name: 3.14` |
| `TextValue` | `slot_name:` / `  type: nmdc:TextValue` / `  has_raw_value: "value"` |
| `QuantityValue` | `slot_name:` / `  type: nmdc:QuantityValue` / `  has_numeric_value: 30.0` / `  has_raw_value: "30 Cel"` / `  has_unit: Cel` |
| `ControlledIdentifiedTermValue` | `slot_name:` / `  type: nmdc:ControlledIdentifiedTermValue` / `  has_raw_value: "ENVO:00000015"` / `  term:` / `    id: ENVO:00000015` / `    type: nmdc:OntologyClass` |
| `TimestampValue` | `slot_name:` / `  type: nmdc:TimestampValue` / `  has_raw_value: "2015-05-08"` |
| `GeolocationValue` | `slot_name:` / `  type: nmdc:GeolocationValue` / `  has_raw_value: "30.27 N 30.10 E"` / `  latitude: 30.27` / `  longitude: 30.10` |

### Unit normalization (UCUM)

NMDC uses [UCUM](https://ucum.org/ucum) unit codes. Common conversions:

| Human-readable | UCUM code | Notes |
|---|---|---|
| degree Celsius | `Cel` | Not `°C` or `degree Celsius` |
| micrometer | `um` | Not `µm` or `micrometer` |
| milligram per liter | `mg/L` | |
| parts per million | `[ppm]` | Brackets required |
| pH | `[pH]` | Brackets required |
| meter | `m` | |
| centimeter | `cm` | |
| milliliter | `mL` | |
| microliter | `uL` | |
| percent | `%` | |
| atmosphere | `atm` | |
| watt per square meter | `W/m2` | |
| millimoles per liter | `mmol/L` | |
| millisiemens per centimeter | `mS/cm` | |

### Taxonomy CURIEs

Source systems store NCBI taxonomy IDs as plain integers. NMDC wraps them
as `ControlledIdentifiedTermValue` with a `NCBITaxon:` CURIE prefix:

- NCBI `taxonomy_id: 86665` → `NCBITaxon:86665`
- GOLD `ncbi_taxonomy_id: 247157` → `NCBITaxon:247157`

### Enum values

Enum permissible values are **space-separated words**, not snake_case.
Check the schema for exact values:

| Wrong | Correct | Enum |
|---|---|---|
| `free_living` | `free living` | `BioticRelationshipEnum` |
| `Mesophile` | `Mesophilic` | `TemperatureRangeEnum` |
| `wild_type` | `wild type` | `BiolStatEnum` |

### Boolean and yes/no conventions

NMDC uses three different patterns for true/false/unknown values:

| Pattern | Range | Values | When to use |
|---|---|---|---|
| `boolean` | `boolean` | `true`, `false` | Slots that are genuinely binary with no unknown state (e.g., `embargoed`, `lat_long_inferred`) |
| `YesNoEnum` | `YesNoEnum` | `yes`, `no` | Slots from the submission portal and JGI Isolate form (e.g., `dnase_treated`, `single_colony_isolation`). Defined in `portal_enums.yaml`. |
| `YesNoUnknownEnum` | `YesNoUnknownEnum` | `yes`, `no`, `unknown` | Slots from GOLD organism_v2 where the source data has a tri-state (e.g., `cultured`, `type_strain`). Defined in `organism_sample.yaml`. |

Source system conversions:

| Source | Source values | NMDC target |
|---|---|---|
| GOLD organism_v2 | `"Yes"` / `"No"` / `"Unknown"` (strings) | `yes` / `no` / `unknown` (`YesNoUnknownEnum`) |
| JGI Isolate v19 | `Y` / `N` | `yes` / `no` (`YesNoEnum`) |
| NCBI BioSample | varies | Use `boolean` or `YesNoEnum` as appropriate |

Do **not** use `boolean` for GOLD fields that can be `"Unknown"` — the
unknown state would be lost.

---

## Source 1: NCBI BioSample (MIGS.ba package)

### How to identify MIGS-Ba samples

NCBI BioSample `Package` field matches `MIGS.ba.*`. The package includes
the environmental package suffix (e.g., `MIGS.ba.soil.6.0`,
`MIGS.ba.water.6.0`, `MIGS.ba.host-associated.6.0`).

### Field mapping

NCBI attributes use `harmonized_name` when available, falling back to
`attribute_name`. Most map directly to NMDC MIxS slot names.

| NCBI attribute | NMDC slot | Range | Transformation |
|---|---|---|---|
| `Package.content` | *(not stored directly)* | — | Use to identify MIGS-Ba samples |
| `Organism.taxonomy_id` | `samp_taxon_id` | ControlledIdentifiedTermValue | Prefix with `NCBITaxon:` |
| `Organism.OrganismName` | `ncbi_taxonomy_name` | string | Direct |
| `sample_name` | `samp_name` | string | Direct |
| `collection_date` | `collection_date` | TimestampValue | Wrap |
| `geo_loc_name` | `geo_loc_name` | TextValue | Wrap |
| `lat_lon` | `lat_lon` | GeolocationValue | Parse "30.27 N 30.10 E" into lat/lon floats |
| `env_broad_scale` | `env_broad_scale` | ControlledIdentifiedTermValue | May need ENVO CURIE lookup |
| `env_local_scale` | `env_local_scale` | ControlledIdentifiedTermValue | May need ENVO CURIE lookup |
| `env_medium` | `env_medium` | ControlledIdentifiedTermValue | May need ENVO CURIE lookup |
| `isol_growth_condt` | `isol_growth_condt` | TextValue | Wrap |
| `num_replicons` | `num_replicons` | integer | Parse to int |
| `ref_biomaterial` | `ref_biomaterial` | TextValue | Wrap |
| `biotic_relationship` | `biotic_relationship` | BioticRelationshipEnum | Normalize case/spacing |
| `encoded_traits` | `encoded_traits` | TextValue | Wrap |
| `estimated_size` | `estimated_size` | string | Parse; NCBI may say "1M bp" → "1000000" |
| `pathogenicity` | `pathogenicity` | TextValue | Wrap |
| `rel_to_oxygen` | `rel_to_oxygen` | RelToOxygenEnum | Direct (values match) |
| `trophic_level` | `trophic_level` | TrophicLevelEnum | Direct |
| `subspecf_gen_lin` | `subspecf_gen_lin` | string | Direct |
| `oxy_stat_samp` | `oxy_stat_samp` | OxyStatSampEnum | Direct |
| `depth` | `depth` | QuantityValue | Parse value and unit |
| `temp` | `temp` | QuantityValue | Parse; convert unit to UCUM `Cel` |
| `samp_size` | `samp_size` | QuantityValue | Parse value and unit |
| `samp_collect_device` | `samp_collec_device` | string | Note NMDC name uses `collec` not `collect` |
| `samp_collect_method` | `samp_collec_method` | string | Note NMDC name uses `collec` not `collect` |
| `samp_mat_process` | `samp_mat_process` | ControlledTermValue | Wrap |
| `samp_vol_we_dna_ext` | `samp_vol_we_dna_ext` | QuantityValue | Parse value and unit |
| `samp_store_dur` | `samp_store_dur` | TextValue | Wrap |
| `samp_store_loc` | `samp_store_loc` | TextValue | Wrap |
| `samp_store_temp` | `samp_store_temp` | QuantityValue | Parse; convert unit to UCUM `Cel` |
| `source_material_id` | `source_mat_id` | TextValue | Wrap |
| `salinity` | `salinity` | QuantityValue | Parse value and unit; use UCUM `[ppm]` |
| `host_taxid` | `host_taxid` | ControlledIdentifiedTermValue | Prefix with `NCBITaxon:` |
| `strain` | *(use in `samp_name` or `subspecf_gen_lin`)* | — | No direct NMDC slot for strain alone |

### NCBI quirks

- **`env_broad_scale`, `env_local_scale`, `env_medium`**: NCBI stores these
  as free text (e.g., "salty lack"). NMDC requires ENVO ontology CURIEs.
  Human curation or automated ontology lookup is needed.
- **`missing` / `not collected` / `not applicable` / `not determined`**:
  NCBI uses these sentinel values. Omit these slots from NMDC rather than
  storing the sentinel.
- **`source_material_id`**: NCBI submitters often put extraction method here
  (e.g., "qiagen DNA isolation kit") rather than a culture collection ID.
  Validate before mapping.

### Data access

Local MongoDB: `ncbi_metadata.biosamples` collection. Filter with
`{"Package.content": /^MIGS\.ba/}`. Attributes are in
`Attributes.Attribute` array with `{harmonized_name, attribute_name, content}`.

---

## Source 2: GOLD organism_v2

### How to identify organism records

Every row in the `organism_v2` table is an organism record. Filter with
`cultured = 'Yes'` for cultured isolates. Note: boolean fields are stored
as strings (`"Yes"`, `"No"`, `"Unknown"`), not actual booleans.

### Field mapping

| GOLD column | NMDC slot | Range | Transformation |
|---|---|---|---|
| `organism_name` | `name` (on OrganismSample) | string | Direct |
| `genus` | `organism_genus` | string | Direct |
| `species` | `organism_species` | string | Direct |
| `strain` | *(use in `name` or `source_mat_id`)* | — | |
| `ncbi_taxonomy_id` | `samp_taxon_id` | ControlledIdentifiedTermValue | Prefix with `NCBITaxon:` |
| `ncbi_taxonomy_name` | `ncbi_taxonomy_name` | string | Direct |
| `gold_id` | `gold_biosample_identifiers` | — | **Do not use** — `gold_id` is `Go*` (organism), not `Gb*` (biosample). Store in description or `external_database_identifiers` instead. |
| `organism_type` | `gold_organism_type` | string | Direct (e.g., "Natural") |
| `cultured` | `cultured` | YesNoUnknownEnum | `"Yes"` → `yes`, `"No"` → `no`, `"Unknown"` → `unknown` |
| `culture_type` | `culture_type` | CultureTypeEnum | Lowercase: `"Isolate"` → `isolate` |
| `uncultured_type` | `uncultured_type` | UnculturedTypeEnum | |
| `type_strain` | `type_strain` | YesNoUnknownEnum | `"Yes"` → `yes`, `"No"` → `no`, `"Unknown"` → `unknown` |
| `domain` | `organism_domain` | string | Direct (e.g., "BACTERIAL" → "Bacteria") |
| `gold_phylogeny` | `gold_phylogeny` | string | Direct |
| `genbank_16s_id` | `genbank_16s_id` | string | Direct |
| `clade` | `clade` | string | Direct |
| `common_name` | `organism_common_name` | string | Direct |
| `genus_synonyms` | `genus_synonyms` | string | Direct |
| `species_synonyms` | `species_synonyms` | string | Direct |
| `culture_collection_id` | `source_mat_id` | TextValue | Wrap |
| `gram_stain` | `gram_stain` | GramStainEnum | Direct (`"Gram-"`, `"Gram+"`) |
| `cell_shape` | `cell_shape` | string | Direct |
| `cell_length` | `cell_length` | QuantityValue | Parse; use UCUM `um` |
| `cell_diameter` | `cell_diameter` | QuantityValue | Parse; use UCUM `um` |
| `motility` | `motility` | string | Direct |
| `sporulation` | `sporulation` | string | Direct |
| `temperature_range` | `temperature_range` | TemperatureRangeEnum | Add `-ic` suffix: `"Mesophile"` → `Mesophilic` |
| `oxygen_requirement` | `rel_to_oxygen` | RelToOxygenEnum | Lowercase: `"Anaerobe"` → `anaerobe` |
| `carbon_source` | `carbon_source` | string | Direct |
| `color` | `organism_color` | string | Direct |
| `geographic_location` | `geo_loc_name` | TextValue | Wrap |
| `latitude` / `longitude` | `lat_lon` | GeolocationValue | Combine into lat_lon |
| `lat_long_inferred` | `lat_long_inferred` | boolean | `"Yes"` → `true` |
| `sample_collection_site` | `sample_collection_site` | string | Direct |
| `sample_isolation_comments` | `sample_isolation_comments` | string | Direct |
| `sample_collection_year`/`month`/`day` | `collection_date` | TimestampValue | Combine into ISO date |
| `ecosystem` | `ecosystem` | string | Direct |
| `ecosystem_category` | `ecosystem_category` | string | Direct |
| `ecosystem_type` | `ecosystem_type` | string | Direct |
| `ecosystem_subtype` | `ecosystem_subtype` | string | Direct |
| `specific_ecosystem` | `specific_ecosystem` | string | Direct |
| `ecosystem_path_id` | `ecosystem_path_id` | string | Direct |
| `other_ecosystem` | `other_ecosystem` | string | Direct |
| `depth` / `depth2` | `depth` | QuantityValue | `depth` → `has_numeric_value`, `depth2` → `has_maximum_numeric_value`, unit `m` |
| `altitude` / `altitude2` | `alt` | QuantityValue | Same range pattern, unit `m` |
| `elevation` / `elevation2` | `elev` | float | `elevation` → value, `elevation2` unused |
| `subsurface_depth1` / `subsurface_depth2` | `subsurface_depth` | QuantityValue | Same range pattern, unit `m` |
| `ph1` / `ph2` | `isolation_site_ph` | QuantityValue | `ph1` → `has_numeric_value`, `ph2` → `has_maximum_numeric_value`, unit `[pH]` |
| `growth_temperature` / `growth_temperature2` | `temp` | QuantityValue | Range pattern, unit `Cel` |
| `sample_collection_temperature` / `sample_collection_temperature2` | *(same as `temp` or separate slot)* | QuantityValue | Context-dependent |
| `salinity` | `salinity` | QuantityValue | Parse value and unit |
| `pressure` | `pressure` | QuantityValue | Parse; use UCUM `atm` |
| `chlorophyll_concentration` | `chlorophyll_concentration` | QuantityValue | Parse; unit `mg/L` |
| `nitrate_concentration` | `nitrate_concentration` | QuantityValue | Parse; unit `mg/L` |
| `oxygen_concentration` | `oxygen_concentration` | QuantityValue | Parse; unit `mg/L` |
| `salinity_concentration` | `salinity_concentration` | QuantityValue | Parse; unit `[ppm]` |
| `tot_org_carbon` | `tot_org_carbon` | QuantityValue | Unit `mg/kg` |
| `tot_nitrogen` | `tot_nitrogen` | QuantityValue | Unit `mg/kg` |
| `bicarbonate_millimol` | `bicarbonate_millimol` | QuantityValue | Unit `mmol/L` |
| `h2s_millimol` | `h2s_millimol` | QuantityValue | Unit `mmol/L` |
| `h2s_present` | `h2s_present` | string | Direct |
| `irradiance` | `irradiance` | QuantityValue | Unit `W/m2` |
| `methane_conc_millimol` | `methane_conc_millimol` | QuantityValue | Unit `mmol/L` |
| `sample_conductivity` | `sample_conductivity` | QuantityValue | Unit `mS/cm` |
| `host_name` | `specific_host` | string | Direct |
| `host_taxonomy_id` | `host_taxid` | ControlledIdentifiedTermValue | Prefix with `NCBITaxon:` |
| `host_gender` | `host_gender` | string | Direct |
| `host_race` | `host_race` | string | Direct |
| `host_age` | `host_age` | string | Direct |
| `host_medication` | `host_medication` | string | Direct |
| `host_body_site` | `host_body_site` | string | Direct |
| `host_body_subsite` | `host_body_subsite` | string | Direct |
| `host_body_product` | `host_body_product` | string | Direct |
| `host_comments` | `host_comments` | string | Direct |
| `patient_visit_number` | `patient_visit_number` | integer | Direct |
| `mrn` | `medical_record_number` | string | Direct |
| `known_non_hosts` | `known_non_hosts` | string | Direct |
| `other_hosts` | `other_hosts` | string | Direct |
| `pathogenicity` | `pathogenicity` | TextValue | Wrap |
| `encoded_traits` | `encoded_traits` | TextValue | Wrap |
| `env_broad_scale` / `env_local_scale` / `env_medium` | same | ControlledIdentifiedTermValue | GOLD stores as free text; needs ENVO CURIE lookup |
| `biosample_id` | *(FK to GOLD biosample)* | — | Use to link to GOLD biosample if needed |

### GOLD quirks

- **Range pairs**: GOLD stores min/max as separate columns (`depth`/`depth2`,
  `ph1`/`ph2`, etc.). NMDC collapses these into a single `QuantityValue`
  using `has_numeric_value` and `has_maximum_numeric_value`.
- **Tri-state strings**: `cultured`, `type_strain` store
  `"Yes"`/`"No"`/`"Unknown"` as VARCHAR in GOLD. NMDC maps these to
  `YesNoUnknownEnum` (`yes`/`no`/`unknown`), not boolean.
  `lat_long_inferred` is truly binary and uses `boolean`.
- **`temperature_range` enum mismatch**: GOLD uses `"Mesophile"` but NMDC
  enum values end in `-ic` (`Mesophilic`). Same for `Thermophile` →
  `Thermophilic`, etc.
- **`domain` values**: GOLD uses `"BACTERIAL"`, NMDC uses `"Bacteria"`.
- **`gold_id` (Go*) vs `gold_biosample_identifiers` (Gb*)**: The organism
  `gold_id` uses a `Go` prefix. Do not store it in
  `gold_biosample_identifiers` which expects `Gb` (biosample) identifiers.
- **Junction tables**: Multi-valued attributes (biotic_rel, metabolism,
  energy_source, habitat, disease, phenotype, cell_arrangement) are in
  separate junction tables keyed by `organism_id`. Query these separately
  and resolve CV IDs via `cv*` lookup tables.

### Data access

JGI Dremio lakehouse: `"gold-db-2 postgresql".gold.organism_v2`

Requires `DREMIO_URL`, `DREMIO_USER`, `DREMIO_PASSWORD`, and
`CF_AUTHORIZATION` environment variables. See `~/.env`.

Inferred LinkML schema:
`~/gitrepos/bridge-schemas/src/bridge_schemas/schema/jgi/gold.linkml.yaml`

---

## Source 3: JGI Isolate (NA) v19

### Status

The JGI Isolate submission form metadata has **not yet been located** in
the JGI Dremio lakehouse. It may reside in:

- `"gold-db-2 postgresql".gold.biosample_submission_2`
- `portal-db-1` (JGI portal database)
- An internal JGI submission system not exposed via Dremio

Slots defined in `src/schema/organism_sample.yaml` with `in_subset:
jgi_isolate` are modeled from the JGI Isolate (NA) v19 spreadsheet
attached to issue #2803. The mapping table below is based on that
spreadsheet, not on programmatic data access.

### Field mapping (from spreadsheet)

| JGI Form Field | NMDC slot | Range | Notes |
|---|---|---|---|
| Genus | `organism_genus` | string | JGI requires separate genus/species |
| Species | `organism_species` | string | |
| Strain | *(use in `name`)* | — | |
| Isolate Name | `isolate_name` | string | Distinct from strain |
| Biosafety Material Category | `biosafety_material_category` | BiosafetyMaterialCategoryEnum | |
| GC Content % | `gc_content` | QuantityValue | Unit `%` |
| Ploidy Comments | `ploidy` | string | |
| Reference Genome | `reference_genome` | string | IMG taxon OID preferred |
| Ribosomal Sequence | `ribosomal_sequence` | string | Only ACGTN, no header |
| Ribosomal Sequence Type | `ribosomal_sequence_type` | RibosomalSequenceTypeEnum | 16S, ITS, etc. |
| Is Sample from Single Colony | `single_colony_isolation` | GoldYesNoEnum | Y/N |
| Volume | `analyte_volume` | QuantityValue | Unit `uL` |
| Sample Container | `sample_container` | SampleContainerEnum | tube or plate |
| Sample Format | `sample_format` | SampleFormatEnum | Pellet, Ethanol, etc. |
| Was Sample DNAse Treated | `dnase_treated` | GoldYesNoEnum | Y/N |
| Tube or Plate Label | `tube_or_plate_label` | string | Must be unique, <20 chars |
| Plate Location (Well #) | `plate_well_location` | string | e.g., A4, B5 |

### JGI quirks

- **What JGI calls an "isolate sample"** is really a vial of extracted
  DNA/RNA. The form conflates organism identity with physical analyte
  properties (concentration, volume, absorbance). In NMDC terms, a JGI
  isolate submission spans both `OrganismSample` and `ProcessedSample`.
- **Genus/Species as separate fields**: MIxS lumps these into
  `subspecf_gen_lin` or derives from `samp_taxon_id`. JGI requires
  separate fields.
- **Ribosomal sequence verification**: JGI requires actual nucleotide
  sequence data (16S >1300 nt or ITS >450 nt) for strain verification.
  No other source system requires this.

---

## Cross-Authority Slot Overlap

Many slots are shared across authorities. The `in_subset` annotations on
each slot indicate which authorities use it. When populating an
OrganismSample, you may draw data from multiple sources for the same
record:

| Slot | MIGS-Ba | GOLD | JGI | Notes |
|---|---|---|---|---|
| `samp_taxon_id` | yes | yes | yes | All three provide NCBI taxonomy |
| `collection_date` | yes | yes | yes | GOLD splits into year/month/day |
| `geo_loc_name` | yes | yes | yes | |
| `lat_lon` | yes | yes | yes | GOLD has separate lat/lon columns |
| `env_broad_scale` | yes | yes | yes | Often free text; needs ENVO curation |
| `isol_growth_condt` | yes | yes | yes | |
| `biotic_relationship` | yes | yes | — | |
| `rel_to_oxygen` | yes | yes | — | GOLD calls it `oxygen_requirement` |
| `temp` | yes | yes | — | GOLD has growth + collection temps |
| `depth` | yes | yes | — | GOLD has range (depth/depth2) |
| `nucl_acid_ext` | yes | — | yes | JGI captures extraction method |
| `samp_store_temp` | — | yes | yes | |

See `assets/yq-for-mixs-customizations.txt` for the complete subset
assignments on MIxS-derived slots.
