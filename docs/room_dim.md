# Slot: room dimensions (room_dim)


_The length, width and height of sampling room_



URI: [MIXS:0000192](https://w3id.org/mixs/0000192)




## Inheritance

* [core_field](core_field.md)
    * **room_dim**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* room dimensions




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_dim
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: The length, width and height of sampling room
title: room dimensions
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room dimensions
rank: 1000
is_a: core field
string_serialization: '{integer} {unit} x {integer} {unit} x {integer} {unit}'
slot_uri: MIXS:0000192
multivalued: false
alias: room_dim
domain_of:
- Biosample
range: TextValue

```
</details>