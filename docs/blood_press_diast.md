# Slot: host blood pressure diastolic (blood_press_diast)


_Resting diastolic blood pressure, measured as mm mercury_



URI: [MIXS:0000258](https://w3id.org/mixs/0000258)




## Inheritance

* [core_field](core_field.md)
    * **blood_press_diast**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host blood pressure diastolic




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millimeter mercury || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: blood_press_diast
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millimeter mercury
  occurrence:
    tag: occurrence
    value: '1'
description: Resting diastolic blood pressure, measured as mm mercury
title: host blood pressure diastolic
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host blood pressure diastolic
rank: 1000
is_a: core field
slot_uri: MIXS:0000258
multivalued: false
alias: blood_press_diast
domain_of:
- Biosample
range: QuantityValue

```
</details>