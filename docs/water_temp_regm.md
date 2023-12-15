# Slot: water temperature regimen (water_temp_regm)


_Information about treatment involving an exposure to water with varying degree of temperature, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000590](https://w3id.org/mixs/0000590)




## Inheritance

* [core_field](core_field.md)
    * **water_temp_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* water temperature regimen




## Examples

| Value |
| --- |
| 15 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value;treatment interval and duration || preferred_unit | degree Celsius || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_temp_regm
annotations:
  expected_value:
    tag: expected_value
    value: measurement value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: degree Celsius
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving an exposure to water with varying
  degree of temperature, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple regimens
title: water temperature regimen
examples:
- value: 15 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water temperature regimen
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000590
multivalued: true
alias: water_temp_regm
domain_of:
- Biosample
range: TextValue

```
</details>