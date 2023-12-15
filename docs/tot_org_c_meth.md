# Slot: total organic carbon method (tot_org_c_meth)


_Reference or method used in determining total organic carbon_



URI: [MIXS:0000337](https://w3id.org/mixs/0000337)




## Inheritance

* [core_field](core_field.md)
    * **tot_org_c_meth**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* total organic carbon method




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
name: tot_org_c_meth
annotations:
  expected_value:
    tag: expected_value
    value: PMID,DOI or url
  occurrence:
    tag: occurrence
    value: '1'
description: Reference or method used in determining total organic carbon
title: total organic carbon method
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total organic carbon method
rank: 1000
is_a: core field
string_serialization: '{PMID}|{DOI}|{URL}'
slot_uri: MIXS:0000337
multivalued: false
alias: tot_org_c_meth
domain_of:
- Biosample
range: TextValue

```
</details>