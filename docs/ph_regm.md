# Slot: pH regimen (ph_regm)


_Information about treatment involving exposure of plants to varying levels of ph of the growth media, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimen_



URI: [MIXS:0001056](https://w3id.org/mixs/0001056)




## Inheritance

* [core_field](core_field.md)
    * **ph_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* pH regimen




## Examples

| Value |
| --- |
| 7.6;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;treatment interval and duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ph_regm
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;treatment interval and duration
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving exposure of plants to varying levels
  of ph of the growth media, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple regimen
title: pH regimen
examples:
- value: 7.6;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pH regimen
rank: 1000
is_a: core field
string_serialization: '{float};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0001056
multivalued: true
alias: ph_regm
domain_of:
- Biosample
range: TextValue

```
</details>