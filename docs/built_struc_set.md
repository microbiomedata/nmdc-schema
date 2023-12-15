# Slot: built structure setting (built_struc_set)


_The characterization of the location of the built structure as high or low human density_



URI: [MIXS:0000778](https://w3id.org/mixs/0000778)




## Inheritance

* [core_field](core_field.md)
    * **built_struc_set**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* built structure setting




## Examples

| Value |
| --- |
| rural |

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
name: built_struc_set
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The characterization of the location of the built structure as high or
  low human density
title: built structure setting
examples:
- value: rural
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- built structure setting
rank: 1000
is_a: core field
string_serialization: '[urban|rural]'
slot_uri: MIXS:0000778
multivalued: false
alias: built_struc_set
domain_of:
- Biosample
range: TextValue

```
</details>