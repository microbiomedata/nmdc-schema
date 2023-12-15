# Slot: bacterial respiration (bac_resp)


_Measurement of bacterial respiration in the water column_



URI: [MIXS:0000684](https://w3id.org/mixs/0000684)




## Inheritance

* [core_field](core_field.md)
    * **bac_resp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* bacterial respiration




## Examples

| Value |
| --- |
| 300 micromole oxygen per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per cubic meter per day, micromole oxygen per liter per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bac_resp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per cubic meter per day, micromole oxygen per liter per hour
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of bacterial respiration in the water column
title: bacterial respiration
examples:
- value: 300 micromole oxygen per liter per hour
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bacterial respiration
rank: 1000
is_a: core field
slot_uri: MIXS:0000684
multivalued: false
alias: bac_resp
domain_of:
- Biosample
range: QuantityValue

```
</details>