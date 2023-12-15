# Slot: activity_set


_This property links a database object to the set of workflow activities._



URI: [nmdc:activity_set](https://w3id.org/nmdc/activity_set)




## Inheritance

* **activity_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [WorkflowExecutionActivity](WorkflowExecutionActivity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: activity_set
description: This property links a database object to the set of workflow activities.
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: activity_set
domain_of:
- Database
range: WorkflowExecutionActivity
inlined: true
inlined_as_list: true

```
</details>