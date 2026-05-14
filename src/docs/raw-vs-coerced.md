# Raw-vs-coerced provenance pattern

This document names a convention used throughout `nmdc-schema`: classes that
buffer a raw, contributor-supplied form of a value alongside a coerced,
NMDC-normalized form. The pattern is implicit and undocumented today; this
doc names it so future class designers don't re-derive it.

## The pattern

A wrapper class holds two parallel representations of the same fact:

1. A **raw form** that preserves the contributor's exact submission.
2. A **coerced form** that is NMDC's normalized, validated, or
   ontology-resolved interpretation of the raw form.

This is implicit slot-value-level provenance: NMDC retains the original
input as evidence even after applying its own parse, classification, or
canonicalization. It is the field-level analogue of the audit trail that
`ProvenanceMetadata` provides at the record level.

## Canonical examples

### `QuantityValue` (`attribute_values.yaml`)

- Raw: `has_raw_value: "50 kPa"`
- Coerced: `has_numeric_value: 50`, `has_unit: kPa`

### `TimestampValue`

- Raw: `has_raw_value: "30-OCT-14 12.00.00.000000000 AM"` (e.g. GOLD format)
- Coerced: ISO-8601 datetime; v11.17.0's `normalize_date_to_datetime()`
  does the migration.

### `ControlledIdentifiedTermValue`

- Raw: free-text term string
- Coerced: `term` reference to an `OntologyClass`

### `PropertyAssertion`

The most disciplined instance. `has_raw_value` is **required**. Used as
the fallback class for properties that don't align with policy-governed
slots; preserves the contributor's string so nothing is lost in coercion.

### `Doi`

- Raw: `doi_value` (the literal CURIE)
- Coerced: `doi_provider` (classified into `DoiProviderEnum`),
  `doi_category` (classified into `DoiCategoryEnum`)

### `Organism` and `expected_organism`

- Raw: `name`, `alternative_names`, `strain_name`, `isolate_name`
- Coerced: `classified_as` (range `OntologyClass`, narrowed to NcbiTaxon)

`expected_organism`'s description explicitly notes "May be contradicted by
sequencing results" — the asserted-vs-observed split is part of the
convention.

### `gold_path_field` family versus the ENVO triad

Parallel representation on `Biosample`:

- Raw: `ecosystem`, `ecosystem_category`, `ecosystem_subtype`,
  `ecosystem_type`, `specific_ecosystem` — GOLD ecosystem path tokens
- Coerced: `env_broad_scale`, `env_local_scale`, `env_medium`
  (range `ControlledIdentifiedTermValue`) — NMDC's ENVO-canonicalized triad

## Recommended discipline for new wrapper classes

When designing a class that coerces a contributor input into a structured
form:

1. **Provide a raw-capture slot.** `has_raw_value` for AttributeValue
   descendants; a literal-typed slot like `doi_value` otherwise.
2. **Make the raw-capture slot required.** Today only `PropertyAssertion`
   enforces this. The cost of optional raw-capture is that the raw form
   gets silently dropped after coercion, losing field-level provenance.
3. **Provide one or more coerced slots** holding NMDC's interpretation.
4. **When coercion can change over time** (NcbiTaxon reclassification,
   ENVO term replacement, etc.), document this in the class and consider
   whether a future `SlotLevelProvenance` record should accompany
   re-coercions.

## Gaps to fill

Slots that currently lack a coerced counterpart but should arguably have
one:

- `isolation_source` (MIxS, range `TextValue`): gets `has_raw_value` for
  free but has no ENVO-coercion target.
- `geo_loc_name` (MIxS, range `TextValue`): no structured form for country
  or locality. `GeolocationValue` covers only lat/lon.
- `env_package` (`core.yaml:1521`): ranged at `TextValue` instead of a
  coerced enum despite only certain package names being valid.
- `processing_institution_workflow_metadata`: single free-string slot;
  no structured form for vendor metadata blobs.

## Related

- `attribute_values.yaml` — the `AttributeValue` hierarchy.
- `basic_classes.yaml` — the `Doi` and `Organism` classes.
- `src/schema/external_identifiers.yaml` — identity-overlap patterns.
- `src/schema/slot_level_provenance.yaml` — companion draft of an
  explicit field-level provenance log for changes over time.
- Contributor guide umbrella: see issue #3069 for the broader effort to
  document data-shape conventions.
