# Slot: extreme_unusual_properties/Al saturation (al_sat)


_Aluminum saturation (esp. For tropical soils)_



URI: [MIXS:0000607](https://w3id.org/mixs/0000607)




## Inheritance

* [core_field](core_field.md)
    * **al_sat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* extreme_unusual_properties/Al saturation




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | percentage || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: al_sat
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: percentage
  occurrence:
    tag: occurrence
    value: '1'
description: Aluminum saturation (esp. For tropical soils)
title: extreme_unusual_properties/Al saturation
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- extreme_unusual_properties/Al saturation
rank: 1000
is_a: core field
slot_uri: MIXS:0000607
multivalued: false
alias: al_sat
domain_of:
- Biosample
range: QuantityValue

```
</details>