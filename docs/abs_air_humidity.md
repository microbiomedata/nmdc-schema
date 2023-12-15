# Slot: absolute air humidity (abs_air_humidity)


_Actual mass of water vapor - mh20 - present in the air water vapor mixture_



URI: [MIXS:0000122](https://w3id.org/mixs/0000122)




## Inheritance

* [core_field](core_field.md)
    * **abs_air_humidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* absolute air humidity




## Examples

| Value |
| --- |
| 9 gram per gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram per gram, kilogram per kilogram, kilogram, pound || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: abs_air_humidity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per gram, kilogram per kilogram, kilogram, pound
  occurrence:
    tag: occurrence
    value: '1'
description: Actual mass of water vapor - mh20 - present in the air water vapor mixture
title: absolute air humidity
examples:
- value: 9 gram per gram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- absolute air humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000122
multivalued: false
alias: abs_air_humidity
domain_of:
- Biosample
range: QuantityValue

```
</details>