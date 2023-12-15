# Slot: tidal stage (tidal_stage)


_Stage of tide_



URI: [MIXS:0000750](https://w3id.org/mixs/0000750)




## Inheritance

* [core_field](core_field.md)
    * **tidal_stage**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TidalStageEnum](TidalStageEnum.md)



## Aliases


* tidal stage




## Examples

| Value |
| --- |
| high tide |

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
name: tidal_stage
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Stage of tide
title: tidal stage
examples:
- value: high tide
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- tidal stage
rank: 1000
is_a: core field
slot_uri: MIXS:0000750
multivalued: false
alias: tidal_stage
domain_of:
- Biosample
range: tidal_stage_enum

```
</details>