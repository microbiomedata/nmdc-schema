# Slot: surface humidity (surf_humidity)


_Surfaces: water activity as a function of air and material moisture_



URI: [MIXS:0000123](https://w3id.org/mixs/0000123)




## Inheritance

* [core_field](core_field.md)
    * **surf_humidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* surface humidity




## Examples

| Value |
| --- |
| 10% |

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
name: surf_humidity
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
description: 'Surfaces: water activity as a function of air and material moisture'
title: surface humidity
examples:
- value: 10%
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- surface humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000123
multivalued: false
alias: surf_humidity
domain_of:
- Biosample
range: QuantityValue

```
</details>