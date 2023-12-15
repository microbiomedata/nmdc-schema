# Slot: wind speed (wind_speed)


_Speed of wind measured at the time of sampling_



URI: [MIXS:0000118](https://w3id.org/mixs/0000118)




## Inheritance

* [core_field](core_field.md)
    * **wind_speed**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* wind speed




## Examples

| Value |
| --- |
| 21 kilometer per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter per second, kilometer per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: wind_speed
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter per second, kilometer per hour
  occurrence:
    tag: occurrence
    value: '1'
description: Speed of wind measured at the time of sampling
title: wind speed
examples:
- value: 21 kilometer per hour
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wind speed
rank: 1000
is_a: core field
slot_uri: MIXS:0000118
multivalued: false
alias: wind_speed
domain_of:
- Biosample
range: QuantityValue

```
</details>