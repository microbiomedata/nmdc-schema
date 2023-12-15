# Slot: room door distance (room_door_dist)


_Distance between doors (meters) in the hallway between the sampling room and adjacent rooms_



URI: [MIXS:0000193](https://w3id.org/mixs/0000193)




## Inheritance

* [core_field](core_field.md)
    * **room_door_dist**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* room door distance




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
name: room_door_dist
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
description: Distance between doors (meters) in the hallway between the sampling room
  and adjacent rooms
title: room door distance
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room door distance
rank: 1000
is_a: core field
string_serialization: '{integer} {unit}'
slot_uri: MIXS:0000193
multivalued: false
alias: room_door_dist
domain_of:
- Biosample
range: TextValue

```
</details>