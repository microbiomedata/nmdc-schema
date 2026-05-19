# Provenance mechanisms in NMDC

NMDC tracks changes to records during their custody through several
independent mechanisms. Some are expressed in this schema as slots on
records; others live operationally in `nmdc-runtime` (in sibling Mongo
namespaces, supplementary collections, or repository artifacts). This
page inventories all of them and shows how to query each.

This document is descriptive, not prescriptive. The mechanisms below
accumulated over time, and a unifying query mechanism that returns all
provenance for a given record (regardless of which mechanism recorded it)
does not yet exist. The `SlotLevelProvenance` class proposed in PR #3071
adds a missing piece (slot-level audit records) and articulates the
unifying-query goal; it does not subsume the existing mechanisms.

A working illustration of every in-schema mechanism in one Database
instance lives at
[`src/data/valid/Database-provenance-forms.yaml`](../data/valid/Database-provenance-forms.yaml).

## In-schema mechanisms

These are expressible as slot values on records in this schema. They
travel with the record and are visible to any consumer of nmdc-schema
data.

### 1. `ProvenanceMetadata` class

A small embedded class with slots for `add_date`, `mod_date`, `version`,
`git_url`, `source_system_of_record`, `submission_portal_identifier`,
`type`. Carried on records via a `provenance_metadata` slot. Wired onto
Biosample, OrganismSample, and several other top-level classes.

Captures: when the record entered NMDC, when it was last modified, the
schema version in effect at modification, the upstream source system,
and the originating submission portal entry.

Does NOT capture: who modified it, what slot changed, or why.

Caveat (per Alicia, 2026-03-06): records imported from GOLD before
~March 2026 may carry `add_date` / `mod_date` values reflecting GOLD's
dates rather than NMDC's ingest dates.

Query example:

```javascript
// All Biosamples in NMDC modified after a given date
db.biosample_set.find({"provenance_metadata.mod_date": {$gt: ISODate("2026-04-01")}})
```

### 2. `has_raw_value` (raw-vs-coerced pattern)

Required slot on every `AttributeValue` subclass (`TextValue`,
`QuantityValue`, `ControlledTermValue`, `TimestampValue`,
`ControlledIdentifiedTermValue`, `PropertyAssertion`, `GeoLocationNameValue`,
and others). Stores the value as the submitter wrote it, alongside the
parsed / typed / structured fields.

Captures: what the submitter wrote, so the original input is recoverable
after the schema applies a coercion or normalization.

Does NOT capture: when the coercion happened or who applied it.

See [`raw-vs-coerced.md`](./raw-vs-coerced.md) for the pattern in detail.

### 3. PROV-style timestamps on `WorkflowExecution`

`started_at_time`, `ended_at_time` (mapped to `prov:startedAtTime` /
`prov:endedAtTime`) plus `version`, `execution_resource`, `git_url`.

Captures: when each workflow ran and which version of which pipeline.

### 4. `was_informed_by` links

On `WorkflowExecution`. Points to the upstream `DataGeneration` instance
that the workflow processed.

Captures: a lineage edge from a workflow run to its informing data-
generation event.

### 5. `was_generated_by` on `DataObject`

Points to the process (a `DataEmitterProcess`, typically a
`WorkflowExecution` or `DataGeneration`) that produced the data object.

Captures: a lineage edge from a file to its producing process.

### 6. `superseded_by` on `DataObject` and `ReadQcAnalysis`

Self-referential pointer to a newer version of the same logical record.

Captures: that a record has been replaced; consumers should follow the
pointer to find the current version. The older record is retained.

### 7. DRS-stored changesheets (DataObjects with changesheet content)

Every executed changesheet is saved to MongoDB GridFS by `nmdc-runtime`
and registered as a `DataObject`-like DRS entry. The contents are the
TSV the curator submitted. The runtime uses `types: metadata-changesheet`
at the JSON level; there is not yet a dedicated `FileTypeEnum` value
for this in nmdc-schema.

Captures: full text of every applied changesheet, plus the submitting
user and timestamp.

Does NOT directly link to which documents were changed; reconstruction
requires replaying the sheet against the DB state at that timestamp.

Source: [`nmdc-runtime/nmdc_runtime/api/endpoints/metadata.py`](https://github.com/microbiomedata/nmdc-runtime/blob/main/nmdc_runtime/api/endpoints/metadata.py) (around lines 67-108 at this writing).

Query examples:

```javascript
// All stored changesheets in Mongo
db.objects.find({"types": "metadata-changesheet"})
```

```bash
# Or via the public API
curl -s "https://api.microbiomedata.org/objects/<drs_object_id>"
```

## Operational mechanisms (not in the schema)

These live in `nmdc-runtime` collections and sibling Mongo namespaces.
They are not expressible as instance data in this schema but are part
of NMDC's provenance story.

### 8. `nmdc_deleted` and `nmdc_updated` shadow databases

Sibling Mongo databases (not collections in `nmdc`). Before any delete
or update via `POST /queries:run`, the runtime copies the pre-image:

- Deletes → `nmdc_deleted.<collection_name>` with `{ "doc": <original>, "deleted_at": <datetime> }`
- Updates → `nmdc_updated.<collection_name>` with `{ "doc": <pre-update-doc>, "updated_at": <datetime> }`

Captures: the document as it was immediately before the mutation, with
a timestamp.

Does NOT capture: the actor (no username on the shadow copy).

Not exposed via the public API; accessible only by direct Mongo access.

Source: [`nmdc-runtime/nmdc_runtime/api/endpoints/queries.py`](https://github.com/microbiomedata/nmdc-runtime/blob/main/nmdc_runtime/api/endpoints/queries.py)
(around the `ran_at` / `insert_many_result` pattern, both `DeleteCommand`
and `UpdateCommand` branches).

Query (direct Mongo, in the parallel `nmdc_deleted` database):

```javascript
use nmdc_deleted
db.biosample_set.find({"doc.id": "nmdc:bsm-13-amrnys72"})
```

### 9. `txn_log` collection

Lightweight append-only log inside `nmdc` of every upsert through the
Dagster `RuntimeApiSiteClient` resource. Each record:

```json
{ "tgt": {"id": "<object_id>", "c": "<collection_name>"}, "type": "upsert", "ts": <datetime> }
```

Captures: object id + collection + timestamp + operation type.

Does NOT capture: actor, before/after content, or reason.

Source: [`nmdc-runtime/nmdc_runtime/site/resources.py`](https://github.com/microbiomedata/nmdc-runtime/blob/main/nmdc_runtime/site/resources.py)
(line 564 at this writing).

Query:

```javascript
// All upserts touching a particular record
db.txn_log.find({"tgt.id": "nmdc:bsm-13-amrnys72"})
```

### 10. `run_events` collection

Workflow-run events posted by the runtime. The closest thing NMDC has
to a W3C-PROV-compatible provenance graph. Each event records `run.id`,
`type` (STARTED, COMPLETED, FAILED, etc.), `time`, `inputs`, `outputs`,
`producer`, `job`.

Captures: which workflow produced which outputs from which inputs.

Does NOT capture: changes made by manual edits (changesheets, queries:run
mutations). Only workflow-automation activity is recorded here.

Source: [`nmdc-runtime/nmdc_runtime/api/endpoints/runs.py`](https://github.com/microbiomedata/nmdc-runtime/blob/main/nmdc_runtime/api/endpoints/runs.py).

Query (API):

```bash
curl -s "https://api.microbiomedata.org/runs/<run_id>/events"
```

### 11. Schema-migration notebooks

Jupyter notebooks at
[`nmdc-runtime/db/migrations/notebooks/`](https://github.com/microbiomedata/nmdc-runtime/tree/main/db/migrations/notebooks),
one per schema-version bump. They document the MongoDB mutations applied
to advance a database between schema versions (currently from `7.7.2`
through `11.17.x` and beyond).

Captures: schema-evolution history at the level of "going from version X
to version Y required these mutations."

Does NOT capture: when a given production database was migrated; that
needs to be cross-referenced from Git history and announcement channels
(`#squad-provenance`, `#infra-admin`).

Read these in the GitHub UI; they are human-readable, not directly
queryable as data.

### 12. `operations` collection (Dagster job lifecycle)

Tracks the full lifecycle of async Dagster jobs (request, status, result).
Feeds the Dagit UI. Related to `run_events` but at a higher level
(job-level rather than event-level).

Source: in `nmdc-runtime`'s Dagster wiring.

## Open gaps (what none of the mechanisms above capture)

| Question | Closest mechanism | What's still missing |
|---|---|---|
| Who specifically changed value X? | `nmdc_updated` shadow DB (no actor); changesheets DRS (actor at sheet level, not value level) | Per-slot actor attribution |
| What was the value before / after at the slot level? | `nmdc_updated` (whole-doc pre-image, requires diffing); changesheet TSV (requires replay) | Slot-level before/after |
| Why was a change made? | Changesheet TSV (free-text per sheet); none for runtime / migrator activity | Per-slot rationale |
| What slot changed within a record? | `nmdc_updated` (requires diff against current state) | Direct identification |
| How can I get all provenance about document X in one query? | None | A unified read interface |

The first four gaps are what the `SlotLevelProvenance` class proposed
in PR #3071 is designed to address. The unified-query gap is the
explicit binding design constraint on whatever shape ultimately ships.
