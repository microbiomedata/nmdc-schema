# Slot: RNA seq project name (rna_seq_project_name)

URI: [nmdc:rna_seq_project_name](https://w3id.org/nmdc/rna_seq_project_name)



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
| JGI Pond metatranscriptomics |

## Comments

* Do not edit these values. A template will be provided by NMDC in which these values have been pre-filled.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_seq_project_name
title: RNA seq project name
comments:
- Do not edit these values. A template will be provided by NMDC in which these values
  have been pre-filled.
examples:
- value: JGI Pond metatranscriptomics
from_schema: https://w3id.org/nmdc/nmdc
rank: 2
string_serialization: '{text}'
alias: rna_seq_project_name
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true

```
</details>