# Slot: DNA concentration in ng/ul (dna_concentration)

URI: [nmdc:dna_concentration](https://w3id.org/nmdc/dna_concentration)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[ProcessedSample](ProcessedSample.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Recommended: True

* Minimum Value: 0

* Maximum Value: 2000






## Examples

| Value |
| --- |
| 100 |

## Comments

* Units must be in ng/uL. Enter the numerical part only. Must be calculated using a fluorometric method. Acceptable values are 0-2000.

## See Also

* [nmdc:nucleic_acid_concentration](https://w3id.org/nmdc/nucleic_acid_concentration)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: dna_concentration
title: DNA concentration in ng/ul
comments:
- Units must be in ng/uL. Enter the numerical part only. Must be calculated using
  a fluorometric method. Acceptable values are 0-2000.
examples:
- value: '100'
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- nmdc:nucleic_acid_concentration
rank: 5
alias: dna_concentration
domain_of:
- Biosample
- ProcessedSample
slot_group: JGI-Metagenomics
range: float
recommended: true
minimum_value: 0
maximum_value: 2000

```
</details>