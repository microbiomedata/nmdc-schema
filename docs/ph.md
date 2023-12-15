# Slot: pH (ph)


_Ph measurement of the sample, or liquid portion of sample, or aqueous phase of the fluid_



URI: [MIXS:0001001](https://w3id.org/mixs/0001001)




## Inheritance

* [core_field](core_field.md)
    * **ph**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Double](Double.md)



## Aliases


* pH




## Examples

| Value |
| --- |
| 7.2 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: ph
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Ph measurement of the sample, or liquid portion of sample, or aqueous
  phase of the fluid
title: pH
examples:
- value: '7.2'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pH
rank: 1000
is_a: core field
slot_uri: MIXS:0001001
multivalued: false
alias: ph
domain_of:
- Biosample
range: double

```
</details>