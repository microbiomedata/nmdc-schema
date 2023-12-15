# Slot: host subspecific genetic lineage (host_subspecf_genlin)


_Information about the genetic distinctness of the host organism below the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123._



URI: [MIXS:0001318](https://w3id.org/mixs/0001318)




## Inheritance

* [core_field](core_field.md)
    * **host_subspecf_genlin**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True



## Aliases


* host subspecific genetic lineage




## Examples

| Value |
| --- |
| serovar:Newport, variety:glabrum, cultivar: Red Delicious |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | Genetic lineage below lowest rank of NCBI taxonomy, which is subspecies, e.g. serovar, biotype, ecotype, variety, cultivar. || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_subspecf_genlin
annotations:
  expected_value:
    tag: expected_value
    value: Genetic lineage below lowest rank of NCBI taxonomy, which is subspecies,
      e.g. serovar, biotype, ecotype, variety, cultivar.
  occurrence:
    tag: occurrence
    value: m
description: Information about the genetic distinctness of the host organism below
  the subspecies level e.g., serovar, serotype, biotype, ecotype, variety, cultivar,
  or any relevant genetic typing schemes like Group I plasmid. Subspecies should not
  be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name
  and the lineage rank separated by a colon, e.g., biovar:abc123.
title: host subspecific genetic lineage
examples:
- value: 'serovar:Newport, variety:glabrum, cultivar: Red Delicious'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host subspecific genetic lineage
rank: 1000
is_a: core field
string_serialization: '{rank name}:{text}'
slot_uri: MIXS:0001318
multivalued: true
alias: host_subspecf_genlin
domain_of:
- Biosample
range: string

```
</details>