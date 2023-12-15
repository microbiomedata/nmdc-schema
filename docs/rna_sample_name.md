# Slot: RNA sample name (rna_sample_name)


_Give the RNA sample a name that is meaningful to you. Sample names must be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only._



URI: [nmdc:rna_sample_name](https://w3id.org/nmdc/rna_sample_name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Minimum Value: 0

* Maximum Value: 2000






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
name: rna_sample_name
description: Give the RNA sample a name that is meaningful to you. Sample names must
  be unique across all JGI projects and contain a-z, A-Z, 0-9, - and _ only.
title: RNA sample name
examples:
- value: JGI_pond_041618
from_schema: https://w3id.org/nmdc/nmdc
rank: 4
string_serialization: '{text}'
alias: rna_sample_name
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true
minimum_value: 0
maximum_value: 2000

```
</details>