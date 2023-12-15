# Slot: dissolved carbon dioxide (diss_carb_dioxide)


_Concentration of dissolved carbon dioxide in the sample or liquid portion of the sample_



URI: [MIXS:0000436](https://w3id.org/mixs/0000436)




## Inheritance

* [core_field](core_field.md)
    * **diss_carb_dioxide**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved carbon dioxide




## Examples

| Value |
| --- |
| 5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_carb_dioxide
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved carbon dioxide in the sample or liquid portion
  of the sample
title: dissolved carbon dioxide
examples:
- value: 5 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved carbon dioxide
rank: 1000
is_a: core field
slot_uri: MIXS:0000436
multivalued: false
alias: diss_carb_dioxide
domain_of:
- Biosample
range: QuantityValue

```
</details>