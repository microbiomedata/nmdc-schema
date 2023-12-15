# Slot: soil_taxonomic/local classification (local_class)


_Soil classification based on local soil classification system_



URI: [MIXS:0000330](https://w3id.org/mixs/0000330)




## Inheritance

* [core_field](core_field.md)
    * **local_class**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FieldResearchSite](FieldResearchSite.md) | A site, outside of a laboratory, from which biosamples may be collected |  no  |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* soil_taxonomic/local classification




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | local classification name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: local_class
annotations:
  expected_value:
    tag: expected_value
    value: local classification name
  occurrence:
    tag: occurrence
    value: '1'
description: Soil classification based on local soil classification system
title: soil_taxonomic/local classification
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil_taxonomic/local classification
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000330
multivalued: false
alias: local_class
domain_of:
- FieldResearchSite
- Biosample
range: TextValue

```
</details>