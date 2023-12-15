# Slot: door type, metal (door_type_metal)


_The type of metal door_



URI: [MIXS:0000796](https://w3id.org/mixs/0000796)




## Inheritance

* [core_field](core_field.md)
    * **door_type_metal**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorTypeMetalEnum](DoorTypeMetalEnum.md)



## Aliases


* door type, metal




## Examples

| Value |
| --- |
| hollow |

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
name: door_type_metal
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of metal door
title: door type, metal
examples:
- value: hollow
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door type, metal
rank: 1000
is_a: core field
slot_uri: MIXS:0000796
multivalued: false
alias: door_type_metal
domain_of:
- Biosample
range: door_type_metal_enum

```
</details>