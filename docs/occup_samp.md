# Slot: occupancy at sampling (occup_samp)


_Number of occupants present at time of sample within the given space_



URI: [MIXS:0000772](https://w3id.org/mixs/0000772)




## Inheritance

* [core_field](core_field.md)
    * **occup_samp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* occupancy at sampling




## Examples

| Value |
| --- |
| 10 |

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
name: occup_samp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Number of occupants present at time of sample within the given space
title: occupancy at sampling
examples:
- value: '10'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- occupancy at sampling
rank: 1000
is_a: core field
slot_uri: MIXS:0000772
multivalued: false
alias: occup_samp
domain_of:
- Biosample
range: QuantityValue

```
</details>