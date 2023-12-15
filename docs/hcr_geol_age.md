# Slot: hydrocarbon resource geological age (hcr_geol_age)


_Geological age of hydrocarbon resource (Additional info: https://en.wikipedia.org/wiki/Period_(geology)). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000993](https://w3id.org/mixs/0000993)




## Inheritance

* [core_field](core_field.md)
    * **hcr_geol_age**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [HcrGeolAgeEnum](HcrGeolAgeEnum.md)



## Aliases


* hydrocarbon resource geological age




## Examples

| Value |
| --- |
| Silurian |

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
name: hcr_geol_age
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: 'Geological age of hydrocarbon resource (Additional info: https://en.wikipedia.org/wiki/Period_(geology)).
  If "other" is specified, please propose entry in "additional info" field'
title: hydrocarbon resource geological age
examples:
- value: Silurian
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- hydrocarbon resource geological age
rank: 1000
is_a: core field
slot_uri: MIXS:0000993
multivalued: false
alias: hcr_geol_age
domain_of:
- Biosample
range: hcr_geol_age_enum

```
</details>