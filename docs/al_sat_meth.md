# Slot: extreme_unusual_properties/Al saturation method (al_sat_meth)


_Reference or method used in determining Al saturation_



URI: [MIXS:0000324](https://w3id.org/mixs/0000324)




## Inheritance

* [core_field](core_field.md)
    * **al_sat_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* extreme_unusual_properties/Al saturation method




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI or URL || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: al_sat_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or URL
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining Al saturation
title: extreme_unusual_properties/Al saturation method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- extreme_unusual_properties/Al saturation method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000324
multivalued: false
alias: al_sat_meth
domain_of:
- Biosample
range: TextValue

```
</details>