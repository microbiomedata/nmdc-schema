# Slot: host body temperature (host_body_temp)


_Core body temperature of the host when sample was collected_



URI: [MIXS:0000274](https://w3id.org/mixs/0000274)




## Inheritance

* [core_field](core_field.md)
    * **host_body_temp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host body temperature




## Examples

| Value |
| --- |
| 15 degree Celsius |

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
name: host_body_temp
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
description: Core body temperature of the host when sample was collected
title: host body temperature
examples:
- value: 15 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host body temperature
rank: 1000
is_a: core field
slot_uri: MIXS:0000274
multivalued: false
alias: host_body_temp
domain_of:
- Biosample
range: QuantityValue

```
</details>