# Slot: ceiling thermal mass (ceil_thermal_mass)


_The ability of the ceiling to provide inertia against temperature fluctuations. Generally this means concrete that is exposed. A metal deck that supports a concrete slab will act thermally as long as it is exposed to room air flow_



URI: [MIXS:0000143](https://w3id.org/mixs/0000143)




## Inheritance

* [core_field](core_field.md)
    * **ceil_thermal_mass**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* ceiling thermal mass




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
name: ceil_thermal_mass
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
description: The ability of the ceiling to provide inertia against temperature fluctuations.
  Generally this means concrete that is exposed. A metal deck that supports a concrete
  slab will act thermally as long as it is exposed to room air flow
title: ceiling thermal mass
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- ceiling thermal mass
rank: 1000
is_a: core field
slot_uri: MIXS:0000143
multivalued: false
alias: ceil_thermal_mass
domain_of:
- Biosample
range: QuantityValue

```
</details>