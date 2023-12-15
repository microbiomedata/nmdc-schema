# Slot: soil texture measurement (soil_text_measure)


_The relative proportion of different grain sizes of mineral particles in a soil, as described using a standard system; express as % sand (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty clay loam) optional._



URI: [MIXS:0000335](https://w3id.org/mixs/0000335)




## Inheritance

* [core_field](core_field.md)
    * **soil_text_measure**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* soil texture measurement




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soil_text_measure
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The relative proportion of different grain sizes of mineral particles
  in a soil, as described using a standard system; express as % sand (50 um to 2 mm),
  silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty clay loam)
  optional.
title: soil texture measurement
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil texture measurement
rank: 1000
is_a: core field
slot_uri: MIXS:0000335
multivalued: false
alias: soil_text_measure
domain_of:
- Biosample
range: QuantityValue

```
</details>