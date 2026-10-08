# MongoDB queries for checking NMDC data

These are mongosh scripts for checking an NMDC MongoDB database by hand. Nothing in the build, the tests, or other microbiomedata repositories runs them. They were written in 2024 for https://github.com/microbiomedata/nmdc-schema/issues/1865 and https://github.com/microbiomedata/nmdc-schema/issues/1880.

For a full referential integrity check, use [refscan](https://github.com/microbiomedata/refscan) instead. It reads the schema to find every slot that refers to another record and checks all of them, while each query here checks one slot. The queries are still useful for a quick look at one relationship, or for listing the offending records.

## Running a query

Pipe the file into mongosh:

```shell
mongosh "mongodb://<user>@<host>:<port>/nmdc?authSource=admin" < assets/mongodb_queries/data_qc/biosample_part_of_study.js
```

`mongosh --file` runs the query but does not print the results of an `aggregate(...)` that ends a script, so use the pipe form above, or paste the query into an interactive mongosh session or MongoDB Compass. `data_object_was_generated_by_workflow_execution_or_data_generation.js` prints its own results, so it works either way.

## Queries that find problems (read-only)

Each query returns the records with a problem, so an empty result means the check passed.

| file | returns |
|---|---|
| `data_qc/biosample_part_of_study.js` | Biosamples whose `associated_studies` matches no `study_set` record |
| `data_qc/data_generation_associated_studies.js` | Data generation records whose `associated_studies` matches no `study_set` record |
| `data_qc/data_generation_has_input_biosample_or_processed_sample.js` | Data generation records whose `has_input` matches neither a biosample nor a processed sample |
| `data_qc/data_generation_has_output_data_objects.js` | Each data generation `has_output` value that matches no `data_object_set` record |
| `data_qc/data_object_was_generated_by_workflow_execution_or_data_generation.js` | Data objects whose `was_generated_by` matches neither a workflow execution nor a data generation record |
| `data_qc/functional_annotation_agg_metagenome_metatranscriptome_annotation_id.js` | `functional_annotation_agg` records whose `was_generated_by` matches no workflow execution. The collection has tens of millions of records, so this one is slow; add a `$match` on `was_generated_by` to check one workflow |
| `data_qc/material_processing_has_input_biosample_or_processed_sample.js` | Material processing records whose `has_input` matches neither a biosample nor a processed sample |
| `find_id_nonconforming_data_objects.js` | Data objects whose `id` does not contain `nmdc:dobj-` |

On 2026-10-08 every query in this table except the `functional_annotation_agg` one returned no records against the production database ([issue 3492](https://github.com/microbiomedata/nmdc-schema/issues/3492)).

## One-off cleanup scripts (these delete data)

Do not run these to check data. They delete records, and they were written for specific cleanups in 2024.

| file | deletes |
|---|---|
| `delete_bioscales_data_objects.js` | Data objects with non-NMDC ids and the description "Raw sequencer read data", left over from the Bioscales study |
| `delete_data_generation_has_output_ref_integrity_exceptions.js` | Every data generation record that has at least one `has_output` value matching no data object. It deletes the whole record, not only the bad value |

On 2026-10-08 neither script matched any record in the production database.
