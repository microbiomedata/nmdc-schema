# Slot: growth habit (growth_habit)


_Characteristic shape, appearance or growth form of a plant species_



URI: [MIXS:0001044](https://w3id.org/mixs/0001044)




## Inheritance

* [core_field](core_field.md)
    * **growth_habit**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [GrowthHabitEnum](GrowthHabitEnum.md)



## Aliases


* growth habit




## Examples

| Value |
| --- |
| spreading |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: growth_habit
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Characteristic shape, appearance or growth form of a plant species
title: growth habit
examples:
- value: spreading
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- growth habit
rank: 1000
is_a: core field
slot_uri: MIXS:0001044
multivalued: false
alias: growth_habit
domain_of:
- Biosample
range: growth_habit_enum

```
</details>