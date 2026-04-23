# Taxon Class and Taxonomy Slot Routing

## What this PR adds

- **`Taxon` class** (`is_a: OntologyClass`) — a semantic subclass for formal taxonomy
  terms. No new slots, no typecode, no dedicated MongoDB collection. Instances go into
  `ontology_class_set` with external CURIEs (e.g. `NCBITaxon:511145`). Current validation
  requires `Taxon.id` to match `^NCBITaxon:\d+$`.

- **`classified_as` slot** (`range: Taxon`, multivalued) — a
  general-purpose classification slot for direct references to `Taxon`
  instances. Not yet assigned to any class; OrganismSample (#2884) will be the
  first consumer.

## What is NOT in this PR — and where it goes

| Information | Destination | Tracking |
|---|---|---|
| Strain identity (culture collection ID, strain designator, lab name) | Text slots on OrganismSample or a future Strain class | #2971 |
| Sub-species lineage strings | `subspecf_gen_lin` (existing MIxS slot), assigned to OrganismSample | #2884 |
| GTDB taxonomy | Same `Taxon` class, add `GTDB` to `id_prefixes`, widen `Taxon.id` pattern, load into `ontology_class_set` | Future — needs a GTDB-to-OntologyClass loader since GTDB ships as TSV, not OWL |
| LPSN / SeqCode nomenclature | Same pattern — CURIE-identified Taxon instances, plus widening `Taxon.id` validation | Future, when needed |
| Novel organisms with no taxon ID | Strain-level text slots; `classified_as` left empty or pointed at nearest ancestor | Strain class PR |
| Organism genus/species as separate text fields (JGI requirement) | Slots on OrganismSample (`organism_genus`, `organism_species`) | #2884 |
| GOLD organism identifiers (`Go*`) | `gold_organism_identifiers` slot | #2973 |
| Genbank 16S / INSDC accessions | String or external identifier slots | #2960 |
| Deprecation of `known_as` on PortionOfSubstance | Replace with `classified_as` | Future issue |
| Direct `Taxon` example data | `Taxon-minimal.yaml` (valid), `Taxon-invalid-prefix.yaml` (invalid) | This PR |

## Relationship to existing taxonomy slots

`samp_taxon_id` and `host_taxid` already use `ControlledIdentifiedTermValue` with
`range: OntologyClass` via the `term` slot. These are MIxS-originated slots with
MIxS-specific structured patterns. `classified_as` is an NMDC-native slot without
MIxS constraints, intended for use on new classes like OrganismSample, and points
directly to `Taxon`.

At present, `Taxon` validation is intentionally NCBITaxon-specific. The schema keeps
`id_prefixes` so the intended authority list is explicit, but actual instance validation
is enforced by a regex on `Taxon.id`. When GTDB, LPSN, or SeqCode support is added, both
`id_prefixes` and the `Taxon.id` pattern should be updated together.

## Loading taxonomy data into ontology_class_set

`ontology_class_set` currently contains ENVO (4,366), UBERON (16,061), and PO (1,998)
terms. NCBITaxon (~2.5M terms) can be loaded using the same pipeline. GTDB (~131K
species clusters) would need a custom loader since it ships as TSV rather than OWL.
