# Slot: host length (host_length)


_The length of subject_



URI: [MIXS:0000256](https://w3id.org/mixs/0000256)




## Inheritance

* [core_field](core_field.md)
    * **host_length**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host length




## Examples

| Value |
| --- |
| 1 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | centimeter, millimeter, meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_length
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: centimeter, millimeter, meter
  occurrence:
    tag: occurrence
    value: '1'
description: The length of subject
title: host length
examples:
- value: 1 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host length
rank: 1000
is_a: core field
slot_uri: MIXS:0000256
multivalued: false
alias: host_length
domain_of:
- Biosample
range: QuantityValue

```
</details>