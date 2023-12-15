# Slot: design, construction, and operation documents (build_docs)


_The building design, construction and operation documents_



URI: [MIXS:0000787](https://w3id.org/mixs/0000787)




## Inheritance

* [core_field](core_field.md)
    * **build_docs**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [BuildDocsEnum](BuildDocsEnum.md)



## Aliases


* design, construction, and operation documents




## Examples

| Value |
| --- |
| maintenance plans |

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
name: build_docs
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The building design, construction and operation documents
title: design, construction, and operation documents
examples:
- value: maintenance plans
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- design, construction, and operation documents
rank: 1000
is_a: core field
slot_uri: MIXS:0000787
multivalued: false
alias: build_docs
domain_of:
- Biosample
range: build_docs_enum

```
</details>