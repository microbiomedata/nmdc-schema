# Slot: total phosphate (tot_phosphate)


_Total amount or concentration of phosphate_



URI: [MIXS:0000689](https://w3id.org/mixs/0000689)




## Inheritance

* [core_field](core_field.md)
    * **tot_phosphate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total phosphate




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_phosphate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Total amount or concentration of phosphate
title: total phosphate
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total phosphate
rank: 1000
is_a: core field
slot_uri: MIXS:0000689
multivalued: false
alias: tot_phosphate
domain_of:
- Biosample
range: QuantityValue

```
</details>