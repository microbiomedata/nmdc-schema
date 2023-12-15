# Slot: vfa in formation water (vfa_fw)


_Original volatile fatty acid concentration in the hydrocarbon resource_



URI: [MIXS:0000408](https://w3id.org/mixs/0000408)




## Inheritance

* [core_field](core_field.md)
    * **vfa_fw**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* vfa in formation water




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
name: vfa_fw
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
description: Original volatile fatty acid concentration in the hydrocarbon resource
title: vfa in formation water
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- vfa in formation water
rank: 1000
is_a: core field
slot_uri: MIXS:0000408
multivalued: false
alias: vfa_fw
domain_of:
- Biosample
range: QuantityValue

```
</details>