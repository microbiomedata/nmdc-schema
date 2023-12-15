# Slot: chemical administration (chem_administration)


_List of chemical compounds administered to the host or site where sampling occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can include multiple compounds. For chemical entities of biological interest ontology (chebi) (v 163), http://purl.bioontology.org/ontology/chebi_



URI: [MIXS:0000751](https://w3id.org/mixs/0000751)




## Inheritance

* [core_field](core_field.md)
    * **chem_administration**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledTermValue](ControlledTermValue.md)

* Multivalued: True



## Aliases


* chemical administration




## Examples

| Value |
| --- |
| agar [CHEBI:2509];2018-05-11T20:00Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | CHEBI;timestamp || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: chem_administration
annotations:
  expected_value:
    tag: expected_value
    value: CHEBI;timestamp
  occurrence:
    tag: occurrence
    value: m
description: List of chemical compounds administered to the host or site where sampling
  occurred, and when (e.g. Antibiotics, n fertilizer, air filter); can include multiple
  compounds. For chemical entities of biological interest ontology (chebi) (v 163),
  http://purl.bioontology.org/ontology/chebi
title: chemical administration
examples:
- value: agar [CHEBI:2509];2018-05-11T20:00Z
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chemical administration
rank: 1000
is_a: core field
string_serialization: '{termLabel} {[termID]};{timestamp}'
slot_uri: MIXS:0000751
multivalued: true
alias: chem_administration
domain_of:
- Biosample
range: ControlledTermValue

```
</details>