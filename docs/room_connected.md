# Slot: rooms connected by a doorway (room_connected)


_List of rooms connected to the sampling room by a doorway_



URI: [MIXS:0000826](https://w3id.org/mixs/0000826)




## Inheritance

* [core_field](core_field.md)
    * **room_connected**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RoomConnectedEnum](RoomConnectedEnum.md)



## Aliases


* rooms connected by a doorway




## Examples

| Value |
| --- |
| office |

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
name: room_connected
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: List of rooms connected to the sampling room by a doorway
title: rooms connected by a doorway
examples:
- value: office
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooms connected by a doorway
rank: 1000
is_a: core field
slot_uri: MIXS:0000826
multivalued: false
alias: room_connected
domain_of:
- Biosample
range: room_connected_enum

```
</details>