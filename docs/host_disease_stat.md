# Slot: host disease status (host_disease_stat)


_List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text_



URI: [MIXS:0000031](https://w3id.org/mixs/0000031)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **host_disease_stat**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* host disease status




## Examples

| Value |
| --- |
| rabies [DOID:11260] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | disease name or Disease Ontology term |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_disease_stat
annotations:
  expected_value:
    tag: expected_value
    value: disease name or Disease Ontology term
description: List of diseases with which the host has been diagnosed; can include
  multiple diagnoses. The value of the field depends on host; for humans the terms
  should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org,
  non-human host diseases are free text
title: host disease status
examples:
- value: rabies [DOID:11260]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host disease status
rank: 1000
is_a: nucleic acid sequence source field
string_serialization: '{termLabel} {[termID]}|{text}'
slot_uri: MIXS:0000031
multivalued: false
alias: host_disease_stat
domain_of:
- Biosample
range: TextValue

```
</details>