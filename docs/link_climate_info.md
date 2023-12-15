# Slot: link to climate information (link_climate_info)


_Link to climate resource_



URI: [MIXS:0000328](https://w3id.org/mixs/0000328)




## Inheritance

* [core_field](core_field.md)
    * **link_climate_info**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* link to climate information




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
name: link_climate_info
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Link to climate resource
title: link to climate information
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- link to climate information
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000328
multivalued: false
alias: link_climate_info
domain_of:
- Biosample
range: TextValue

```
</details>