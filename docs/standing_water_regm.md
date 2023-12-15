# Slot: standing water regimen (standing_water_regm)


_Treatment involving an exposure to standing water during a plant's life span, types can be flood water or standing water, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0001069](https://w3id.org/mixs/0001069)




## Inheritance

* [core_field](core_field.md)
    * **standing_water_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* standing water regimen




## Examples

| Value |
| --- |
| standing water;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | standing water type;treatment interval and duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: standing_water_regm
annotations:
  expected_value:
    tag: expected_value
    value: standing water type;treatment interval and duration
  occurrence:
    tag: occurrence
    value: m
description: Treatment involving an exposure to standing water during a plant's life
  span, types can be flood water or standing water, treatment regimen including how
  many times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple regimens
title: standing water regimen
examples:
- value: standing water;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- standing water regimen
rank: 1000
is_a: core field
string_serialization: '{text};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0001069
multivalued: true
alias: standing_water_regm
domain_of:
- Biosample
range: TextValue

```
</details>