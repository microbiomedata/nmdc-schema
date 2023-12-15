# Slot: non-microbial biomass method (non_microb_biomass_method)


_Reference or method used in determining biomass_



URI: [nmdc:non_microb_biomass_method](https://w3id.org/nmdc/non_microb_biomass_method)



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
| https://doi.org/10.1038/s41467-021-26181-3 |

## Comments

* required if "non-microbial biomass" is provided

## See Also

* [MIXS:0000650](https://w3id.org/mixs/0000650)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: non_microb_biomass_method
description: Reference or method used in determining biomass
title: non-microbial biomass method
comments:
- required if "non-microbial biomass" is provided
examples:
- value: https://doi.org/10.1038/s41467-021-26181-3
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000650
rank: 9
string_serialization: '{PMID}|{DOI}|{URL}'
alias: non_microb_biomass_method
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>