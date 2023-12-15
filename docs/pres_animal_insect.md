# Slot: presence of pets, animals, or insects (pres_animal_insect)


_The type and number of animals or insects present in the sampling space._



URI: [MIXS:0000819](https://w3id.org/mixs/0000819)




## Inheritance

* [core_field](core_field.md)
    * **pres_animal_insect**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^(cat|dog|rodent|snake|other);\d+$`



## Aliases


* presence of pets, animals, or insects




## Examples

| Value |
| --- |
| cat;5 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration;count || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pres_animal_insect
annotations:
  expected_value:
    tag: expected_value
    value: enumeration;count
  occurrence:
    tag: occurrence
    value: '1'
description: The type and number of animals or insects present in the sampling space.
title: presence of pets, animals, or insects
examples:
- value: cat;5
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- presence of pets, animals, or insects
rank: 1000
is_a: core field
slot_uri: MIXS:0000819
multivalued: false
alias: pres_animal_insect
domain_of:
- Biosample
range: string
pattern: ^(cat|dog|rodent|snake|other);\d+$

```
</details>