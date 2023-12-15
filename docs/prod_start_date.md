# Slot: production start date (prod_start_date)


_Date of field's first production_



URI: [MIXS:0001008](https://w3id.org/mixs/0001008)




## Inheritance

* [core_field](core_field.md)
    * **prod_start_date**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [TimestampValue](TimestampValue.md)



## Aliases


* production start date




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
name: prod_start_date
annotations:
  expected_value:
    tag: expected_value
    value: timestamp
  occurrence:
    tag: occurrence
    value: '1'
description: Date of field's first production
title: production start date
examples:
- value: '2018-05-11'
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- production start date
rank: 1000
is_a: core field
slot_uri: MIXS:0001008
multivalued: false
alias: prod_start_date
domain_of:
- Biosample
range: TimestampValue

```
</details>