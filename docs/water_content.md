# Slot: water content (water_content)


_Water content measurement_



URI: [MIXS:0000185](https://w3id.org/mixs/0000185)




## Inheritance

* [core_field](core_field.md)
    * **water_content**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* water content




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram per gram or cubic centimeter per cubic centimeter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_content
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per gram or cubic centimeter per cubic centimeter
  occurrence:
    tag: occurrence
    value: '1'
description: Water content measurement
title: water content
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water content
rank: 1000
is_a: core field
slot_uri: MIXS:0000185
multivalued: false
alias: water_content
domain_of:
- Biosample
range: QuantityValue

```
</details>