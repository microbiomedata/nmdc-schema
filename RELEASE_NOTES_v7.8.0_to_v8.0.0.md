## Overhaul of the definition and usage of CURIe prefixes. 
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

## New data migration code:
- `Extraction`s must replace usages of the `sample_mass` slot with `input_mass`
- replacement of `GOLD` prefixes with `gold` prefixes in three classes 
- updates to `src/data` files: `/valid` shows the post migration state.

## Other
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
