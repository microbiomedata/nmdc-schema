# Slot: window condition (window_cond)


_The physical condition of the window at the time of sampling_



URI: [MIXS:0000849](https://w3id.org/mixs/0000849)




## Inheritance

* [core_field](core_field.md)
    * **window_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowCondEnum](WindowCondEnum.md)



## Aliases


* window condition




## Examples

| Value |
| --- |
| rupture |

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
name: window_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The physical condition of the window at the time of sampling
title: window condition
examples:
- value: rupture
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000849
multivalued: false
alias: window_cond
domain_of:
- Biosample
range: window_cond_enum

```
</details>