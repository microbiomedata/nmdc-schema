# Slot: adjacent rooms (adj_room)


_List of rooms (room number, room name) immediately adjacent to the sampling room_



URI: [MIXS:0000219](https://w3id.org/mixs/0000219)




## Inheritance

* [core_field](core_field.md)
    * **adj_room**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* adjacent rooms




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
name: adj_room
annotations:
  expected_value:
    tag: expected_value
    value: room name;room number
  occurrence:
    tag: occurrence
    value: '1'
description: List of rooms (room number, room name) immediately adjacent to the sampling
  room
title: adjacent rooms
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- adjacent rooms
rank: 1000
is_a: core field
string_serialization: '{text};{integer}'
slot_uri: MIXS:0000219
multivalued: false
alias: adj_room
domain_of:
- Biosample
range: TextValue

```
</details>