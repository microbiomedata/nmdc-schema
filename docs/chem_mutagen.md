# Slot: chemical mutagen (chem_mutagen)


_Treatment involving use of mutagens; should include the name of mutagen, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mutagen regimens_



URI: [MIXS:0000555](https://w3id.org/mixs/0000555)




## Inheritance

* [core_field](core_field.md)
    * **chem_mutagen**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* chemical mutagen




## Examples

| Value |
| --- |
| nitrous acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | mutagen name;mutagen amount;treatment interval and duration || preferred_unit | milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chem_mutagen
annotations:
  expected_value:
    tag: expected_value
    value: mutagen name;mutagen amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Treatment involving use of mutagens; should include the name of mutagen,
  amount administered, treatment regimen including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple mutagen regimens
title: chemical mutagen
examples:
- value: nitrous acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chemical mutagen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000555
multivalued: true
alias: chem_mutagen
domain_of:
- Biosample
range: TextValue

```
</details>