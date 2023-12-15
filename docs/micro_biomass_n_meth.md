# Slot: microbial biomass nitrogen method (micro_biomass_n_meth)


_Reference or method used in determining microbial biomass nitrogen_



URI: [nmdc:micro_biomass_n_meth](https://w3id.org/nmdc/micro_biomass_n_meth)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://doi.org/10.1016/0038-0717(87)90052-6 |
| https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526 |

## Comments

* required if "microbial_biomass_n" is provided

## See Also

* [MIXS:0000339](https://w3id.org/mixs/0000339)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: micro_biomass_n_meth
description: Reference or method used in determining microbial biomass nitrogen
title: microbial biomass nitrogen method
comments:
- required if "microbial_biomass_n" is provided
examples:
- value: https://doi.org/10.1016/0038-0717(87)90052-6
- value: https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000339
rank: 13
string_serialization: '{PMID}|{DOI}|{URL}'
alias: micro_biomass_n_meth
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>