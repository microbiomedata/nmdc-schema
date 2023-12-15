# Slot: rainfall regimen (rainfall_regm)


_Information about treatment involving an exposure to a given amount of rainfall, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000576](https://w3id.org/mixs/0000576)




## Inheritance

* [core_field](core_field.md)
    * **rainfall_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* rainfall regimen




## Examples

| Value |
| --- |
| 15 millimeter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;treatment interval and duration || preferred_unit | millimeter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rainfall_regm
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: millimeter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving an exposure to a given amount of
  rainfall, treatment regimen including how many times the treatment was repeated,
  how long each treatment lasted, and the start and end time of the entire treatment;
  can include multiple regimens
title: rainfall regimen
examples:
- value: 15 millimeter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rainfall regimen
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000576
multivalued: true
alias: rainfall_regm
domain_of:
- Biosample
range: TextValue

```
</details>