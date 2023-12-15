# Slot: current vegetation method (cur_vegetation_meth)


_Reference or method used in vegetation classification_



URI: [MIXS:0000314](https://w3id.org/mixs/0000314)




## Inheritance

* [core_field](core_field.md)
    * **cur_vegetation_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* current vegetation method




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
name: cur_vegetation_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in vegetation classification
title: current vegetation method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- current vegetation method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000314
multivalued: false
alias: cur_vegetation_meth
domain_of:
- Biosample
range: TextValue

```
</details>