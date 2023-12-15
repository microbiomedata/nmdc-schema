# Slot: humidity (humidity)


_Amount of water vapour in the air, at the time of sampling_



URI: [MIXS:0000100](https://w3id.org/mixs/0000100)




## Inheritance

* [core_field](core_field.md)
    * **humidity**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* humidity




## Examples

| Value |
| --- |
| 25 gram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | gram per cubic meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: humidity
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: gram per cubic meter
  occurrence:
    tag: occurrence
    value: '1'
description: Amount of water vapour in the air, at the time of sampling
title: humidity
examples:
- value: 25 gram per cubic meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- humidity
rank: 1000
is_a: core field
slot_uri: MIXS:0000100
multivalued: false
alias: humidity
domain_of:
- Biosample
range: QuantityValue

```
</details>