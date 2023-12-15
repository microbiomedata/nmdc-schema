# Slot: mineral nutrient regimen (mineral_nutr_regm)


_Information about treatment involving the use of mineral supplements; should include the name of mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mineral nutrient regimens_



URI: [MIXS:0000570](https://w3id.org/mixs/0000570)




## Inheritance

* [core_field](core_field.md)
    * **mineral_nutr_regm**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* mineral nutrient regimen




## Examples

| Value |
| --- |
| potassium;15 gram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | mineral nutrient name;mineral nutrient amount;treatment interval and duration || preferred_unit | gram, mole per liter, milligram per liter || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: mineral_nutr_regm
annotations:
  expected_value:
    tag: expected_value
    value: mineral nutrient name;mineral nutrient amount;treatment interval and duration
  preferred_unit:
    tag: preferred_unit
    value: gram, mole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: m
description: Information about treatment involving the use of mineral supplements;
  should include the name of mineral nutrient, amount administered, treatment regimen
  including how many times the treatment was repeated, how long each treatment lasted,
  and the start and end time of the entire treatment; can include multiple mineral
  nutrient regimens
title: mineral nutrient regimen
examples:
- value: potassium;15 gram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mineral nutrient regimen
rank: 1000
is_a: core field
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000570
multivalued: true
alias: mineral_nutr_regm
domain_of:
- Biosample
range: TextValue

```
</details>