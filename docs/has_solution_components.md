# Slot: has_solution_components


_Relationship from a Solution to one or more constituent solution components_



URI: [nmdc:has_solution_components](https://w3id.org/nmdc/has_solution_components)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Solution](Solution.md) | A mixture that is homogeneous, made up of two or more scattered molecular agg... |  no  |







## Properties

* Range: [SolutionComponent](SolutionComponent.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: has_solution_components
description: Relationship from a Solution to one or more constituent solution components
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: Solution
multivalued: true
alias: has_solution_components
domain_of:
- Solution
range: SolutionComponent
required: true
inlined: true
inlined_as_list: true
minimum_cardinality: 1

```
</details>