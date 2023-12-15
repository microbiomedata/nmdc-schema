# Slot: mean seasonal precipitation (season_precpt)


_The average of all seasonal precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps._



URI: [MIXS:0000645](https://w3id.org/mixs/0000645)




## Inheritance

* [core_field](core_field.md)
    * **season_precpt**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* mean seasonal precipitation




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millimeter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: season_precpt
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millimeter
  occurrence:
    tag: occurrence
    value: '1'
description: The average of all seasonal precipitation values known, or an estimated
  equivalent value derived by such methods as regional indexes or Isohyetal maps.
title: mean seasonal precipitation
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mean seasonal precipitation
rank: 1000
is_a: core field
slot_uri: MIXS:0000645
multivalued: false
alias: season_precpt
domain_of:
- Biosample
range: QuantityValue

```
</details>