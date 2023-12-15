# Slot: wall area (wall_area)


_The total area of the sampled room's walls_



URI: [MIXS:0000198](https://w3id.org/mixs/0000198)




## Inheritance

* [core_field](core_field.md)
    * **wall_area**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* wall area




## Examples

| Value |
| --- |
|  |

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
name: wall_area
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
description: The total area of the sampled room's walls
title: wall area
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall area
rank: 1000
is_a: core field
slot_uri: MIXS:0000198
multivalued: false
alias: wall_area
domain_of:
- Biosample
range: QuantityValue

```
</details>