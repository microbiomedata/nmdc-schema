# Slot: sequence quality check (seq_quality_check)


_Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA_



URI: [MIXS:0000051](https://w3id.org/mixs/0000051)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **seq_quality_check**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sequence quality check




## Examples

| Value |
| --- |
| none |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | none or manually edited |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: seq_quality_check
annotations:
  expected_value:
    tag: expected_value
    value: none or manually edited
description: Indicate if the sequence has been called by automatic systems (none)
  or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms).
  Applied only for sequences that are not submitted to SRA,ENA or DRA
title: sequence quality check
examples:
- value: none
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sequence quality check
rank: 1000
is_a: sequencing field
string_serialization: '[none|manually edited]'
slot_uri: MIXS:0000051
multivalued: false
alias: seq_quality_check
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>