# Slot: dissolved oxygen in fluids (diss_oxygen_fluid)


_Concentration of dissolved oxygen in the oil field produced fluids as it contributes to oxgen-corrosion and microbial activity (e.g. Mic)._



URI: [MIXS:0000438](https://w3id.org/mixs/0000438)




## Inheritance

* [core_field](core_field.md)
    * **diss_oxygen_fluid**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved oxygen in fluids




## Examples

| Value |
| --- |
|  |

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
name: diss_oxygen_fluid
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
description: Concentration of dissolved oxygen in the oil field produced fluids as
  it contributes to oxgen-corrosion and microbial activity (e.g. Mic).
title: dissolved oxygen in fluids
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved oxygen in fluids
rank: 1000
is_a: core field
slot_uri: MIXS:0000438
multivalued: false
alias: diss_oxygen_fluid
domain_of:
- Biosample
range: QuantityValue

```
</details>