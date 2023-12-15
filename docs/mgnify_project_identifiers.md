# Slot: mgnify_project_identifiers


_identifiers for corresponding project in MGnify_



URI: [nmdc:mgnify_project_identifiers](https://w3id.org/nmdc/mgnify_project_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **mgnify_project_identifiers** [ [mgnify_identifiers](mgnify_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^mgnify.proj:[A-Z]+[0-9]+$`






## Examples

| Value |
| --- |
| https://bioregistry.io/mgnify.proj:MGYS00005757 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: mgnify_project_identifiers
description: identifiers for corresponding project in MGnify
examples:
- value: https://bioregistry.io/mgnify.proj:MGYS00005757
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: study_identifiers
mixins:
- mgnify_identifiers
domain: Study
multivalued: true
alias: mgnify_project_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^mgnify.proj:[A-Z]+[0-9]+$

```
</details>