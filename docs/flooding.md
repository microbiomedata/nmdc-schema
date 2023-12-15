# Slot: history/flooding (flooding)


_Historical and/or physical evidence of flooding_



URI: [MIXS:0000319](https://w3id.org/mixs/0000319)




## Inheritance

* [core_field](core_field.md)
    * **flooding**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* history/flooding




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | date || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: flooding
annotations:
  expected_value:
    tag: expected_value
    value: date
  occurrence:
    tag: occurrence
    value: '1'
description: Historical and/or physical evidence of flooding
title: history/flooding
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/flooding
rank: 1000
is_a: core field
slot_uri: MIXS:0000319
multivalued: false
alias: flooding
domain_of:
- Biosample
range: TimestampValue

```
</details>