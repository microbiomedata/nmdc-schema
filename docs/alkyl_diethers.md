# Slot: alkyl diethers (alkyl_diethers)


_Concentration of alkyl diethers_



URI: [MIXS:0000490](https://w3id.org/mixs/0000490)




## Inheritance

* [core_field](core_field.md)
    * **alkyl_diethers**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* alkyl diethers




## Examples

| Value |
| --- |
| 0.005 mole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | mole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alkyl_diethers
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: mole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of alkyl diethers
title: alkyl diethers
examples:
- value: 0.005 mole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- alkyl diethers
rank: 1000
is_a: core field
slot_uri: MIXS:0000490
multivalued: false
alias: alkyl_diethers
domain_of:
- Biosample
range: QuantityValue

```
</details>