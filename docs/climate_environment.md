# Slot: climate environment (climate_environment)


_Treatment involving an exposure to a particular climate; treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple climates_



URI: [MIXS:0001040](https://w3id.org/mixs/0001040)




## Inheritance

* [core_field](core_field.md)
    * **climate_environment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* climate environment




## Examples

| Value |
| --- |
| tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | climate name;treatment interval and duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: climate_environment
annotations:
  expected_value:
    tag: expected_value
    value: climate name;treatment interval and duration
  occurrence:
    tag: occurrence
    value: m
description: Treatment involving an exposure to a particular climate; treatment regimen
  including how many times the treatment was repeated, how long each treatment lasted,
  and the start and end time of the entire treatment; can include multiple climates
title: climate environment
examples:
- value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- climate environment
rank: 1000
is_a: core field
string_serialization: '{text};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0001040
multivalued: true
alias: climate_environment
domain_of:
- Biosample
range: TextValue

```
</details>