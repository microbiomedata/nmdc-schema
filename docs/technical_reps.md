# Slot: number technical replicate (technical_reps)


_If sending technical replicates of the same sample, indicate the replicate count._



URI: [nmdc:technical_reps](https://w3id.org/nmdc/technical_reps)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 2 |

## Comments

* This field is only required when completing metadata for samples being submitted to EMSL for analyses.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: technical_reps
description: If sending technical replicates of the same sample, indicate the replicate
  count.
title: number technical replicate
comments:
- This field is only required when completing metadata for samples being submitted
  to EMSL for analyses.
examples:
- value: '2'
from_schema: https://w3id.org/nmdc/nmdc
rank: 5
string_serialization: '{integer}'
alias: technical_reps
domain_of:
- Biosample
slot_group: EMSL
range: string
recommended: true

```
</details>