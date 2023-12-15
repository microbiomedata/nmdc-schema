# Slot: wall thermal mass (wall_thermal_mass)


_The ability of the wall to provide inertia against temperature fluctuations. Generally this means concrete or concrete block that is either exposed or covered only with paint_



URI: [MIXS:0000222](https://w3id.org/mixs/0000222)




## Inheritance

* [core_field](core_field.md)
    * **wall_thermal_mass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* wall thermal mass




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | joule per degree Celsius || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: wall_thermal_mass
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: joule per degree Celsius
  occurrence:
    tag: occurrence
    value: '1'
description: The ability of the wall to provide inertia against temperature fluctuations.
  Generally this means concrete or concrete block that is either exposed or covered
  only with paint
title: wall thermal mass
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- wall thermal mass
rank: 1000
is_a: core field
slot_uri: MIXS:0000222
multivalued: false
alias: wall_thermal_mass
domain_of:
- Biosample
range: QuantityValue

```
</details>