# Slot: RNA concentration in ng/ul (rna_concentration)

URI: [nmdc:rna_concentration](https://w3id.org/nmdc/rna_concentration)



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
name: rna_concentration
title: RNA concentration in ng/ul
comments:
- Units must be in ng/uL. Enter the numerical part only. Must be calculated using
  a fluorometric method. Acceptable values are 0-2000.
examples:
- value: '100'
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- nmdc:nucleic_acid_concentration
rank: 5
string_serialization: '{float}'
alias: rna_concentration
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: float
recommended: true
minimum_value: 0
maximum_value: 1000

```
</details>