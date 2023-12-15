# Slot: door type, wood (door_type_wood)


_The type of wood door_



URI: [MIXS:0000797](https://w3id.org/mixs/0000797)




## Inheritance

* [core_field](core_field.md)
    * **door_type_wood**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorTypeWoodEnum](DoorTypeWoodEnum.md)



## Aliases


* door type, wood




## Examples

| Value |
| --- |
| battened |

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
name: door_type_wood
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of wood door
title: door type, wood
examples:
- value: battened
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door type, wood
rank: 1000
is_a: core field
slot_uri: MIXS:0000797
multivalued: false
alias: door_type_wood
domain_of:
- Biosample
range: door_type_wood_enum

```
</details>