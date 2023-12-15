# Slot: profile position (profile_position)


_Cross-sectional position in the hillslope where sample was collected.sample area position in relation to surrounding areas_



URI: [MIXS:0001084](https://w3id.org/mixs/0001084)




## Inheritance

* [core_field](core_field.md)
    * **profile_position**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ProfilePositionEnum](ProfilePositionEnum.md)



## Aliases


* profile position




## Examples

| Value |
| --- |
| summit |

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
name: profile_position
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Cross-sectional position in the hillslope where sample was collected.sample
  area position in relation to surrounding areas
title: profile position
examples:
- value: summit
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- profile position
rank: 1000
is_a: core field
slot_uri: MIXS:0001084
multivalued: false
alias: profile_position
domain_of:
- Biosample
range: profile_position_enum

```
</details>