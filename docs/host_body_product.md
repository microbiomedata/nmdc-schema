# Slot: host body product (host_body_product)


_Substance produced by the body, e.g. Stool, mucus, where the sample was obtained from. For foundational model of anatomy ontology (fma) or Uber-anatomy ontology (UBERON) terms, please see https://www.ebi.ac.uk/ols/ontologies/fma or https://www.ebi.ac.uk/ols/ontologies/uberon_



URI: [MIXS:0000888](https://w3id.org/mixs/0000888)




## Inheritance

* [core_field](core_field.md)
    * **host_body_product**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)



## Aliases


* host body product




## Examples

| Value |
| --- |
| Portion of mucus [fma66938] |

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
name: host_body_product
annotations:
  expected_value:
    tag: expected_value
    value: FMA or UBERON
  occurrence:
    tag: occurrence
    value: '1'
description: Substance produced by the body, e.g. Stool, mucus, where the sample was
  obtained from. For foundational model of anatomy ontology (fma) or Uber-anatomy
  ontology (UBERON) terms, please see https://www.ebi.ac.uk/ols/ontologies/fma or
  https://www.ebi.ac.uk/ols/ontologies/uberon
title: host body product
examples:
- value: Portion of mucus [fma66938]
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host body product
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]}'
slot_uri: MIXS:0000888
multivalued: false
alias: host_body_product
domain_of:
- Biosample
range: ControlledTermValue

```
</details>