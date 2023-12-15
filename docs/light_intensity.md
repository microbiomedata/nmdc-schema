# Slot: light intensity (light_intensity)


_Measurement of light intensity_



URI: [MIXS:0000706](https://w3id.org/mixs/0000706)




## Inheritance

* [core_field](core_field.md)
    * **light_intensity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* light intensity




## Examples

| Value |
| --- |
| 0.3 lux |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | lux || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: light_intensity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: lux
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of light intensity
title: light intensity
examples:
- value: 0.3 lux
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- light intensity
rank: 1000
is_a: core field
slot_uri: MIXS:0000706
multivalued: false
alias: light_intensity
domain_of:
- Biosample
range: QuantityValue

```
</details>