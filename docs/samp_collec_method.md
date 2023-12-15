# Slot: sample collection method (samp_collec_method)


_The method employed for collecting the sample._



URI: [MIXS:0001225](https://w3id.org/mixs/0001225)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **samp_collec_method**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* sample collection method




## Examples

| Value |
| --- |
| swabbing |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI,url , or text |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_collec_method
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI,url , or text
description: The method employed for collecting the sample.
title: sample collection method
examples:
- value: swabbing
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample collection method
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{PMID}|{DOI}|{URL}|{text}'
slot_uri: MIXS:0001225
multivalued: false
alias: samp_collec_method
domain_of:
- Biosample
range: string

```
</details>