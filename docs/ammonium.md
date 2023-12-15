# Slot: ammonium (ammonium)


_Concentration of ammonium in the sample_



URI: [MIXS:0000427](https://w3id.org/mixs/0000427)




## Inheritance

* [core_field](core_field.md)
    * **ammonium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* ammonium




## Examples

| Value |
| --- |
| 1.5 milligram per liter |

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
name: ammonium
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
description: Concentration of ammonium in the sample
title: ammonium
examples:
- value: 1.5 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ammonium
rank: 1000
is_a: core field
slot_uri: MIXS:0000427
multivalued: false
alias: ammonium
domain_of:
- Biosample
range: QuantityValue

```
</details>