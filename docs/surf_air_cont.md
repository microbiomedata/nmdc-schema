# Slot: surface-air contaminant (surf_air_cont)


_Contaminant identified on surface_



URI: [MIXS:0000759](https://w3id.org/mixs/0000759)




## Inheritance

* [core_field](core_field.md)
    * **surf_air_cont**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SurfAirContEnum](SurfAirContEnum.md)

* Multivalued: True



## Aliases


* surface-air contaminant




## Examples

| Value |
| --- |
| radon |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: surf_air_cont
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: Contaminant identified on surface
title: surface-air contaminant
examples:
- value: radon
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface-air contaminant
rank: 1000
is_a: core field
slot_uri: MIXS:0000759
multivalued: true
alias: surf_air_cont
domain_of:
- Biosample
range: surf_air_cont_enum

```
</details>