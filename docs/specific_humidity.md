# Slot: specific humidity (specific_humidity)


_The mass of water vapour in a unit mass of moist air, usually expressed as grams of vapour per kilogram of air, or, in air conditioning, as grains per pound._



URI: [MIXS:0000214](https://w3id.org/mixs/0000214)




## Inheritance

* [core_field](core_field.md)
    * **specific_humidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* specific humidity




## Examples

| Value |
| --- |
| 15 per kilogram of air |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram of air, kilogram of air || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: specific_humidity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram of air, kilogram of air
  occurrence:
    tag: occurrence
    value: '1'
description: The mass of water vapour in a unit mass of moist air, usually expressed
  as grams of vapour per kilogram of air, or, in air conditioning, as grains per pound.
title: specific humidity
examples:
- value: 15 per kilogram of air
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- specific humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000214
multivalued: false
alias: specific_humidity
domain_of:
- Biosample
range: QuantityValue

```
</details>