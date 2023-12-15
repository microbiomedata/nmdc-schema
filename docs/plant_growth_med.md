# Slot: plant growth medium (plant_growth_med)


_Specification of the media for growing the plants or tissue cultured samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in vitro liquid culture medium. Recommended value is a specific value from EO:plant growth medium (follow this link for terms http://purl.obolibrary.org/obo/EO_0007147) or other controlled vocabulary_



URI: [MIXS:0001057](https://w3id.org/mixs/0001057)




## Inheritance

* [core_field](core_field.md)
    * **plant_growth_med**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* plant growth medium




## Examples

| Value |
| --- |
| hydroponic plant culture media [EO:0007067] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | EO or enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: plant_growth_med
annotations:
  expected_value:
    tag: expected_value
    value: EO or enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Specification of the media for growing the plants or tissue cultured
  samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in vitro
  liquid culture medium. Recommended value is a specific value from EO:plant growth
  medium (follow this link for terms http://purl.obolibrary.org/obo/EO_0007147) or
  other controlled vocabulary
title: plant growth medium
examples:
- value: hydroponic plant culture media [EO:0007067]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- plant growth medium
rank: 1000
is_a: core field
slot_uri: MIXS:0001057
multivalued: false
alias: plant_growth_med
domain_of:
- Biosample
range: ControlledTermValue

```
</details>