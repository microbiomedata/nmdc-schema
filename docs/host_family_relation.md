# Slot: host family relationship (host_family_relation)


_Familial relationships to other hosts in the same study; can include multiple relationships_



URI: [MIXS:0000872](https://w3id.org/mixs/0000872)




## Inheritance

* [core_field](core_field.md)
    * **host_family_relation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True



## Aliases


* host family relationship




## Examples

| Value |
| --- |
| offspring;Mussel25 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | relationship type;arbitrary identifier || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_family_relation
annotations:
  expected_value:
    tag: expected_value
    value: relationship type;arbitrary identifier
  occurrence:
    tag: occurrence
    value: m
description: Familial relationships to other hosts in the same study; can include
  multiple relationships
title: host family relationship
examples:
- value: offspring;Mussel25
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host family relationship
rank: 1000
is_a: core field
string_serialization: '{text};{text}'
slot_uri: MIXS:0000872
multivalued: true
alias: host_family_relation
domain_of:
- Biosample
range: string

```
</details>