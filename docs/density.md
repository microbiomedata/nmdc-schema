# Slot: density (density)


_Density of the sample, which is its mass per unit volume (aka volumetric mass density)_



URI: [MIXS:0000435](https://w3id.org/mixs/0000435)




## Inheritance

* [core_field](core_field.md)
    * **density**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* density




## Examples

| Value |
| --- |
| 1000 kilogram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram per cubic meter, gram per cubic centimeter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: density
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per cubic meter, gram per cubic centimeter
  occurrence:
    tag: occurrence
    value: '1'
description: Density of the sample, which is its mass per unit volume (aka volumetric
  mass density)
title: density
examples:
- value: 1000 kilogram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- density
rank: 1000
is_a: core field
slot_uri: MIXS:0000435
multivalued: false
alias: density
domain_of:
- Biosample
range: QuantityValue

```
</details>