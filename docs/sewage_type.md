# Slot: sewage type (sewage_type)


_Type of wastewater treatment plant as municipial or industrial_



URI: [MIXS:0000215](https://w3id.org/mixs/0000215)




## Inheritance

* [core_field](core_field.md)
    * **sewage_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* sewage type




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | sewage type name || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: sewage_type
annotations:
  expected_value:
    tag: expected_value
    value: sewage type name
  occurrence:
    tag: occurrence
    value: '1'
description: Type of wastewater treatment plant as municipial or industrial
title: sewage type
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- sewage type
rank: 1000
is_a: core field
string_serialization: '{text}'
slot_uri: MIXS:0000215
multivalued: false
alias: sewage_type
domain_of:
- Biosample
range: TextValue

```
</details>