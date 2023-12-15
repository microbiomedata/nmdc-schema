# Slot: calcium (calcium)


_Concentration of calcium in the sample_



URI: [MIXS:0000432](https://w3id.org/mixs/0000432)




## Inheritance

* [core_field](core_field.md)
    * **calcium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* calcium




## Examples

| Value |
| --- |
| 0.2 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, micromole per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: calcium
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, micromole per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of calcium in the sample
title: calcium
examples:
- value: 0.2 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- calcium
rank: 1000
is_a: core field
slot_uri: MIXS:0000432
multivalued: false
alias: calcium
domain_of:
- Biosample
range: QuantityValue

```
</details>