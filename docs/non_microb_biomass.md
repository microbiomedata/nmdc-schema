# Slot: non-microbial biomass (non_microb_biomass)


_Amount of biomass; should include the name for the part of biomass measured, e.g.insect, plant, total. Can include multiple measurements separated by ;_



URI: [nmdc:non_microb_biomass](https://w3id.org/nmdc/non_microb_biomass)



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
| insect 0.23 ug; plant 1g |

## See Also

* [MIXS:0000174](https://w3id.org/mixs/0000174)
* [MIXS:0000650](https://w3id.org/mixs/0000650)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: non_microb_biomass
description: Amount of biomass; should include the name for the part of biomass measured,
  e.g.insect, plant, total. Can include multiple measurements separated by ;
title: non-microbial biomass
examples:
- value: insect 0.23 ug; plant 1g
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIXS:0000174
- MIXS:0000650
rank: 8
string_serialization: '{text};{float} {unit}'
alias: non_microb_biomass
domain_of:
- Biosample
slot_group: MIxS Inspired
range: string

```
</details>