# Slot: window type (window_type)


_The type of windows_



URI: [MIXS:0000856](https://w3id.org/mixs/0000856)




## Inheritance

* [core_field](core_field.md)
    * **window_type**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WindowTypeEnum](WindowTypeEnum.md)



## Aliases


* window type




## Examples

| Value |
| --- |
| fixed window |

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
name: window_type
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The type of windows
title: window type
examples:
- value: fixed window
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window type
rank: 1000
is_a: core field
slot_uri: MIXS:0000856
multivalued: false
alias: window_type
domain_of:
- Biosample
range: window_type_enum

```
</details>