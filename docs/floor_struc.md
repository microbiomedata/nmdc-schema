# Slot: floor structure (floor_struc)


_Refers to the structural elements and subfloor upon which the finish flooring is installed_



URI: [MIXS:0000806](https://w3id.org/mixs/0000806)




## Inheritance

* [core_field](core_field.md)
    * **floor_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FloorStrucEnum](FloorStrucEnum.md)



## Aliases


* floor structure




## Examples

| Value |
| --- |
| concrete |

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
name: floor_struc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Refers to the structural elements and subfloor upon which the finish
  flooring is installed
title: floor structure
examples:
- value: concrete
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- floor structure
rank: 1000
is_a: core field
slot_uri: MIXS:0000806
multivalued: false
alias: floor_struc
domain_of:
- Biosample
range: floor_struc_enum

```
</details>