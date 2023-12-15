# Slot: all_proteins


_the list of protein identifiers that are associated with the peptide sequence_



URI: [nmdc:all_proteins](https://w3id.org/nmdc/all_proteins)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PeptideQuantification](PeptideQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific peptide... |  no  |
[ProteinQuantification](ProteinQuantification.md) | This is used to link a metaproteomics analysis workflow to a specific protein |  yes  |







## Properties

* Range: [GeneProduct](GeneProduct.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: all_proteins
description: the list of protein identifiers that are associated with the peptide
  sequence
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
multivalued: true
alias: all_proteins
domain_of:
- PeptideQuantification
- ProteinQuantification
range: GeneProduct

```
</details>