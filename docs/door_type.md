# Slot: door type (door_type)


_The type of door material_



URI: [MIXS:0000794](https://w3id.org/mixs/0000794)




## Inheritance

* [core_field](core_field.md)
    * **door_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DoorTypeEnum](DoorTypeEnum.md)



## Aliases


* door type




## Examples

| Value |
| --- |
| wooden |

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
name: door_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of door material
title: door type
examples:
- value: wooden
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- door type
rank: 1000
is_a: core field
slot_uri: MIXS:0000794
multivalued: false
alias: door_type
domain_of:
- Biosample
range: door_type_enum

```
</details>