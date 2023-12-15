# Slot: RNA collection site (rna_collect_site)


_Provide information on the site your RNA sample was collected from_



URI: [nmdc:rna_collect_site](https://w3id.org/nmdc/rna_collect_site)



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
| untreated pond water |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_collect_site
description: Provide information on the site your RNA sample was collected from
title: RNA collection site
examples:
- value: untreated pond water
from_schema: https://w3id.org/nmdc/nmdc
rank: 15
string_serialization: '{text}'
alias: rna_collect_site
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true

```
</details>