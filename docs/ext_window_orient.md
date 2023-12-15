# Slot: orientations of exterior window (ext_window_orient)


_The compass direction the exterior window of the room is facing_



URI: [MIXS:0000818](https://w3id.org/mixs/0000818)




## Inheritance

* [core_field](core_field.md)
    * **ext_window_orient**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ExtWindowOrientEnum](ExtWindowOrientEnum.md)



## Aliases


* orientations of exterior window




## Examples

| Value |
| --- |
| southwest |

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
name: ext_window_orient
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The compass direction the exterior window of the room is facing
title: orientations of exterior window
examples:
- value: southwest
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- orientations of exterior window
rank: 1000
is_a: core field
slot_uri: MIXS:0000818
multivalued: false
alias: ext_window_orient
domain_of:
- Biosample
range: ext_window_orient_enum

```
</details>