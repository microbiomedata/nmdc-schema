# Slot: room architectural elements (room_architec_elem)


_The unique details and component parts that, together, form the architecture of a distinguisahable space within a built structure_



URI: [MIXS:0000233](https://w3id.org/mixs/0000233)




## Inheritance

* [core_field](core_field.md)
    * **room_architec_elem**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* room architectural elements




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
name: room_architec_elem
annotations:
  expected_value:
    tag: expected_value
    value: free text
  occurrence:
    tag: occurrence
    value: '1'
description: The unique details and component parts that, together, form the architecture
  of a distinguisahable space within a built structure
title: room architectural elements
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room architectural elements
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000233
multivalued: false
alias: room_architec_elem
domain_of:
- Biosample
range: string

```
</details>