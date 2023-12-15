# Slot: microbial biomass carbon (microbial_biomass_c)


_The part of the organic matter in the soil that constitutes living microorganisms smaller than 5-10 micrometer._



URI: [nmdc:microbial_biomass_c](https://w3id.org/nmdc/microbial_biomass_c)



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
| 0.05 ug C/g dry soil |

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
name: microbial_biomass_c
description: The part of the organic matter in the soil that constitutes living microorganisms
  smaller than 5-10 micrometer.
title: microbial biomass carbon
comments:
- If you provide this, correction factors used for conversion to the final units and
  method are required
examples:
- value: 0.05 ug C/g dry soil
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000650
rank: 10
string_serialization: '{float} {unit}'
alias: microbial_biomass_c
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>