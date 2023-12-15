# Slot: alternative_names


_A list of alternative names used to refer to the entity. The distinction between name and alternative names is application-specific._



URI: [nmdc:alternative_names](https://w3id.org/nmdc/alternative_names)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Study](Study.md) | A study summarizes the overall goal of a research initiative and outlines the... |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: alternative_names
description: A list of alternative names used to refer to the entity. The distinction
  between name and alternative names is application-specific.
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- dcterms:alternative
- skos:altLabel
rank: 1000
multivalued: true
alias: alternative_names
domain_of:
- Study
range: string

```
</details>