# Slot: host subject id (host_subject_id)


_A unique identifier by which each subject can be referred to, de-identified._



URI: [MIXS:0000861](https://w3id.org/mixs/0000861)




## Inheritance

* [core_field](core_field.md)
    * **host_subject_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host subject id




## Examples

| Value |
| --- |
| MPI123 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | unique identifier || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_subject_id
annotations:
  expected_value:
    tag: expected_value
    value: unique identifier
  occurrence:
    tag: occurrence
    value: '1'
description: A unique identifier by which each subject can be referred to, de-identified.
title: host subject id
examples:
- value: MPI123
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host subject id
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000861
multivalued: false
alias: host_subject_id
domain_of:
- Biosample
range: TextValue

```
</details>