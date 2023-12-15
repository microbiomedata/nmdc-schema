# Slot: silicate (silicate)


_Concentration of silicate_



URI: [MIXS:0000184](https://w3id.org/mixs/0000184)




## Inheritance

* [core_field](core_field.md)
    * **silicate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* silicate




## Examples

| Value |
| --- |
| 0.05 micromole per liter |

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
name: silicate
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
description: Concentration of silicate
title: silicate
examples:
- value: 0.05 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- silicate
rank: 1000
is_a: core field
slot_uri: MIXS:0000184
multivalued: false
alias: silicate
domain_of:
- Biosample
range: QuantityValue

```
</details>