# Slot: number of houseplants (number_plants)


_The number of plant(s) in the sampling space_



URI: [MIXS:0000230](https://w3id.org/mixs/0000230)




## Inheritance

* [core_field](core_field.md)
    * **number_plants**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* number of houseplants




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
name: number_plants
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of plant(s) in the sampling space
title: number of houseplants
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- number of houseplants
rank: 1000
is_a: core field
slot_uri: MIXS:0000230
multivalued: false
alias: number_plants
domain_of:
- Biosample
range: QuantityValue

```
</details>