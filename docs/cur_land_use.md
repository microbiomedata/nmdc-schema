# Slot: current land use (cur_land_use)


_Present state of sample site_



URI: [MIXS:0001080](https://w3id.org/mixs/0001080)




## Inheritance

* [core_field](core_field.md)
    * **cur_land_use**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [CurLandUseEnum](CurLandUseEnum.md)



## Aliases


* current land use




## Examples

| Value |
| --- |
| conifers |

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
name: cur_land_use
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Present state of sample site
title: current land use
examples:
- value: conifers
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- current land use
rank: 1000
is_a: core field
slot_uri: MIXS:0001080
multivalued: false
alias: cur_land_use
domain_of:
- Biosample
range: cur_land_use_enum

```
</details>