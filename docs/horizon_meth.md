# Slot: soil horizon method (horizon_meth)


_Reference or method used in determining the horizon_



URI: [MIXS:0000321](https://w3id.org/mixs/0000321)




## Inheritance

* [core_field](core_field.md)
    * **horizon_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* soil horizon method




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | PMID,DOI or url || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: horizon_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining the horizon
title: soil horizon method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- soil horizon method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000321
multivalued: false
alias: horizon_meth
domain_of:
- Biosample
range: TextValue

```
</details>