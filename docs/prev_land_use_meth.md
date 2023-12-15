# Slot: history/previous land use method (prev_land_use_meth)


_Reference or method used in determining previous land use and dates_



URI: [MIXS:0000316](https://w3id.org/mixs/0000316)




## Inheritance

* [core_field](core_field.md)
    * **prev_land_use_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* history/previous land use method




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
name: prev_land_use_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining previous land use and dates
title: history/previous land use method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/previous land use method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000316
multivalued: false
alias: prev_land_use_meth
domain_of:
- Biosample
range: string

```
</details>