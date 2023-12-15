# Slot: room location in building (room_loc)


_The position of the room within the building_



URI: [MIXS:0000823](https://w3id.org/mixs/0000823)




## Inheritance

* [core_field](core_field.md)
    * **room_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RoomLocEnum](RoomLocEnum.md)



## Aliases


* room location in building




## Examples

| Value |
| --- |
| interior room |

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
name: room_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The position of the room within the building
title: room location in building
examples:
- value: interior room
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room location in building
rank: 1000
is_a: core field
slot_uri: MIXS:0000823
multivalued: false
alias: room_loc
domain_of:
- Biosample
range: room_loc_enum

```
</details>