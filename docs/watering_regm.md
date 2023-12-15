# Slot: watering regimen (watering_regm)


_Information about treatment involving an exposure to watering frequencies, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000591](https://w3id.org/mixs/0000591)




## Inheritance

* [core_field](core_field.md)
    * **watering_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* watering regimen




## Examples

| Value |
| --- |
| 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;treatment interval and duration || preferred_unit | milliliter, liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: watering_regm
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: milliliter, liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving an exposure to watering frequencies,
  treatment regimen including how many times the treatment was repeated, how long
  each treatment lasted, and the start and end time of the entire treatment; can include
  multiple regimens
title: watering regimen
examples:
- value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- watering regimen
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000591
multivalued: true
alias: watering_regm
domain_of:
- Biosample
range: TextValue

```
</details>