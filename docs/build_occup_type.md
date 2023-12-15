# Slot: building occupancy type (build_occup_type)


_The primary function for which a building or discrete part of a building is intended to be used_



URI: [MIXS:0000761](https://w3id.org/mixs/0000761)




## Inheritance

* [core_field](core_field.md)
    * **build_occup_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [BuildOccupTypeEnum](BuildOccupTypeEnum.md)

* Multivalued: True



## Aliases


* building occupancy type




## Examples

| Value |
| --- |
| market |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: build_occup_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: The primary function for which a building or discrete part of a building
  is intended to be used
title: building occupancy type
examples:
- value: market
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- building occupancy type
rank: 1000
is_a: core field
slot_uri: MIXS:0000761
multivalued: true
alias: build_occup_type
domain_of:
- Biosample
range: build_occup_type_enum

```
</details>