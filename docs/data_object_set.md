# Slot: data_object_set


_This property links a database object to the set of data objects within it._



URI: [nmdc:data_object_set](https://w3id.org/nmdc/data_object_set)




## Inheritance

* **data_object_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [DataObject](DataObject.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: data_object_set
description: This property links a database object to the set of data objects within
  it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: data_object_set
domain_of:
- Database
range: DataObject
inlined: true
inlined_as_list: true

```
</details>