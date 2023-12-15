# Slot: weekday (weekday)


_The day of the week when sampling occurred_



URI: [MIXS:0000848](https://w3id.org/mixs/0000848)




## Inheritance

* [core_field](core_field.md)
    * **weekday**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [WeekdayEnum](WeekdayEnum.md)



## Aliases


* weekday




## Examples

| Value |
| --- |
| Sunday |

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
name: weekday
annotations:
  expected_value:
    tag: expected_value
    value: enumeration
  occurrence:
    tag: occurrence
    value: '1'
description: The day of the week when sampling occurred
title: weekday
examples:
- value: Sunday
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- weekday
rank: 1000
is_a: core field
slot_uri: MIXS:0000848
multivalued: false
alias: weekday
domain_of:
- Biosample
range: weekday_enum

```
</details>