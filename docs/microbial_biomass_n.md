# Slot: microbial biomass nitrogen (microbial_biomass_n)


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer._



URI: [nmdc:microbial_biomass_n](https://w3id.org/nmdc/microbial_biomass_n)



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
| 0.05 ug N/g dry soil |

## Comments

* If you provide this, correction factors used for conversion to the final units and method are required

## See Also

* [MIXS:0000650](https://w3id.org/mixs/0000650)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: microbial_biomass_n
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer.
title: microbial biomass nitrogen
comments:
- If you provide this, correction factors used for conversion to the final units and
  method are required
examples:
- value: 0.05 ug N/g dry soil
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000650
rank: 12
string_serialization: '{float} {unit}'
alias: microbial_biomass_n
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>