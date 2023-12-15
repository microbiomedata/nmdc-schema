# Slot: date last rain (date_last_rain)


_The date of the last time it rained_



URI: [MIXS:0000786](https://w3id.org/mixs/0000786)




## Inheritance

* [core_field](core_field.md)
    * **date_last_rain**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* date last rain




## Examples

| Value |
| --- |
| 2018-05-11:T14:30Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | timestamp || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: date_last_rain
annotations:
  expected_value:
    tag: expected_value
    value: timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: The date of the last time it rained
title: date last rain
examples:
- value: 2018-05-11:T14:30Z
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- date last rain
rank: 1000
is_a: core field
slot_uri: MIXS:0000786
multivalued: false
alias: date_last_rain
domain_of:
- Biosample
range: TimestampValue

```
</details>