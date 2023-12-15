# Slot: wall construction type (wall_const_type)


_The building class of the wall defined by the composition of the building elements and fire-resistance rating._



URI: [MIXS:0000841](https://w3id.org/mixs/0000841)




## Inheritance

* [core_field](core_field.md)
    * **wall_const_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WallConstTypeEnum](WallConstTypeEnum.md)



## Aliases


* wall construction type




## Examples

| Value |
| --- |
| fire resistive |

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
name: wall_const_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The building class of the wall defined by the composition of the building
  elements and fire-resistance rating.
title: wall construction type
examples:
- value: fire resistive
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall construction type
rank: 1000
is_a: core field
slot_uri: MIXS:0000841
multivalued: false
alias: wall_const_type
domain_of:
- Biosample
range: wall_const_type_enum

```
</details>