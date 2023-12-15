# Slot: water current (water_current)


_Measurement of magnitude and direction of flow within a fluid_



URI: [MIXS:0000203](https://w3id.org/mixs/0000203)




## Inheritance

* [core_field](core_field.md)
    * **water_current**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* water current




## Examples

| Value |
| --- |
| 10 cubic meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | cubic meter per second, knots || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_current
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: cubic meter per second, knots
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of magnitude and direction of flow within a fluid
title: water current
examples:
- value: 10 cubic meter per second
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water current
rank: 1000
is_a: core field
slot_uri: MIXS:0000203
multivalued: false
alias: water_current
domain_of:
- Biosample
range: QuantityValue

```
</details>