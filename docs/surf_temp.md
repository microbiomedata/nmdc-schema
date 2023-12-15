# Slot: surface temperature (surf_temp)


_Temperature of the surface at the time of sampling_



URI: [MIXS:0000125](https://w3id.org/mixs/0000125)




## Inheritance

* [core_field](core_field.md)
    * **surf_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* surface temperature




## Examples

| Value |
| --- |
| 15 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | degree Celsius || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: surf_temp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: degree Celsius
  occurrence:
    tag: occurrence
    value: '1'
description: Temperature of the surface at the time of sampling
title: surface temperature
examples:
- value: 15 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000125
multivalued: false
alias: surf_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>