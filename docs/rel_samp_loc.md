# Slot: relative sampling location (rel_samp_loc)


_The sampling location within the train car_



URI: [MIXS:0000821](https://w3id.org/mixs/0000821)




## Inheritance

* [core_field](core_field.md)
    * **rel_samp_loc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RelSampLocEnum](RelSampLocEnum.md)



## Aliases


* relative sampling location




## Examples

| Value |
| --- |
| center of car |

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
name: rel_samp_loc
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The sampling location within the train car
title: relative sampling location
examples:
- value: center of car
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- relative sampling location
rank: 1000
is_a: core field
slot_uri: MIXS:0000821
multivalued: false
alias: rel_samp_loc
domain_of:
- Biosample
range: rel_samp_loc_enum

```
</details>