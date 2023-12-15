# Slot: relative air humidity (rel_air_humidity)


_Partial vapor and air pressure, density of the vapor and air, or by the actual mass of the vapor and air_



URI: [MIXS:0000121](https://w3id.org/mixs/0000121)




## Inheritance

* [core_field](core_field.md)
    * **rel_air_humidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* relative air humidity




## Examples

| Value |
| --- |
| 80% |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | percentage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rel_air_humidity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: percentage
  occurrence:
    tag: occurrence
    value: '1'
description: Partial vapor and air pressure, density of the vapor and air, or by the
  actual mass of the vapor and air
title: relative air humidity
examples:
- value: 80%
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- relative air humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000121
multivalued: false
alias: rel_air_humidity
domain_of:
- Biosample
range: QuantityValue

```
</details>