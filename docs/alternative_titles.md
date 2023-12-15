# Slot: alternative_titles


_A list of alternative titles for the entity. The distinction between title and alternative titles is application-specific._



URI: [nmdc:alternative_titles](https://w3id.org/nmdc/alternative_titles)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alternative_titles
description: A list of alternative titles for the entity. The distinction between
  title and alternative titles is application-specific.
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- dcterms:alternative
rank: 1000
multivalued: true
alias: alternative_titles
domain_of:
- Study
range: string

```
</details>