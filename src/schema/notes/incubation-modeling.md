# Modeling incubation samples without the `*_inc` slots

Supports the deprecation of `collection_date_inc` (issue
https://github.com/microbiomedata/nmdc-schema/issues/2658, PR
https://github.com/microbiomedata/nmdc-schema/pull/3287) by showing how the same
data is represented without it.

There are three sibling slots in the same family: `collection_time_inc`,
`start_date_inc`, and `start_time_inc`. Only `collection_date_inc` has an agreed
deprecation (issue 2658). The mapping below covers all four so the full picture
is visible, but the other three are **not** deprecated here; whether they should
follow is a separate proposal (issue
https://github.com/microbiomedata/nmdc-schema/issues/3289).

## The scenario (from issue 2658)

Material is collected from the field on 2021-04-15, then incubated and harvested
later. The harvested sample shares one field collection date but differs in when
the incubation started and ended.

## Old modeling (what the `*_inc` slots did)

One sample carried the field `collection_date` plus four incubation-specific slots
for the incubation's start and harvest date and time:

```yaml
collection_date: "2021-04-15"        # field collection
start_date_inc:  "2021-04-16"        # incubation started
start_time_inc:  "09:00"
collection_date_inc: "2021-04-17"    # harvested
collection_time_inc: "14:30"
```

The incubation start and the harvest are packed onto the sample as parallel
"shadow" date fields. That conflates a process (the incubation) with a material
entity (the sample).

## Proposed modeling (no `*_inc` slots): `Culturing`

Model the incubation as a first-class process using `Culturing`
(`is_a MaterialProcessing`). Its `has_input` and `has_output` are both
`OrganismSample`, and `OrganismSample` carries `collection_date`. So the
incubation is a process with a start and an end, and the harvested culture's date
is simply the output sample's own `collection_date`.

The full, schema-valid instance data is in
`src/data/valid/Database-incubation-as-culturing.yaml`: two `OrganismSample`s (the
input organism and the cultured output, each with its own `collection_date`)
linked by a `Culturing` process that carries `start_date` and `end_date`.

## How each `*_inc` slot maps under the `Culturing` model

| `*_inc` slot | Replacement | Owning element |
| --- | --- | --- |
| `collection_date_inc` (harvest date) | `collection_date` of the output `OrganismSample`, and/or `Culturing.end_date` | sample / process |
| `collection_time_inc` (harvest time) | the time component of that `collection_date` `TimestampValue` | sample |
| `start_date_inc` (start date) | `Culturing.start_date` | process |
| `start_time_inc` (start time) | the time component of the start (see open question 2) | process |

`collection_date_inc` is deprecated here (issue 2658). The other three rows are
shown to inform the separate proposal (issue 3289); they are not deprecated in
this PR.

All four are empty in production: 0 of 27,352 `biosample_set` documents use any of
them (verified against prod Mongo 2026-07-21), so deprecation carries no migration
risk.

## Open questions

1. **`Culturing` inputs and outputs are `OrganismSample`s** (single-organism
   intent). The scenario in issue 2658 is a soil incubation, and soil is a
   `Biosample` (a community), not an `OrganismSample`. There is no community-in,
   community-out process class analogous to `Culturing`. Decide whether soil-style
   incubations reuse a process class or keep describing the treatment on the
   `Biosample`.

2. **`Culturing.start_date` and `end_date` are date strings, with no time of day.**
   `collection_date` (a `TimestampValue`) can hold a time, but the process start and
   end cannot. Decide whether minute-level incubation timing needs a home.
