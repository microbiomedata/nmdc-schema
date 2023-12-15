# Slot: solar irradiance (solar_irradiance)


_The amount of solar energy that arrives at a specific area of a surface during a specific time interval_



URI: [MIXS:0000112](https://w3id.org/mixs/0000112)




## Inheritance

* [core_field](core_field.md)
    * **solar_irradiance**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* solar irradiance




## Examples

| Value |
| --- |
| 1.36 kilowatts per square meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | kilowatts per square meter per day, ergs per square centimeter per second || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: solar_irradiance
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: kilowatts per square meter per day, ergs per square centimeter per second
  occurrence:
    tag: occurrence
    value: '1'
description: The amount of solar energy that arrives at a specific area of a surface
  during a specific time interval
title: solar irradiance
examples:
- value: 1.36 kilowatts per square meter per day
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- solar irradiance
rank: 1000
is_a: core field
slot_uri: MIXS:0000112
multivalued: false
alias: solar_irradiance
domain_of:
- Biosample
range: QuantityValue

```
</details>