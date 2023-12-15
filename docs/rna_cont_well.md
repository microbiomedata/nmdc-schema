# Slot: RNA plate position (rna_cont_well)

URI: [nmdc:rna_cont_well](https://w3id.org/nmdc/rna_cont_well)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$`






## Examples

| Value |
| --- |
| B2 |

## Comments

* Required when 'plate' is selected for container type.
* Leave blank if the sample will be shipped in a tube.
* JGI will not process samples in corner wells, so A1, A12, H1 and H12 will not pass validation.
* For partial plates, fill by columns, like B1-G1,A2-H2,A3-D3 (NOT A2-A11,B1-B8).

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_cont_well
title: RNA plate position
comments:
- Required when 'plate' is selected for container type.
- Leave blank if the sample will be shipped in a tube.
- JGI will not process samples in corner wells, so A1, A12, H1 and H12 will not pass
  validation.
- For partial plates, fill by columns, like B1-G1,A2-H2,A3-D3 (NOT A2-A11,B1-B8).
examples:
- value: B2
from_schema: https://w3id.org/nmdc/nmdc
rank: 11
string_serialization: '{96 well plate pos}'
alias: rna_cont_well
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true
pattern: ^(?!A1|A12|H1|H12)(([A-H][1-9])|([A-H]1[0-2]))$

```
</details>