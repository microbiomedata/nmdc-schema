# Slot: carbon dioxide (carb_dioxide)


_Carbon dioxide (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000097](https://w3id.org/mixs/0000097)




## Inheritance

* [core_field](core_field.md)
    * **carb_dioxide**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* carbon dioxide




## Examples

| Value |
| --- |
| 410 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: carb_dioxide
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Carbon dioxide (gas) amount or concentration at the time of sampling
title: carbon dioxide
examples:
- value: 410 parts per million
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- carbon dioxide
rank: 1000
is_a: core field
slot_uri: MIXS:0000097
multivalued: false
alias: carb_dioxide
domain_of:
- Biosample
range: QuantityValue

```
</details>