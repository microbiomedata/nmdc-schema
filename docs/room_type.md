# Slot: room type (room_type)


_The main purpose or activity of the sampling room. A room is any distinguishable space within a structure_



URI: [MIXS:0000825](https://w3id.org/mixs/0000825)




## Inheritance

* [core_field](core_field.md)
    * **room_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RoomTypeEnum](RoomTypeEnum.md)



## Aliases


* room type




## Examples

| Value |
| --- |
| bathroom |

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
name: room_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The main purpose or activity of the sampling room. A room is any distinguishable
  space within a structure
title: room type
examples:
- value: bathroom
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room type
rank: 1000
is_a: core field
slot_uri: MIXS:0000825
multivalued: false
alias: room_type
domain_of:
- Biosample
range: room_type_enum

```
</details>