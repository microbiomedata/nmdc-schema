# Slot: room occupancy (room_occup)


_Count of room occupancy at time of sampling_



URI: [MIXS:0000236](https://w3id.org/mixs/0000236)




## Inheritance

* [core_field](core_field.md)
    * **room_occup**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* room occupancy




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_occup
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Count of room occupancy at time of sampling
title: room occupancy
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room occupancy
rank: 1000
is_a: core field
slot_uri: MIXS:0000236
multivalued: false
alias: room_occup
domain_of:
- Biosample
range: QuantityValue

```
</details>