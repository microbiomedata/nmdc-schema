# Slot: soil horizon (soil_horizon)


_Specific layer in the land area which measures parallel to the soil surface and possesses physical characteristics which differ from the layers above and beneath_



URI: [MIXS:0001082](https://w3id.org/mixs/0001082)




## Inheritance

* [core_field](core_field.md)
    * **soil_horizon**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SoilHorizonEnum](SoilHorizonEnum.md)



## Aliases


* soil horizon




## Examples

| Value |
| --- |
| A horizon |

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
name: soil_horizon
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Specific layer in the land area which measures parallel to the soil surface
  and possesses physical characteristics which differ from the layers above and beneath
title: soil horizon
examples:
- value: A horizon
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil horizon
rank: 1000
is_a: core field
slot_uri: MIXS:0001082
multivalued: false
alias: soil_horizon
domain_of:
- Biosample
range: soil_horizon_enum

```
</details>