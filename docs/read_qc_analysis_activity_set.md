# Slot: read_qc_analysis_activity_set


_This property links a database object to the set of read QC analysis activities._



URI: [nmdc:read_qc_analysis_activity_set](https://w3id.org/nmdc/read_qc_analysis_activity_set)




## Inheritance

* **read_qc_analysis_activity_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [ReadQcAnalysisActivity](ReadQcAnalysisActivity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: read_qc_analysis_activity_set
description: This property links a database object to the set of read QC analysis
  activities.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: read_qc_analysis_activity_set
domain_of:
- Database
range: ReadQcAnalysisActivity
inlined: true
inlined_as_list: true

```
</details>