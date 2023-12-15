# Slot: host phenotype (host_phenotype)


_Phenotype of human or other host. For phenotypic quality ontology (pato) (v 2018-03-27) terms, please see http://purl.bioontology.org/ontology/pato. For Human Phenotype Ontology (HP) (v 2018-06-13) please see http://purl.bioontology.org/ontology/HP_



URI: [MIXS:0000874](https://w3id.org/mixs/0000874)




## Inheritance

* [core_field](core_field.md)
    * **host_phenotype**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* host phenotype




## Examples

| Value |
| --- |
| elongated [PATO:0001154] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PATO or HP || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_phenotype
annotations:
  expected_value:
    tag: expected_value
    value: PATO or HP
  occurrence:
    tag: occurrence
    value: '1'
description: Phenotype of human or other host. For phenotypic quality ontology (pato)
  (v 2018-03-27) terms, please see http://purl.bioontology.org/ontology/pato. For
  Human Phenotype Ontology (HP) (v 2018-06-13) please see http://purl.bioontology.org/ontology/HP
title: host phenotype
examples:
- value: elongated [PATO:0001154]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host phenotype
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000874
multivalued: false
alias: host_phenotype
domain_of:
- Biosample
range: ControlledTermValue

```
</details>