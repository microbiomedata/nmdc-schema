# Slot: sample collection device (samp_collec_device)


_The device used to collect an environmental sample. This field accepts terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO). This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094)._



URI: [MIXS:0000002](https://w3id.org/mixs/0000002)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **samp_collec_device**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* sample collection device




## Examples

| Value |
| --- |
| swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | device name |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: samp_collec_device
annotations:
  expected_value:
    tag: expected_value
    value: device name
description: The device used to collect an environmental sample. This field accepts
  terms listed under environmental sampling device (http://purl.obolibrary.org/obo/ENVO).
  This field also accepts terms listed under specimen collection device (http://purl.obolibrary.org/obo/GENEPIO_0002094).
title: sample collection device
examples:
- value: swab, biopsy, niskin bottle, push core, drag swab [GENEPIO:0002713]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sample collection device
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{termLabel} {[termID]}|{text}'
slot_uri: MIXS:0000002
multivalued: false
alias: samp_collec_device
domain_of:
- Biosample
range: string

```
</details>