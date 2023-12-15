# Slot: outside relative humidity (rel_humidity_out)


_The recorded outside relative humidity value at the time of sampling_



URI: [MIXS:0000188](https://w3id.org/mixs/0000188)




## Inheritance

* [core_field](core_field.md)
    * **rel_humidity_out**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* outside relative humidity




## Examples

| Value |
| --- |
| 12 per kilogram of air |

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
name: rel_humidity_out
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
description: The recorded outside relative humidity value at the time of sampling
title: outside relative humidity
examples:
- value: 12 per kilogram of air
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- outside relative humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000188
multivalued: false
alias: rel_humidity_out
domain_of:
- Biosample
range: QuantityValue

```
</details>