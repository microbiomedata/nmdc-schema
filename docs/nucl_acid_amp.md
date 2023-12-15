# Slot: nucleic acid amplification (nucl_acid_amp)


_A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of specific nucleic acids_



URI: [MIXS:0000038](https://w3id.org/mixs/0000038)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **nucl_acid_amp**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* nucleic acid amplification




## Examples

| Value |
| --- |
| https://phylogenomics.me/protocols/16s-pcr-protocol/ |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID, DOI or URL |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: nucl_acid_amp
annotations:
  expected_value:
    tag: expected_value
    value: PMID, DOI or URL
description: A link to a literature reference, electronic resource or a standard operating
  procedure (SOP), that describes the enzymatic amplification (PCR, TMA, NASBA) of
  specific nucleic acids
title: nucleic acid amplification
examples:
- value: https://phylogenomics.me/protocols/16s-pcr-protocol/
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- nucleic acid amplification
rank: 1000
is_a: sequencing field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000038
multivalued: false
alias: nucl_acid_amp
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>