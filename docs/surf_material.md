# Slot: surface material (surf_material)


_Surface materials at the point of sampling_



URI: [MIXS:0000758](https://w3id.org/mixs/0000758)




## Inheritance

* [core_field](core_field.md)
    * **surf_material**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SurfMaterialEnum](SurfMaterialEnum.md)



## Aliases


* surface material




## Examples

| Value |
| --- |
| wood |

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
name: surf_material
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Surface materials at the point of sampling
title: surface material
examples:
- value: wood
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface material
rank: 1000
is_a: core field
slot_uri: MIXS:0000758
multivalued: false
alias: surf_material
domain_of:
- Biosample
range: surf_material_enum

```
</details>