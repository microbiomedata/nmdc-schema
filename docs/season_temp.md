# Slot: mean seasonal temperature (season_temp)


_Mean seasonal temperature_



URI: [MIXS:0000643](https://w3id.org/mixs/0000643)




## Inheritance

* [core_field](core_field.md)
    * **season_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* mean seasonal temperature




## Examples

| Value |
| --- |
| 18 degree Celsius |

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
name: season_temp
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
description: Mean seasonal temperature
title: mean seasonal temperature
examples:
- value: 18 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mean seasonal temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000643
multivalued: false
alias: season_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>