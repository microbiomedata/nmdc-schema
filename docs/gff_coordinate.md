# Slot: gff_coordinate


_A positive 1-based integer coordinate indicating start or end_



URI: [nmdc:gff_coordinate](https://w3id.org/nmdc/gff_coordinate)




## Inheritance

* **gff_coordinate**
    * [end](end.md)
    * [start](start.md)








## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1





## Comments

* For features that cross the origin of a circular feature (e.g. most bacterial genomes, plasmids, and some viral genomes), the requirement for start to be less than or equal to end is satisfied by making end = the position of the end + the length of the landmark feature.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: gff_coordinate
description: A positive 1-based integer coordinate indicating start or end
comments:
- For features that cross the origin of a circular feature (e.g. most bacterial genomes,
  plasmids, and some viral genomes), the requirement for start to be less than or
  equal to end is satisfied by making end = the position of the end + the length of
  the landmark feature.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
alias: gff_coordinate
range: integer
minimum_value: 1

```
</details>