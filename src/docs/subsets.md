# Subsets in the NMDC schema

LinkML subsets are named tags. A subset is declared once in a `subsets:` block,
and any element (class, slot, permissible value) can claim membership with
`in_subset`. Subsets do not change validation. They group elements for
documentation, tooling, and (now) metadata-quality scoring.

This page explains three separate populations of subsets that are easy to
confuse: the MIxS subsets we remove during the build, an orphan NMDC subsets
file that is not wired into the schema, and the badge subsets we add.

## 1. MIxS subsets (removed during `mixs.yaml` generation)

Upstream GSC MIxS declares 5 subsets: `combination_classes`, `sequencing`,
`environment`, `nucleic acid sequence source`, and `investigation`. MIxS tags
its slots into these with `in_subset`.

NMDC does not use the MIxS checklist and section machinery, so the `mixs.yaml`
build strips both the declarations and the memberships. In
`assets/yq-for-mixs-customizations.txt`:

- `'del(.subsets)'` removes the declarations.
- `'del(.slots.[].in_subset)'` removes the per-slot memberships.

After that strip, the same file re-adds NMDC badge memberships (population 3).
The ordering matters: anything added before the strip would be deleted.

## 2. The orphan `nmdc_subsets.yaml` (declared but not imported)

`src/schema/nmdc_subsets.yaml` declares 9 subsets: `data object subset`,
`data_portal_subset`, `environment`, `investigation`,
`nucleic acid sequence source`, `proteases`, `sample subset`, `sequencing`,
`workflow subset`.

This file is **not imported by any schema**, so none of these subsets reach the
materialized schema, and nothing references them. The active schema uses none of
these names. The file is inert.

Its relationship to population 1 is the source of the confusion: 4 of its 9
names (`environment`, `sequencing`, `investigation`,
`nucleic acid sequence source`) are copied from the MIxS subsets, and those 4
are exactly the entries left without a description. The other 5
(`data object subset`, `data_portal_subset`, `sample subset`, `workflow subset`,
`proteases`) are NMDC-authored and carry descriptions. So the file is a stale,
never-activated mix of copied MIxS names and NMDC-authored names. It is a
candidate for removal, tracked separately from the badge work.

## 3. Badge subsets (added, active)

Badge subsets group the slots that a metadata-quality badge is scored against.
They are declared in `src/schema/basic_slots.yaml` and are themselves members of
the `badge_topic` group subset (`in_subset: [badge_topic]`), which is how tooling
and the sync test tell them apart from other subsets (for example `jgi_isolate`,
which is not a badge topic). This uses the native subset mechanism rather than a
custom annotation.

Current badge subsets:

| subset | members | scored slots |
| --- | --- | --- |
| `biogeochemistry` | 24 | measured chemical analytes (N, P, C, S, Fe, core physicochemistry, gases) |
| `land_use_and_vegetation` | 17 | current vegetation, land-use history, management, soil and site context |

Most members are MIxS slots defined in the generated `mixs.yaml`, so their
membership cannot be hand-edited on the slot. It is asserted in
`assets/yq-for-mixs-customizations.txt`, after the MIxS `in_subset` strip
described in population 1.

The badge subsets are mirrored by the `MetadataBadgeEnum` permissible values
(`<topic>_<level>`, for example `biogeochemistry_gold`), the range of the
`badges` slot. Which classes carry the `badges` slot is decided in separate
attachment PRs, not here. A test keeps the enum and the badge subsets in sync:
every badge-topic subset has matching permissible values, and every permissible
value resolves to a badge-topic subset.

See https://github.com/microbiomedata/nmdc-schema/issues/3227 (badges slot and
enum) and https://github.com/microbiomedata/nmdc-schema/issues/3228 (subsets).

## Summary

| population | where | status | tags |
| --- | --- | --- | --- |
| MIxS subsets | upstream MIxS | removed in build | slots |
| orphan NMDC subsets | `nmdc_subsets.yaml` | inert, not imported | none active |
| `jgi_isolate` | `basic_slots.yaml` | active | slots |
| badge subsets | `basic_slots.yaml` + mixs customizations | active | slots |
