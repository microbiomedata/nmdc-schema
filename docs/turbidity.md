# Slot: turbidity (turbidity)


_Measure of the amount of cloudiness or haziness in water caused by individual particles_



URI: [MIXS:0000191](https://w3id.org/mixs/0000191)




## Inheritance

* [core_field](core_field.md)
    * **turbidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* turbidity




## Examples

| Value |
| --- |
| 0.3 nephelometric turbidity units |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | formazin turbidity unit, formazin nephelometric units || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: turbidity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: formazin turbidity unit, formazin nephelometric units
  occurrence:
    tag: occurrence
    value: '1'
description: Measure of the amount of cloudiness or haziness in water caused by individual
  particles
title: turbidity
examples:
- value: 0.3 nephelometric turbidity units
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- turbidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000191
multivalued: false
alias: turbidity
domain_of:
- Biosample
range: QuantityValue

```
</details>