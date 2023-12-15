# Slot: fertilizer regimen (fertilizer_regm)


_Information about treatment involving the use of fertilizers; should include the name of fertilizer, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple fertilizer regimens_



URI: [MIXS:0000556](https://w3id.org/mixs/0000556)




## Inheritance

* [core_field](core_field.md)
    * **fertilizer_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* fertilizer regimen




## Examples

| Value |
| --- |
| urea;0.6 milligram per liter;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | fertilizer name;fertilizer amount;treatment interval and duration || preferred_unit | gram, mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: fertilizer_regm
annotations:
  expected_value:
    tag: expected_value
    value: fertilizer name;fertilizer amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving the use of fertilizers; should
  include the name of fertilizer, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple fertilizer regimens
title: fertilizer regimen
examples:
- value: urea;0.6 milligram per liter;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- fertilizer regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000556
multivalued: true
alias: fertilizer_regm
domain_of:
- Biosample
range: TextValue

```
</details>