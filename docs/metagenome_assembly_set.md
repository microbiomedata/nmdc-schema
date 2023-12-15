# Slot: metagenome_assembly_set


_This property links a database object to the set of metagenome assembly activities._



URI: [nmdc:metagenome_assembly_set](https://w3id.org/nmdc/metagenome_assembly_set)




## Inheritance

* **metagenome_assembly_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [MetagenomeAssembly](MetagenomeAssembly.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: metagenome_assembly_set
description: This property links a database object to the set of metagenome assembly
  activities.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: metagenome_assembly_set
domain_of:
- Database
range: MetagenomeAssembly
inlined: true
inlined_as_list: true

```
</details>