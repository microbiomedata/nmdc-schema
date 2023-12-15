# Slot: best_protein


_the specific protein identifier most correctly associated with the peptide sequence_



URI: [nmdc:best_protein](https://w3id.org/nmdc/best_protein)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PeptideQuantification](PeptideQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific peptide... |  no  |
[ProteinQuantification](ProteinQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific protein |  yes  |







## Properties

* Range: [GeneProduct](GeneProduct.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: best_protein
description: the specific protein identifier most correctly associated with the peptide
  sequence
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: best_protein
domain_of:
- PeptideQuantification
- ProteinQuantification
range: GeneProduct

```
</details>