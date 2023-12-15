# Slot: primary treatment (primary_treatment)


_The process to produce both a generally homogeneous liquid capable of being treated biologically and a sludge that can be separately treated or processed_



URI: [MIXS:0000349](https://w3id.org/mixs/0000349)




## Inheritance

* [core_field](core_field.md)
    * **primary_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* primary treatment




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | primary treatment type || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: primary_treatment
annotations:
  expected_value:
    tag: expected_value
    value: primary treatment type
  occurrence:
    tag: occurrence
    value: '1'
description: The process to produce both a generally homogeneous liquid capable of
  being treated biologically and a sludge that can be separately treated or processed
title: primary treatment
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- primary treatment
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000349
multivalued: false
alias: primary_treatment
domain_of:
- Biosample
range: TextValue

```
</details>