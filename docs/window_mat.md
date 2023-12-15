# Slot: window material (window_mat)


_The type of material used to finish a window_



URI: [MIXS:0000853](https://w3id.org/mixs/0000853)




## Inheritance

* [core_field](core_field.md)
    * **window_mat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowMatEnum](WindowMatEnum.md)



## Aliases


* window material




## Examples

| Value |
| --- |
| wood |

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
name: window_mat
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of material used to finish a window
title: window material
examples:
- value: wood
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window material
rank: 1000
is_a: core field
slot_uri: MIXS:0000853
multivalued: false
alias: window_mat
domain_of:
- Biosample
range: window_mat_enum

```
</details>