# Slot: host taxid (host_taxid)


_NCBI taxon id of the host, e.g. 9606_



URI: [MIXS:0000250](https://w3id.org/mixs/0000250)




## Inheritance

* [core_field](core_field.md)
    * **host_taxid**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [ControlledIdentifiedTermValue](ControlledIdentifiedTermValue.md)



## Aliases


* host taxid



## Comments

* Homo sapiens [NCBITaxon:9606] would be a reasonable has_raw_value

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | NCBI taxon identifier || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: host_taxid
annotations:
  expected_value:
    tag: expected_value
    value: NCBI taxon identifier
  occurrence:
    tag: occurrence
    value: '1'
description: NCBI taxon id of the host, e.g. 9606
title: host taxid
comments:
- Homo sapiens [NCBITaxon:9606] would be a reasonable has_raw_value
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- host taxid
rank: 1000
is_a: core field
slot_uri: MIXS:0000250
multivalued: false
alias: host_taxid
domain_of:
- Biosample
range: ControlledIdentifiedTermValue

```
</details>