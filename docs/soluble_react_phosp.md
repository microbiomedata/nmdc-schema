# Slot: soluble reactive phosphorus (soluble_react_phosp)


_Concentration of soluble reactive phosphorus_



URI: [MIXS:0000738](https://w3id.org/mixs/0000738)




## Inheritance

* [core_field](core_field.md)
    * **soluble_react_phosp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* soluble reactive phosphorus




## Examples

| Value |
| --- |
| 0.1 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: soluble_react_phosp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of soluble reactive phosphorus
title: soluble reactive phosphorus
examples:
- value: 0.1 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soluble reactive phosphorus
rank: 1000
is_a: core field
slot_uri: MIXS:0000738
multivalued: false
alias: soluble_react_phosp
domain_of:
- Biosample
range: QuantityValue

```
</details>