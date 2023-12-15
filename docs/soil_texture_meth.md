# Slot: soil texture method (soil_texture_meth)


_Reference or method used in determining soil texture_



URI: [MIXS:0000336](https://w3id.org/mixs/0000336)




## Inheritance

* [core_field](core_field.md)
    * **soil_texture_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* soil texture method




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI or url || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soil_texture_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining soil texture
title: soil texture method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil texture method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000336
multivalued: false
alias: soil_texture_meth
domain_of:
- Biosample
range: string

```
</details>