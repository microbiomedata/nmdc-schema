# Slot: DNA container type (dna_cont_type)


_Tube or plate (96-well)_



URI: [nmdc:dna_cont_type](https://w3id.org/nmdc/dna_cont_type)



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
name: dna_cont_type
description: Tube or plate (96-well)
title: DNA container type
examples:
- value: plate
from_schema: https://w3id.org/nmdc/nmdc
rank: 10
alias: dna_cont_type
domain_of:
- Biosample
slot_group: JGI-Metagenomics
range: JgiContTypeEnum
recommended: true

```
</details>