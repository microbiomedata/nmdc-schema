# Slot: amount or size of sample collected (samp_size)


_The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected._



URI: [MIXS:0000001](https://w3id.org/mixs/0000001)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **samp_size**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* amount or size of sample collected




## Examples

| Value |
| --- |
| 5 liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millliter, gram, milligram, liter |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_size
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millliter, gram, milligram, liter
description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample
  collected.
title: amount or size of sample collected
examples:
- value: 5 liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- amount or size of sample collected
rank: 1000
is_a: nucleic acid sequence source field
slot_uri: MIXS:0000001
multivalued: false
alias: samp_size
domain_of:
- Biosample
range: QuantityValue

```
</details>