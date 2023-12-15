# Slot: number of pets (number_pets)


_The number of pets residing in the sampled space_



URI: [MIXS:0000231](https://w3id.org/mixs/0000231)




## Inheritance

* [core_field](core_field.md)
    * **number_pets**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* number of pets




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
name: number_pets
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of pets residing in the sampled space
title: number of pets
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- number of pets
rank: 1000
is_a: core field
slot_uri: MIXS:0000231
multivalued: false
alias: number_pets
domain_of:
- Biosample
range: QuantityValue

```
</details>