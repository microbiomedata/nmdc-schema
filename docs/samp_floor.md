# Slot: sampling floor (samp_floor)


_The floor of the building, where the sampling room is located_



URI: [MIXS:0000828](https://w3id.org/mixs/0000828)




## Inheritance

* [core_field](core_field.md)
    * **samp_floor**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SampFloorEnum](SampFloorEnum.md)



## Aliases


* sampling floor




## Examples

| Value |
| --- |
| 4th floor |

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
name: samp_floor
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The floor of the building, where the sampling room is located
title: sampling floor
examples:
- value: 4th floor
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sampling floor
rank: 1000
is_a: core field
slot_uri: MIXS:0000828
multivalued: false
alias: samp_floor
domain_of:
- Biosample
range: samp_floor_enum

```
</details>