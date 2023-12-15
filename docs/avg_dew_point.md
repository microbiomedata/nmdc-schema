# Slot: average dew point (avg_dew_point)


_The average of dew point measures taken at the beginning of every hour over a 24 hour period on the sampling day_



URI: [MIXS:0000141](https://w3id.org/mixs/0000141)




## Inheritance

* [core_field](core_field.md)
    * **avg_dew_point**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* average dew point




## Examples

| Value |
| --- |
| 25.5 degree Celsius |

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
name: avg_dew_point
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
description: The average of dew point measures taken at the beginning of every hour
  over a 24 hour period on the sampling day
title: average dew point
examples:
- value: 25.5 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- average dew point
rank: 1000
is_a: core field
slot_uri: MIXS:0000141
multivalued: false
alias: avg_dew_point
domain_of:
- Biosample
range: QuantityValue

```
</details>