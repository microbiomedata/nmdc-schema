# Slot: slope gradient (slope_gradient)


_Commonly called 'slope'. The angle between ground surface and a horizontal line (in percent). This is the direction that overland water would flow. This measure is usually taken with a hand level meter or clinometer_



URI: [MIXS:0000646](https://w3id.org/mixs/0000646)




## Inheritance

* [core_field](core_field.md)
    * **slope_gradient**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* slope gradient




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
name: slope_gradient
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
description: Commonly called 'slope'. The angle between ground surface and a horizontal
  line (in percent). This is the direction that overland water would flow. This measure
  is usually taken with a hand level meter or clinometer
title: slope gradient
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- slope gradient
rank: 1000
is_a: core field
slot_uri: MIXS:0000646
multivalued: false
alias: slope_gradient
domain_of:
- Biosample
range: QuantityValue

```
</details>