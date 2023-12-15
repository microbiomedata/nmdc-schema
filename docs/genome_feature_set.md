# Slot: genome_feature_set


_This property links a database object to the set of all features_



URI: [nmdc:genome_feature_set](https://w3id.org/nmdc/genome_feature_set)




## Inheritance

* **genome_feature_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [GenomeFeature](GenomeFeature.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: genome_feature_set
description: This property links a database object to the set of all features
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: genome_feature_set
domain_of:
- Database
range: GenomeFeature
inlined: true
inlined_as_list: true

```
</details>