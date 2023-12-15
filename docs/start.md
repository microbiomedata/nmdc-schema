# Slot: start


_The start of the feature in positive 1-based integer coordinates_



URI: [nmdc:start](https://w3id.org/nmdc/start)




## Inheritance

* [gff_coordinate](gff_coordinate.md)
    * **start**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  yes  |







## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: start
description: The start of the feature in positive 1-based integer coordinates
from_schema: https://w3id.org/nmdc/nmdc
close_mappings:
- biolink:start_interbase_coordinate
rank: 1000
is_a: gff_coordinate
domain: GenomeFeature
alias: start
domain_of:
- GenomeFeature
range: integer
minimum_value: 1

```
</details>