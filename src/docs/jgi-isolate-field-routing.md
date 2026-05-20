# JGI Isolate Form Field Routing

Complete routing of all 55 fields from the JGI Isolate (NA) v19 submission form
to nmdc-schema classes, submission-schema, or deferred.

## OrganismSample (osm)

| # | JGI Field | nmdc-schema slot | Provenance |
|---|---|---|---|
| 4 | Sample Name* | `samp_name` | MIxS (existing) |
| 31 | Single colony isolation?* | ~~`single_colony_isolation`~~ → submission-schema `JgiIsolateInterface.isolate_single_colony` | Moved: JGI submission logistics, not an NMDC data-model field. See submission-schema#418. |
| 32 | Known / Suspected Organisms | ~~`known_suspected_organisms`~~ → submission-schema `JgiIsolateInterface.isolate_known_contaminants` | Moved: same reason. |
| 33 | First ribosomal sequence* | ~~`ribosomal_sequence`~~ → submission-schema `JgiIsolateInterface.isolate_ribosomal_seq` | Moved: same reason. |
| 34 | First ribosomal sequence type* | ~~`ribosomal_sequence_type`~~ → submission-schema `JgiIsolateInterface.isolate_ribosomal_seq_type` | Moved: same reason. |
| 35 | First ribosomal sequence comments | ~~`ribosomal_sequence_comments`~~ → submission-schema `JgiIsolateInterface.isolate_ribosomal_seq_comments` | Moved: same reason. |
| 36 | Second ribosomal sequence | ~~`second_ribosomal_sequence`~~ → submission-schema `JgiIsolateInterface.isolate_second_ribosomal_seq` | Moved: same reason. |
| 37 | Second ribosomal sequence type | ~~`second_ribosomal_sequence_type`~~ → submission-schema `JgiIsolateInterface.isolate_second_ribosomal_seq_type` | Moved: same reason. |
| 38 | Second ribosomal sequence comments | ~~`second_ribosomal_sequence_comments`~~ → submission-schema `JgiIsolateInterface.isolate_second_ribosomal_seq_comments` | Moved: same reason. |
| 29 | Fungal 16S screening?* | ~~`fungal_16s_screening`~~ → submission-schema `JgiIsolateInterface.isolate_fungal_16s_screening` | Moved: same reason. |
| 30 | ITS match UNITE?* | ~~`its_match_unite`~~ → submission-schema `JgiIsolateInterface.isolate_its_match_unite` | Moved: same reason. |
| 40 | Sample Isolation Method* | `sample_isolation_method` | JGI-native (new) |
| 44 | Sample Isolated From* | `sample_isolated_from` | JGI-native (new) — origin matrix only ("the *what* the organism came out of") |
| 45a | Collection Site or Growth Conditions* (collection-site half) | `sample_collection_site` | NMDC-native (pre-existing slot, reused for OrganismSample) — geographic / environmental site context |
| 45b | Collection Site or Growth Conditions* (growth-conditions half) | `sample_growth_conditions` | JGI-native (new) — in-vitro lab maintenance context. MIxS `isol_growth_condt` (MIXS:0000003) was considered but its DOI/PMID/URL pattern doesn't fit free text |
| 41-43 | Collection Year/Month/Day* | `collection_date` | MIxS (existing) |
| 46-47 | Latitude/Longitude* | `lat_lon` | MIxS (existing) |
| 48-49 | Depth/Max depth* | (deferred — removed from OrganismSample in PR #2977 review pass; see review thread for retain-vs-drop discussion) | MIxS (existing) |
| 50-51 | Elevation/Max elevation* | `elev` | MIxS (existing) |
| 52 | Country* | `geo_loc_name` | MIxS (existing) |
| — | Expected organism | `expected_organism` | NMDC-native |
| 19 | Host NCBI Tax ID* (and host name) | `host_organism` (on `OrganismSample`); same pattern as `expected_organism` — a typed reference to an `Organism` instance, whose `classified_as` carries the NCBI Taxonomy CURIE and whose `organism_genus / organism_species / strain_name` carry the JGI-form host-name text fields | NMDC-native (new in #3054) |

### Note on `host_organism` vs the legacy `host_taxid` slot

`OrganismSample` uses `host_organism` (range: `Organism`) rather than the
flat MIxS `host_taxid` slot. The pattern mirrors `expected_organism`:
`OrganismSample → host_organism → Organism → classified_as → NcbiTaxon`,
with `Organism.organism_genus / organism_species / strain_name` providing
the text-level redundancy the JGI Isolate v19 form expects (Host Genus /
Host Species / Host Strain).

This is the same pattern used for the focal organism; reusing it for the
host avoids parallel ID-only and name-only host slots on OrganismSample.
The Pf-5-from-cotton example (`Database-rhizosphere-isolate.yaml`) is the
canonical demonstration: a cotton `Organism` record carries
`classified_as: NCBITaxon:3635`, `organism_genus: Gossypium`,
`organism_species: hirsutum`, and the bacterial-isolate `OrganismSample`
references it via `host_organism: nmdc:orgn-99-cot0001`.

`Biosample` continues to use the legacy flat `host_taxid` /
`host_genus` / `host_species` / `host_strain` slots; aligning Biosample to
the same linked-data pattern is out of scope for #3054 and is tracked as
a follow-up.

Broader normalization of taxon-bearing slots to use `NcbiTaxon` as their
range (rather than strings or CURIEs in `has_raw_value`) is tracked in
[#3000](https://github.com/microbiomedata/nmdc-schema/issues/3000).

## Organism (orgn)

| # | JGI Field | nmdc-schema slot | Provenance |
|---|---|---|---|
| 11 | NCBI Tax ID* | `classified_as` | NMDC-native (#2975) |
| 39 | Biosafety Material Category* | → submission-schema (microbiomedata/submission-schema#423) | Moved: JGI submission-time routing field, not an NMDC data-model attribute. The 10 permissible values come from the JGI Isolate (NA) v19 form; see PR #423 thread for the verified list and the GOLD/MIxS comparison. |
| 6 | Genus* | `organism_genus` | JGI-native (new) |
| 7 | Species* | `organism_species` | JGI-native (new) |
| 8 | Strain or cultivar* | `strain_name` | JGI-native (new) |
| 9 | Isolate | `isolate_name` | JGI-native (new) |
| 10 | Culture Collection and ID | `source_mat_id` | MIxS (existing, slot_usage override) |
| 12 | Estimated Genome Size* | `estimated_size` | MIxS (newly imported) |
| 13 | GC Content % | `gc_content` | JGI-native (new) |
| 14 | Ploidy Comments | `ploidy` | MIxS (newly imported) |
| 15 | Reference Genome* | `ref_biomaterial` | MIxS (newly imported) |
| 16 | Host Genus* (viral) | `host_genus` (on Biosample) | JGI-native (new) |
| 17 | Host Species* (viral) | `host_species` (on Biosample) | JGI-native (new) |
| 18 | Host Strain* (viral) | `host_strain` (on Biosample) | JGI-native (new) |

## submission-schema only (not persisted to MongoDB)

| # | JGI Field | Why |
|---|---|---|
| 1 | Seq Project ID | JGI internal identifier |
| 2 | Seq Project Name | JGI internal |
| 3 | Sample ID | JGI internal |
| 5 | Biological replicate/group Name* | Submission logistics |
| 20 | Concentration* (ng/ul) | Analyte property (future Analyte class) |
| 21 | Volume* (ul) | Analyte property |
| 22 | Absorbance 260/280* | Analyte property |
| 23 | Absorbance 260/230* | Analyte property |
| 24 | Tube or Plate Label* | Shipping logistics |
| 25 | Sample Container* | Shipping logistics |
| 26 | Plate location* | Shipping logistics |
| 27 | Sample Format* | Shipping logistics |
| 28 | DNAse treated?* | Analyte prep |
| 53 | Seq Project PI Name | JGI internal |
| 54 | Seq Project Sample Contact Name | JGI internal |
| 55 | Proposal ID | JGI internal |

## MIxS slots newly imported in this PR

| Slot | MIXS ID | Used on | JGI Field |
|---|---|---|---|
| `estimated_size` | MIXS:0000024 | Organism | Estimated Genome Size |
| `ploidy` | MIXS:0000021 | Organism | Ploidy Comments |
| `ref_biomaterial` | MIXS:0000025 | Organism | Reference Genome |

`isol_growth_condt` (MIXS:0000003) was imported but not assigned. Its MIxS semantics are
"publication reference for isolation/growth conditions" (DOI/PMID/URL pattern), which does
not match the JGI free-text field. It remains available for future use where a publication
reference is appropriate.

Note: `ref_biomaterial` may be renamed in a future MIxS release. Montana Smith has
ongoing MIxS renaming work that may affect this slot.

## `source_mat_id`: CURIE normalization for culture-collection identifiers

`source_mat_id` (MIXS:0000026) on `OrganismSample` carries the culture-collection
catalog identifier from which the sample was sourced. Routed from JGI Isolate (NA)
v19 field 10 ("Culture Collection and ID"). The slot reuses the MIxS source_mat_id
slot but is scoped here to culture-collection ordering provenance specifically;
JGI's label is a `NARROW_SYNONYM` of the broader MIxS slot.

### Preferred form

CURIE using a bioregistry-declared prefix:

```
dsmz:DSM-15171
atcc:700808
lmg:23168
```

### Per-collection normalization (GOLD → CURIE)

GOLD organism_v2 stores the field space-separated (e.g. `DSM 6724`,
`ATCC 700808`). Ingest normalization differs by collection:

| Source form (GOLD) | Normalized CURIE | Rule |
|---|---|---|
| `DSM 6724` | `dsmz:DSM-6724` | Replace space with hyphen, keep sub-collection letters |
| `ATCC 700808` | `atcc:700808` | Strip prefix letters and space, keep numeric local ID |
| `JCM 20004` | `jcm:20004` | Same as ATCC: numeric local ID only |
| `NBRC 13719` | `nbrc:13719` | Same as ATCC |
| `BCRC 10694` | `bcrc:10694` | Same as ATCC |
| `CCUG 12345` | `ccug:12345` | Same as ATCC |
| `LMG 23168` | `lmg:23168` | Same as ATCC |

### Prefix coverage

**Declared prefixes** (covering the top GOLD collections by record count):
`dsmz` (~18K records), `atcc` (~14K), `lmg` (~13K), `ccug` (~12K), `jcm`
(~7K), `nbrc` (~4K), `bcrc` (~3K). All seven resolve via the prefix
declarations in `src/schema/basic_classes.yaml`.

**Common GOLD collections without declared prefixes** (use space-separated
form e.g. `CIP 54.8` until prefixes are added):

| Collection | GOLD record count |
|---|---|
| CIP | ~7K |
| ICMP | ~4K |
| NCIMB | ~4K |
| NCTC | ~4K |
| CFBP | ~4K |
| KCTC | ~4K |
| NRRL | ~3K |
| CCRC | ~3K |

Adding bioregistry-resolvable prefixes for these is tracked in
[#3036](https://github.com/microbiomedata/nmdc-schema/issues/3036).

## Decomposing GOLD compound `sample_isolated_from` values into NMDC typed slots

GOLD's `dw_samples.sample_isolated_from` is a single free-text column historically populated with values that conflate origin matrix, collection site, growth conditions, and host context. Per [#3054](https://github.com/microbiomedata/nmdc-schema/issues/3054), NMDC splits these concepts into typed slots on `OrganismSample`:

- `sample_isolated_from` — origin matrix (the *what*), enum-typed
- `sample_collection_site` — site category (the *where*), enum-typed
- `sample_growth_conditions` — lab maintenance (interim free-text; full decomposition in [#3027](https://github.com/microbiomedata/nmdc-schema/issues/3027) / [#3065](https://github.com/microbiomedata/nmdc-schema/issues/3065))
- `host_organism` — typed reference to an `Organism` instance whose `classified_as` carries the host's NCBI Taxonomy CURIE

On export back to GOLD/JGI, the typed slots recombine into the legacy flat string. For the host string fields (JGI v19 fields Host Genus / Species / Strain), traverse `host_organism.organism_genus` / `host_organism.organism_species` / `host_organism.strain_name`.

### Worked examples

| GOLD source value | `sample_isolated_from` | `sample_collection_site` | `host_organism.classified_as` | `geo_loc_name` | Notes |
|---|---|---|---|---|---|
| `leaf` / `Leaf` / `Leaves` | `leaf` | — | — | — | Case/plural variants all map to single PV; structured_aliases attribute the originals |
| `Sorghum bicolor - root` | `root` | — | `NCBITaxon:4558` (via Sorghum Organism record) | — | Host + tissue compound: host goes to a typed Organism reference, tissue to origin matrix |
| `maize rhizosphere soils` | `rhizosphere` | — | `NCBITaxon:4577` (via Zea Organism record) | — | Same pattern; rhizosphere is the matrix, maize is the host |
| `Switchgrass Roots` | `root` | — | `NCBITaxon:38727` (via Panicum Organism record) | — | Plant-host isolate from root tissue |
| `Iron-rich microbial mat from hydrothermal vent` | `microbial_mat` | — | — | — | Narrative GOLD value collapses to single PV; remaining geo context goes to `geo_loc_name` / `lat_lon` |
| `seawater` | `sea_water` | — | — | — | Case-normalized |
| `DSMZ catalog vial` | — | `culture_collection` | — | — | No origin matrix; site is "culture_collection"; catalog accession on `source_mat_id` |
| `Greenhouse` (alone) | — | `greenhouse` | — | — | Site-only value, no matrix |
| `Field-grown common garden of wild sourced seedlots, near Greytown, KZN, South Africa` | — | `field` | — | `South Africa` | Narrative site description: site category → enum PV, place name → `geo_loc_name` |
| `Liquid culture from a frozen stock` | — | — | — | — | Growth-state value: routes to `sample_growth_conditions` PV `liquid_culture` |
| `single colony isolate` | — | — | — | — | Routes to `sample_isolation_method` (the *how*), not to any of the three new slots |

### Mapping advice for the JGI/GOLD round-trip

**NMDC → JGI field 44 (Sample Isolated From\*)**: the PV's label for `sample_isolated_from` (e.g., `leaf` → "leaf"). If the matrix is host-tissue, optionally prepend the host's organism name from `host_organism.name` for JGI's preferred display ("Sorghum bicolor - root").

**NMDC → JGI field 45 (Collection Site or Growth Conditions\*)**: prefer the populated slot. If `sample_growth_conditions` is set, emit its label. If `sample_collection_site` is set, emit its label (optionally suffixed by `geo_loc_name`).

**NMDC → GOLD `dw_samples.sample_isolated_from`**: concatenate matrix + site + growth + host in whatever order GOLD historically uses, semicolon-separated, with empty parts elided. The unit tests for the exporter should round-trip the worked examples above.

### What does NOT belong in any of these three slots

- Sample names ("S1321") → `samp_name`
- Submitter notes / project descriptions → `description` (inherited)
- Sample-to-sample provenance ("Y was isolated from X") → `sample_link` / typed link (see [#3033](https://github.com/microbiomedata/nmdc-schema/issues/3033))
- Specific lat/lon → `lat_lon`; elevation → `elev`; country → `geo_loc_name`
- Collection date → `collection_date`
- DNA extraction kit / protocol → `sample_isolation_method` (the *how*, not the *what* or *where*)
