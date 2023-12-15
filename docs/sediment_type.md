# Slot: sediment type (sediment_type)


_Information about the sediment type based on major constituents_



URI: [MIXS:0001078](https://w3id.org/mixs/0001078)




## Inheritance

* [core_field](core_field.md)
    * **sediment_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [SedimentTypeEnum](SedimentTypeEnum.md)



## Aliases


* sediment type




## Examples

| Value |
| --- |
| biogenous |

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
name: sediment_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Information about the sediment type based on major constituents
title: sediment type
examples:
- value: biogenous
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sediment type
rank: 1000
is_a: core field
slot_uri: MIXS:0001078
multivalued: false
alias: sediment_type
domain_of:
- Biosample
range: sediment_type_enum

```
</details>