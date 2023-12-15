# Slot: alkalinity (alkalinity)


_Alkalinity, the ability of a solution to neutralize acids to the equivalence point of carbonate or bicarbonate_



URI: [MIXS:0000421](https://w3id.org/mixs/0000421)




## Inheritance

* [core_field](core_field.md)
    * **alkalinity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* alkalinity




## Examples

| Value |
| --- |
| 50 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milliequivalent per liter, milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alkalinity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milliequivalent per liter, milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Alkalinity, the ability of a solution to neutralize acids to the equivalence
  point of carbonate or bicarbonate
title: alkalinity
examples:
- value: 50 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- alkalinity
rank: 1000
is_a: core field
slot_uri: MIXS:0000421
multivalued: false
alias: alkalinity
domain_of:
- Biosample
range: QuantityValue

```
</details>