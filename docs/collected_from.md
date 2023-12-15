# Slot: collected_from


_The Site from which a Biosample was collected_



URI: [nmdc:collected_from](https://w3id.org/nmdc/collected_from)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [FieldResearchSite](FieldResearchSite.md)





## Comments

* this illustrates implementing a Biosample relation with a (binary) slot

## TODOs

* add an OBO slot_uri ?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: collected_from
description: The Site from which a Biosample was collected
todos:
- add an OBO slot_uri ?
comments:
- this illustrates implementing a Biosample relation with a (binary) slot
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: Biosample
alias: collected_from
domain_of:
- Biosample
range: FieldResearchSite

```
</details>