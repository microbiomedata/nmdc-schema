# Slot: dew point (dew_point)


_The temperature to which a given parcel of humid air must be cooled, at constant barometric pressure, for water vapor to condense into water._



URI: [MIXS:0000129](https://w3id.org/mixs/0000129)




## Inheritance

* [core_field](core_field.md)
    * **dew_point**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dew point




## Examples

| Value |
| --- |
| 22 degree Celsius |

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
name: dew_point
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
description: The temperature to which a given parcel of humid air must be cooled,
  at constant barometric pressure, for water vapor to condense into water.
title: dew point
examples:
- value: 22 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dew point
rank: 1000
is_a: core field
slot_uri: MIXS:0000129
multivalued: false
alias: dew_point
domain_of:
- Biosample
range: QuantityValue

```
</details>