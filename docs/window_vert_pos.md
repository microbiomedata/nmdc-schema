# Slot: window vertical position (window_vert_pos)


_The vertical position of the window on the wall_



URI: [MIXS:0000857](https://w3id.org/mixs/0000857)




## Inheritance

* [core_field](core_field.md)
    * **window_vert_pos**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowVertPosEnum](WindowVertPosEnum.md)



## Aliases


* window vertical position




## Examples

| Value |
| --- |
| middle |

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
name: window_vert_pos
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The vertical position of the window on the wall
title: window vertical position
examples:
- value: middle
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window vertical position
rank: 1000
is_a: core field
slot_uri: MIXS:0000857
multivalued: false
alias: window_vert_pos
domain_of:
- Biosample
range: window_vert_pos_enum

```
</details>