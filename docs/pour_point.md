# Slot: pour point (pour_point)


_Temperature at which a liquid becomes semi solid and loses its flow characteristics. In crude oil a high¬†pour point¬†is generally associated with a high paraffin content, typically found in crude deriving from a larger proportion of plant material. (soure: https://en.wikipedia.org/wiki/pour_point)_



URI: [MIXS:0000127](https://w3id.org/mixs/0000127)




## Inheritance

* [core_field](core_field.md)
    * **pour_point**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* pour point




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | degree Celsius || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pour_point
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: degree Celsius
  occurrence:
    tag: occurrence
    value: '1'
description: 'Temperature at which a liquid becomes semi solid and loses its flow
  characteristics. In crude oil a high¬†pour point¬†is generally associated with a
  high paraffin content, typically found in crude deriving from a larger proportion
  of plant material. (soure: https://en.wikipedia.org/wiki/pour_point)'
title: pour point
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pour point
rank: 1000
is_a: core field
slot_uri: MIXS:0000127
multivalued: false
alias: pour_point
domain_of:
- Biosample
range: QuantityValue

```
</details>