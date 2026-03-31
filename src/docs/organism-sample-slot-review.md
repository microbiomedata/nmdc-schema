# OrganismSample Slot Review

PR #2884 introduces 112 new slot definitions and assigns 143 total slots
to OrganismSample. This document reviews which slots belong on
OrganismSample, which should move to other classes, and which can be
collapsed with existing slots.

## Schema element delta vs v11.17.1

|  | main (v11.17.1) | PR branch | delta |
|---|---|---|---|
| **slots** | 873 | 985 | +112 |
| **classes** | 82 | 83 | +1 (OrganismSample) |
| **enums** | 143 | 158 | +15 |

Of the 143 slots assigned to OrganismSample, 31 already exist on main
(reused from Biosample, MIxS, etc.) and 112 are new definitions. The
new definitions are drawn from three authority standards:

- **MIxS MIGS-Ba** — Minimum Information about a Genome Sequence: bacteria/archaea
- **GOLD organism_v2** — JGI's Genomes OnLine Database organism table
- **JGI Isolate v19** — JGI's isolate submission form

## Action 1: Remove facility logistics slots (7 slots)

These slots describe the physical vial shipped to JGI, not the organism.
The submission-schema (`nmdc_submission_schema.yaml`) already defines
equivalent slots on `JgiMgInterface` / `JgiMtInterface` /
`JgiMgLrInterface`. They live in the portal Postgres database and are
passed to JGI — they do not belong in nmdc-schema (MongoDB).

| PR #2884 slot | submission-schema equivalent | What it describes |
|---|---|---|
| `analyte_volume` | `jgi_sample_volume` | DNA volume shipped |
| `sample_container` | `cont_type` | tube vs plate |
| `sample_format` | `jgi_sample_format` | pellet, ethanol, etc. |
| `dnase_treated` | `dnase` | Y/N DNase treatment |
| `tube_or_plate_label` | `container_name` | shipping label |
| `plate_well_location` | `cont_well` | well position |
| `biosafety_material_category` | `biosafety_mat_cat` | BSL category |

**Action:** Remove these 7 slots from OrganismSample and from
`organism_sample.yaml`. Also remove `SampleContainerEnum`,
`SampleFormatEnum`, and `BiosafetyMaterialCategoryEnum` if they are
only used by these slots.

## Action 2: Move sequencing/assembly/library slots (18 slots)

These slots describe workflows, library preparation, and assembly
outputs — not the organism itself. The PR description already says
"Sequencing/assembly slots belong on DataGeneration /
LibraryPreparation / WorkflowExecution" but 18 remain.

**Assembly and annotation (belong on WorkflowExecution):**
- `assembly_name`
- `assembly_qual`
- `assembly_software`
- `compl_score`
- `compl_software`
- `number_contig`
- `feat_pred`
- `annot`
- `sim_search_meth`
- `ref_db`

**Library preparation (belong on DataGeneration or LibraryPreparation):**
- `adapters`
- `lib_layout`
- `lib_reads_seqd`
- `lib_screen`
- `lib_size`
- `lib_vector`

**Controls and project linkage:**
- `neg_cont_type`
- `pos_cont_type`

**Action:** Remove these 18 slots from OrganismSample. They may need to
be assigned to existing workflow/data generation classes in a follow-up
PR, or filed as issues if those classes don't have them yet.

Also remove `AssemblyQualEnum`, `LibLayoutEnum`, `NegContTypeEnum`,
and `TaxIdentEnum` if they are only used by slots being removed.

## Action 3: Collapse redundant slots (6 slots)

These new slots overlap semantically with slots already on main. Using
the existing slot avoids introducing a near-duplicate.

| New slot | Existing slot on main | Recommendation |
|---|---|---|
| `host_gender` | `host_sex` | Use `host_sex`. MIxS standard name; same concept. |
| `specific_host` | `host_name` | Use `host_name`. Already defined on main; same concept (free-text host organism name). |
| `isolation_site_ph` | `ph` | Use `ph`. Both are QuantityValue measurements of pH. GOLD's min/max pattern fits in `has_numeric_value` / `has_maximum_numeric_value`. |
| `salinity_concentration` | `salinity` | Use `salinity`. Already defined on main with QuantityValue range. |
| `host_body_site_id` | *(drop)* | GOLD-internal integer FK. Not meaningful outside GOLD. |
| `host_body_subsite_id` | *(drop)* | GOLD-internal integer FK. Not meaningful outside GOLD. |

**Also consider dropping** `host_body_product_id` — same rationale as
the other GOLD-internal integer FKs.

**Action:** Remove these 6–7 slots. For `host_gender`, `specific_host`,
`isolation_site_ph`, and `salinity_concentration`, update the data
mapping guide to map source data to the existing slot name instead.

## Action 4: Needs discussion (not clear-cut)

These overlaps need team input before deciding:

| New slot | Overlaps with | Question |
|---|---|---|
| `organism_domain` | `gtdbtk_domain` (on MagBin) | Different provenance (GOLD vs GTDB). Could one `taxonomic_domain` slot serve both? Or are GOLD organism domain and GTDB-tk assignment semantically distinct? |
| `organism_genus` / `organism_species` | derivable from `samp_taxon_id` | JGI requires separate genus/species fields. Are these convenience slots for ingest, or do they carry information beyond what the NCBITaxon CURIE provides? |
| `tot_nitrogen` / `tot_org_carbon` | `nitrate_nitrogen`, `ammonium_nitrogen` on main | Different measurements (total vs specific forms). Probably not duplicates, but worth confirming. |
| `single_colony_isolation` | *(no equivalent)* | Describes how the organism was obtained. Arguably belongs on OrganismSample (it defines what it *is*), but could also be a MaterialProcessing attribute. |
| `project_name` | `name` on Study | What is this slot capturing that isn't already on Study? |
| `associated_resource` | `associated_studies` (already assigned) | MIxS slot; may overlap with NMDC's study linkage pattern. |
| `ribosomal_sequence` / `second_ribosomal_sequence` | *(no equivalent)* | JGI requires actual nucleotide data for strain verification. Does NMDC want to store raw sequences, or just GenBank accession references? |

## Summary

If actions 1–3 are applied:

| Action | Slots removed | Enums removed |
|---|---|---|
| Facility logistics | 7 | up to 3 |
| Sequencing/assembly | 18 | up to 4 |
| Collapse redundant | 6–7 | 0 |
| **Total** | **31–32** | **up to 7** |

This would bring the new slot count from 112 down to ~80, and the total
OrganismSample slot assignments from 143 down to ~111.

## Related issues

- #2892 — Analyte slot scope
- #2893 — JGI validation rules
- #2803 — Model isolates/organisms as distinct from environmental Biosamples
- #1769 — Need clarity on .yaml files that have NMDC schema elements
