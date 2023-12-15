# Slot: omics_type


_The type of omics data_



URI: [nmdc:omics_type](https://w3id.org/nmdc/omics_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)






## Examples

| Value |
| --- |
| metatranscriptome |
| metagenome |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: omics_type
description: The type of omics data
examples:
- value: metatranscriptome
- value: metagenome
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
domain: OmicsProcessing
alias: omics_type
domain_of:
- OmicsProcessing
range: ControlledTermValue

```
</details>