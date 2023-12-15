# Slot: bacterial production (bac_prod)


_Bacterial production in the water column measured by isotope uptake_



URI: [MIXS:0000683](https://w3id.org/mixs/0000683)




## Inheritance

* [core_field](core_field.md)
    * **bac_prod**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* bacterial production




## Examples

| Value |
| --- |
| 5 milligram per cubic meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per cubic meter per day || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bac_prod
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per cubic meter per day
  occurrence:
    tag: occurrence
    value: '1'
description: Bacterial production in the water column measured by isotope uptake
title: bacterial production
examples:
- value: 5 milligram per cubic meter per day
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bacterial production
rank: 1000
is_a: core field
slot_uri: MIXS:0000683
multivalued: false
alias: bac_prod
domain_of:
- Biosample
range: QuantityValue

```
</details>