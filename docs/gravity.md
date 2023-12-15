# Slot: gravity (gravity)


_Information about treatment involving use of gravity factor to study various types of responses in presence, absence or modified levels of gravity; treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple treatments_



URI: [MIXS:0000559](https://w3id.org/mixs/0000559)




## Inheritance

* [core_field](core_field.md)
    * **gravity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* gravity




## Examples

| Value |
| --- |
| 12 g;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gravity factor value;treatment interval and duration || preferred_unit | meter per square second, g || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gravity
annotations:
  expected_value:
    tag: expected_value
    value: gravity factor value;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: meter per square second, g
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving use of gravity factor to study
  various types of responses in presence, absence or modified levels of gravity; treatment
  regimen including how many times the treatment was repeated, how long each treatment
  lasted, and the start and end time of the entire treatment; can include multiple
  treatments
title: gravity
examples:
- value: 12 g;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- gravity
rank: 1000
is_a: core field
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000559
multivalued: true
alias: gravity
domain_of:
- Biosample
range: TextValue

```
</details>