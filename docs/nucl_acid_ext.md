# Slot: nucleic acid extraction (nucl_acid_ext)


_A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample_



URI: [MIXS:0000037](https://w3id.org/mixs/0000037)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **nucl_acid_ext**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* nucleic acid extraction




## Examples

| Value |
| --- |
| https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf |

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
name: nucl_acid_ext
annotations:
  expected_value:
    tag: expected_value
    value: PMID, DOI or URL
description: A link to a literature reference, electronic resource or a standard operating
  procedure (SOP), that describes the material separation to recover the nucleic acid
  fraction from a sample
title: nucleic acid extraction
examples:
- value: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- nucleic acid extraction
rank: 1000
is_a: sequencing field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000037
multivalued: false
alias: nucl_acid_ext
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>