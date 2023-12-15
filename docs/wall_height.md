# Slot: wall height (wall_height)


_The average height of the walls in the sampled room_



URI: [MIXS:0000221](https://w3id.org/mixs/0000221)




## Inheritance

* [core_field](core_field.md)
    * **wall_height**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* wall height




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || preferred_unit | centimeter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: wall_height
annotations:
  expected_value:
    tag: expected_value
    value: value
  preferred_unit:
    tag: preferred_unit
    value: centimeter
  occurrence:
    tag: occurrence
    value: '1'
description: The average height of the walls in the sampled room
title: wall height
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall height
rank: 1000
is_a: core field
slot_uri: MIXS:0000221
multivalued: false
alias: wall_height
domain_of:
- Biosample
range: QuantityValue

```
</details>