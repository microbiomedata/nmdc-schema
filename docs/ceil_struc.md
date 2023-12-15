# Slot: ceiling structure (ceil_struc)


_The construction format of the ceiling_



URI: [MIXS:0000782](https://w3id.org/mixs/0000782)




## Inheritance

* [core_field](core_field.md)
    * **ceil_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* ceiling structure




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
name: ceil_struc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The construction format of the ceiling
title: ceiling structure
examples:
- value: concrete
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling structure
rank: 1000
is_a: core field
string_serialization: '[wood frame|concrete]'
slot_uri: MIXS:0000782
multivalued: false
alias: ceil_struc
domain_of:
- Biosample
range: TextValue

```
</details>