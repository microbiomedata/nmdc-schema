# Slot: water content method (water_cont_soil_meth)


_Reference or method used in determining the water content of soil_



URI: [MIXS:0000323](https://w3id.org/mixs/0000323)




## Inheritance

* [core_field](core_field.md)
    * **water_cont_soil_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [String](String.md)



## Aliases


* water content method




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
name: water_cont_soil_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining the water content of soil
title: water content method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water content method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000323
multivalued: false
alias: water_cont_soil_meth
domain_of:
- Biosample
range: string

```
</details>