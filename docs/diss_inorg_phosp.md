# Slot: dissolved inorganic phosphorus (diss_inorg_phosp)


_Concentration of dissolved inorganic phosphorus in the sample_



URI: [MIXS:0000106](https://w3id.org/mixs/0000106)




## Inheritance

* [core_field](core_field.md)
    * **diss_inorg_phosp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved inorganic phosphorus




## Examples

| Value |
| --- |
| 56.5 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_inorg_phosp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved inorganic phosphorus in the sample
title: dissolved inorganic phosphorus
examples:
- value: 56.5 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved inorganic phosphorus
rank: 1000
is_a: core field
slot_uri: MIXS:0000106
multivalued: false
alias: diss_inorg_phosp
domain_of:
- Biosample
range: QuantityValue

```
</details>