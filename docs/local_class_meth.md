# Slot: soil_taxonomic/local classification method (local_class_meth)


_Reference or method used in determining the local soil classification_



URI: [MIXS:0000331](https://w3id.org/mixs/0000331)




## Inheritance

* [core_field](core_field.md)
    * **local_class_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* soil_taxonomic/local classification method




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
name: local_class_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining the local soil classification
title: soil_taxonomic/local classification method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil_taxonomic/local classification method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000331
multivalued: false
alias: local_class_meth
domain_of:
- Biosample
range: TextValue

```
</details>