# Slot: neon_study_identifiers

URI: [nmdc:neon_study_identifiers](https://w3id.org/nmdc/neon_study_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **neon_study_identifiers** [ [neon_identifiers](neon_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: neon_study_identifiers
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
is_a: study_identifiers
mixins:
- neon_identifiers
domain: Study
multivalued: true
alias: neon_study_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^[a-zA-Z0-9][a-zA-Z0-9_\.]+:[a-zA-Z0-9_][a-zA-Z0-9_\-\/\.,]*$

```
</details>