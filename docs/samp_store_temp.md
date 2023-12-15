# Slot: sample storage temperature (samp_store_temp)


_Temperature at which sample was stored, e.g. -80 degree Celsius_



URI: [MIXS:0000110](https://w3id.org/mixs/0000110)




## Inheritance

* [core_field](core_field.md)
    * **samp_store_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sample storage temperature




## Examples

| Value |
| --- |
| -80 degree Celsius |

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
name: samp_store_temp
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
description: Temperature at which sample was stored, e.g. -80 degree Celsius
title: sample storage temperature
examples:
- value: -80 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample storage temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000110
multivalued: false
alias: samp_store_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>