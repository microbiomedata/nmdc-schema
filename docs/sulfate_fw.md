# Slot: sulfate in formation water (sulfate_fw)


_Original sulfate concentration in the hydrocarbon resource_



URI: [MIXS:0000407](https://w3id.org/mixs/0000407)




## Inheritance

* [core_field](core_field.md)
    * **sulfate_fw**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sulfate in formation water




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sulfate_fw
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Original sulfate concentration in the hydrocarbon resource
title: sulfate in formation water
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sulfate in formation water
rank: 1000
is_a: core field
slot_uri: MIXS:0000407
multivalued: false
alias: sulfate_fw
domain_of:
- Biosample
range: QuantityValue

```
</details>