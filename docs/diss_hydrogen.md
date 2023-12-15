# Slot: dissolved hydrogen (diss_hydrogen)


_Concentration of dissolved hydrogen_



URI: [MIXS:0000179](https://w3id.org/mixs/0000179)




## Inheritance

* [core_field](core_field.md)
    * **diss_hydrogen**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved hydrogen




## Examples

| Value |
| --- |
| 0.3 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: diss_hydrogen
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of dissolved hydrogen
title: dissolved hydrogen
examples:
- value: 0.3 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved hydrogen
rank: 1000
is_a: core field
slot_uri: MIXS:0000179
multivalued: false
alias: diss_hydrogen
domain_of:
- Biosample
range: QuantityValue

```
</details>