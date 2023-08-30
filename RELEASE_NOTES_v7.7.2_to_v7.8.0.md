- More aggressive .gitigore for cleaner merges
    - for releases: git add -f examples nmdc_schema project src
- Refactored Makefile and project.Makefile
    - doesn't regenerate src/schema/mixs.yaml by default on every `make all`
    - routine: `make squeaky-clean all only-test`
    - for regenerating `src/schema/mixs.yaml: make squeaky-clean mixs-yaml-clean all only-test`
- New `OmicsProcessing-all` meta target for illustrating the automatic generation and execution of SPARQL queries for a
  specified class
- New `assets/sparql` folder for SPARQL that were generated with the `class-sparql` CLI and which could be edited and
  resubmitted to `class-sparql` for in `--query-file` mode
- New `make-rdf` meta target dumps MongoDB in the shape of an NMDC Database instance, makes migrations (including `doi`
  migration and CURIe coercion), linkml-validation, conversion to RDF/TTL and casting anyURI-typed strings to real
  CURIes
    - skips functional_annotation_agg and metaproteomics_analysis_activity_set by default
    - `dois` migrations can be performed in one `Study`
      with `nmdc_schema.migration_recursion:migrate_studies_7_7_2_to_7_8_0`
- New `accepting-legacy-ids-all` meta target for validating MongoDB data that includes legacy `id`s
- Commented out old exploratory NEON targets in project.Makefile
- Commented out old `assets/MIxS_6_term_updates_MIxS6*` targets in project.Makefile
- `project/prefixmap/nmdc.json` is generated as a YAML file. We're renaming it in Makefile's `gen-project` target
    - see https://github.com/linkml/linkml/issues/1598
- Created some new redundancy in terms of supplements to the prefixes defined in the merged NMDC schema
    - `assets/misc/extra_prefix_expansions.yaml`
    - `project/jsonld/nmdc.context.jsonld`
    - `project/prefixmap/nmdc.json`
    - hardcoded prefix expansions in `nmdc_schema/class_sparql.py`
- makefiles:
    - added squeaky-clean target
    - harmonization of PROJECT_FOLDERS and the includes/excludes for gen-project and test-schema
    - standardize naming of cleanup targets
    - use hyphens in target names, not underscores
- Potential sources of breakage for downstream users of the nmdc-schema package:
    - Moved several legacy Python scripts from nmdc_schema/ to assets/old_python
    - removed several `pyproject.toml` dependencies, or relocated to `tool.poetry.group.dev.dependencies`
    - removed several legacy `tool.poetry.scripts` CLI definitions
- Structural schema changes:
    - addition of class `FunctionalAnnotationAggMember`, `Database` slot `functional_annotation_agg`
      and `FunctionalAnnotationAggMember`
      slots `metagenome_annotation_id`, `WorkflowExecutionActivity`, `gene_function_id` and `count`.
        - `count` sure is a vague slot name
        - example data:
            - `src/data/valid/FunctionalAnnotationAggMember-minimal.yaml`
            - `src/data/valid/Database-functional_annotation_agg.yaml`
    - removal of `doi` slot, along with its assignment to class `Study`. Requires migration. Also switching from scalar
      to multivalued and from `TextValue.has_raw_value` to `uriorcurie` ranges
        - valid example data like `src/data/valid/Study-exhaustive.yaml` changed to match the schema changes
    - addition of `award_dois`, `dataset_dois` `publication_dois`
        - example data: `src/data/valid/Database-study-set-with-dois.yaml`
    - removed transient 200-character limit on `funding_sources` slot
    - moved `emsl_project_dois` from `external_identifiers.yaml` to `nmdc.yaml` and re-rooted in `dois` including new
      pattern
    - `abstract` slot has been moved from class `Study`
- Schema annotation changes
    - updated `examples`, `comments` and `description` for `jgi_portal_study_identifiers` (
      in `src/schema/external_identifiers.yaml`)
    - the `description` for class `Study` clarifies that the `description` of `Study` instances should not include
      hyperlinks
    - the comments on slot `elev` in class `Biosample` have been updated
