# Slot: temperature (temp)


_Temperature of the sample at the time of sampling._



URI: [MIXS:0000113](https://w3id.org/mixs/0000113)




## Inheritance

* [environment_field](environment_field.md)
    * **temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* temperature




## Examples

| Value |
| --- |
| 25 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | degree Celsius |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: temp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: degree Celsius
description: Temperature of the sample at the time of sampling.
title: temperature
examples:
- value: 25 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- temperature
rank: 1000
is_a: environment field
slot_uri: MIXS:0000113
multivalued: false
alias: temp
domain_of:
- Biosample
range: QuantityValue

```
</details>