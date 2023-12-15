# Slot: ancestral data (ances_data)


_Information about either pedigree or other ancestral information description (e.g. parental variety in case of mutant or selection), e.g. A/3*B (meaning [(A x B) x B] x B)_



URI: [MIXS:0000247](https://w3id.org/mixs/0000247)




## Inheritance

* [core_field](core_field.md)
    * **ances_data**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* ancestral data




## Examples

| Value |
| --- |
| A/3*B |

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
name: ances_data
annotations:
  expected_value:
    tag: expected_value
    value: free text
  occurrence:
    tag: occurrence
    value: '1'
description: Information about either pedigree or other ancestral information description
  (e.g. parental variety in case of mutant or selection), e.g. A/3*B (meaning [(A
  x B) x B] x B)
title: ancestral data
examples:
- value: A/3*B
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ancestral data
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000247
multivalued: false
alias: ances_data
domain_of:
- Biosample
range: TextValue

```
</details>