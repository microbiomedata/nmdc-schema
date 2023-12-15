# Slot: DNA sample name (dna_sample_name)


_Give the DNA sample a name that is meaningful to you. Sample names must be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only._



URI: [nmdc:dna_sample_name](https://w3id.org/nmdc/dna_sample_name)



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
| JGI_pond_041618 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: dna_sample_name
description: Give the DNA sample a name that is meaningful to you. Sample names must
  be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only.
title: DNA sample name
examples:
- value: JGI_pond_041618
from_schema: https://w3id.org/nmdc/nmdc
rank: 4
string_serialization: '{text}'
alias: dna_sample_name
domain_of:
- Biosample
slot_group: JGI-Metagenomics
range: string
recommended: true

```
</details>