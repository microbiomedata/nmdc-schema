```shell
git diff --name-only HEAD^ | grep -v examples/output
```

There some other files that have beena added in other PRs between v7.7.2 and now

### handcrafted
* OmicsProcessing-to-catted-Biosamples.rq

### output from OmicsProcessing-to-catted-Biosamples.rq, with tidying
* OmicsProcessing-to-catted-Biosamples.tsv

### Infrastructure
* poetry.lock
* pyproject.toml
  * pure-export = "nmdc_schema.mongo_dump_api_emph:cli"
  * migration-recursion = 'nmdc_schema.migration_recursion:main'
  * anyuri-strings-to-iris = 'nmdc_schema.anyuri_strings_to_iris:expand_curies'

### routinely regenerated... but change that!
* src/schema/mixs.yaml

### regenerate with nmdc_schema/class_sparql.py
* Biosample.rq
* OmicsProcessing.rq
* OmicsProcessing.tsv

### project/
project/prefixmap/nmdc.json is generated as a YAML file. We're renaming it in Makefile's `gen-project` target 
There's a LinkML issue: ???

see also:
* assets/misc/extra_prefix_expansions.yaml
* project/jsonld/nmdc.context.jsonld
* hardcoded prefix expansions in nmdc_schema/class_sparql.py

----

* nmdc_schema/nmdc_schema_accepting_legacy_ids.yaml
  * not really new, but required for validating MongoDB data against the latest schema

----

* Makefile
  * use hyphens in target names, not underscores
  * standardize naming of cleanup targets
  * added squeaky-clean target
  * harmonization of PROJECT_FOLDERS and the includes/excludes for gen-project and test-schema
  * trying to eliminate routine deletion and regeneration of src/schema/mixs.yaml
  * renaming of generated project/prefixmap/nmdc.yaml to project/prefixmap/nmdc.json


* nmdc_schema/class_sparql.py
* project.Makefile
  * `make-rdf` meta target
  * `local/study_set_doi.tsv`... ???

* src/schema/nmdc.yaml
  * addition of class `FunctionalAnnotationAggMember`, `Database` slot `functional_annotation_agg` and `FunctionalAnnotationAggMember` slots `metagenome_annotation_id`, `WorkflowExecutionActivity`, `gene_function_id` and `count`.
    * `count` sure is a vague slot name
    * example data: 
      * `src/data/valid/FunctionalAnnotationAggMember-minimal.yaml`
      * `src/data/valid/Database-functional_annotation_agg.yaml`
  * removal of `doi` slot, along with its assignment to class `Study`. Requires migration. See below. Also switching from scalar to multivalued and from `TextValue.has_raw_value` to `uriorcurie` ranges
    * valid example data like `src/data/valid/Study-exhaustive.yaml` changed to match the schema changes
  * addition of `award_dois`, `dataset_dois` `publication_dois`
    * example data: `src/data/valid/Database-study-set-with-dois.yaml`
  * removed transient 200-character limit on `funding_sources` slot
  * moved `emsl_project_dois` from `external_identifiers.yaml` to `nmdc.yaml` and re-rooted in `dois` including new pattern
  * updated `examples`, `comments` and `description` for `jgi_portal_study_identifiers` (in `src/schema/external_identifiers.yaml`)

### new
* nmdc_schema/migration_recursion.py
* nmdc_schema/migration_library.py
* nmdc_schema/get_study_doi_report.py
* nmdc_schema/class_sparql.py (see sparql-all in project.Makefile)
* nmdc_schema/anyuri_strings_to_iris.py (part of `make-rdf` meta target)


### to delete?
* nmdc_schema/mongotest.py
* nmdc_schema/mongodb_direct_to_nmdc_Database_file.py (deprecated by nmdc_schema/mongo_dump_api_emph.py ?)