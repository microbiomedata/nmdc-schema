# Slot: building setting (building_setting)


_A location (geography) where a building is set_



URI: [MIXS:0000768](https://w3id.org/mixs/0000768)




## Inheritance

* [core_field](core_field.md)
    * **building_setting**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [BuildingSettingEnum](BuildingSettingEnum.md)



## Aliases


* building setting




## Examples

| Value |
| --- |
| rural |

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
name: building_setting
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: A location (geography) where a building is set
title: building setting
examples:
- value: rural
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- building setting
rank: 1000
is_a: core field
slot_uri: MIXS:0000768
multivalued: false
alias: building_setting
domain_of:
- Biosample
range: building_setting_enum

```
</details>