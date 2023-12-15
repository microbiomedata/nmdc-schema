# Slot: radiation regimen (radiation_regm)


_Information about treatment involving exposure of plant or a plant part to a particular radiation regimen; should include the radiation type, amount or intensity administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple radiation regimens_



URI: [MIXS:0000575](https://w3id.org/mixs/0000575)




## Inheritance

* [core_field](core_field.md)
    * **radiation_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* radiation regimen




## Examples

| Value |
| --- |
| gamma radiation;60 gray;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | radiation type name;radiation amount;treatment interval and duration || preferred_unit | rad, gray || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: radiation_regm
annotations:
  expected_value:
    tag: expected_value
    value: radiation type name;radiation amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: rad, gray
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving exposure of plant or a plant part
  to a particular radiation regimen; should include the radiation type, amount or
  intensity administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple radiation regimens
title: radiation regimen
examples:
- value: gamma radiation;60 gray;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- radiation regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000575
multivalued: true
alias: radiation_regm
domain_of:
- Biosample
range: TextValue

```
</details>