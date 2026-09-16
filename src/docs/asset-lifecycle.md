# Retiring a file from `assets/`

`assets/` holds inputs to the build (for example `assets/import_mixs_slots_regardless.tsv`,
which decides which MIxS slots are imported), a few committed reports, and reference data
kept by hand. It is no longer the default place to write generated output; see the
output-destination row in the policy table in
[CONTRIBUTING.md](https://github.com/microbiomedata/nmdc-schema/blob/main/CONTRIBUTING.md).

A file that lands there and is then named by nothing has no way to fail. It is not
regenerated, so it does not get refreshed; it is not read, so a wrong value never surfaces.
It just sits at whatever the schema looked like on the day it was written. Two consequences
have already been paid for:

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

`tests/test_no_new_unreferenced_assets.py` enforces this going forward. It runs in `make
test` and so in CI. Files that predate the check are listed in its allowlist, grouped with
the reason each is still there and the issue tracking its retirement.

## Checking one file

Run the report:

```bash
make report-asset-usage
```

It prints three lists: assets referenced nowhere in this repo, assets naming an element
defined in `src/schema/deprecated.yaml`, and the intersection. A file in the third list can
be deleted without a remapping decision, because nothing reads it and the elements it names
are retired.

The report only sees this repository. Before deleting, check the rest of the organization,
because another repo can read a raw GitHub URL without any local reference:

```bash
gh search code --owner microbiomedata "<filename without extension>"
```

Zero results there plus zero references here is the evidence to act on. Record both in the
pull request. Worked example: `assets/misc/neon_nmdc_term_mapping.tsv` was deleted on
2026-08-26 after `gh search code --owner microbiomedata neon_nmdc_term_mapping` returned
nothing and a grep across every local clone of `nmdc-runtime`, `nmdc-server`,
`nmdc-lakehouse`, and `external-metadata-awareness` returned nothing.
NEON (National Ecological Observatory Network) ingest, which might have used it, does its
own term mapping in `nmdc_runtime/site/translation/neon_soil_translator.py` and siblings.

Deleting it also moots
[write tests about assets/misc/neon_nmdc_term_mapping.tsv divergence from schema](https://github.com/microbiomedata/nmdc-schema/issues/1703),
open since 2024-01-23, which asked for a test that would detect the divergence. There is no
divergence to detect once the file is gone, and the general version of what it asked for is
the report and ratchet described above.

## Retiring one

1. Confirm it is unreferenced here and in the organization, as above.
2. Delete it with `git rm`. Git history is the archive; there is no need to keep a copy in
   the tree. This is the same disposition as
   [Remove SPARQL query files and unreferenced OWL customization artifact](https://github.com/microbiomedata/nmdc-schema/pull/3132),
   which removed `assets/sparql/*.rq`, and commit `bb2ba3f73`, which removed manually
   regenerated outputs.
3. Remove its entry from the allowlist in `tests/test_no_new_unreferenced_assets.py`. The
   test fails if an allowlisted path stops being unreferenced or stops existing, so the list
   cannot drift into fiction.
4. Say in the pull request how you know nothing uses it. A reader a year from now cannot
   redo the search from a claim that it was unused.

If the file is referenced but stale, regenerate it instead of deleting it, and check whether
its Makefile target is a prerequisite of anything. If it is not, nothing will regenerate it
next time either, which is the actual defect.

## Deprecation is the usual trigger

Retiring a schema element is what most often exposes a stale asset, because the element name
is what makes the staleness visible. The second release cycle of
[the deprecation guide](schema_element_deprecation_guide.md) now includes a step for this.

Two limits worth knowing before trusting the check:

- It reads element names out of `src/schema/deprecated.yaml`, so it only sees elements that
  have completed the second release cycle. An element marked deprecated but not yet moved is
  invisible to it. So is a rename: `OmicsProcessing` became `DataGeneration` without passing
  through `deprecated.yaml`, and the check does not flag the assets that still name it.
- Permissible values cannot be moved into `deprecated.yaml` at all, so a retired permissible
  value is never flagged. Deleting it and noting the removal in the release notes is the
  current practice.
