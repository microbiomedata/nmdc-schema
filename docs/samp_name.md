# Slot: sample name (samp_name)


_A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name._



URI: [MIXS:0001107](https://w3id.org/mixs/0001107)




## Inheritance

* [investigation_field](investigation_field.md)
    * **samp_name**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* sample name




## Examples

| Value |
| --- |
| ISDsoil1 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | text |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_name
annotations:
  expected_value:
    tag: expected_value
    value: text
description: A local identifier or name that for the material sample used for extracting
  nucleic acids, and subsequent sequencing. It can refer either to the original material
  collected or to any derived sub-samples. It can have any format, but we suggest
  that you make it concise, unique and consistent within your lab, and as informative
  as possible. INSDC requires every sample name from a single Submitter to be unique.
  Use of a globally unique identifier for the field source_mat_id is recommended in
  addition to sample_name.
title: sample name
examples:
- value: ISDsoil1
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample name
rank: 1000
is_a: investigation field
string_serialization: '{text}'
slot_uri: MIXS:0001107
multivalued: false
alias: samp_name
domain_of:
- Biosample
range: string

```
</details>