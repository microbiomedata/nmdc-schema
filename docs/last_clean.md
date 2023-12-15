# Slot: last time swept/mopped/vacuumed (last_clean)


_The last time the floor was cleaned (swept, mopped, vacuumed)_



URI: [MIXS:0000814](https://w3id.org/mixs/0000814)




## Inheritance

* [core_field](core_field.md)
    * **last_clean**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* last time swept/mopped/vacuumed




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
name: last_clean
annotations:
  expected_value:
    tag: expected_value
    value: timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: The last time the floor was cleaned (swept, mopped, vacuumed)
title: last time swept/mopped/vacuumed
examples:
- value: 2018-05-11:T14:30Z
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- last time swept/mopped/vacuumed
rank: 1000
is_a: core field
slot_uri: MIXS:0000814
multivalued: false
alias: last_clean
domain_of:
- Biosample
range: TimestampValue

```
</details>