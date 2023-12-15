# Slot: carbon/nitrogen ratio (carb_nitro_ratio)


_Ratio of amount or concentrations of carbon to nitrogen_



URI: [MIXS:0000310](https://w3id.org/mixs/0000310)




## Inheritance

* [core_field](core_field.md)
    * **carb_nitro_ratio**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* carbon/nitrogen ratio




## Examples

| Value |
| --- |
| 0.417361111 |

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
name: carb_nitro_ratio
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Ratio of amount or concentrations of carbon to nitrogen
title: carbon/nitrogen ratio
examples:
- value: '0.417361111'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- carbon/nitrogen ratio
rank: 1000
is_a: core field
slot_uri: MIXS:0000310
multivalued: false
alias: carb_nitro_ratio
domain_of:
- Biosample
range: QuantityValue

```
</details>