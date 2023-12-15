# Slot: target gene (target_gene)


_Targeted gene or locus name for marker gene studies_



URI: [MIXS:0000044](https://w3id.org/mixs/0000044)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **target_gene**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* target gene




## Examples

| Value |
| --- |
| 16S rRNA, 18S rRNA, nif, amoA, rpo |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gene name |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: target_gene
annotations:
  expected_value:
    tag: expected_value
    value: gene name
description: Targeted gene or locus name for marker gene studies
title: target gene
examples:
- value: 16S rRNA, 18S rRNA, nif, amoA, rpo
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- target gene
rank: 1000
is_a: sequencing field
string_serialization: '{text}'
slot_uri: MIXS:0000044
multivalued: false
alias: target_gene
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>