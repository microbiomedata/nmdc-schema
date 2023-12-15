# Slot: extreme_unusual_properties/heavy metals method (heavy_metals_meth)


_Reference or method used in determining heavy metals_



URI: [MIXS:0000343](https://w3id.org/mixs/0000343)




## Inheritance

* [core_field](core_field.md)
    * **heavy_metals_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* extreme_unusual_properties/heavy metals method




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
name: heavy_metals_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining heavy metals
title: extreme_unusual_properties/heavy metals method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- extreme_unusual_properties/heavy metals method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000343
multivalued: false
alias: heavy_metals_meth
domain_of:
- Biosample
range: TextValue

```
</details>