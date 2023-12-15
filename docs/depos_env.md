# Slot: depositional environment (depos_env)


_Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000992](https://w3id.org/mixs/0000992)




## Inheritance

* [core_field](core_field.md)
    * **depos_env**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DeposEnvEnum](DeposEnvEnum.md)



## Aliases


* depositional environment




## Examples

| Value |
| --- |
| Continental - Alluvial |

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
name: depos_env
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment).
  If "other" is specified, please propose entry in "additional info" field
title: depositional environment
examples:
- value: Continental - Alluvial
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- depositional environment
rank: 1000
is_a: core field
slot_uri: MIXS:0000992
multivalued: false
alias: depos_env
domain_of:
- Biosample
range: depos_env_enum

```
</details>