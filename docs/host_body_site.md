# Slot: host body site (host_body_site)


_Name of body site where the sample was obtained from, such as a specific organ or tissue (tongue, lung etc...). For foundational model of anatomy ontology (fma) (v 4.11.0) or Uber-anatomy ontology (UBERON) (v releases/2014-06-15) terms, please see http://purl.bioontology.org/ontology/FMA or http://purl.bioontology.org/ontology/UBERON_



URI: [MIXS:0000867](https://w3id.org/mixs/0000867)




## Inheritance

* [core_field](core_field.md)
    * **host_body_site**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* host body site




## Examples

| Value |
| --- |
| gill [UBERON:0002535] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | FMA or UBERON || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_body_site
annotations:
  expected_value:
    tag: expected_value
    value: FMA or UBERON
  occurrence:
    tag: occurrence
    value: '1'
description: Name of body site where the sample was obtained from, such as a specific
  organ or tissue (tongue, lung etc...). For foundational model of anatomy ontology
  (fma) (v 4.11.0) or Uber-anatomy ontology (UBERON) (v releases/2014-06-15) terms,
  please see http://purl.bioontology.org/ontology/FMA or http://purl.bioontology.org/ontology/UBERON
title: host body site
examples:
- value: gill [UBERON:0002535]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host body site
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000867
multivalued: false
alias: host_body_site
domain_of:
- Biosample
range: ControlledTermValue

```
</details>