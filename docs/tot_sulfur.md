# Slot: total sulfur (tot_sulfur)


_Concentration of total sulfur in the sample_



URI: [MIXS:0000419](https://w3id.org/mixs/0000419)




## Inheritance

* [core_field](core_field.md)
    * **tot_sulfur**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total sulfur




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_sulfur
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of total sulfur in the sample
title: total sulfur
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total sulfur
rank: 1000
is_a: core field
slot_uri: MIXS:0000419
multivalued: false
alias: tot_sulfur
domain_of:
- Biosample
range: QuantityValue

```
</details>