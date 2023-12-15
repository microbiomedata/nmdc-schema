# Slot: RNA expected organisms (rna_organisms)


_List any organisms known or suspected to grow in co-culture, as well as estimated % of the organism in that culture._



URI: [nmdc:rna_organisms](https://w3id.org/nmdc/rna_organisms)



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
| expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles (1%) |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_organisms
description: List any organisms known or suspected to grow in co-culture, as well
  as estimated % of the organism in that culture.
title: RNA expected organisms
examples:
- value: expected to contain microbes (59%) fungi (30%), viruses (10%), tadpoles (1%)
from_schema: https://w3id.org/nmdc/nmdc
rank: 14
string_serialization: '{text}'
alias: rna_organisms
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true

```
</details>