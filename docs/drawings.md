# Slot: drawings (drawings)


_The buildings architectural drawings; if design is chosen, indicate phase-conceptual, schematic, design development, and construction documents_



URI: [MIXS:0000798](https://w3id.org/mixs/0000798)




## Inheritance

* [core_field](core_field.md)
    * **drawings**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [DrawingsEnum](DrawingsEnum.md)



## Aliases


* drawings




## Examples

| Value |
| --- |
| sketch |

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
name: drawings
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The buildings architectural drawings; if design is chosen, indicate phase-conceptual,
  schematic, design development, and construction documents
title: drawings
examples:
- value: sketch
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- drawings
rank: 1000
is_a: core field
slot_uri: MIXS:0000798
multivalued: false
alias: drawings
domain_of:
- Biosample
range: drawings_enum

```
</details>