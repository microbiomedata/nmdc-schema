# Slot: plant structure (plant_struc)


_Name of plant structure the sample was obtained from; for Plant Ontology (PO) (v releases/2017-12-14) terms, see http://purl.bioontology.org/ontology/PO, e.g. petiole epidermis (PO_0000051). If an individual flower is sampled, the sex of it can be recorded here._



URI: [MIXS:0001060](https://w3id.org/mixs/0001060)




## Inheritance

* [core_field](core_field.md)
    * **plant_struc**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* plant structure




## Examples

| Value |
| --- |
| epidermis [PO:0005679] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PO || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: plant_struc
annotations:
  expected_value:
    tag: expected_value
    value: PO
  occurrence:
    tag: occurrence
    value: '1'
description: Name of plant structure the sample was obtained from; for Plant Ontology
  (PO) (v releases/2017-12-14) terms, see http://purl.bioontology.org/ontology/PO,
  e.g. petiole epidermis (PO_0000051). If an individual flower is sampled, the sex
  of it can be recorded here.
title: plant structure
examples:
- value: epidermis [PO:0005679]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- plant structure
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0001060
multivalued: false
alias: plant_struc
domain_of:
- Biosample
range: ControlledTermValue

```
</details>