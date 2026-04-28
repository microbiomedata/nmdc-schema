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
| 44 | Sample Isolated From* | `sample_isolated_from` | JGI-native (new) |
| 45 | Collection Site or Growth Conditions* | `sample_isolated_from` | JGI-native (new) — combined with field 44. MIxS isol_growth_condt (MIXS:0000003) was considered but its semantics are "publication reference for growth conditions," not free text |
| 41-43 | Collection Year/Month/Day* | `collection_date` | MIxS (existing) |
| 46-47 | Latitude/Longitude* | `lat_lon` | MIxS (existing) |
| 48-49 | Depth/Max depth* | (deferred — removed from OrganismSample in PR #2977 review pass; see review thread for retain-vs-drop discussion) | MIxS (existing) |
| 50-51 | Elevation/Max elevation* | `elev` | MIxS (existing) |
| 52 | Country* | `geo_loc_name` | MIxS (existing) |
| — | Expected organism | `expected_organism` | NMDC-native (new) |

## Organism (orgn)

| # | JGI Field | nmdc-schema slot | Provenance |
|---|---|---|---|
| 11 | NCBI Tax ID* | `classified_as` | NMDC-native (#2975) |
| 39 | Biosafety Material Category* | `biosafety_material_category` | JGI-native (new) |
| 6 | Genus* | `organism_genus` | JGI-native (new) |
| 7 | Species* | `organism_species` | JGI-native (new) |
| 8 | Strain or cultivar* | `strain_name` | JGI-native (new) |
| 9 | Isolate | `isolate_name` | JGI-native (new) |
| 10 | Culture Collection and ID | `source_mat_id` | MIxS (existing, slot_usage override) |
| 12 | Estimated Genome Size* | `estimated_size` | MIxS (newly imported) |
| 13 | GC Content % | `gc_content` | JGI-native (new) |
| 14 | Ploidy Comments | `ploidy` | MIxS (newly imported) |
| 15 | Reference Genome* | `ref_biomaterial` | MIxS (newly imported) |
| 16 | Host Genus* (viral) | `viral_host_genus` | JGI-native (new) |
| 17 | Host Species* (viral) | `viral_host_species` | JGI-native (new) |
| 18 | Host Strain* (viral) | `viral_host_strain` | JGI-native (new) |
| 19 | Host NCBI Tax ID* | `host_taxid` | MIxS (existing, slot_usage override) |

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
