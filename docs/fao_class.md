# Slot: soil_taxonomic/FAO classification (fao_class)


_Soil classification from the FAO World Reference Database for Soil Resources. The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups_



URI: [MIXS:0001083](https://w3id.org/mixs/0001083)




## Inheritance

* [core_field](core_field.md)
    * **fao_class**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FaoClassEnum](FaoClassEnum.md)



## Aliases


* soil_taxonomic/FAO classification




## Examples

| Value |
| --- |
| Luvisols |

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
name: fao_class
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Soil classification from the FAO World Reference Database for Soil Resources.
  The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups
title: soil_taxonomic/FAO classification
examples:
- value: Luvisols
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil_taxonomic/FAO classification
rank: 1000
is_a: core field
slot_uri: MIXS:0001083
multivalued: false
alias: fao_class
domain_of:
- Biosample
range: fao_class_enum

```
</details>