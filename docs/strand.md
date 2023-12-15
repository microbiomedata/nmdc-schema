# Slot: strand


_The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand)._



URI: [nmdc:strand](https://w3id.org/nmdc/strand)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  no  |







## Properties

* Range: [String](String.md)





## TODOs

* set the range to an enum?

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: strand
description: The strand on which a feature is located. Has a value of '+' (sense strand
  or forward strand) or '-' (anti-sense strand or reverse strand).
todos:
- set the range to an enum?
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:strand
rank: 1000
domain: GenomeFeature
alias: strand
domain_of:
- GenomeFeature
range: string

```
</details>