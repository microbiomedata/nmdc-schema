# Slot: plant sex (plant_sex)


_Sex of the reproductive parts on the whole plant, e.g. pistillate, staminate, monoecieous, hermaphrodite._



URI: [MIXS:0001059](https://w3id.org/mixs/0001059)




## Inheritance

* [core_field](core_field.md)
    * **plant_sex**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [PlantSexEnum](PlantSexEnum.md)



## Aliases


* plant sex




## Examples

| Value |
| --- |
| Hermaphroditic |

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
name: plant_sex
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Sex of the reproductive parts on the whole plant, e.g. pistillate, staminate,
  monoecieous, hermaphrodite.
title: plant sex
examples:
- value: Hermaphroditic
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- plant sex
rank: 1000
is_a: core field
slot_uri: MIXS:0001059
multivalued: false
alias: plant_sex
domain_of:
- Biosample
range: plant_sex_enum

```
</details>