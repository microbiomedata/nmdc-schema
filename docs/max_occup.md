# Slot: maximum occupancy (max_occup)


_The maximum amount of people allowed in the indoor environment_



URI: [MIXS:0000229](https://w3id.org/mixs/0000229)




## Inheritance

* [core_field](core_field.md)
    * **max_occup**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* maximum occupancy




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: max_occup
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The maximum amount of people allowed in the indoor environment
title: maximum occupancy
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- maximum occupancy
rank: 1000
is_a: core field
slot_uri: MIXS:0000229
multivalued: false
alias: max_occup
domain_of:
- Biosample
range: QuantityValue

```
</details>