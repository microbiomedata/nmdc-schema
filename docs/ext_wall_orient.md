# Slot: orientations of exterior wall (ext_wall_orient)


_The orientation of the exterior wall_



URI: [MIXS:0000817](https://w3id.org/mixs/0000817)




## Inheritance

* [core_field](core_field.md)
    * **ext_wall_orient**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExtWallOrientEnum](ExtWallOrientEnum.md)



## Aliases


* orientations of exterior wall




## Examples

| Value |
| --- |
| northwest |

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
name: ext_wall_orient
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The orientation of the exterior wall
title: orientations of exterior wall
examples:
- value: northwest
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- orientations of exterior wall
rank: 1000
is_a: core field
slot_uri: MIXS:0000817
multivalued: false
alias: ext_wall_orient
domain_of:
- Biosample
range: ext_wall_orient_enum

```
</details>