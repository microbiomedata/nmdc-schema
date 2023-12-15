# Slot: sulfate (sulfate)


_Concentration of sulfate in the sample_



URI: [MIXS:0000423](https://w3id.org/mixs/0000423)




## Inheritance

* [core_field](core_field.md)
    * **sulfate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sulfate




## Examples

| Value |
| --- |
| 5 micromole per liter |

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
name: sulfate
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
description: Concentration of sulfate in the sample
title: sulfate
examples:
- value: 5 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sulfate
rank: 1000
is_a: core field
slot_uri: MIXS:0000423
multivalued: false
alias: sulfate
domain_of:
- Biosample
range: QuantityValue

```
</details>