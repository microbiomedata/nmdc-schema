# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) beginning with the 8.1.0 version. Previous content was copied over without reformatting.

Versioning for this project is based on [Semantic Versioning](https://semver.org/spec/v2.0.0.html) with the following guidelines:

* Patch versions: changes that have no effect on the data format described by the schema. For example: updates to slot descriptions, adding examples.
* Minor versions: changes that have backwards-compatible effects on the data format. For example: adding a new, non-required slot to a class, broadening the range of a slot.
* Major version: changes that have backwards-incompatible effects of the data format. These changes will require existing data to be migrated in order to be compatible with the new version. For example: adding a required slot to a class, changing a slot from multivalued to single-valued.

## Unreleased

### Added
- pattern to the `websites` slot that accepts websites that start with http or https (case insensitive) and does not allow doi.org.

## 9.1.0 - 2023-11-07 (multiple releases since 8.1.0)

### Added
- `Doi` class with slots `doi_value`, `doi_category`, and `doi_provider`.
- `DoiProviderEnum` and `DoiCategoryEnum`

### Removed
- deprecated the following slots: `dois`, `dataset_dois`, `publication_dois`, `award_dois`, `ess_dive_datasets`, `massive_identifiers`, and `massive_study_identifiers`

## 8.1.0 - 2023-10-03

### Fixed

- Remove incorrect description of `lat_lon` slot
- Remove non-monotonic range override on `used` slot of `MetaproteomicsAnalysis` class.
- make `study_category` slot required.

### Removed

- `emsl_project_dois` slot from `Study` class usage. Added deprecation to global slot. 
- `publications` slot from `Study` class usage. Added deprecation to global slot.

## 8.0.0 - 2023-09-21

### Overhaul of the definition and usage of CURIe prefixes. 
- Most notably, the `default_curi_maps` assertions have been 
removed from all schema source file, like `src/schema/nmdc.yaml`. All prefixes that will be used in the schema 
(`slot_uri`s, `mappings`, `id_prefixes`, etc.) must be defined in either `nmdc.yaml` or  another source field that it
`imports`. There is now a single file that contains all prefix definitions across the merged schema: 
`project/jsonld/nmdc.context.jsonld`. Note that it uses two pattern for expanding prefixes, Both are accessed from the
`@context` outer key.
  - direct: `"EFO": "http://www.ebi.ac.uk/efo/"`
  - via an `@id` inner key: `"ENVO": { "@id": "http://purl.obolibrary.org/obo/ENVO_"}`. 
Other keys in these dictionaries can usually be ignored.
- The `GOLD` prefix is no longer allowed in the schema or any schema compliant data. Only `gold` is allowed now.
- A discussion of prefixes, CURIes, identifiers and mappings has been added: `src/docs/prefixes_curies_ids_mappings_etc.md`
- https://bioregistry.io is now consistently preferred over http://identifiers.org as a CURIe resolving service.
The version is this release is a draft, and community members are welcome to ask questions or make suggestions.

### New data migration code:
- `Extraction`s must replace usages of the `sample_mass` slot with `input_mass`
- replacement of `GOLD` prefixes with `gold` prefixes in three classes 
- updates to `src/data` files: `/valid` shows the post migration state.

### Other
- SPARQL queries have beena dded or updated in `assets/sparql`
  - see also  `nmdc_schema/class_sparql.py`
- example python QC code, using LinkML SchemaView, has been added
  - `nmdc_schema/list_id_prefixes_and_patterns.py`
  - `nmdc_schema/list_slot_usages.py`
  - `nmdc_schema/list_structured_patterns.py`
- many definitional attributes of slots have been moved out of per-class `slot_usage` blocks. 
Especially in `src/schema/workflow_execution_activity.yaml`. Likewise, all class should not assert their slots with a
`slots` list, not implicitly via the `slot_usage` blocks. `required: true`, customized `range`s and customized `description`s 
can still be found in `slot_usage` blocks. Not that some of these are non-monotonic and need further attention. 
An exampl would be when the global definition of a slot uses an enumeration `range` but a slot_usage uses a `string` `range`.

## 7.8.0 - 2023-08-30

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
    - skips functional_annotation_agg and metaproteomics_analysis_set by default
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
      slots `metagenome_annotation_id`, `WorkflowExecution`, `gene_function_id` and `count`.
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
