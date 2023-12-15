# Slot: indoor surface (indoor_surf)


_Type of indoor surface_



URI: [MIXS:0000764](https://w3id.org/mixs/0000764)




## Inheritance

* [core_field](core_field.md)
    * **indoor_surf**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [IndoorSurfEnum](IndoorSurfEnum.md)



## Aliases


* indoor surface




## Examples

| Value |
| --- |
| wall |

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
name: indoor_surf
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Type of indoor surface
title: indoor surface
examples:
- value: wall
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- indoor surface
rank: 1000
is_a: core field
slot_uri: MIXS:0000764
multivalued: false
alias: indoor_surf
domain_of:
- Biosample
range: indoor_surf_enum

```
</details>