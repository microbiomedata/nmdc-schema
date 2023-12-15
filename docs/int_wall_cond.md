# Slot: interior wall condition (int_wall_cond)


_The physical condition of the wall at the time of sampling; photos or video preferred; use drawings to indicate location of damaged areas_



URI: [MIXS:0000813](https://w3id.org/mixs/0000813)




## Inheritance

* [core_field](core_field.md)
    * **int_wall_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [IntWallCondEnum](IntWallCondEnum.md)



## Aliases


* interior wall condition




## Examples

| Value |
| --- |
| damaged |

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
name: int_wall_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The physical condition of the wall at the time of sampling; photos or
  video preferred; use drawings to indicate location of damaged areas
title: interior wall condition
examples:
- value: damaged
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- interior wall condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000813
multivalued: false
alias: int_wall_cond
domain_of:
- Biosample
range: int_wall_cond_enum

```
</details>