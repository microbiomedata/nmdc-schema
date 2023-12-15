# Slot: ceiling condition (ceil_cond)


_The physical condition of the ceiling at the time of sampling; photos or video preferred; use drawings to indicate location of damaged areas_



URI: [MIXS:0000779](https://w3id.org/mixs/0000779)




## Inheritance

* [core_field](core_field.md)
    * **ceil_cond**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [CeilCondEnum](CeilCondEnum.md)



## Aliases


* ceiling condition




## Examples

| Value |
| --- |
| damaged |

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
name: ceil_cond
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The physical condition of the ceiling at the time of sampling; photos
  or video preferred; use drawings to indicate location of damaged areas
title: ceiling condition
examples:
- value: damaged
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling condition
rank: 1000
is_a: core field
slot_uri: MIXS:0000779
multivalued: false
alias: ceil_cond
domain_of:
- Biosample
range: ceil_cond_enum

```
</details>