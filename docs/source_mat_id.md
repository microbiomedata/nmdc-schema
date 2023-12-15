# Slot: source material identifiers (source_mat_id)


_A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2)._



URI: [MIXS:0000026](https://w3id.org/mixs/0000026)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **source_mat_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* source material identifiers




## Examples

| Value |
| --- |
| MPI012345 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | for cultures of microorganisms: identifiers for two culture collections; for other material a unique arbitrary identifer |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: source_mat_id
annotations:
  expected_value:
    tag: expected_value
    value: 'for cultures of microorganisms: identifiers for two culture collections;
      for other material a unique arbitrary identifer'
description: A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID,
  and as opposed to a particular digital record of a material sample) used for extracting
  nucleic acids, and subsequent sequencing. The identifier can refer either to the
  original material collected or to any derived sub-samples. The INSDC qualifiers
  /specimen_voucher, /bio_material, or /culture_collection may or may not share the
  same value as the source_mat_id field. For instance, the /specimen_voucher qualifier
  and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen
  voucher and sampled tissue with the same identifier. However, the /culture_collection
  qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id
  would refer to an identifier from some derived culture from which the nucleic acids
  were extracted (e.g. xatc123 or ark:/2154/R2).
title: source material identifiers
examples:
- value: MPI012345
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- source material identifiers
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{text}'
slot_uri: MIXS:0000026
multivalued: false
alias: source_mat_id
domain_of:
- Biosample
range: TextValue

```
</details>