# Slot: DNase treatment DNA (dna_dnase)

URI: [nmdc:dna_dnase](https://w3id.org/nmdc/dna_dnase)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [YesNoEnum](YesNoEnum.md)

* Recommended: True






## Examples

| Value |
| --- |
| no |

## Comments

* Note DNase treatment is required for all RNA samples.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: dna_dnase
title: DNase treatment DNA
comments:
- Note DNase treatment is required for all RNA samples.
examples:
- value: 'no'
from_schema: https://w3id.org/nmdc/nmdc
rank: 13
alias: dna_dnase
domain_of:
- Biosample
slot_group: JGI-Metagenomics
range: YesNoEnum
recommended: true

```
</details>