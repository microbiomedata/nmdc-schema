# Deprecating NMDC schema elements

When deprecating schema elements, it is a two step process:

1. For one release cycle, the schema will include deprecation annotations to the element's definition and commenting out any usages of the slot (e.g. in a class, domain, range, etc) including a deprecation date (e.g. `# doi_awards deprecated on 11/12/2023` in a class's usage)
2. Prior to a new release, fully removing the element from the schema including all commented out portions of the element in addition to the element itself. 


## The following annotations should be added or updated to the element's definition:

- [deprecated_element_has_exact_replacement](https://linkml.io/linkml-model/latest/docs/deprecated_element_has_exact_replacement/), [deprecated_element_has_possible_replacement](https://linkml.io/linkml-model/latest/docs/deprecated_element_has_possible_replacement/) and/or [deprecated](https://linkml.io/linkml-model/latest/docs/deprecated/), in that order of preference. Note that `deprecated_element_has_exact_replacement` and `deprecated_element_has_possible_replacement` should have `Uriorcurie` as the value. If using the replacement annotations, please also add the `deprecated` annotation with a string explaining the reason for deprecation along with a link to the corresponding issue. If there is not a replacement, then using only `deprecated` with an explanation string and issue link is fine.
- [last_updated_on](https://linkml.io/linkml-model/latest/docs/last_updated_on/)
- [modified_by](https://linkml.io/linkml-model/latest/docs/modified_by/), with an ORCID value

## When a class is to be deprecated

- That class should not be in the domain or range of any slot
- No class should claim the deprecated class as its `is_a` parent or as a mixin

## When a slot is to be deprecated 

That slot should be removed from all classes

## Deprecated elements should stay in the schema for one release

The annotations listed above will aid in deleting the deprecated elements after one release cycle, in consultation with the dates of the releases.