# Slot: study_set


_This property links a database object to the set of studies within it._



URI: [nmdc:study_set](https://w3id.org/nmdc/study_set)




## Inheritance

* **study_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [Study](Study.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: study_set
description: This property links a database object to the set of studies within it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: study_set
domain_of:
- Database
range: Study
inlined: true
inlined_as_list: true

```
</details>