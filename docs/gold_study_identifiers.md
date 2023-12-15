# Slot: GOLD Study Identifiers (gold_study_identifiers)


_identifiers for corresponding project(s) in GOLD_



URI: [nmdc:gold_study_identifiers](https://w3id.org/nmdc/gold_study_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **gold_study_identifiers** [ [gold_identifiers](gold_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^gold:Gs[0-9]+$`






## Examples

| Value |
| --- |
| https://bioregistry.io/gold:Gs0110115 |

## Comments

* uses the prefix GS (but possibly in a different case)

## See Also

* [https://gold.jgi.doe.gov/studies](https://gold.jgi.doe.gov/studies)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gold_study_identifiers
description: identifiers for corresponding project(s) in GOLD
title: GOLD Study Identifiers
comments:
- uses the prefix GS (but possibly in a different case)
examples:
- value: https://bioregistry.io/gold:Gs0110115
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://gold.jgi.doe.gov/studies
rank: 1000
is_a: study_identifiers
mixins:
- gold_identifiers
domain: Study
multivalued: true
alias: gold_study_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^gold:Gs[0-9]+$

```
</details>