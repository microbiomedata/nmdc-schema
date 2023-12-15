# Slot: frequency of cooking (freq_cook)


_The number of times a meal is cooked per week_



URI: [MIXS:0000227](https://w3id.org/mixs/0000227)




## Inheritance

* [core_field](core_field.md)
    * **freq_cook**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* frequency of cooking




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
name: freq_cook
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of times a meal is cooked per week
title: frequency of cooking
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- frequency of cooking
rank: 1000
is_a: core field
slot_uri: MIXS:0000227
multivalued: false
alias: freq_cook
domain_of:
- Biosample
range: QuantityValue

```
</details>