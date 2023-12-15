# Slot: host growth conditions (host_growth_cond)


_Literature reference giving growth conditions of the host_



URI: [MIXS:0000871](https://w3id.org/mixs/0000871)




## Inheritance

* [core_field](core_field.md)
    * **host_growth_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host growth conditions




## Examples

| Value |
| --- |
| https://academic.oup.com/icesjms/article/68/2/349/617247 |

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
name: host_growth_cond
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI,url or free text
  occurrence:
    tag: occurrence
    value: '1'
description: Literature reference giving growth conditions of the host
title: host growth conditions
examples:
- value: https://academic.oup.com/icesjms/article/68/2/349/617247
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host growth conditions
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}|{text}'
slot_uri: MIXS:0000871
multivalued: false
alias: host_growth_cond
domain_of:
- Biosample
range: TextValue

```
</details>