# Slot: host height (host_height)


_The height of subject_



URI: [MIXS:0000264](https://w3id.org/mixs/0000264)




## Inheritance

* [core_field](core_field.md)
    * **host_height**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* host height




## Examples

| Value |
| --- |
| 0.1 meter |

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
name: host_height
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
description: The height of subject
title: host height
examples:
- value: 0.1 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host height
rank: 1000
is_a: core field
slot_uri: MIXS:0000264
multivalued: false
alias: host_height
domain_of:
- Biosample
range: QuantityValue

```
</details>