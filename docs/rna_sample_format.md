# Slot: RNA sample format (rna_sample_format)


_Solution in which the RNA sample has been suspended_



URI: [nmdc:rna_sample_format](https://w3id.org/nmdc/rna_sample_format)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [RnaSampleFormatEnum](RnaSampleFormatEnum.md)

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
name: rna_sample_format
description: Solution in which the RNA sample has been suspended
title: RNA sample format
examples:
- value: Water
from_schema: https://w3id.org/nmdc/nmdc
rank: 12
alias: rna_sample_format
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: rna_sample_format_enum
recommended: true

```
</details>