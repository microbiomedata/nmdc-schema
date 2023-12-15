# Slot: architectural structure (arch_struc)


_An architectural structure is a human-made, free-standing, immobile outdoor construction_



URI: [MIXS:0000774](https://w3id.org/mixs/0000774)




## Inheritance

* [core_field](core_field.md)
    * **arch_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ArchStrucEnum](ArchStrucEnum.md)



## Aliases


* architectural structure




## Examples

| Value |
| --- |
| shed |

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
name: arch_struc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: An architectural structure is a human-made, free-standing, immobile outdoor
  construction
title: architectural structure
examples:
- value: shed
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- architectural structure
rank: 1000
is_a: core field
slot_uri: MIXS:0000774
multivalued: false
alias: arch_struc
domain_of:
- Biosample
range: arch_struc_enum

```
</details>