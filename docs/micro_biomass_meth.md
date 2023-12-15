# Slot: microbial biomass method (micro_biomass_meth)


_Reference or method used in determining microbial biomass_



URI: [MIXS:0000339](https://w3id.org/mixs/0000339)




## Inheritance

* [core_field](core_field.md)
    * **micro_biomass_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* microbial biomass method




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
name: micro_biomass_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining microbial biomass
title: microbial biomass method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- microbial biomass method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000339
multivalued: false
alias: micro_biomass_meth
domain_of:
- Biosample
range: string

```
</details>