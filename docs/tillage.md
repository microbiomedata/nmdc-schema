# Slot: history/tillage (tillage)


_Note method(s) used for tilling_



URI: [MIXS:0001081](https://w3id.org/mixs/0001081)




## Inheritance

* [core_field](core_field.md)
    * **tillage**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TillageEnum](TillageEnum.md)

* Multivalued: True



## Aliases


* history/tillage




## Examples

| Value |
| --- |
| chisel |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | enumeration || occurrence | m |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tillage
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: m
description: Note method(s) used for tilling
title: history/tillage
examples:
- value: chisel
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/tillage
rank: 1000
is_a: core field
slot_uri: MIXS:0001081
multivalued: true
alias: tillage
domain_of:
- Biosample
range: tillage_enum

```
</details>