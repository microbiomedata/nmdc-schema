# Slot: wall surface treatment (wall_surf_treatment)


_The surface treatment of interior wall_



URI: [MIXS:0000845](https://w3id.org/mixs/0000845)




## Inheritance

* [core_field](core_field.md)
    * **wall_surf_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WallSurfTreatmentEnum](WallSurfTreatmentEnum.md)



## Aliases


* wall surface treatment




## Examples

| Value |
| --- |
| paneling |

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
name: wall_surf_treatment
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The surface treatment of interior wall
title: wall surface treatment
examples:
- value: paneling
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall surface treatment
rank: 1000
is_a: core field
slot_uri: MIXS:0000845
multivalued: false
alias: wall_surf_treatment
domain_of:
- Biosample
range: wall_surf_treatment_enum

```
</details>