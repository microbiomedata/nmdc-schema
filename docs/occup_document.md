# Slot: occupancy documentation (occup_document)


_The type of documentation of occupancy_



URI: [MIXS:0000816](https://w3id.org/mixs/0000816)




## Inheritance

* [core_field](core_field.md)
    * **occup_document**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [OccupDocumentEnum](OccupDocumentEnum.md)



## Aliases


* occupancy documentation




## Examples

| Value |
| --- |
| estimate |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: occup_document
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of documentation of occupancy
title: occupancy documentation
examples:
- value: estimate
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- occupancy documentation
rank: 1000
is_a: core field
slot_uri: MIXS:0000816
multivalued: false
alias: occup_document
domain_of:
- Biosample
range: occup_document_enum

```
</details>