# Slot: amount of light (amount_light)


_The unit of illuminance and luminous emittance, measuring luminous flux per unit area_



URI: [MIXS:0000140](https://w3id.org/mixs/0000140)




## Inheritance

* [core_field](core_field.md)
    * **amount_light**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* amount of light




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | lux, lumens per square meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: amount_light
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: lux, lumens per square meter
  occurrence:
    tag: occurrence
    value: '1'
description: The unit of illuminance and luminous emittance, measuring luminous flux
  per unit area
title: amount of light
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- amount of light
rank: 1000
is_a: core field
slot_uri: MIXS:0000140
multivalued: false
alias: amount_light
domain_of:
- Biosample
range: QuantityValue

```
</details>