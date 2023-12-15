# Slot: RNA volume in ul (rna_volume)

URI: [nmdc:rna_volume](https://w3id.org/nmdc/rna_volume)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [Float](Float.md)

* Recommended: True

* Minimum Value: 0

* Maximum Value: 1000






## Examples

| Value |
| --- |
| 25 |

## Comments

* Units must be in uL. Enter the numerical part only. Value must be 0-1000. This form accepts values < 25, but JGI may refuse to process them unless permission has been granted by a project manager

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_volume
title: RNA volume in ul
comments:
- Units must be in uL. Enter the numerical part only. Value must be 0-1000. This form
  accepts values < 25, but JGI may refuse to process them unless permission has been
  granted by a project manager
examples:
- value: '25'
from_schema: https://w3id.org/nmdc/nmdc
rank: 6
string_serialization: '{float}'
alias: rna_volume
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: float
recommended: true
minimum_value: 0
maximum_value: 1000

```
</details>