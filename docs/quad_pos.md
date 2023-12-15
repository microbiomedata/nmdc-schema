# Slot: quadrant position (quad_pos)


_The quadrant position of the sampling room within the building_



URI: [MIXS:0000820](https://w3id.org/mixs/0000820)




## Inheritance

* [core_field](core_field.md)
    * **quad_pos**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuadPosEnum](QuadPosEnum.md)



## Aliases


* quadrant position




## Examples

| Value |
| --- |
| West side |

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
name: quad_pos
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The quadrant position of the sampling room within the building
title: quadrant position
examples:
- value: West side
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- quadrant position
rank: 1000
is_a: core field
slot_uri: MIXS:0000820
multivalued: false
alias: quad_pos
domain_of:
- Biosample
range: quad_pos_enum

```
</details>