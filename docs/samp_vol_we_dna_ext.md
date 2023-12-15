# Slot: sample volume or weight for DNA extraction (samp_vol_we_dna_ext)


_Volume (ml) or mass (g) of total collected sample processed for DNA extraction. Note: total sample collected should be entered under the term Sample Size (MIXS:0000001)._



URI: [MIXS:0000111](https://w3id.org/mixs/0000111)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **samp_vol_we_dna_ext**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* sample volume or weight for DNA extraction




## Examples

| Value |
| --- |
| 1500 milliliter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | millliter, gram, milligram, square centimeter |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_vol_we_dna_ext
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: millliter, gram, milligram, square centimeter
description: 'Volume (ml) or mass (g) of total collected sample processed for DNA
  extraction. Note: total sample collected should be entered under the term Sample
  Size (MIXS:0000001).'
title: sample volume or weight for DNA extraction
examples:
- value: 1500 milliliter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample volume or weight for DNA extraction
rank: 1000
is_a: nucleic acid sequence source field
slot_uri: MIXS:0000111
multivalued: false
alias: samp_vol_we_dna_ext
domain_of:
- Biosample
- OmicsProcessing
range: QuantityValue

```
</details>