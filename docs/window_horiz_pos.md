# Slot: window horizontal position (window_horiz_pos)


_The horizontal position of the window on the wall_



URI: [MIXS:0000851](https://w3id.org/mixs/0000851)




## Inheritance

* [core_field](core_field.md)
    * **window_horiz_pos**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowHorizPosEnum](WindowHorizPosEnum.md)



## Aliases


* window horizontal position




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
name: window_horiz_pos
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The horizontal position of the window on the wall
title: window horizontal position
examples:
- value: middle
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window horizontal position
rank: 1000
is_a: core field
slot_uri: MIXS:0000851
multivalued: false
alias: window_horiz_pos
domain_of:
- Biosample
range: window_horiz_pos_enum

```
</details>