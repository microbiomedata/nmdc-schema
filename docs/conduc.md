# Slot: conductivity (conduc)


_Electrical conductivity of water_



URI: [MIXS:0000692](https://w3id.org/mixs/0000692)




## Inheritance

* [core_field](core_field.md)
    * **conduc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* conductivity




## Examples

| Value |
| --- |
| 10 milliSiemens per centimeter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milliSiemens per centimeter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: conduc
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milliSiemens per centimeter
  occurrence:
    tag: occurrence
    value: '1'
description: Electrical conductivity of water
title: conductivity
examples:
- value: 10 milliSiemens per centimeter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- conductivity
rank: 1000
is_a: core field
slot_uri: MIXS:0000692
multivalued: false
alias: conduc
domain_of:
- Biosample
range: QuantityValue

```
</details>