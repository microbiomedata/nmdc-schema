# Slot: RNA absorbance 260/280 (rna_absorb1)


_260/280 measurement of RNA sample purity_



URI: [nmdc:rna_absorb1](https://w3id.org/nmdc/rna_absorb1)




## Inheritance

* [biomaterial_purity](biomaterial_purity.md)
    * **rna_absorb1**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Float](Float.md)

* Recommended: True






## Examples

| Value |
| --- |
| 2.02 |

## Comments

* Recommended value is between 1 and 3.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_absorb1
description: 260/280 measurement of RNA sample purity
title: RNA absorbance 260/280
comments:
- Recommended value is between 1 and 3.
examples:
- value: '2.02'
from_schema: https://w3id.org/nmdc/nmdc
rank: 7
is_a: biomaterial_purity
string_serialization: '{float}'
domain: ProcessedSample
alias: rna_absorb1
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: float
recommended: true

```
</details>