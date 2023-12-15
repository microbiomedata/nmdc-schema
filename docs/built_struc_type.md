# Slot: built structure type (built_struc_type)


_A physical structure that is a body or assemblage of bodies in space to form a system capable of supporting loads_



URI: [MIXS:0000721](https://w3id.org/mixs/0000721)




## Inheritance

* [core_field](core_field.md)
    * **built_struc_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* built structure type




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | free text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: built_struc_type
annotations:
  expected_value:
    tag: expected_value
    value: free text
  occurrence:
    tag: occurrence
    value: '1'
description: A physical structure that is a body or assemblage of bodies in space
  to form a system capable of supporting loads
title: built structure type
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- built structure type
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000721
multivalued: false
alias: built_struc_type
domain_of:
- Biosample
range: TextValue

```
</details>