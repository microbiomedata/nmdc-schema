# Slot: door location (door_loc)


_The relative location of the door in the room_



URI: [MIXS:0000790](https://w3id.org/mixs/0000790)




## Inheritance

* [core_field](core_field.md)
    * **door_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorLocEnum](DoorLocEnum.md)



## Aliases


* door location




## Examples

| Value |
| --- |
| north |

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
name: door_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The relative location of the door in the room
title: door location
examples:
- value: north
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door location
rank: 1000
is_a: core field
slot_uri: MIXS:0000790
multivalued: false
alias: door_loc
domain_of:
- Biosample
range: door_loc_enum

```
</details>