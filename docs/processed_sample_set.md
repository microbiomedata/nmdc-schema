# Slot: processed_sample_set


_This property links a database object to the set of processed samples within it._



URI: [nmdc:processed_sample_set](https://w3id.org/nmdc/processed_sample_set)




## Inheritance

* **processed_sample_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [ProcessedSample](ProcessedSample.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: processed_sample_set
description: This property links a database object to the set of processed samples
  within it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: processed_sample_set
domain_of:
- Database
range: ProcessedSample
inlined: true
inlined_as_list: true

```
</details>