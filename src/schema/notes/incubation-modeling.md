# Modeling incubation samples without the `*_inc` slots

Supports the deprecation of `collection_date_inc` (issue
https://github.com/microbiomedata/nmdc-schema/issues/2658, PR
https://github.com/microbiomedata/nmdc-schema/pull/3287) by showing how the same
data is represented without it.

There are three sibling slots in the same family: `collection_time_inc`,
`start_date_inc`, and `start_time_inc`. Only `collection_date_inc` has an agreed
deprecation (issue 2658). The mapping below covers all four so the full picture
is visible, but the other three are **not** deprecated here; whether they should
follow is a separate proposal for Montana's input, not a decision made in this PR.

## The scenario (from issue 2658)

50 g of soil is collected from the field on 2021-04-15. 10 g is weighed into each
of 5 jars, incubated, and harvested one jar per day. The 5 harvested samples share
one field collection date but differ in when the incubation started and ended.

## Old modeling (what the `*_inc` slots did)

One `Biosample` carried the field `collection_date` plus four incubation-specific
slots for the incubation's start and harvest date/time:

```yaml
# one Biosample per jar, all pointing back to the same field event
collection_date: "2021-04-15"        # field collection
start_date_inc:  "2021-04-16"        # incubation started
start_time_inc:  "09:00"
collection_date_inc: "2021-04-17"    # jar harvested
collection_time_inc: "14:30"
```

The incubation start and the harvest are packed onto the sample as parallel
"shadow" date fields. That conflates a process (the incubation) with a material
entity (the sample).

## Proposed modeling (no `*_inc` slots)

Model the incubation as a first-class process. A field `Biosample` is the input;
each harvested jar is a separate sample output; the incubation itself is a
`MaterialProcessing` that carries the start and end.

```yaml
# 1. the field sample
biosample_set:
  - id: nmdc:bsm-11-fieldsoil
    collection_date: "2021-04-15"          # the field collection event
    # env_triad, etc.

# 2. the incubation, modeled as a MaterialProcessing
#    The id prefix is a placeholder: no incubation subclass exists yet
#    (open question 1), so there is no assigned id pattern.
material_processing_set:
  - id: nmdc:INCUBATION-PROCESS-ID
    has_input:  [nmdc:bsm-11-fieldsoil]
    has_output: [nmdc:procsm-11-jar01]     # a ProcessedSample (open question 2)
    start_date: "2021-04-16"               # incubation started (PlannedProcess slot)
    end_date:   "2021-04-17"               # jar harvested (PlannedProcess slot)
    # duration could also record elapsed incubation time

# 3. the harvested incubation sample, one per jar
#    Shown as a Biosample so it can carry collection_date (open question 2).
  - id: nmdc:bsm-11-jar01
    collection_date: "2021-04-17"          # the jar's harvest date
```

The last block is under `biosample_set`, not `material_processing_set`. It is
placed here in sequence for readability.

## How each `*_inc` slot would map

`collection_date_inc` is deprecated here. The other three rows show where their
data would go under the same model, to inform the separate proposal about them.

| `*_inc` slot | Replacement | Owning element |
| --- | --- | --- |
| `collection_date_inc` (harvest date) | `collection_date` of the harvested sample, and/or `end_date` of the incubation process | sample / process |
| `collection_time_inc` (harvest time) | `collection_time` of the harvested sample | sample |
| `start_date_inc` (start date) | `start_date` of the incubation `MaterialProcessing` | process |
| `start_time_inc` (start time) | no clean home yet (see open question 3) | process |

All four are **empty in production**: 0 of 27,352 `biosample_set` documents use any
of them (verified against prod Mongo 2026-07-21), so deprecation carries no
migration risk.

## Open questions for review (James, Montana)

1. **There is no incubation subclass of `MaterialProcessing` yet.** `MaterialProcessing`
   is abstract; the concrete subclasses today are `SubSamplingProcess`,
   `MixingProcess`, `FiltrationProcess`, `StorageProcess`,
   `ChromatographicSeparationProcess`, `DissolvingProcess`,
   `ChemicalConversionProcess`, and `Extraction`. An incubation is none of these.
   Do we add an `IncubationProcess` (or `CulturingProcess`) subclass?

2. **`MaterialProcessing.has_output` is a `ProcessedSample`, which has no
   `collection_date`** (only `Biosample` does). So "the incubation sample carries
   its own `collection_date`" only works if the harvested sample is a `Biosample`,
   which is not the declared process output type. We need to decide one of:
   - model the harvested incubation sample as a `Biosample` (keeps `collection_date`,
     but it is then not the `has_output` `ProcessedSample` of the process), or
   - add `collection_date` / `collection_time` to `ProcessedSample` (or to the
     shared `Sample` parent).

3. **`PlannedProcess` has `start_date` and `end_date` but no time-of-day slot.**
   The date component of an incubation's start/end has a home (`start_date` /
   `end_date`); the `*_time_inc` minute-level precision does not. Do we need
   process-level start/end times, or is date precision enough for incubations?
