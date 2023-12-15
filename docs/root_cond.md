# Slot: rooting conditions (root_cond)


_Relevant rooting conditions such as field plot size, sowing density, container dimensions, number of plants per container._



URI: [MIXS:0001061](https://w3id.org/mixs/0001061)




## Inheritance

* [core_field](core_field.md)
    * **root_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* rooting conditions




## Examples

| Value |
| --- |
| http://himedialabs.com/TD/PT158.pdf |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI,url or free text || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: root_cond
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI,url or free text
  occurrence:
    tag: occurrence
    value: '1'
description: Relevant rooting conditions such as field plot size, sowing density,
  container dimensions, number of plants per container.
title: rooting conditions
examples:
- value: http://himedialabs.com/TD/PT158.pdf
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- rooting conditions
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}|{text}'
slot_uri: MIXS:0001061
multivalued: false
alias: root_cond
domain_of:
- Biosample
range: TextValue

```
</details>