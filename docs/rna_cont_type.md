# Slot: RNA container type (rna_cont_type)


_Tube or plate (96-well)_



URI: [nmdc:rna_cont_type](https://w3id.org/nmdc/rna_cont_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [JgiContTypeEnum](JgiContTypeEnum.md)

* Recommended: True






## Examples

| Value |
| --- |
| plate |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_cont_type
description: Tube or plate (96-well)
title: RNA container type
examples:
- value: plate
from_schema: https://w3id.org/nmdc/nmdc
rank: 10
alias: rna_cont_type
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: JgiContTypeEnum
recommended: true

```
</details>