# Slot: target subfragment (target_subfragment)


_Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA_



URI: [MIXS:0000045](https://w3id.org/mixs/0000045)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **target_subfragment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* target subfragment




## Examples

| Value |
| --- |
| V6, V9, ITS |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | gene fragment name |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: target_subfragment
annotations:
  expected_value:
    tag: expected_value
    value: gene fragment name
description: Name of subfragment of a gene or locus. Important to e.g. identify special
  regions on marker genes like V6 on 16S rRNA
title: target subfragment
examples:
- value: V6, V9, ITS
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- target subfragment
rank: 1000
is_a: sequencing field
string_serialization: '{text}'
slot_uri: MIXS:0000045
multivalued: false
alias: target_subfragment
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>