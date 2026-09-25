# Proposal: ecosystem deprecation audit

Status: proposed, with a bounded feasibility pilot performed on 2026-09-16. The
organization-wide scanner, complete historical catalog, and scheduled runs are not yet
implemented. This complements the repository-local asset check proposed in
[PR #3423](https://github.com/microbiomedata/nmdc-schema/pull/3423).

Retired schema names can remain in consumer code, mapping tables, notebooks, and
documentation. Some references must remain, including frozen migrations and invalid
examples. The goal is to make the references visible, identify current dependencies,
and record intentional historical uses.

## Scope

Recurring scans cover the current default branch of each active (non-archived)
repository in `microbiomedata`, including active forks. Enumerate repositories and
re-evaluate their archived status and default branch on every run. Record inaccessible
repositories as coverage gaps; the inventory is limited by the audit credential's access.

The only intentional source exclusion is the exact repository/path pair
`microbiomedata/nmdc-schema:src/schema/deprecated.yaml`. Copies elsewhere remain in
scope. Search current documentation, generated files, notebooks, fixtures, migrations,
and assets. Keep their matches visible and classify their purpose.

Historical discovery has a different scope: examine nmdc-schema's merged history and
release tags to learn which names were removed or renamed. Old tags and non-default
branches are not part of recurring scans for current references.

## A catalog with explicit evidence

| Origin | Source | Meaning |
|---|---|---|
| Explicitly retired | Definitions in `src/schema/deprecated.yaml` at the selected schema commit | Read afresh each run; no manually maintained duplicate |
| Historically removed or renamed | Reviewed changes to schema definitions in merged history | A retired name with evidence and a replacement when established |
| Historical candidate | A definition disappeared but its disposition is unresolved | Visible for investigation; not yet an established deprecation |

An optional early-warning view can include active definitions carrying a `deprecated:`
annotation. Keep these distinct: they are still available during the first release cycle.

Identify elements by kind and namespace. Identify permissible values by enum and value,
so removing a value from one enum does not retire that spelling globally. Record a slot's
removal from a particular class separately from retirement of the slot itself.

A historical record should contain the old name, kind, scope, disposition, verified
replacement if any, source path, before/after commits, date, first affected release when
known, PR/issue links, rationale, and review status. Preserve lifecycle intervals when a
name was removed and later reinstated.

## One historical backfill, then incremental maintenance

Produce both a reviewed machine-readable catalog and a dated narrative report. A static
document alone cannot supply names to future scans or reliably record subsequent changes.

1. Establish the schema's historical source roots and import layouts. A fixed
   `src/schema/` path misses earlier layouts.
2. Compare structured definition inventories across releases and relevant commits.
   Compare the union across source modules and, where reconstructable, the effective
   imported/exported schema. Distinguish source-inventory changes from confirmed changes
   to the exported schema when historical dependency resolution is uncertain.
3. Treat disappearance as a candidate. Check moves, changes to upstream imports,
   generated-file refreshes, renames, reversions, and reinstatements. A deleted description
   or a removed use of a still-existing slot does not retire the element.
4. Use diffs as evidence and associated PRs, issues, migrators, release notes, and commit
   messages to interpret them. Do not infer a replacement solely from similar names.
5. Review candidates, preserve unresolved cases, and record the history tip and release
   range examined. Subsequent maintenance processes new changes rather than rediscovering
   the entire history.

Only recoverable history can be assessed. Missing or rewritten commits, unavailable
historical dependencies, and parse failures are coverage gaps. A parse failure must not
be treated as an empty schema from which all definitions have disappeared.

Two verified examples illustrate the distinction:

- [c4f516bb5](https://github.com/microbiomedata/nmdc-schema/commit/c4f516bb5ebe360daa74253ff5509a800e06dc71)
  renamed `OmicsProcessing` to `DataGeneration` and `omics_processing_set` to
  `data_generation_set` in December 2023. It retained the old class name as an alias.
  The retired spelling belongs in the catalog; the alias is an intentional reference.
- [2d059e962](https://github.com/microbiomedata/nmdc-schema/commit/2d059e9626a5179c07535956442e63c7e92ad198)
  moved the schema directory. Deleted definition lines in that change do not indicate
  retirement of the classes and slots being moved.

## Scan pinned repository snapshots

Enumerate repositories through the paginated organization API, select active repos,
resolve their default-branch commit SHAs, and fetch into an isolated cache. Scan Git
objects at those revisions rather than developers' working trees. Record collection
time per repository: an organization scan is a set of pinned snapshots, not an atomic
snapshot of all repositories. Cache unchanged blobs for repeat scans.

Enumerate every tracked entry and give it a coverage status:

- Scan text contents and paths without a filename-extension allowlist or a small-file
  size cutoff. Stream large files. Match identifier boundaries so `ChemicalEntity` does
  not match `ChemicalEntityEnum`.
- Extract supported notebook, Office, PDF, and archive contents, retaining cell, page,
  or member locations. Distinguish notebook source from output. Record extraction and
  resource limits explicitly.
- Resolve pinned LFS payloads and submodule revisions when accessible; otherwise record
  them as unscanned. A scanned pointer is not a scanned payload.
- Record unsupported binary formats, decoding failures, symlinks, unavailable repos,
  and empty repositories. Do not follow symlinks outside the snapshot or turn a failed
  fetch into a clean result.

Coverage reporting must distinguish repositories enumerated, out of scope, scanned,
and unavailable, together with files scanned or unsupported. Arbitrary binary formats
and dynamically assembled identifiers prevent a universal semantic guarantee about
every reference. A lexical match requires interpretation too.

GitHub code search is a discovery aid, not the coverage mechanism. Its
[legacy index](https://docs.github.com/en/search-github/searching-on-github/searching-code)
excludes archived repositories, restricts fork coverage, and searches files smaller than
384 KB. The [GitHub CLI uses that engine](https://cli.github.com/manual/gh_search_code).
The fork and file-size limits matter even with active default branches as the scan scope.

## Triage without hiding references

Preserve raw matches and attach a reviewed disposition:

| Disposition | Examples | Action |
|---|---|---|
| Current dependency | Import config, active transform, query, or schema | Update consumer or coordinate a release |
| Current documentation or data appears stale | Valid examples, mapping tables, generated current docs | Correct, regenerate, or retire |
| Intentional compatibility or history | Frozen migrators, invalid examples, changelogs, aliases, audit catalogs | Retain with a reason |
| Unrelated spelling or unresolved | Ordinary use of `Pathway`, ambiguous enum value, uncertain script use | Mark unrelated or investigate |

Path-based classification can suggest a disposition but cannot establish it. Do not
edit released migrators just to remove matches. If a repository becomes archived,
retain its earlier findings as history and label it out of scope; that is not a resolved
reference.

Each finding needs the repository, commit, path, location, element identity, origin,
context, permalink, review disposition, reason, and any follow-up issue or assigned
owner. Match identity should survive line-number shifts. Recheck acknowledgments when
the relevant content changes. Distinguish newly introduced references from old references
newly discovered because the catalog expanded.

Store machine-readable findings and coverage manifests as run artifacts. Generate a
dated Markdown or HTML report showing new, resolved, acknowledged, and unreviewed
matches. Public summaries must contain public-repository evidence only; store private
findings with equivalent access restrictions. If reports or catalogs are committed in
scanned repos, classify their matches as audit evidence rather than suppressing them.

## Feasibility pilot

On 2026-09-16, a text-content pilot searched the following pinned default-branch
snapshots against 31 names in nmdc-schema's `deprecated.yaml` (7 classes and 24 slots)
and the two verified December 2023 rename seeds above. The schema source revision was
`135349819d0bc0db674330bccf0e6b6a008bbb6b`.

| Repository and scanned commit | Tracked blobs | Files with matches | Element/line pairs |
|---|---:|---:|---:|
| [nmdc-schema](https://github.com/microbiomedata/nmdc-schema/tree/135349819d0bc0db674330bccf0e6b6a008bbb6b) | 731 | 44 | 336 |
| [submission-schema](https://github.com/microbiomedata/submission-schema/tree/5bb3d0ff33ed53d5043dc6404985f596b8d5d249) | 284 | 3 | 4 |
| [nmdc-runtime](https://github.com/microbiomedata/nmdc-runtime/tree/dd4b8b90cc58283cfabf41ef1d61b85057d2deeb) | 377 | 12 | 32 |
| [nmdc-lakehouse](https://github.com/microbiomedata/nmdc-lakehouse/tree/891129957730cc61394ef265567356282f4e3a6e) | 154 | 0 | 0 |

The pilot used `git grep -n -I -w -F` with one name per pattern-file line, searching
the pinned commit rather than the working tree. It excluded only this repository's
`src/schema/deprecated.yaml`. Each element was counted once per matching line; different
elements on the same line counted separately. A corresponding invocation is:

```sh
git grep --no-color -n -I -w -F -f /path/to/retired-names.txt COMMIT -- .
# For nmdc-schema, append the exact exclusion:
# ':(exclude)src/schema/deprecated.yaml'
```

This pilot did not scan filenames, binary contents, LFS payloads, submodules, or the
full historical catalog. These are lexical observations, not defect counts. The
submission-schema matches are invalid examples and commented-out fields. Runtime
matches include a migration notebook, comments, fixtures, and executable code requiring
review. Zero lakehouse matches apply only to these 33 names and the scanned text at
that revision.

## Implementation sequence

1. Complete the bounded asset-check corrections in PR #3423.
2. Build and review the historical catalog, preserving both extraction tooling and the
   dated report. Add new removal and rename records during subsequent schema maintenance.
3. Run the complete baseline scan of active repositories' default branches. Publish
   coverage and triage the backlog. Use read-only credentials with access to the intended
   repositories; a workflow's default token need not cover other repositories.
4. Schedule a weekly report, support an on-demand pre-release run, and run again when
   the retirement catalog changes.
5. Add a deterministic schema-PR check for newly removed definitions requiring a recorded
   disposition. Keep cross-repository network scans out of ordinary `make test`.

Start with reporting. After triage, consider alerts for new actionable matches or
acknowledgments needing review. A permanent zero-mention gate would conflict with
necessary migration history and invalid test cases.
