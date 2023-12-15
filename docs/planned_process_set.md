# Slot: planned_process_set


_This property links a database object to the set of planned processes within it._



URI: [nmdc:planned_process_set](https://w3id.org/nmdc/planned_process_set)




## Inheritance

* **planned_process_set** [ [object_set](object_set.md)]





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Database](Database.md) | An abstract holder for any set of metadata and data |  no  |







## Properties

* Range: [PlannedProcess](PlannedProcess.md)

* Multivalued: True





## Comments

* PlannedProcess instances aggregated by this slot will require the designated_class slot

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: planned_process_set
description: This property links a database object to the set of planned processes
  within it.
comments:
- PlannedProcess instances aggregated by this slot will require the designated_class
  slot
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
mixins:
- object_set
domain: Database
multivalued: true
alias: planned_process_set
domain_of:
- Database
range: PlannedProcess
inlined: true
inlined_as_list: true

```
</details>