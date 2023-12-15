# Slot: rooms that are on the same hallway (room_hallway)


_List of room(s) (room number, room name) located in the same hallway as sampling room_



URI: [MIXS:0000238](https://w3id.org/mixs/0000238)




## Inheritance

* [core_field](core_field.md)
    * **room_hallway**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooms that are on the same hallway




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
name: room_hallway
annotations:
  expected_value:
    tag: expected_value
    value: room name;room number
  occurrence:
    tag: occurrence
    value: '1'
description: List of room(s) (room number, room name) located in the same hallway
  as sampling room
title: rooms that are on the same hallway
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooms that are on the same hallway
rank: 1000
is_a: core field
string_serialization: '{text};{integer}'
slot_uri: MIXS:0000238
multivalued: false
alias: room_hallway
domain_of:
- Biosample
range: TextValue

```
</details>