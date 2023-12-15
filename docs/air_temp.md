# Slot: air temperature (air_temp)


_Temperature of the air at the time of sampling_



URI: [MIXS:0000124](https://w3id.org/mixs/0000124)




## Inheritance

* [core_field](core_field.md)
    * **air_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* air temperature




## Examples

| Value |
| --- |
| 20 degree Celsius |

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
name: air_temp
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
description: Temperature of the air at the time of sampling
title: air temperature
examples:
- value: 20 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- air temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000124
multivalued: false
alias: air_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>