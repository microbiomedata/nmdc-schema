# Slot: door type, composite (door_comp_type)


_The composite type of the door_



URI: [MIXS:0000795](https://w3id.org/mixs/0000795)




## Inheritance

* [core_field](core_field.md)
    * **door_comp_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorCompTypeEnum](DoorCompTypeEnum.md)



## Aliases


* door type, composite




## Examples

| Value |
| --- |
| revolving |

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
name: door_comp_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The composite type of the door
title: door type, composite
examples:
- value: revolving
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door type, composite
rank: 1000
is_a: core field
slot_uri: MIXS:0000795
multivalued: false
alias: door_comp_type
domain_of:
- Biosample
range: door_comp_type_enum

```
</details>