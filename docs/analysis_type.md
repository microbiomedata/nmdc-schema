# Slot: analysis/data type (analysis_type)


_Select all the data types associated or available for this biosample_



URI: [nmdc:analysis_type](https://w3id.org/nmdc/analysis_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [AnalysisTypeEnum](AnalysisTypeEnum.md)

* Multivalued: True

* Recommended: True






## Examples

| Value |
| --- |
| metagenomics; metabolomics; proteomics |

## See Also

* [MIxS:investigation_type](https://w3id.org/mixs/investigation_type)

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: analysis_type
description: Select all the data types associated or available for this biosample
title: analysis/data type
examples:
- value: metagenomics; metabolomics; proteomics
from_schema: https://w3id.org/nmdc/nmdc
see_also:
- MIxS:investigation_type
rank: 3
multivalued: true
alias: analysis_type
domain_of:
- Biosample
slot_group: Sample ID
range: analysis_type_enum
recommended: true

```
</details>