# Slot: phase


_The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2._



URI: [nmdc:phase](https://w3id.org/nmdc/phase)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  no  |







## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 0

* Maximum Value: 2





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: phase
description: The phase for a coding sequence entity. For example, phase of a CDS as
  represented in a GFF3 with a value of 0, 1 or 2.
from_schema: https://w3id.org/nmdc/nmdc
exact_mappings:
- biolink:phase
rank: 1000
domain: GenomeFeature
alias: phase
domain_of:
- GenomeFeature
range: integer
minimum_value: 0
maximum_value: 2

```
</details>