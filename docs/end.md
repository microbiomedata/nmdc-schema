# Slot: end


_The end of the feature in positive 1-based integer coordinates_



URI: [nmdc:end](https://w3id.org/nmdc/end)




## Inheritance

* [gff_coordinate](gff_coordinate.md)
    * **end**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeFeature](GenomeFeature.md) | A feature localized to an interval along a genome |  yes  |







## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1





## Comments

* - "constraint: end > start" - "For features that cross the origin of a circular feature,  end = the position of the end + the length of the landmark feature."

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: end
description: The end of the feature in positive 1-based integer coordinates
comments:
- '- "constraint: end > start" - "For features that cross the origin of a circular
  feature,  end = the position of the end + the length of the landmark feature."'
from_schema: https://w3id.org/nmdc/nmdc
close_mappings:
- biolink:end_interbase_coordinate
rank: 1000
is_a: gff_coordinate
domain: GenomeFeature
alias: end
domain_of:
- GenomeFeature
range: integer
minimum_value: 1

```
</details>