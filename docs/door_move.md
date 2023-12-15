# Slot: door movement (door_move)


_The type of movement of the door_



URI: [MIXS:0000792](https://w3id.org/mixs/0000792)




## Inheritance

* [core_field](core_field.md)
    * **door_move**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorMoveEnum](DoorMoveEnum.md)



## Aliases


* door movement




## Examples

| Value |
| --- |
| swinging |

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
name: door_move
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of movement of the door
title: door movement
examples:
- value: swinging
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door movement
rank: 1000
is_a: core field
slot_uri: MIXS:0000792
multivalued: false
alias: door_move
domain_of:
- Biosample
range: door_move_enum

```
</details>