# Slot: wall finish material (wall_finish_mat)


_The material utilized to finish the outer most layer of the wall_



URI: [MIXS:0000842](https://w3id.org/mixs/0000842)




## Inheritance

* [core_field](core_field.md)
    * **wall_finish_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WallFinishMatEnum](WallFinishMatEnum.md)



## Aliases


* wall finish material




## Examples

| Value |
| --- |
| wood |

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
name: wall_finish_mat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The material utilized to finish the outer most layer of the wall
title: wall finish material
examples:
- value: wood
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall finish material
rank: 1000
is_a: core field
slot_uri: MIXS:0000842
multivalued: false
alias: wall_finish_mat
domain_of:
- Biosample
range: wall_finish_mat_enum

```
</details>