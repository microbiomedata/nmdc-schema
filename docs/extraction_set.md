# Slot: extraction_set


_This property links a database object to the set of extractions within it._



URI: [nmdc:extraction_set](https://w3id.org/nmdc/extraction_set)




## Inheritance

* **extraction_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [Extraction](Extraction.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: extraction_set
description: This property links a database object to the set of extractions within
  it.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: extraction_set
domain_of:
- Database
range: Extraction
inlined: true
inlined_as_list: true

```
</details>