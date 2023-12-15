# Slot: perturbation (perturbation)


_Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with perturbation regimen including how many times the perturbation was repeated, how long each perturbation lasted, and the start and end time of the entire perturbation period; can include multiple perturbation types_



URI: [MIXS:0000754](https://w3id.org/mixs/0000754)




## Inheritance

* [core_field](core_field.md)
    * **perturbation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* perturbation




## Examples

| Value |
| --- |
| antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | perturbation type name;perturbation interval and duration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: perturbation
annotations:
  expected_value:
    tag: expected_value
    value: perturbation type name;perturbation interval and duration
  occurrence:
    tag: occurrence
    value: m
description: Type of perturbation, e.g. chemical administration, physical disturbance,
  etc., coupled with perturbation regimen including how many times the perturbation
  was repeated, how long each perturbation lasted, and the start and end time of the
  entire perturbation period; can include multiple perturbation types
title: perturbation
examples:
- value: antibiotic addition;R2/2018-05-11T14:30Z/2018-05-11T19:30Z/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- perturbation
rank: 1000
is_a: core field
string_serialization: '{text};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000754
multivalued: true
alias: perturbation
domain_of:
- Biosample
range: TextValue

```
</details>