# Slot: door area or size (door_size)


_The size of the door_



URI: [MIXS:0000158](https://w3id.org/mixs/0000158)




## Inheritance

* [core_field](core_field.md)
    * **door_size**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* door area or size




## Examples

| Value |
| --- |
| 2.5 square meter |

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
name: door_size
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
description: The size of the door
title: door area or size
examples:
- value: 2.5 square meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door area or size
rank: 1000
is_a: core field
slot_uri: MIXS:0000158
multivalued: false
alias: door_size
domain_of:
- Biosample
range: QuantityValue

```
</details>