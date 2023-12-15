# Slot: salinity method (salinity_meth)


_Reference or method used in determining salinity_



URI: [MIXS:0000341](https://w3id.org/mixs/0000341)




## Inheritance

* [core_field](core_field.md)
    * **salinity_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* salinity method




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
name: salinity_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining salinity
title: salinity method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- salinity method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000341
multivalued: false
alias: salinity_meth
domain_of:
- Biosample
range: TextValue

```
</details>