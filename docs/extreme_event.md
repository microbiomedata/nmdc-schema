# Slot: history/extreme events (extreme_event)


_Unusual physical events that may have affected microbial populations_



URI: [MIXS:0000320](https://w3id.org/mixs/0000320)




## Inheritance

* [core_field](core_field.md)
    * **extreme_event**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* history/extreme events




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
name: extreme_event
annotations:
  expected_value:
    tag: expected_value
    value: date
  occurrence:
    tag: occurrence
    value: '1'
description: Unusual physical events that may have affected microbial populations
title: history/extreme events
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/extreme events
rank: 1000
is_a: core field
slot_uri: MIXS:0000320
multivalued: false
alias: extreme_event
domain_of:
- Biosample
range: TimestampValue

```
</details>