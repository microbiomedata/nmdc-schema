# Slot: soil type method (soil_type_meth)


_Reference or method used in determining soil series name or other lower-level classification_



URI: [MIXS:0000334](https://w3id.org/mixs/0000334)




## Inheritance

* [core_field](core_field.md)
    * **soil_type_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* soil type method




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
name: soil_type_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining soil series name or other lower-level
  classification
title: soil type method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil type method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000334
multivalued: false
alias: soil_type_meth
domain_of:
- Biosample
range: TextValue

```
</details>