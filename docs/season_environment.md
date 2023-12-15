# Slot: seasonal environment (season_environment)


_Treatment involving an exposure to a particular season (e.g. Winter, summer, rabi, rainy etc.), treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment_



URI: [MIXS:0001068](https://w3id.org/mixs/0001068)




## Inheritance

* [core_field](core_field.md)
    * **season_environment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* seasonal environment




## Examples

| Value |
| --- |
| rainy;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | seasonal environment name;treatment interval and duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: season_environment
annotations:
  expected_value:
    tag: expected_value
    value: seasonal environment name;treatment interval and duration
  occurrence:
    tag: occurrence
    value: m
description: Treatment involving an exposure to a particular season (e.g. Winter,
  summer, rabi, rainy etc.), treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment
title: seasonal environment
examples:
- value: rainy;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- seasonal environment
rank: 1000
is_a: core field
string_serialization: '{text};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0001068
multivalued: true
alias: season_environment
domain_of:
- Biosample
range: TextValue

```
</details>