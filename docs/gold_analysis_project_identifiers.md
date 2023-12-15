# Slot: gold_analysis_project_identifiers


_identifiers for corresponding analysis project in GOLD_



URI: [nmdc:gold_analysis_project_identifiers](https://w3id.org/nmdc/gold_analysis_project_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [analysis_identifiers](analysis_identifiers.md)
            * **gold_analysis_project_identifiers** [ [gold_identifiers](gold_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MetagenomeAnnotationActivity](MetagenomeAnnotationActivity.md) | A workflow execution activity that provides functional and structural annotat... |  no  |
[MetatranscriptomeAnnotationActivity](MetatranscriptomeAnnotationActivity.md) |  |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^gold:Ga[0-9]+$`






## Examples

| Value |
| --- |
| https://bioregistry.io/gold:Ga0526289 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gold_analysis_project_identifiers
description: identifiers for corresponding analysis project in GOLD
examples:
- value: https://bioregistry.io/gold:Ga0526289
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: analysis_identifiers
mixins:
- gold_identifiers
multivalued: true
alias: gold_analysis_project_identifiers
domain_of:
- MetagenomeAnnotationActivity
- MetatranscriptomeAnnotationActivity
range: external_identifier
pattern: ^gold:Ga[0-9]+$

```
</details>