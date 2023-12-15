# Slot: mechanical structure (mech_struc)


_mechanical structure: a moving structure_



URI: [MIXS:0000815](https://w3id.org/mixs/0000815)




## Inheritance

* [core_field](core_field.md)
    * **mech_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [MechStrucEnum](MechStrucEnum.md)



## Aliases


* mechanical structure




## Examples

| Value |
| --- |
| elevator |

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
name: mech_struc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: 'mechanical structure: a moving structure'
title: mechanical structure
examples:
- value: elevator
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mechanical structure
rank: 1000
is_a: core field
slot_uri: MIXS:0000815
multivalued: false
alias: mech_struc
domain_of:
- Biosample
range: mech_struc_enum

```
</details>