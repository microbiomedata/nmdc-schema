# Slot: growth facility (growth_facil)


_Type of facility where the sampled plant was grown; controlled vocabulary: growth chamber, open top chamber, glasshouse, experimental garden, field. Alternatively use Crop Ontology (CO) terms, see http://www.cropontology.org/ontology/CO_715/Crop%20Research_



URI: [MIXS:0001043](https://w3id.org/mixs/0001043)




## Inheritance

* [core_field](core_field.md)
    * **growth_facil**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* growth facility




## Examples

| Value |
| --- |
| Growth chamber [CO_715:0000189] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | free text or CO || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: growth_facil
annotations:
  expected_value:
    tag: expected_value
    value: free text or CO
  occurrence:
    tag: occurrence
    value: '1'
description: 'Type of facility where the sampled plant was grown; controlled vocabulary:
  growth chamber, open top chamber, glasshouse, experimental garden, field. Alternatively
  use Crop Ontology (CO) terms, see http://www.cropontology.org/ontology/CO_715/Crop%20Research'
title: growth facility
examples:
- value: Growth chamber [CO_715:0000189]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- growth facility
rank: 1000
is_a: core field
string_serialization: '{text}|{termLabel} {[termID]}'
slot_uri: MIXS:0001043
multivalued: false
alias: growth_facil
domain_of:
- Biosample
range: ControlledTermValue

```
</details>