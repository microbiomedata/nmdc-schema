# Slot: microbial biomass carbon method (micro_biomass_c_meth)


_Reference or method used in determining microbial biomass carbon_



URI: [nmdc:micro_biomass_c_meth](https://w3id.org/nmdc/micro_biomass_c_meth)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| https://doi.org/10.1016/0038-0717(87)90052-6 |
| https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526 |

## Comments

* required if "microbial_biomass_c" is provided

## TODOs

* How should we separate values? | or ;? lets be consistent

## See Also

* [MIXS:0000339](https://w3id.org/mixs/0000339)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: micro_biomass_c_meth
description: Reference or method used in determining microbial biomass carbon
title: microbial biomass carbon method
todos:
- How should we separate values? | or ;? lets be consistent
comments:
- required if "microbial_biomass_c" is provided
examples:
- value: https://doi.org/10.1016/0038-0717(87)90052-6
- value: https://doi.org/10.1016/0038-0717(87)90052-6 | https://www.sciencedirect.com/science/article/abs/pii/0038071787900526
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000339
rank: 11
string_serialization: '{PMID}|{DOI}|{URL}'
alias: micro_biomass_c_meth
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string
recommended: true

```
</details>