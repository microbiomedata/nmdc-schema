# Slot: occupant density at sampling (occup_density_samp)


_Average number of occupants at time of sampling per square footage_



URI: [MIXS:0000217](https://w3id.org/mixs/0000217)




## Inheritance

* [core_field](core_field.md)
    * **occup_density_samp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* occupant density at sampling




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
name: occup_density_samp
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  occurrence:
    tag: occurrence
    value: '1'
description: Average number of occupants at time of sampling per square footage
title: occupant density at sampling
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- occupant density at sampling
rank: 1000
is_a: core field
slot_uri: MIXS:0000217
multivalued: false
alias: occup_density_samp
domain_of:
- Biosample
range: QuantityValue

```
</details>