# Slot: primary production (primary_prod)


_Measurement of primary production, generally measured as isotope uptake_



URI: [MIXS:0000728](https://w3id.org/mixs/0000728)




## Inheritance

* [core_field](core_field.md)
    * **primary_prod**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* primary production




## Examples

| Value |
| --- |
| 100 milligram per cubic meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per cubic meter per day, gram per square meter per day || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: primary_prod
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per cubic meter per day, gram per square meter per day
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of primary production, generally measured as isotope uptake
title: primary production
examples:
- value: 100 milligram per cubic meter per day
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- primary production
rank: 1000
is_a: core field
slot_uri: MIXS:0000728
multivalued: false
alias: primary_prod
domain_of:
- Biosample
range: QuantityValue

```
</details>