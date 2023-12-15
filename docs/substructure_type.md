# Slot: substructure type (substructure_type)


_The substructure or under building is that largely hidden section of the building which is built off the foundations to the ground floor level_



URI: [MIXS:0000767](https://w3id.org/mixs/0000767)




## Inheritance

* [core_field](core_field.md)
    * **substructure_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SubstructureTypeEnum](SubstructureTypeEnum.md)

* Multivalued: True



## Aliases


* substructure type




## Examples

| Value |
| --- |
| basement |

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
name: substructure_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: The substructure or under building is that largely hidden section of
  the building which is built off the foundations to the ground floor level
title: substructure type
examples:
- value: basement
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- substructure type
rank: 1000
is_a: core field
slot_uri: MIXS:0000767
multivalued: true
alias: substructure_type
domain_of:
- Biosample
range: substructure_type_enum

```
</details>