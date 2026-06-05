# NcbiTaxon Class and Taxonomy Slot Routing

## What this PR adds

- **`NcbiTaxon` class** (`is_a: OntologyClass`) — a concrete subclass for NCBI Taxonomy terms.
  Instances are identified by NCBITaxon CURIEs (e.g. `NCBITaxon:511145`), stored in
  `ontology_class_set`, and validated against `^NCBITaxon:\d+$`. No new slots, typecodes,
  or MongoDB collections.

- **`classified_as` slot** (`range: OntologyClass`, multivalued) — a general-purpose
  classification slot. Narrowing to `NcbiTaxon` on specific classes via `slot_usage` is
  tracked in #3016. Not yet assigned to any class; OrganismSample (#2884) will be the first
  consumer.

## What is NOT in this PR — and where it goes

| Information | Destination | Tracking |
|---|---|---|
| Strain identity (culture collection ID, strain designator, lab name) | Slots on Organism (`strain_name`, `isolate_name`, `source_mat_id`) | #2977 |
| Sub-species lineage strings | `subspecf_gen_lin` (existing MIxS slot), assigned to OrganismSample | #2884 |
| GTDB taxonomy | New class or widen `NcbiTaxon.id_prefixes`; needs a GTDB-to-OntologyClass loader (GTDB ships as TSV, not OWL) | Future |
| LPSN / SeqCode nomenclature | Same pattern — CURIE-identified taxon instances | Future |
| Novel organisms with no taxon ID | Organism-level text slots; `classified_as` left empty or pointed at nearest ancestor | #2977 |
| Organism genus/species as separate text fields (JGI requirement) | Slots on Organism (`organism_genus`, `organism_species`) | #2977 |
| GOLD organism identifiers (`Go*`) | `gold_organism_identifiers` slot | #2973 |
| Genbank 16S / INSDC accessions | String or external identifier slots | #2960 |
| Direct `NcbiTaxon` example data | `NcbiTaxon-minimal.yaml` (valid), `NcbiTaxon-invalid-prefix.yaml` (invalid) | This PR |

## Relationship to existing taxonomy slots

`samp_taxon_id` and `host_taxid` use `ControlledIdentifiedTermValue` with `term` having
`range: OntologyClass`. These are MIxS-originated slots; `classified_as` is an NMDC-native
slot intended for new classes like OrganismSample. The target design narrows
organism-oriented uses to `NcbiTaxon` via class-specific `slot_usage` (#3016) rather than
making the global slot range taxon-specific.

At present, `NcbiTaxon` validation is intentionally NCBITaxon-specific. The schema keeps
`id_prefixes` so the intended authority list is explicit, but actual instance validation
is enforced by a regex on `NcbiTaxon.id`. When GTDB, LPSN, or SeqCode support is added, both
`id_prefixes` and the `NcbiTaxon.id` pattern should be updated together.

The remaining modeling question is how much of this specificity should live on the
global `classified_as` slot versus on class-local `slot_usage`. That is tracked in #3016.

## Loading taxonomy data into ontology_class_set

`ontology_class_set` currently contains ENVO (4,366), UBERON (16,061), and PO (1,998)
terms. NCBITaxon (~2.7M active terms) can be loaded using the same pipeline once
microbiomedata/ontology-loader#9-#12 are resolved — those issues cover a blocking CURIE
prefix bug, memory constraints from full-list materialization, and upsert throughput.
GTDB (~143K species clusters as of R226) would additionally need a custom loader since
it ships as TSV rather than OWL.
