# Slot: barometric pressure (barometric_press)


_Force per unit area exerted against a surface by the weight of air above that surface_



URI: [MIXS:0000096](https://w3id.org/mixs/0000096)




## Inheritance

* [core_field](core_field.md)
    * **barometric_press**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* barometric pressure




## Examples

| Value |
| --- |
| 5 millibar |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millibar || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: barometric_press
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millibar
  occurrence:
    tag: occurrence
    value: '1'
description: Force per unit area exerted against a surface by the weight of air above
  that surface
title: barometric pressure
examples:
- value: 5 millibar
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- barometric pressure
rank: 1000
is_a: core field
slot_uri: MIXS:0000096
multivalued: false
alias: barometric_press
domain_of:
- Biosample
range: QuantityValue

```
</details>