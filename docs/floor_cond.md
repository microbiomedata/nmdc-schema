# Slot: floor condition (floor_cond)


_The physical condition of the floor at the time of sampling; photos or video preferred; use drawings to indicate location of damaged areas_



URI: [MIXS:0000803](https://w3id.org/mixs/0000803)




## Inheritance

* [core_field](core_field.md)
    * **floor_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FloorCondEnum](FloorCondEnum.md)



## Aliases


* floor condition




## Examples

| Value |
| --- |
| new |

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
name: floor_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The physical condition of the floor at the time of sampling; photos or
  video preferred; use drawings to indicate location of damaged areas
title: floor condition
examples:
- value: new
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- floor condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000803
multivalued: false
alias: floor_cond
domain_of:
- Biosample
range: floor_cond_enum

```
</details>