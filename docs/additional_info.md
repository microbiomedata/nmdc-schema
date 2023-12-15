# Slot: additional info (additional_info)


_Information that doesn't fit anywhere else. Can also be used to propose new entries for fields with controlled vocabulary_



URI: [MIXS:0000300](https://w3id.org/mixs/0000300)




## Inheritance

* [core_field](core_field.md)
    * **additional_info**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* additional info




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: additional_info
annotations:
  expected_value:
    tag: expected_value
    value: text
  occurrence:
    tag: occurrence
    value: '1'
description: Information that doesn't fit anywhere else. Can also be used to propose
  new entries for fields with controlled vocabulary
title: additional info
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- additional info
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000300
multivalued: false
alias: additional_info
domain_of:
- Biosample
range: TextValue

```
</details>