# Slot: DNase treated (dnase_rna)

URI: [nmdc:dnase_rna](https://w3id.org/nmdc/dnase_rna)



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
name: dnase_rna
title: DNase treated
comments:
- Note DNase treatment is required for all RNA samples.
examples:
- value: 'no'
from_schema: https://w3id.org/nmdc/nmdc
rank: 13
alias: dnase_rna
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: YesNoEnum
recommended: true

```
</details>