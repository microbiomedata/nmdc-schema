# Slot: humidity regimen (humidity_regm)


_Information about treatment involving an exposure to varying degree of humidity; information about treatment involving use of growth hormones; should include amount of humidity administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000568](https://w3id.org/mixs/0000568)




## Inheritance

* [core_field](core_field.md)
    * **humidity_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* humidity regimen




## Examples

| Value |
| --- |
| 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | humidity value;treatment interval and duration || preferred_unit | gram per cubic meter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: humidity_regm
annotations:
  expected_value:
    tag: expected_value
    value: humidity value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: gram per cubic meter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving an exposure to varying degree of
  humidity; information about treatment involving use of growth hormones; should include
  amount of humidity administered, treatment regimen including how many times the
  treatment was repeated, how long each treatment lasted, and the start and end time
  of the entire treatment; can include multiple regimens
title: humidity regimen
examples:
- value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- humidity regimen
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000568
multivalued: true
alias: humidity_regm
domain_of:
- Biosample
range: TextValue

```
</details>