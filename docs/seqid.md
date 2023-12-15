# Slot: seqid


_The ID of the landmark used to establish the coordinate system for the current feature._



URI: [nmdc:seqid](https://w3id.org/nmdc/seqid)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  yes  |







## Properties

* Range: [String](String.md)





## TODOs

* change range from string to object

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: seqid
description: The ID of the landmark used to establish the coordinate system for the
  current feature.
todos:
- change range from string to object
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: seqid
domain_of:
- GenomeFeature
range: string

```
</details>