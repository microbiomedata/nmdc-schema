# Slot: room air exchange rate (room_air_exch_rate)


_The rate at which outside air replaces indoor air in a given space_



URI: [MIXS:0000169](https://w3id.org/mixs/0000169)




## Inheritance

* [core_field](core_field.md)
    * **room_air_exch_rate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* room air exchange rate




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | liter per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: room_air_exch_rate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: liter per hour
  occurrence:
    tag: occurrence
    value: '1'
description: The rate at which outside air replaces indoor air in a given space
title: room air exchange rate
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- room air exchange rate
rank: 1000
is_a: core field
slot_uri: MIXS:0000169
multivalued: false
alias: room_air_exch_rate
domain_of:
- Biosample
range: QuantityValue

```
</details>