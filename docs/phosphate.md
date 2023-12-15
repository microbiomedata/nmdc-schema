# Slot: phosphate (phosphate)


_Concentration of phosphate_



URI: [MIXS:0000505](https://w3id.org/mixs/0000505)




## Inheritance

* [core_field](core_field.md)
    * **phosphate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* phosphate




## Examples

| Value |
| --- |
| 0.7 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: phosphate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of phosphate
title: phosphate
examples:
- value: 0.7 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- phosphate
rank: 1000
is_a: core field
slot_uri: MIXS:0000505
multivalued: false
alias: phosphate
domain_of:
- Biosample
range: QuantityValue

```
</details>