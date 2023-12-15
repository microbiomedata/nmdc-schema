# Slot: biosample_set


_This property links a database object to the set of samples within it._



URI: [nmdc:biosample_set](https://w3id.org/nmdc/biosample_set)




## Inheritance

* **biosample_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [Biosample](Biosample.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biosample_set
description: This property links a database object to the set of samples within it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: biosample_set
domain_of:
- Database
range: Biosample
inlined: true
inlined_as_list: true

```
</details>