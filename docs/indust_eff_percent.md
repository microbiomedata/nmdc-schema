# Slot: industrial effluent percent (indust_eff_percent)


_Percentage of industrial effluents received by wastewater treatment plant_



URI: [MIXS:0000662](https://w3id.org/mixs/0000662)




## Inheritance

* [core_field](core_field.md)
    * **indust_eff_percent**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* industrial effluent percent




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | percentage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: indust_eff_percent
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: percentage
  occurrence:
    tag: occurrence
    value: '1'
description: Percentage of industrial effluents received by wastewater treatment plant
title: industrial effluent percent
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- industrial effluent percent
rank: 1000
is_a: core field
slot_uri: MIXS:0000662
multivalued: false
alias: indust_eff_percent
domain_of:
- Biosample
range: QuantityValue

```
</details>