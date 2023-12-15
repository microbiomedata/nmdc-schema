# Slot: window status (window_status)


_Defines whether the windows were open or closed during environmental testing_



URI: [MIXS:0000855](https://w3id.org/mixs/0000855)




## Inheritance

* [core_field](core_field.md)
    * **window_status**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* window status




## Examples

| Value |
| --- |
| open |

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
name: window_status
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: Defines whether the windows were open or closed during environmental
  testing
title: window status
examples:
- value: open
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window status
rank: 1000
is_a: core field
string_serialization: '[closed|open]'
slot_uri: MIXS:0000855
multivalued: false
alias: window_status
domain_of:
- Biosample
range: TextValue

```
</details>