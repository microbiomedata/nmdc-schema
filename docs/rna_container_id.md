# Slot: RNA container label (rna_container_id)

URI: [nmdc:rna_container_id](https://w3id.org/nmdc/rna_container_id)



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
| Pond_MT_041618 |

## Comments

* Must be unique across all tubes and plates, and <20 characters. All samples in a plate should have the same plate label.

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_container_id
title: RNA container label
comments:
- Must be unique across all tubes and plates, and <20 characters. All samples in a
  plate should have the same plate label.
examples:
- value: Pond_MT_041618
from_schema: https://w3id.org/nmdc/nmdc
rank: 9
string_serialization: '{text < 20 characters}'
alias: rna_container_id
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true

```
</details>