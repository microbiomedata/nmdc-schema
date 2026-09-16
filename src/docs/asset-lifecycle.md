# Retiring a file from `assets/`

`assets/` holds inputs to the build (for example `assets/import_mixs_slots_regardless.tsv`,
which decides which MIxS slots are imported), a few committed reports, and reference data
kept by hand. It is no longer the default place to write generated output; see the
output-destination row in the policy table in
[CONTRIBUTING.md](https://github.com/microbiomedata/nmdc-schema/blob/main/CONTRIBUTING.md).

An asset without a maintained consumer or regeneration step can stay unchanged as the
schema evolves. Searching for references helps identify files needing review, although
the absence of a literal filename does not prove that a file is unused. Two examples of
stale assets illustrate the problem:

- `assets/schema_pattern_linting.txt` was last regenerated on 2025-12-03 (commit
  `086cb897a`). On 2026-02-13, commit `11139a97a` moved `chemical_entity_set`, `inchi`,
  `inchi_key`, and `smiles` into `src/schema/deprecated.yaml`. The committed report still
  lists all four as slots with no class, which stopped being true that day.
- `src/scripts/ncbi_nmdc_exact_term_matching.py` broke because it referenced the
  `OmicsProcessing` class, removed in v11. Recorded in
  [Test regeneration of assets after CLI alias removal](https://github.com/microbiomedata/nmdc-schema/issues/2762).
  The script was fixed. Its committed output was not, and
  `assets/ncbi_mappings/ncbi_attribute_mappings.tsv` still carries a 35-row
  `OmicsProcessing` block.

## The rule

Every file tracked under `assets/` must be named by something else in the repo: a Makefile
target that builds it, a script or test that reads it, or a document that explains what it
is for. If none of those is true, it is a retirement candidate.

`tests/test_no_new_unreferenced_assets.py` checks for literal references going forward. It
runs in `make test` and so in CI. Files that predate the check are listed in its allowlist,
grouped with the reason each is still there and the issue tracking its retirement. Audit
prose and the detector's own fixtures do not count as consumers. An actual consumer using
a constructed path may need a documentation reference or a reasoned allowlist entry.

## Checking one file

Run the report:

```bash
make report-asset-usage
```

It prints three lists: assets with no literal reference found in the searched repository
files, assets naming an element defined in `src/schema/deprecated.yaml`, and the intersection.
Files in the third list are priorities for retirement review. Check consumers before
deciding to delete, regenerate, or retain them.

The report only sees this repository. Before deleting, check the rest of the organization,
because another repo can read a raw GitHub URL without any local reference. This preliminary
search filters out this repository's own matches:

```bash
gh search code --owner microbiomedata "<filename without extension>" \
  --limit 1000 --json repository,path,url \
  --jq '.[] | select(.repository.nameWithOwner != "microbiomedata/nmdc-schema")'
```

Zero results are supporting evidence, not proof of non-use. The
[GitHub CLI uses the legacy code-search index](https://cli.github.com/manual/gh_search_code),
which has coverage restrictions, and results may reach the requested limit. Inspect likely
consumer repositories directly, including scripts that construct paths or use globs.
Record repository revisions, search terms, coverage gaps, and the retirement rationale in
the pull request. A failed or incomplete search must not be reported as zero matches.

Worked example: the metadata squad decided on 2026-08-26 to delete
`assets/misc/neon_nmdc_term_mapping.tsv`. The investigation found no code-search hits and
no filename references in the local clones of `nmdc-runtime`, `nmdc-server`,
`nmdc-lakehouse`, and `external-metadata-awareness` that it checked.
NEON (National Ecological Observatory Network) ingest, which might have used it, does its
own term mapping in `nmdc_runtime/site/translation/neon_soil_translator.py` and siblings.

Deleting it also moots
[write tests about assets/misc/neon_nmdc_term_mapping.tsv divergence from schema](https://github.com/microbiomedata/nmdc-schema/issues/1703),
open since 2024-01-23, which asked for a test that would detect the divergence. There is no
divergence to detect once the file is gone, and the general version of what it asked for is
the report and ratchet described above.

## Retiring one

1. Review local and external consumers, as above, and record the evidence supporting retirement.
2. Delete it with `git rm`. Git history is the archive; there is no need to keep a copy in
   the tree. This is the same disposition as
   [Remove SPARQL query files and unreferenced OWL customization artifact](https://github.com/microbiomedata/nmdc-schema/pull/3132),
   which removed `assets/sparql/*.rq`, and commit `bb2ba3f73`, which removed manually
   regenerated outputs.
3. Remove its entry from the allowlist in `tests/test_no_new_unreferenced_assets.py`. The
   test fails if an allowlisted path stops being unreferenced or stops existing, so the list
   cannot drift into fiction.
4. Say in the pull request what you checked and why retirement is appropriate. A reader a
   year from now cannot redo the search from a claim that the file was unused.

If the file is referenced but stale, regenerate it instead of deleting it, and check whether
its Makefile target is a prerequisite of anything. If it is not, nothing will regenerate it
next time either, which is the actual defect.

## Deprecation is the usual trigger

Retiring a schema element is what most often exposes a stale asset, because the element name
is what makes the staleness visible. The second release cycle of
[the deprecation guide](schema_element_deprecation_guide.md) now includes a step for this.

Limits worth knowing before trusting the check:

- Reference detection searches selected text formats in tracked files. It excludes generated
  trees, `assets/` itself, and audit prose; see `SEARCHABLE_SUFFIXES`, `ROOT_EXCLUDED_DIRS`,
  and `AUDIT_FILES` in `src/scripts/report_asset_usage.py` for the exact scope. It does not
  resolve dynamically constructed paths or establish that a textual mention is a live dependency.
- It reads element names out of `src/schema/deprecated.yaml`, so it only sees elements that
  have completed the second release cycle. An element marked deprecated but not yet moved is
  invisible to it. So is a rename: `OmicsProcessing` became `DataGeneration` without passing
  through `deprecated.yaml`, and the check does not flag the assets that still name it.
- Permissible values cannot be moved into `deprecated.yaml` at all, so a retired permissible
  value is never flagged. Deleting it and noting the removal in the release notes is the
  current practice.
