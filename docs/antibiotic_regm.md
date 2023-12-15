# Slot: antibiotic regimen (antibiotic_regm)


_Information about treatment involving antibiotic administration; should include the name of antibiotic, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple antibiotic regimens_



URI: [MIXS:0000553](https://w3id.org/mixs/0000553)




## Inheritance

* [core_field](core_field.md)
    * **antibiotic_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* antibiotic regimen




## Examples

| Value |
| --- |
| penicillin;5 milligram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | antibiotic name;antibiotic amount;treatment interval and duration || preferred_unit | milligram || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: antibiotic_regm
annotations:
  expected_value:
    tag: expected_value
    value: antibiotic name;antibiotic amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: milligram
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving antibiotic administration; should
  include the name of antibiotic, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple antibiotic regimens
title: antibiotic regimen
examples:
- value: penicillin;5 milligram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- antibiotic regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000553
multivalued: true
alias: antibiotic_regm
domain_of:
- Biosample
range: TextValue

```
</details>