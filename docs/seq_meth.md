# Slot: sequencing method (seq_meth)


_Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103)._



URI: [MIXS:0000050](https://w3id.org/mixs/0000050)




## Inheritance

* [sequencing_field](sequencing_field.md)
    * **seq_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |
[OmicsProcessing](OmicsProcessing.md) | The methods and processes used to generate omics data from a biosample or org... |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sequencing method




## Examples

| Value |
| --- |
| 454 Genome Sequencer FLX [OBI:0000702] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | Text or OBI |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: seq_meth
annotations:
  expected_value:
    tag: expected_value
    value: Text or OBI
description: Sequencing machine used. Where possible the term should be taken from
  the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103).
title: sequencing method
examples:
- value: 454 Genome Sequencer FLX [OBI:0000702]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sequencing method
rank: 1000
is_a: sequencing field
string_serialization: '{termLabel} {[termID]}|{text}'
slot_uri: MIXS:0000050
multivalued: false
alias: seq_meth
domain_of:
- Biosample
- OmicsProcessing
range: TextValue

```
</details>