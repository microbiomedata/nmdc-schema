# Slot: floor finish material (floor_finish_mat)


_The floor covering type; the finished surface that is walked on_



URI: [MIXS:0000804](https://w3id.org/mixs/0000804)




## Inheritance

* [core_field](core_field.md)
    * **floor_finish_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FloorFinishMatEnum](FloorFinishMatEnum.md)



## Aliases


* floor finish material




## Examples

| Value |
| --- |
| carpet |

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
name: floor_finish_mat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The floor covering type; the finished surface that is walked on
title: floor finish material
examples:
- value: carpet
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- floor finish material
rank: 1000
is_a: core field
slot_uri: MIXS:0000804
multivalued: false
alias: floor_finish_mat
domain_of:
- Biosample
range: floor_finish_mat_enum

```
</details>