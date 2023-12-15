# Slot: production rate (prod_rate)


_Oil and/or gas production rates per well (e.g. 524 m3 / day)_



URI: [MIXS:0000452](https://w3id.org/mixs/0000452)




## Inheritance

* [core_field](core_field.md)
    * **prod_rate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* production rate




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | cubic meter per day || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: prod_rate
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: cubic meter per day
  occurrence:
    tag: occurrence
    value: '1'
description: Oil and/or gas production rates per well (e.g. 524 m3 / day)
title: production rate
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- production rate
rank: 1000
is_a: core field
slot_uri: MIXS:0000452
multivalued: false
alias: prod_rate
domain_of:
- Biosample
range: QuantityValue

```
</details>