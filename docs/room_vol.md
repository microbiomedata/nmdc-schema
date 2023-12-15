# Slot: room volume (room_vol)


_Volume of sampling room_



URI: [MIXS:0000195](https://w3id.org/mixs/0000195)




## Inheritance

* [core_field](core_field.md)
    * **room_vol**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* room volume




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | cubic feet, cubic meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_vol
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: cubic feet, cubic meter
  occurrence:
    tag: occurrence
    value: '1'
description: Volume of sampling room
title: room volume
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room volume
rank: 1000
is_a: core field
string_serialization: '{integer} {unit}'
slot_uri: MIXS:0000195
multivalued: false
alias: room_vol
domain_of:
- Biosample
range: TextValue

```
</details>