# Slot: omics_processing_set


_This property links a database object to the set of omics processings within it._



URI: [nmdc:omics_processing_set](https://w3id.org/nmdc/omics_processing_set)




## Inheritance

* **omics_processing_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [OmicsProcessing](OmicsProcessing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: omics_processing_set
description: This property links a database object to the set of omics processings
  within it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: omics_processing_set
domain_of:
- Database
range: OmicsProcessing
inlined: true
inlined_as_list: true

```
</details>