# Slot: floor signs of water/mold (floor_water_mold)


_Signs of the presence of mold or mildew in a room_



URI: [MIXS:0000805](https://w3id.org/mixs/0000805)




## Inheritance

* [core_field](core_field.md)
    * **floor_water_mold**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FloorWaterMoldEnum](FloorWaterMoldEnum.md)



## Aliases


* floor signs of water/mold




## Examples

| Value |
| --- |
| ceiling discoloration |

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
name: floor_water_mold
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Signs of the presence of mold or mildew in a room
title: floor signs of water/mold
examples:
- value: ceiling discoloration
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- floor signs of water/mold
rank: 1000
is_a: core field
slot_uri: MIXS:0000805
multivalued: false
alias: floor_water_mold
domain_of:
- Biosample
range: floor_water_mold_enum

```
</details>