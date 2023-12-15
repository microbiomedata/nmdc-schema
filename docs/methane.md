# Slot: methane (methane)


_Methane (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000101](https://w3id.org/mixs/0000101)




## Inheritance

* [core_field](core_field.md)
    * **methane**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* methane




## Examples

| Value |
| --- |
| 1800 parts per billion |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter, parts per billion, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: methane
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter, parts per billion, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Methane (gas) amount or concentration at the time of sampling
title: methane
examples:
- value: 1800 parts per billion
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- methane
rank: 1000
is_a: core field
slot_uri: MIXS:0000101
multivalued: false
alias: methane
domain_of:
- Biosample
range: QuantityValue

```
</details>