# Slot: experimental factor (experimental_factor)


_Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI_



URI: [MIXS:0000008](https://w3id.org/mixs/0000008)




## Inheritance

* [investigation_field](investigation_field.md)
    * **experimental_factor**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* experimental factor




## Examples

| Value |
| --- |
| time series design [EFO:EFO_0001779] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | text or EFO and/or OBI |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: experimental_factor
annotations:
  expected_value:
    tag: expected_value
    value: text or EFO and/or OBI
description: Experimental factors are essentially the variable aspects of an experiment
  design which can be used to describe an experiment, or set of experiments, in an
  increasingly detailed manner. This field accepts ontology terms from Experimental
  Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a
  browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO;
  for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI
title: experimental factor
examples:
- value: time series design [EFO:EFO_0001779]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- experimental factor
rank: 1000
is_a: investigation field
string_serialization: '{termLabel} {[termID]}|{text}'
slot_uri: MIXS:0000008
multivalued: false
alias: experimental_factor
domain_of:
- Biosample
range: ControlledTermValue

```
</details>