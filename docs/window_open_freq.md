# Slot: window open frequency (window_open_freq)


_The number of times windows are opened per week_



URI: [MIXS:0000246](https://w3id.org/mixs/0000246)




## Inheritance

* [core_field](core_field.md)
    * **window_open_freq**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TextValue](TextValue.md)



## Aliases


* window open frequency




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | value || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: window_open_freq
annotations:
  expected_value:
    tag: expected_value
    value: value
  occurrence:
    tag: occurrence
    value: '1'
description: The number of times windows are opened per week
title: window open frequency
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- window open frequency
rank: 1000
is_a: core field
slot_uri: MIXS:0000246
multivalued: false
alias: window_open_freq
domain_of:
- Biosample
range: TextValue

```
</details>