# Slot: source rock depositional environment (sr_dep_env)


_Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000996](https://w3id.org/mixs/0000996)




## Inheritance

* [core_field](core_field.md)
    * **sr_dep_env**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SrDepEnvEnum](SrDepEnvEnum.md)



## Aliases


* source rock depositional environment




## Examples

| Value |
| --- |
| Marine |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sr_dep_env
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock).
  If "other" is specified, please propose entry in "additional info" field
title: source rock depositional environment
examples:
- value: Marine
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- source rock depositional environment
rank: 1000
is_a: core field
slot_uri: MIXS:0000996
multivalued: false
alias: sr_dep_env
domain_of:
- Biosample
range: sr_dep_env_enum

```
</details>