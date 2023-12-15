# Slot: non-mineral nutrient regimen (non_min_nutr_regm)


_Information about treatment involving the exposure of plant to non-mineral nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple non-mineral nutrient regimens_



URI: [MIXS:0000571](https://w3id.org/mixs/0000571)




## Inheritance

* [core_field](core_field.md)
    * **non_min_nutr_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True



## Aliases


* non-mineral nutrient regimen




## Examples

| Value |
| --- |
| carbon dioxide;10 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | non-mineral nutrient name;non-mineral nutrient amount;treatment interval and duration || preferred_unit | gram, mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: non_min_nutr_regm
annotations:
  expected_value:
    tag: expected_value
    value: non-mineral nutrient name;non-mineral nutrient amount;treatment interval
      and duration
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving the exposure of plant to non-mineral
  nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral
  nutrient, amount administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple non-mineral nutrient regimens
title: non-mineral nutrient regimen
examples:
- value: carbon dioxide;10 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- non-mineral nutrient regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000571
multivalued: true
alias: non_min_nutr_regm
domain_of:
- Biosample
range: string

```
</details>