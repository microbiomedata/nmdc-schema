# Slot: total nitrogen content (tot_nitro_content)


_Total nitrogen content of the sample_



URI: [MIXS:0000530](https://w3id.org/mixs/0000530)




## Inheritance

* [core_field](core_field.md)
    * **tot_nitro_content**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total nitrogen content




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_nitro_content
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Total nitrogen content of the sample
title: total nitrogen content
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total nitrogen content
rank: 1000
is_a: core field
slot_uri: MIXS:0000530
multivalued: false
alias: tot_nitro_content
domain_of:
- Biosample
range: QuantityValue

```
</details>