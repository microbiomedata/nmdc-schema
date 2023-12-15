# Slot: title


_A name given to the entity that differs from the name/label programmatically assigned to it. For example, when extracting study information for GOLD, the GOLD system has assigned a name/label. However, for display purposes, we may also wish the capture the title of the proposal that was used to fund the study._



URI: [nmdc:title](https://w3id.org/nmdc/title)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: title
description: A name given to the entity that differs from the name/label programmatically
  assigned to it. For example, when extracting study information for GOLD, the GOLD
  system has assigned a name/label. However, for display purposes, we may also wish
  the capture the title of the proposal that was used to fund the study.
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- dcterms:title
rank: 1000
alias: title
domain_of:
- Study
range: string

```
</details>