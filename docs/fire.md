# Slot: history/fire (fire)


_Historical and/or physical evidence of fire_



URI: [MIXS:0001086](https://w3id.org/mixs/0001086)




## Inheritance

* [core_field](core_field.md)
    * **fire**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* history/fire




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
name: fire
annotations:
  expected_value:
    tag: expected_value
    value: date
  occurrence:
    tag: occurrence
    value: '1'
description: Historical and/or physical evidence of fire
title: history/fire
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- history/fire
rank: 1000
is_a: core field
slot_uri: MIXS:0001086
multivalued: false
alias: fire
domain_of:
- Biosample
range: TimestampValue

```
</details>