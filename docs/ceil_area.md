# Slot: ceiling area (ceil_area)


_The area of the ceiling space within the room_



URI: [MIXS:0000148](https://w3id.org/mixs/0000148)




## Inheritance

* [core_field](core_field.md)
    * **ceil_area**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* ceiling area




## Examples

| Value |
| --- |
| 25 square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | square meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ceil_area
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: square meter
  occurrence:
    tag: occurrence
    value: '1'
description: The area of the ceiling space within the room
title: ceiling area
examples:
- value: 25 square meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling area
rank: 1000
is_a: core field
slot_uri: MIXS:0000148
multivalued: false
alias: ceil_area
domain_of:
- Biosample
range: QuantityValue

```
</details>