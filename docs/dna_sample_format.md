# Slot: DNA sample format (dna_sample_format)


_Solution in which the DNA sample has been suspended_



URI: [nmdc:dna_sample_format](https://w3id.org/nmdc/dna_sample_format)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DnaSampleFormatEnum](DnaSampleFormatEnum.md)

* Recommended: True






## Examples

| Value |
| --- |
| Water |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: dna_sample_format
description: Solution in which the DNA sample has been suspended
title: DNA sample format
examples:
- value: Water
from_schema: https://w3id.org/nmdc/nmdc
rank: 12
alias: dna_sample_format
domain_of:
- Biosample
slot_group: JGI-Metagenomics
range: dna_sample_format_enum
recommended: true

```
</details>