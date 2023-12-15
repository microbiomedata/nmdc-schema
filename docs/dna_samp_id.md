# Slot: DNA sample ID (dna_samp_id)

URI: [nmdc:dna_samp_id](https://w3id.org/nmdc/dna_samp_id)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 187654 |

## Comments

* Do not edit these values. A template will be provided by NMDC in which these values have been pre-filled.

## TODOs

* Removed identifier = TRUE from dna_samp_ID in JGI_sample_slots, as a class can't have two identifiers. How to force uniqueness? Moot because that column will be prefilled?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: dna_samp_id
title: DNA sample ID
todos:
- Removed identifier = TRUE from dna_samp_ID in JGI_sample_slots, as a class can't
  have two identifiers. How to force uniqueness? Moot because that column will be
  prefilled?
comments:
- Do not edit these values. A template will be provided by NMDC in which these values
  have been pre-filled.
examples:
- value: '187654'
from_schema: https://w3id.org/nmdc/nmdc
rank: 3
string_serialization: '{text}'
alias: dna_samp_id
domain_of:
- Biosample
slot_group: JGI-Metagenomics
range: string
recommended: true

```
</details>