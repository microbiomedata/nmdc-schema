# Slot: functional_annotation_set


_This property links a database object to the set of all functional annotations_



URI: [nmdc:functional_annotation_set](https://w3id.org/nmdc/functional_annotation_set)




## Inheritance

* **functional_annotation_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [FunctionalAnnotation](FunctionalAnnotation.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: functional_annotation_set
description: This property links a database object to the set of all functional annotations
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: functional_annotation_set
domain_of:
- Database
range: FunctionalAnnotation
inlined: true
inlined_as_list: true

```
</details>