# Slot: wall location (wall_loc)


_The relative location of the wall within the room_



URI: [MIXS:0000843](https://w3id.org/mixs/0000843)




## Inheritance

* [core_field](core_field.md)
    * **wall_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WallLocEnum](WallLocEnum.md)



## Aliases


* wall location




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
name: wall_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The relative location of the wall within the room
title: wall location
examples:
- value: north
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall location
rank: 1000
is_a: core field
slot_uri: MIXS:0000843
multivalued: false
alias: wall_loc
domain_of:
- Biosample
range: wall_loc_enum

```
</details>