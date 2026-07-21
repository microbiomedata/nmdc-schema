# Deprecating `collection_date_inc`

`collection_date_inc` recorded when an incubation sample was harvested, separate
from the field `collection_date`
(https://github.com/microbiomedata/nmdc-schema/issues/2658). It is no longer
needed: an incubation is modeled as a `Culturing` process
(`is_a MaterialProcessing`) whose input and output are both `OrganismSample`.
`OrganismSample` carries `collection_date`, so the harvested culture's date is its
own `collection_date`, and the incubation window is `Culturing.start_date` and
`end_date`.

Worked, schema-valid example:
`src/data/valid/Database-incubation-as-culturing.yaml`.

`collection_date_inc` is empty in production (0 of 27,352 `biosample_set`
documents, checked 2026-07-21), so deprecation carries no migration risk.

Only `collection_date_inc` is deprecated. Whether the sibling slots
(`collection_time_inc`, `start_date_inc`, `start_time_inc`) should also be
deprecated is tracked in
https://github.com/microbiomedata/nmdc-schema/issues/3289.
