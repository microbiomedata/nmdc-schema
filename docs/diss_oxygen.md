# Slot: dissolved oxygen (diss_oxygen)


_Concentration of dissolved oxygen_



URI: [MIXS:0000119](https://w3id.org/mixs/0000119)




## Inheritance

* [core_field](core_field.md)
    * **diss_oxygen**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved oxygen




## Examples

| Value |
| --- |
| 175 micromole per kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per kilogram, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_oxygen
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per kilogram, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved oxygen
title: dissolved oxygen
examples:
- value: 175 micromole per kilogram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved oxygen
rank: 1000
is_a: core field
slot_uri: MIXS:0000119
multivalued: false
alias: diss_oxygen
domain_of:
- Biosample
range: QuantityValue

```
</details>