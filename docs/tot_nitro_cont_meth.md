# Slot: total nitrogen content method (tot_nitro_cont_meth)


_Reference or method used in determining the total nitrogen_



URI: [MIXS:0000338](https://w3id.org/mixs/0000338)




## Inheritance

* [core_field](core_field.md)
    * **tot_nitro_cont_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [String](String.md)



## Aliases


* total nitrogen content method




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
name: tot_nitro_cont_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining the total nitrogen
title: total nitrogen content method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total nitrogen content method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000338
multivalued: false
alias: tot_nitro_cont_meth
domain_of:
- Biosample
range: string

```
</details>