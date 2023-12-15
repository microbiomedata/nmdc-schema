# Slot: pre-treatment (pre_treatment)


_The process of pre-treatment removes materials that can be easily collected from the raw wastewater_



URI: [MIXS:0000348](https://w3id.org/mixs/0000348)




## Inheritance

* [core_field](core_field.md)
    * **pre_treatment**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* pre-treatment




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | pre-treatment type || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: pre_treatment
annotations:
  expected_value:
    tag: expected_value
    value: pre-treatment type
  occurrence:
    tag: occurrence
    value: '1'
description: The process of pre-treatment removes materials that can be easily collected
  from the raw wastewater
title: pre-treatment
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- pre-treatment
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000348
multivalued: false
alias: pre_treatment
domain_of:
- Biosample
range: TextValue

```
</details>