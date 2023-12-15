# Slot: slope aspect (slope_aspect)


_The direction a slope faces. While looking down a slope use a compass to record the direction you are facing (direction or degrees); e.g., nw or 315 degrees. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration._



URI: [MIXS:0000647](https://w3id.org/mixs/0000647)




## Inheritance

* [core_field](core_field.md)
    * **slope_aspect**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* slope aspect




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | degree || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: slope_aspect
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: degree
  occurrence:
    tag: occurrence
    value: '1'
description: The direction a slope faces. While looking down a slope use a compass
  to record the direction you are facing (direction or degrees); e.g., nw or 315 degrees.
  This measure provides an indication of sun and wind exposure that will influence
  soil temperature and evapotranspiration.
title: slope aspect
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- slope aspect
rank: 1000
is_a: core field
slot_uri: MIXS:0000647
multivalued: false
alias: slope_aspect
domain_of:
- Biosample
range: QuantityValue

```
</details>