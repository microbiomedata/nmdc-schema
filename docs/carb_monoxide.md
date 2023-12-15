# Slot: carbon monoxide (carb_monoxide)


_Carbon monoxide (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000098](https://w3id.org/mixs/0000098)




## Inheritance

* [core_field](core_field.md)
    * **carb_monoxide**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* carbon monoxide




## Examples

| Value |
| --- |
| 0.1 parts per million |

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
name: carb_monoxide
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
description: Carbon monoxide (gas) amount or concentration at the time of sampling
title: carbon monoxide
examples:
- value: 0.1 parts per million
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- carbon monoxide
rank: 1000
is_a: core field
slot_uri: MIXS:0000098
multivalued: false
alias: carb_monoxide
domain_of:
- Biosample
range: QuantityValue

```
</details>