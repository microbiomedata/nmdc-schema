# Slot: library_preparation_set


_This property links a database object to the set of DNA extractions within it._



URI: [nmdc:library_preparation_set](https://w3id.org/nmdc/library_preparation_set)




## Inheritance

* **library_preparation_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [LibraryPreparation](LibraryPreparation.md)

* Multivalued: True



## Aliases


* library_construction_set



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: library_preparation_set
description: This property links a database object to the set of DNA extractions within
  it.
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- library_construction_set
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: library_preparation_set
domain_of:
- Database
range: LibraryPreparation
inlined: true
inlined_as_list: true

```
</details>