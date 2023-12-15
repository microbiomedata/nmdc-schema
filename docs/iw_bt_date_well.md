# Slot: injection water breakthrough date of specific well (iw_bt_date_well)


_Injection water breakthrough date per well following a secondary and/or tertiary recovery_



URI: [MIXS:0001010](https://w3id.org/mixs/0001010)




## Inheritance

* [core_field](core_field.md)
    * **iw_bt_date_well**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* injection water breakthrough date of specific well




## Examples

| Value |
| --- |
| 2018-05-11 |

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
name: iw_bt_date_well
annotations:
  expected_value:
    tag: expected_value
    value: timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: Injection water breakthrough date per well following a secondary and/or
  tertiary recovery
title: injection water breakthrough date of specific well
examples:
- value: '2018-05-11'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- injection water breakthrough date of specific well
rank: 1000
is_a: core field
slot_uri: MIXS:0001010
multivalued: false
alias: iw_bt_date_well
domain_of:
- Biosample
range: TimestampValue

```
</details>