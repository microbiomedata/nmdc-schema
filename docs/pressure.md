# Slot: pressure (pressure)


_Pressure to which the sample is subject to, in atmospheres_



URI: [MIXS:0000412](https://w3id.org/mixs/0000412)




## Inheritance

* [core_field](core_field.md)
    * **pressure**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* pressure




## Examples

| Value |
| --- |
| 50 atmosphere |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | atmosphere || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pressure
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: atmosphere
  occurrence:
    tag: occurrence
    value: '1'
description: Pressure to which the sample is subject to, in atmospheres
title: pressure
examples:
- value: 50 atmosphere
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pressure
rank: 1000
is_a: core field
slot_uri: MIXS:0000412
multivalued: false
alias: pressure
domain_of:
- Biosample
range: QuantityValue

```
</details>