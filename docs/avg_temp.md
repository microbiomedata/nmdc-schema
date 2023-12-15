# Slot: average temperature (avg_temp)


_The average of temperatures taken at the beginning of every hour over a 24 hour period on the sampling day_



URI: [MIXS:0000142](https://w3id.org/mixs/0000142)




## Inheritance

* [core_field](core_field.md)
    * **avg_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* average temperature




## Examples

| Value |
| --- |
| 12.5 degree Celsius |

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
name: avg_temp
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
description: The average of temperatures taken at the beginning of every hour over
  a 24 hour period on the sampling day
title: average temperature
examples:
- value: 12.5 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- average temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000142
multivalued: false
alias: avg_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>