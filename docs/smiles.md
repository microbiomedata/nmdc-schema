# Slot: smiles


_A string encoding of a molecular graph, no chiral or isotopic information. There are usually a large number of valid SMILES which represent a given structure. For example, CCO, OCC and C(O)C all specify the structure of ethanol._



URI: [nmdc:smiles](https://w3id.org/nmdc/smiles)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ChemicalEntity](ChemicalEntity.md) | An atom or molecule that can be represented with a chemical formula |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: smiles
description: A string encoding of a molecular graph, no chiral or isotopic information.
  There are usually a large number of valid SMILES which represent a given structure.
  For example, CCO, OCC and C(O)C all specify the structure of ethanol.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
multivalued: true
alias: smiles
domain_of:
- ChemicalEntity
range: string

```
</details>