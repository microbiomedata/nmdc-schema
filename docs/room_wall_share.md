# Slot: rooms that share a wall with sampling room (room_wall_share)


_List of room(s) (room number, room name) sharing a wall with the sampling room_



URI: [MIXS:0000243](https://w3id.org/mixs/0000243)




## Inheritance

* [core_field](core_field.md)
    * **room_wall_share**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooms that share a wall with sampling room




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | room name;room number || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_wall_share
annotations:
  expected_value:
    tag: expected_value
    value: room name;room number
  occurrence:
    tag: occurrence
    value: '1'
description: List of room(s) (room number, room name) sharing a wall with the sampling
  room
title: rooms that share a wall with sampling room
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooms that share a wall with sampling room
rank: 1000
is_a: core field
string_serialization: '{text};{integer}'
slot_uri: MIXS:0000243
multivalued: false
alias: room_wall_share
domain_of:
- Biosample
range: TextValue

```
</details>