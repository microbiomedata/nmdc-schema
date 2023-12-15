# Slot: ventilation rate (ventilation_rate)


_Ventilation rate of the system in the sampled premises_



URI: [MIXS:0000114](https://w3id.org/mixs/0000114)




## Inheritance

* [core_field](core_field.md)
    * **ventilation_rate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* ventilation rate




## Examples

| Value |
| --- |
| 750 cubic meter per minute |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | cubic meter per minute, liters per second || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ventilation_rate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: cubic meter per minute, liters per second
  occurrence:
    tag: occurrence
    value: '1'
description: Ventilation rate of the system in the sampled premises
title: ventilation rate
examples:
- value: 750 cubic meter per minute
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ventilation rate
rank: 1000
is_a: core field
slot_uri: MIXS:0000114
multivalued: false
alias: ventilation_rate
domain_of:
- Biosample
range: QuantityValue

```
</details>