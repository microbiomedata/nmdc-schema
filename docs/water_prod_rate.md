# Slot: water production rate (water_prod_rate)


_Water production rates per well (e.g. 987 m3 / day)_



URI: [MIXS:0000453](https://w3id.org/mixs/0000453)




## Inheritance

* [core_field](core_field.md)
    * **water_prod_rate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* water production rate




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | cubic meter per day || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: water_prod_rate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: cubic meter per day
  occurrence:
    tag: occurrence
    value: '1'
description: Water production rates per well (e.g. 987 m3 / day)
title: water production rate
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- water production rate
rank: 1000
is_a: core field
slot_uri: MIXS:0000453
multivalued: false
alias: water_prod_rate
domain_of:
- Biosample
range: QuantityValue

```
</details>