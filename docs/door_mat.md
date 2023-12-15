# Slot: door material (door_mat)


_The material the door is composed of_



URI: [MIXS:0000791](https://w3id.org/mixs/0000791)




## Inheritance

* [core_field](core_field.md)
    * **door_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorMatEnum](DoorMatEnum.md)



## Aliases


* door material




## Examples

| Value |
| --- |
| wood |

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
name: door_mat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The material the door is composed of
title: door material
examples:
- value: wood
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door material
rank: 1000
is_a: core field
slot_uri: MIXS:0000791
multivalued: false
alias: door_mat
domain_of:
- Biosample
range: door_mat_enum

```
</details>