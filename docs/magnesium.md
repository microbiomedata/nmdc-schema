# Slot: magnesium (magnesium)


_Concentration of magnesium in the sample_



URI: [MIXS:0000431](https://w3id.org/mixs/0000431)




## Inheritance

* [core_field](core_field.md)
    * **magnesium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* magnesium




## Examples

| Value |
| --- |
| 52.8 micromole per kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | mole per liter, milligram per liter, parts per million, micromole per kilogram || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: magnesium
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: mole per liter, milligram per liter, parts per million, micromole per kilogram
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of magnesium in the sample
title: magnesium
examples:
- value: 52.8 micromole per kilogram
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- magnesium
rank: 1000
is_a: core field
slot_uri: MIXS:0000431
multivalued: false
alias: magnesium
domain_of:
- Biosample
range: QuantityValue

```
</details>