# Slot: water feature type (water_feat_type)


_The type of water feature present within the building being sampled_



URI: [MIXS:0000847](https://w3id.org/mixs/0000847)




## Inheritance

* [core_field](core_field.md)
    * **water_feat_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WaterFeatTypeEnum](WaterFeatTypeEnum.md)



## Aliases


* water feature type




## Examples

| Value |
| --- |
| stream |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_feat_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of water feature present within the building being sampled
title: water feature type
examples:
- value: stream
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water feature type
rank: 1000
is_a: core field
slot_uri: MIXS:0000847
multivalued: false
alias: water_feat_type
domain_of:
- Biosample
range: water_feat_type_enum

```
</details>