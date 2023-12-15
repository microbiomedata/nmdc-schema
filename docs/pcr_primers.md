# Slot: pcr primers (pcr_primers)


_PCR primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single PCR reaction if multiple forward or reverse primers are present in a single PCR reaction. The primer sequence should be reported in uppercase letters_



URI: [MIXS:0000046](https://w3id.org/mixs/0000046)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **pcr_primers**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* pcr primers




## Examples

| Value |
| --- |
| FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | FWD: forward primer sequence;REV:reverse primer sequence |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pcr_primers
annotations:
  expected_value:
    tag: expected_value
    value: 'FWD: forward primer sequence;REV:reverse primer sequence'
description: PCR primers that were used to amplify the sequence of the targeted gene,
  locus or subfragment. This field should contain all the primers used for a single
  PCR reaction if multiple forward or reverse primers are present in a single PCR
  reaction. The primer sequence should be reported in uppercase letters
title: pcr primers
examples:
- value: FWD:GTGCCAGCMGCCGCGGTAA;REV:GGACTACHVGGGTWTCTAAT
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pcr primers
rank: 1000
is_a: sequencing field
string_serialization: FWD:{dna};REV:{dna}
slot_uri: MIXS:0000046
multivalued: false
alias: pcr_primers
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>