# Slot: seasonal use (season_use)


_The seasons the space is occupied_



URI: [MIXS:0000830](https://w3id.org/mixs/0000830)




## Inheritance

* [core_field](core_field.md)
    * **season_use**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SeasonUseEnum](SeasonUseEnum.md)



## Aliases


* seasonal use




## Examples

| Value |
| --- |
| Winter |

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
name: season_use
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The seasons the space is occupied
title: seasonal use
examples:
- value: Winter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- seasonal use
rank: 1000
is_a: core field
slot_uri: MIXS:0000830
multivalued: false
alias: season_use
domain_of:
- Biosample
range: season_use_enum

```
</details>