# Slot: mean peak friction velocity (mean_peak_frict_vel)


_Measurement of mean peak friction velocity_



URI: [MIXS:0000502](https://w3id.org/mixs/0000502)




## Inheritance

* [core_field](core_field.md)
    * **mean_peak_frict_vel**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* mean peak friction velocity




## Examples

| Value |
| --- |
| 1 meter per second |

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
name: mean_peak_frict_vel
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
description: Measurement of mean peak friction velocity
title: mean peak friction velocity
examples:
- value: 1 meter per second
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mean peak friction velocity
rank: 1000
is_a: core field
slot_uri: MIXS:0000502
multivalued: false
alias: mean_peak_frict_vel
domain_of:
- Biosample
range: QuantityValue

```
</details>