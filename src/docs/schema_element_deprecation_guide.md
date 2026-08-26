# Deprecating NMDC Schema elements

By deprecating, rather than deleting, schema elements in the NMDC model, we ensure backward compatibility, extend user 
trust, and provide a valuable historical record, aiding in the understanding of the model's evolution. Therefore, 
'deleting' a schema element in NMDC is instead, a two-step (and two-release) deprecation process.

## First release cycle:

- Add deprecation annotations to the element's definition

| Annotation                                                                                                                                                                                                                                                                           | Value                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| One of: [deprecated_element_has_exact_replacement](https://linkml.io/linkml-model/latest/docs/deprecated_element_has_exact_replacement/) OR [deprecated_element_has_possible_replacement](https://linkml.io/linkml-model/latest/docs/deprecated_element_has_possible_replacement/) * | uriorcurie value required |
| [deprecated](https://linkml.io/linkml-model/latest/docs/deprecated/)                                                                                                                                                                                                                 | A string explaining the reason for deprecation along with a link to the corresponding issue. |
| [last_updated_on](https://linkml.io/linkml-model/latest/docs/last_updated_on/)                                                                                                                                                                                                       |                           |
| [modified_by](https://linkml.io/linkml-model/latest/docs/modified_by/)                                                                                                                                                                                                               | With an ORCID value       |
| Deprecation Date                                                                                                                                                                                                                                                                     | Conforms to iso8601/international dates (e.g., `# doi_awards deprecated on 2023-11-12` in a class's usage). |

\* note: If a replacement is not warranted, then using only the `deprecated` metadata tag with an explanation 
string and issue link is fine.

## Second release cycle:

- Move the deprecated element to the "deprecated.yaml" schema file.  We do this so that the deprecated elements can
still be found in the documentation and via reference from stable unique identifiers (w3ids), but do not appear in the
main schema file nor participate in the validation of data.
- Remove the element itself from the original schema YAML file (e.g. core.yaml, annotation.yaml, etc.). 
- Remove any references to the deprecated element from the original schema YAML file. \*\*  

\*\* note: For a deprecated class, references could be in the `is_a` or `mixin` elements of another class, 
or in the `domain` or `range` elements of an existing slot. For deprecated slots, check all classes that reference that slot, etc.  

- Check whether anything outside the schema source still names the element, and deal with it in the same 
pull request or in a linked issue. Mapping files and committed reports under `assets/` are the usual place 
this shows up.

## Elements named outside the schema source

The steps above cover the schema YAML. They do not cover the mapping files, committed reports, and example 
changesheets under `assets/`, which keep naming an element long after the schema stops exposing it. Run:

```bash
poetry run make report-asset-usage
```

The report lists which assets name an element defined in `deprecated.yaml`. For each one there are three 
outcomes, and all three are fine as long as the choice is recorded in the pull request:

| Situation | What to do |
|---|---|
| Nothing in the repo or the organization reads the file | Delete it. See [Retiring a file from assets/](asset-lifecycle.md). |
| A Makefile target regenerates it | Regenerate it, and check that the target is a prerequisite of something, so it does not go stale again. |
| It is read by something that still needs the old name | Leave it, and say in the pull request why. |

Worked example: [Finalize Deprecation of `collection_date_inc`](https://github.com/microbiomedata/nmdc-schema/pull/3370) 
deprecated `collection_date_inc`, and an automated review flagged that `assets/misc/neon_nmdc_term_mapping.tsv` still 
mapped `incubationLength` to it. Nothing read that file, so it was deleted separately rather than remapped. 
That question, "remove or remap?", was taken to the 2026-08-26 NMDC Schema and Metadata meeting because the 
guide had no answer for it. This section is the answer.

#### TODO - section on updating the portal schema in the context of deprecation