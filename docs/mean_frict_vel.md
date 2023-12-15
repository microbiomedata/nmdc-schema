# Slot: mean friction velocity (mean_frict_vel)


_Measurement of mean friction velocity_



URI: [MIXS:0000498](https://w3id.org/mixs/0000498)




## Inheritance

* [core_field](core_field.md)
    * **mean_frict_vel**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* mean friction velocity




## Examples

| Value |
| --- |
| 0.5 meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter per second || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: mean_frict_vel
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter per second
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of mean friction velocity
title: mean friction velocity
examples:
- value: 0.5 meter per second
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mean friction velocity
rank: 1000
is_a: core field
slot_uri: MIXS:0000498
multivalued: false
alias: mean_frict_vel
domain_of:
- Biosample
range: QuantityValue

```
</details>