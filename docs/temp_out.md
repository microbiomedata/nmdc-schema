# Slot: temperature outside house (temp_out)


_The recorded temperature value at sampling time outside_



URI: [MIXS:0000197](https://w3id.org/mixs/0000197)




## Inheritance

* [core_field](core_field.md)
    * **temp_out**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* temperature outside house




## Examples

| Value |
| --- |
| 5 degree Celsius |

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
name: temp_out
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
description: The recorded temperature value at sampling time outside
title: temperature outside house
examples:
- value: 5 degree Celsius
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- temperature outside house
rank: 1000
is_a: core field
slot_uri: MIXS:0000197
multivalued: false
alias: temp_out
domain_of:
- Biosample
range: QuantityValue

```
</details>