# Slot: train stop collection location (train_stop_loc)


_The train stop collection location_



URI: [MIXS:0000839](https://w3id.org/mixs/0000839)




## Inheritance

* [core_field](core_field.md)
    * **train_stop_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TrainStopLocEnum](TrainStopLocEnum.md)



## Aliases


* train stop collection location




## Examples

| Value |
| --- |
| end |

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
name: train_stop_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The train stop collection location
title: train stop collection location
examples:
- value: end
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- train stop collection location
rank: 1000
is_a: core field
slot_uri: MIXS:0000839
multivalued: false
alias: train_stop_loc
domain_of:
- Biosample
range: train_stop_loc_enum

```
</details>