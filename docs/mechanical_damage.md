# Slot: mechanical damage (mechanical_damage)


_Information about any mechanical damage exerted on the plant; can include multiple damages and sites_



URI: [MIXS:0001052](https://w3id.org/mixs/0001052)




## Inheritance

* [core_field](core_field.md)
    * **mechanical_damage**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)

* Multivalued: True



## Aliases


* mechanical damage




## Examples

| Value |
| --- |
| pruning;bark |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | damage type;body site || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: mechanical_damage
annotations:
  expected_value:
    tag: expected_value
    value: damage type;body site
  occurrence:
    tag: occurrence
    value: m
description: Information about any mechanical damage exerted on the plant; can include
  multiple damages and sites
title: mechanical damage
examples:
- value: pruning;bark
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mechanical damage
rank: 1000
is_a: core field
string_serialization: '{text};{text}'
slot_uri: MIXS:0001052
multivalued: true
alias: mechanical_damage
domain_of:
- Biosample
range: TextValue

```
</details>