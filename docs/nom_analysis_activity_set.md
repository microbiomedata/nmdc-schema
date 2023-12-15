# Slot: nom_analysis_activity_set


_This property links a database object to the set of natural organic matter (NOM) analysis activities._



URI: [nmdc:nom_analysis_activity_set](https://w3id.org/nmdc/nom_analysis_activity_set)




## Inheritance

* **nom_analysis_activity_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [NomAnalysisActivity](NomAnalysisActivity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: nom_analysis_activity_set
description: This property links a database object to the set of natural organic matter
  (NOM) analysis activities.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: nom_analysis_activity_set
domain_of:
- Database
range: NomAnalysisActivity
inlined: true
inlined_as_list: true

```
</details>