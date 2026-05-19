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

Query examples:

```javascript
// Biosamples whose env_broad_scale has_raw_value differs from a clean
// ENVO CURIE — revealing places where the ingest pipeline normalized
// a free-text label into a structured term
db.biosample_set.find({
  "env_broad_scale.has_raw_value": {$not: /^ENVO:\d+$/},
  "env_broad_scale.term.id": {$regex: /^ENVO:\d+$/}
}, {id: 1, "env_broad_scale.has_raw_value": 1, "env_broad_scale.term.id": 1})
```

```javascript
// Distinct raw vs coerced patterns across all has_raw_value occurrences
// on a particular slot — useful for auditing normalization consistency
db.biosample_set.aggregate([
  {$project: {
    raw: "$env_broad_scale.has_raw_value",
    coerced: "$env_broad_scale.term.id"
  }},
  {$group: {_id: {raw: "$raw", coerced: "$coerced"}, n: {$sum: 1}}},
  {$sort: {n: -1}},
  {$limit: 50}
])
```

### 3. PROV-style timestamps on `WorkflowExecution`

`started_at_time`, `ended_at_time` (mapped to `prov:startedAtTime` /
`prov:endedAtTime`) plus `version`, `execution_resource`, `git_url`.

Captures: when each workflow ran and which version of which pipeline.

Query examples:

```javascript
// Workflows that ran during a date window, sorted by duration descending
db.workflow_execution_set.aggregate([
  {$match: {
    started_at_time: {$gte: ISODate("2026-05-01"), $lt: ISODate("2026-06-01")}
  }},
  {$addFields: {
    duration_seconds: {
      $divide: [{$subtract: ["$ended_at_time", "$started_at_time"]}, 1000]
    }
  }},
  {$sort: {duration_seconds: -1}},
  {$limit: 20}
])
```

```javascript
// Distribution of pipeline versions across all workflow executions of one type
db.workflow_execution_set.aggregate([
  {$match: {type: "nmdc:MetagenomeAssembly"}},
  {$group: {_id: {version: "$version", git_url: "$git_url"}, n: {$sum: 1}}},
  {$sort: {n: -1}}
])
```

### 4. `was_informed_by` links

On `WorkflowExecution`. Points to the upstream `DataGeneration` instance
that the workflow processed.

Captures: a lineage edge from a workflow run to its informing data-
generation event.

Query examples:

```javascript
// All workflow runs informed by a particular DataGeneration
db.workflow_execution_set.find(
  {was_informed_by: "nmdc:dgns-11-foo"},
  {id: 1, type: 1, started_at_time: 1, has_output: 1}
)
```

```javascript
// How many runs of each workflow type were informed by each DataGeneration?
// (sanity check that no DataGeneration has surprisingly many reruns)
db.workflow_execution_set.aggregate([
  {$unwind: "$was_informed_by"},
  {$group: {
    _id: {informed_by: "$was_informed_by", type: "$type"},
    n: {$sum: 1}
  }},
  {$match: {n: {$gt: 3}}},
  {$sort: {n: -1}}
])
```

### 5. `was_generated_by` on `DataObject`

Points to the process (a `DataEmitterProcess`, typically a
`WorkflowExecution` or `DataGeneration`) that produced the data object.

Captures: a lineage edge from a file to its producing process.

Query examples:

```javascript
// All DataObjects produced by a particular workflow run
db.data_object_set.find(
  {was_generated_by: "nmdc:wfrqc-11-foo.1"},
  {id: 1, name: 1, data_object_type: 1, file_size_bytes: 1}
)
```

```javascript
// DataObjects that have no producing process recorded — candidates for
// in-source / uploaded raw data
db.data_object_set.find({was_generated_by: {$exists: false}}).count()
```

### 6. `superseded_by` on `DataObject` and `ReadQcAnalysis`

Self-referential pointer to a newer version of the same logical record.

Captures: that a record has been replaced; consumers should follow the
pointer to find the current version. The older record is retained.

Query examples:

```javascript
// All DataObjects that have been superseded (and what replaced them)
db.data_object_set.find(
  {superseded_by: {$exists: true}},
  {id: 1, name: 1, superseded_by: 1}
)
```

```javascript
// Follow a supersession chain: given any DataObject id, walk forward
// through superseded_by to find the current version
db.data_object_set.aggregate([
  {$match: {id: "nmdc:dobj-11-old"}},
  {$graphLookup: {
    from: "data_object_set",
    startWith: "$superseded_by",
    connectFromField: "superseded_by",
    connectToField: "id",
    as: "successor_chain"
  }}
])
```

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

Query examples:

```javascript
// Most recent Dagster operations
db.operations.find({}, {id: 1, metadata: 1, expire_time: 1}).sort({_id: -1}).limit(20)
```

```javascript
// Operations that affected a particular collection
db.operations.find({"metadata.collection_name": "biosample_set"}).sort({_id: -1})
```

## Researching bulk changes outside the schema

Slot-level provenance addresses single-record edits. Many of the
changes that actually happen to NMDC data are bulk transformations:
schema migrations, ETL re-runs, mass corrections, slot renames. None
of those are recorded per-record. Reconstructing them requires reading
code, release notes, and repository history. Here are the practical
recipes.

### Recipe A: Find every change to a specific slot in the schema

Use `git log -S` to find commits that added or removed lines containing
a string, and `git log -G` to find commits where lines matching a
regex were added or removed.

```bash
cd ~/gitrepos/nmdc-schema

# When was the slot env_broad_scale first defined? Most-recently changed?
git log --all -p -S '^  env_broad_scale:' -- src/schema/ | head -80

# Every commit that changed a slot's range
git log --all -p -G 'range: PropertyAssertion' -- src/schema/

# All commits touching a particular class's slot list
git log --all -p -L '/^  Biosample:/,/^  [A-Z]/' -- src/schema/core.yaml
```

`-L` is the most powerful for class-level history: it shows every
commit that touched the range from `^  Biosample:` to the next class
header, with full diffs.

### Recipe B: Find the PR that introduced a particular change

```bash
# Find the commit, then look up the PR
git log --all --oneline -S 'first_of_class_in_chain' -- src/schema/ | head -3
# Then: gh search prs --repo microbiomedata/nmdc-schema "<commit-sha>"
# Or directly:
gh search prs --repo microbiomedata/nmdc-schema "first_of_class_in_chain in:title" \
  --json number,title,mergedAt,author,mergedBy

# All PRs that touched a specific file across all of microbiomedata
gh search prs --owner microbiomedata "in:title organism" \
  --json number,title,repository,mergedAt --limit 30
```

### Recipe C: Read release notes for a specific version

nmdc-schema does not maintain a `CHANGELOG.md`. Use GitHub releases:

```bash
# List recent releases
gh release list --repo microbiomedata/nmdc-schema --limit 20

# Read the auto-generated release notes for one
gh release view v11.17.0 --repo microbiomedata/nmdc-schema

# Same for the runtime, which is where most ETL behavior changes
gh release list --repo microbiomedata/nmdc-runtime --limit 20
gh release view <version> --repo microbiomedata/nmdc-runtime
```

Release notes are derived from PR titles and labels. They are uneven
in detail but always tell you which PRs landed between two versions.

### Recipe D: Inspect schema migrators

nmdc-schema migrators are Python classes that mutate Mongo documents
to make them conform to a target schema version. They live at:

```
~/gitrepos/nmdc-schema/nmdc_schema/migrators/migrator_from_X_Y_Z_to_A_B_C.py
```

Each migrator's docstring and class body describe the transformations.
For a complete picture of how a database was migrated from version X to
version Y, read every migrator file with a name prefix in the range.

```bash
# Find migrators that touched a particular slot or class
grep -rln "env_broad_scale\|provenance_metadata" \
  ~/gitrepos/nmdc-schema/nmdc_schema/migrators/

# List all migrators between two versions, in order
ls ~/gitrepos/nmdc-schema/nmdc_schema/migrators/ \
  | grep -E "migrator_from_11_1[0-9]_" | sort
```

### Recipe E: Inspect runtime migration notebooks

nmdc-runtime contains Jupyter notebooks documenting end-to-end migration
runs against the production database, including any data fixes applied
that are not captured in the schema migrators themselves.

```
~/gitrepos/nmdc-runtime/db/migrations/notebooks/migrate_X_Y_Z_to_A_B_C.ipynb
```

41 notebooks at this writing, covering the transition history from
~`10.0.0` through `11.18.0`. They are read in the GitHub UI or any
notebook viewer; they are not machine-queryable as data.

```bash
# List notebooks bracketing a version transition
ls ~/gitrepos/nmdc-runtime/db/migrations/notebooks/ | grep -E "11_1[0-7]"

# Grep notebook contents for a specific slot or transformation
grep -rln "env_broad_scale" \
  ~/gitrepos/nmdc-runtime/db/migrations/notebooks/

# View a particular notebook on GitHub
open "https://github.com/microbiomedata/nmdc-runtime/blob/main/db/migrations/notebooks/migrate_11_17_0_to_11_17_1.ipynb"
```

### Recipe F: Correlate a record's mod_date with a known migration window

If a Biosample's `provenance_metadata.mod_date` falls near a migration
deploy, the migration is the likely cause of the mutation. To find when
a migration was actually deployed:

1. Look at the git timestamp of the migrator file (when it was merged
   to main).
2. Cross-reference with Slack announcements in `#infra-admin` and
   `#squad-provenance` (search for the schema version string and the
   migrator class name).
3. The runtime's `txn_log` collection records the upsert timestamp for
   every migrator-driven write.

```bash
# When did the v11.17.0 migrator land in main?
cd ~/gitrepos/nmdc-schema
git log --all --pretty=format:'%h %ad %s' --date=short \
  -- nmdc_schema/migrators/migrator_from_11_16_*to_11_17*.py | head -3

# When was the v11.17.0 release published?
gh release view v11.17.0 --repo microbiomedata/nmdc-schema \
  --json publishedAt --jq .publishedAt
```

### Recipe G: Search PRs by author + time + scope

```bash
# All schema PRs by a particular author in a window
gh search prs --repo microbiomedata/nmdc-schema \
  --author <username> --merged \
  --created '>=2026-01-01' --json number,title,mergedAt | head

# All PRs that closed an issue with a specific label
gh search prs --repo microbiomedata/nmdc-schema \
  "label:cleanup is:merged" --json number,title,mergedAt | head
```

### Recipe H: Find what was happening operationally on a given date

Beyond code: contemporaneous Slack messages, BBOP group-meetings
issues, and the NMDC Sync rolling-notes Google Doc all carry context
that does not land in git or releases. The Slack-nmdc MCP and
`gog drive` are the practical entry points.

```bash
# Search Slack-nmdc for messages near a date
# (use the slack-nmdc MCP slack_search_public_and_private tool with
#  after: / before: date filters; mentions of class names, slot names,
#  or migrator filenames are usually the highest-signal hits)

# Read the NMDC Sync rolling notes
gog docs read 1mjICSt3C7bDqgTWc0BrWReuX9UzxqEv5AfEdeMDqLXU
```

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
