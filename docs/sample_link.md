# Slot: sample linkage (sample_link)


_A unique identifier to assign parent-child, subsample, or sibling samples. This is relevant when a sample or other material was used to generate the new sample._



URI: [nmdc:sample_link](https://w3id.org/nmdc/sample_link)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Recommended: True






## Examples

| Value |
| --- |
| IGSN:DSJ0284 |

## Comments

* This field allows multiple entries separated by ; (Examples: Soil collected from the field will link with the soil used in an incubation. The soil a plant was grown in links to the plant sample. An original culture sample was transferred to a new vial and generated a new sample)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sample_link
description: A unique identifier to assign parent-child, subsample, or sibling samples.
  This is relevant when a sample or other material was used to generate the new sample.
title: sample linkage
comments:
- 'This field allows multiple entries separated by ; (Examples: Soil collected from
  the field will link with the soil used in an incubation. The soil a plant was grown
  in links to the plant sample. An original culture sample was transferred to a new
  vial and generated a new sample)'
examples:
- value: IGSN:DSJ0284
from_schema: https://w3id.org/nmdc/nmdc
rank: 5
string_serialization: '{text}:{text}'
multivalued: true
alias: sample_link
domain_of:
- Biosample
slot_group: Sample ID
range: string
recommended: true

```
</details>