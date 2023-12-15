# Slot: observed biotic relationship (biotic_relationship)


_Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g., parasite on species X; mutualist with species Y. The target organism is the subject of the relationship, and the other organism(s) is the object_



URI: [MIXS:0000028](https://w3id.org/mixs/0000028)




## Inheritance

* [nucleic_acid_sequence_source_field](nucleic_acid_sequence_source_field.md)
    * **biotic_relationship**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [BioticRelationshipEnum](BioticRelationshipEnum.md)



## Aliases


* observed biotic relationship




## Examples

| Value |
| --- |
| free living |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biotic_relationship
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
description: Description of relationship(s) between the subject organism and other
  organism(s) it is associated with. E.g., parasite on species X; mutualist with species
  Y. The target organism is the subject of the relationship, and the other organism(s)
  is the object
title: observed biotic relationship
examples:
- value: free living
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- observed biotic relationship
rank: 1000
is_a: nucleic acid sequence source field
slot_uri: MIXS:0000028
multivalued: false
alias: biotic_relationship
domain_of:
- Biosample
range: biotic_relationship_enum

```
</details>