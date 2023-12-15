# Slot: EMSL Project Identifiers (emsl_project_identifiers)


_an identifier that links to an EMSL user facility project_



URI: [nmdc:emsl_project_identifiers](https://w3id.org/nmdc/emsl_project_identifiers)




## Inheritance

* [alternative_identifiers](alternative_identifiers.md)
    * [external_database_identifiers](external_database_identifiers.md)
        * [study_identifiers](study_identifiers.md)
            * **emsl_project_identifiers** [ [emsl_identifiers](emsl_identifiers.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [ExternalIdentifier](ExternalIdentifier.md)

* Multivalued: True

* Regex pattern: `^emsl\.project:[0-9]{5}$`






## Examples

| Value |
| --- |
| emsl.project:60141 |

## TODOs

* elaborate on description

## See Also

* [https://github.com/microbiomedata/nmdc-schema/issues/927#issuecomment-1802136437](https://github.com/microbiomedata/nmdc-schema/issues/927#issuecomment-1802136437)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: emsl_project_identifiers
description: an identifier that links to an EMSL user facility project
title: EMSL Project Identifiers
todos:
- elaborate on description
notes:
- these identifiers are all currently 5 digits long but that could change in the future
examples:
- value: emsl.project:60141
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- https://github.com/microbiomedata/nmdc-schema/issues/927#issuecomment-1802136437
rank: 1000
is_a: study_identifiers
mixins:
- emsl_identifiers
domain: Study
multivalued: true
alias: emsl_project_identifiers
domain_of:
- Study
range: external_identifier
pattern: ^emsl\.project:[0-9]{5}$

```
</details>