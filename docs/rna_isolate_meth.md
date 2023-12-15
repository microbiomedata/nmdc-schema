# Slot: RNA isolation method (rna_isolate_meth)


_Describe the method/protocol/kit used to extract DNA/RNA._



URI: [nmdc:rna_isolate_meth](https://w3id.org/nmdc/rna_isolate_meth)



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
| phenol/chloroform extraction |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: rna_isolate_meth
description: Describe the method/protocol/kit used to extract DNA/RNA.
title: RNA isolation method
examples:
- value: phenol/chloroform extraction
from_schema: https://w3id.org/nmdc/nmdc
rank: 16
string_serialization: '{text}'
alias: rna_isolate_meth
domain_of:
- Biosample
slot_group: JGI-Metatranscriptomics
range: string
recommended: true

```
</details>