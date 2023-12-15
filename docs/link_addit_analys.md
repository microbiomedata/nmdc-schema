# Slot: links to additional analysis (link_addit_analys)


_Link to additional analysis results performed on the sample_



URI: [MIXS:0000340](https://w3id.org/mixs/0000340)




## Inheritance

* [core_field](core_field.md)
    * **link_addit_analys**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* links to additional analysis




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
name: link_addit_analys
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Link to additional analysis results performed on the sample
title: links to additional analysis
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- links to additional analysis
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000340
multivalued: false
alias: link_addit_analys
domain_of:
- Biosample
range: TextValue

```
</details>