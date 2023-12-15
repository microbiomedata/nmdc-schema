# Slot: space typical state (space_typ_state)


_Customary or normal state of the space_



URI: [MIXS:0000770](https://w3id.org/mixs/0000770)




## Inheritance

* [core_field](core_field.md)
    * **space_typ_state**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* space typical state




## Examples

| Value |
| --- |
| typically occupied |

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
name: space_typ_state
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Customary or normal state of the space
title: space typical state
examples:
- value: typically occupied
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- space typical state
rank: 1000
is_a: core field
string_serialization: '[typically occupied|typically unoccupied]'
slot_uri: MIXS:0000770
multivalued: false
alias: space_typ_state
domain_of:
- Biosample
range: TextValue

```
</details>