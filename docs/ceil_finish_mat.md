# Slot: ceiling finish material (ceil_finish_mat)


_The type of material used to finish a ceiling_



URI: [MIXS:0000780](https://w3id.org/mixs/0000780)




## Inheritance

* [core_field](core_field.md)
    * **ceil_finish_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [CeilFinishMatEnum](CeilFinishMatEnum.md)



## Aliases


* ceiling finish material




## Examples

| Value |
| --- |
| stucco |

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
name: ceil_finish_mat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of material used to finish a ceiling
title: ceiling finish material
examples:
- value: stucco
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling finish material
rank: 1000
is_a: core field
slot_uri: MIXS:0000780
multivalued: false
alias: ceil_finish_mat
domain_of:
- Biosample
range: ceil_finish_mat_enum

```
</details>