# Subsets in the NMDC schema

LinkML subsets are named tags. A subset is declared once in a `subsets:` block,
and any element (class, slot, permissible value) can claim membership with
`in_subset`. Subsets do not change validation. They group elements for
documentation, tooling, and metadata-quality scoring.

Every subset in the merged schema is declared in `src/schema/basic_slots.yaml`.
There were once two other populations, and both are gone; the sections below
record what happened to them so the question does not get re-litigated.

## Live subsets

| subset | members | purpose |
| --- | --- | --- |
| `jgi_isolate` | 9 | slots that map to a field on the JGI Isolate (NA) v19 submission form |
| `badge_topic` | 2 | group subset: its members are the completeness badge subsets |
| `biogeochemistry` | 44 | completeness badge subset, bar 2 |
| `host_association` | 35 | completeness badge subset, bar 2 |

A slot may belong to more than one subset. `host_genus`, `host_species` and
`host_strain` are in both `jgi_isolate` and `host_association`.

## MIxS subsets are stripped during the `mixs.yaml` build

Upstream GSC MIxS declares 5 subsets: `combination_classes`, `sequencing`,
`environment`, `nucleic acid sequence source`, and `investigation`. MIxS tags
its slots into these with `in_subset`.

NMDC does not use the MIxS checklist and section machinery, so the `mixs.yaml`
build strips both the declarations and the memberships. In
`assets/yq-for-mixs-customizations.txt`:

- `'del(.subsets)'` removes the declarations.
- `'del(.slots.[].in_subset)'` removes the per-slot memberships.

The same file then re-adds NMDC badge memberships. **The ordering matters**:
anything added before the strip would be deleted by it.

## The former `nmdc_subsets.yaml`

`src/schema/nmdc_subsets.yaml` declared 9 subsets and was imported by nothing.
None of them reached the merged schema and no element referenced any of them. It
was deleted in
https://github.com/microbiomedata/nmdc-schema/pull/3338; the reasoning, and where
each subset's intent went, is in
https://github.com/microbiomedata/nmdc-schema/issues/3337.

Two of its entries are worth remembering, because they will come up again:

- `data_portal_subset` was meant to mark elements the data portal depends on, so
  schema authors would know whom to notify before changing them. Nothing was ever
  labeled, so the obligation was never in force. The question is still open in
  https://github.com/microbiomedata/nmdc-schema/issues/1342, and badges make it
  concrete: they are a portal-facing schema feature.
- `proteases` anticipated chemicals becoming classes that would need grouping.
  They did not. `ChemicalEntity` is in `deprecated.yaml` and proteases are enum
  permissible values in `core.yaml`.

## Badge subsets

A badge subset groups the slots whose completeness one metadata-quality badge
measures. It is declared in `src/schema/basic_slots.yaml` and is itself a member
of the `badge_topic` group subset (`in_subset: [badge_topic]`), which is how
tooling and the sync test tell badge subsets apart from `jgi_isolate`. This uses
the native subset mechanism rather than a custom annotation.

Membership follows the metadata quality squad's Badge Subsets Scratchpad. Most
members are MIxS slots defined in the generated `mixs.yaml`, so their membership
cannot be hand-edited on the slot and is asserted in
`assets/yq-for-mixs-customizations.txt` after the strip described above. Twelve
members are NMDC-native (7 biogeochemistry, 5 host) and carry `in_subset` in
their own definitions.

### The qualifying bar

Each badge subset carries a `badge_minimum_slots` annotation: how many of its
slots a record must populate to earn the badge
(https://github.com/microbiomedata/nmdc-schema/issues/3326).

The bar is an **absolute count of populated slots, never a proportion of the
subset's size**. This is what makes badges stable as the schema grows. Under an
absolute bar, adding a slot to a subset can only ever make a badge easier to
earn, so no record loses a badge it already displays because the schema changed
around it. A proportional bar would revoke badges on any subset that grows, which
users would experience as a badge disappearing for no reason.

The bar lives in the schema so that raising it is a reviewable pull request with
a visible diff, rather than an edit to a scoring service's configuration.

### Badges that are not completeness measures

Not every badge has a subset. `MetadataBadgeEnum` also carries `expert_curation`,
which is awarded from `ProvenanceMetadata.source_system_of_record` (did this
record come through the NMDC submission portal, or from an ETL process over an
external database) rather than from how many slots are populated. It has no badge
subset and no `badge_minimum_slots`, and its enum description says where it comes
from. The sync test exempts it through an explicit `PROVENANCE_BADGES` list, so
adding another such badge is a deliberate act rather than a silent gap.

A badge is present or absent. There are no levels or tiers (metadata quality
squad decision, 2026-08-05).

The badge subsets correspond one-to-one with the completeness permissible values
of `MetadataBadgeEnum`, the range of the `badges` slot on `Biosample`.

See https://github.com/microbiomedata/nmdc-schema/issues/3227 (badges slot and
enum), https://github.com/microbiomedata/nmdc-schema/issues/3228 (subsets) and
https://github.com/microbiomedata/nmdc-schema/issues/3326 (qualifying bar).
