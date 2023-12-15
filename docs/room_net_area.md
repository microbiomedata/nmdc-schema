# Slot: room net area (room_net_area)


_The net floor area of sampling room. Net area excludes wall thicknesses_



URI: [MIXS:0000194](https://w3id.org/mixs/0000194)




## Inheritance

* [core_field](core_field.md)
    * **room_net_area**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* room net area




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | square feet, square meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_net_area
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: square feet, square meter
  occurrence:
    tag: occurrence
    value: '1'
description: The net floor area of sampling room. Net area excludes wall thicknesses
title: room net area
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room net area
rank: 1000
is_a: core field
string_serialization: '{integer} {unit}'
slot_uri: MIXS:0000194
multivalued: false
alias: room_net_area
domain_of:
- Biosample
range: TextValue

```
</details>