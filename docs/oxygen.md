# Slot: oxygen (oxygen)


_Oxygen (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000104](https://w3id.org/mixs/0000104)




## Inheritance

* [core_field](core_field.md)
    * **oxygen**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* oxygen




## Examples

| Value |
| --- |
| 600 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: oxygen
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Oxygen (gas) amount or concentration at the time of sampling
title: oxygen
examples:
- value: 600 parts per million
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- oxygen
rank: 1000
is_a: core field
slot_uri: MIXS:0000104
multivalued: false
alias: oxygen
domain_of:
- Biosample
range: QuantityValue

```
</details>