# Slot: room sampling position (room_samp_pos)


_The horizontal sampling position in the room relative to architectural elements_



URI: [MIXS:0000824](https://w3id.org/mixs/0000824)




## Inheritance

* [core_field](core_field.md)
    * **room_samp_pos**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RoomSampPosEnum](RoomSampPosEnum.md)



## Aliases


* room sampling position




## Examples

| Value |
| --- |
| south corner |

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
name: room_samp_pos
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The horizontal sampling position in the room relative to architectural
  elements
title: room sampling position
examples:
- value: south corner
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room sampling position
rank: 1000
is_a: core field
slot_uri: MIXS:0000824
multivalued: false
alias: room_samp_pos
domain_of:
- Biosample
range: room_samp_pos_enum

```
</details>