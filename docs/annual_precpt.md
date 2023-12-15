# Slot: mean annual precipitation (annual_precpt)


_The average of all annual precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps._



URI: [MIXS:0000644](https://w3id.org/mixs/0000644)




## Inheritance

* [core_field](core_field.md)
    * **annual_precpt**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* mean annual precipitation




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
name: annual_precpt
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
description: The average of all annual precipitation values known, or an estimated
  equivalent value derived by such methods as regional indexes or Isohyetal maps.
title: mean annual precipitation
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- mean annual precipitation
rank: 1000
is_a: core field
slot_uri: MIXS:0000644
multivalued: false
alias: annual_precpt
domain_of:
- Biosample
range: QuantityValue

```
</details>