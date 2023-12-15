# Slot: metaproteomics_analysis_activity_set


_This property links a database object to the set of metaproteomics analysis activities._



URI: [nmdc:metaproteomics_analysis_activity_set](https://w3id.org/nmdc/metaproteomics_analysis_activity_set)




## Inheritance

* **metaproteomics_analysis_activity_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: metaproteomics_analysis_activity_set
description: This property links a database object to the set of metaproteomics analysis
  activities.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: metaproteomics_analysis_activity_set
domain_of:
- Database
range: MetaproteomicsAnalysisActivity
inlined: true
inlined_as_list: true

```
</details>