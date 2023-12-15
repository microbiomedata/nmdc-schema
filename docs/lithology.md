# Slot: lithology (lithology)


_Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000990](https://w3id.org/mixs/0000990)




## Inheritance

* [core_field](core_field.md)
    * **lithology**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [LithologyEnum](LithologyEnum.md)



## Aliases


* lithology




## Examples

| Value |
| --- |
| Volcanic |

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
name: lithology
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: 'Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination).
  If "other" is specified, please propose entry in "additional info" field'
title: lithology
examples:
- value: Volcanic
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- lithology
rank: 1000
is_a: core field
slot_uri: MIXS:0000990
multivalued: false
alias: lithology
domain_of:
- Biosample
range: lithology_enum

```
</details>