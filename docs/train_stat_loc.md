# Slot: train station collection location (train_stat_loc)


_The train station collection location_



URI: [MIXS:0000838](https://w3id.org/mixs/0000838)




## Inheritance

* [core_field](core_field.md)
    * **train_stat_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TrainStatLocEnum](TrainStatLocEnum.md)



## Aliases


* train station collection location




## Examples

| Value |
| --- |
| forest hills |

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
name: train_stat_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The train station collection location
title: train station collection location
examples:
- value: forest hills
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- train station collection location
rank: 1000
is_a: core field
slot_uri: MIXS:0000838
multivalued: false
alias: train_stat_loc
domain_of:
- Biosample
range: train_stat_loc_enum

```
</details>