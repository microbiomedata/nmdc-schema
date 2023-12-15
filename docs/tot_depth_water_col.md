# Slot: total depth of water column (tot_depth_water_col)


_Measurement of total depth of water column_



URI: [MIXS:0000634](https://w3id.org/mixs/0000634)




## Inheritance

* [core_field](core_field.md)
    * **tot_depth_water_col**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total depth of water column




## Examples

| Value |
| --- |
| 500 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_depth_water_col
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: meter
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of total depth of water column
title: total depth of water column
examples:
- value: 500 meter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total depth of water column
rank: 1000
is_a: core field
slot_uri: MIXS:0000634
multivalued: false
alias: tot_depth_water_col
domain_of:
- Biosample
range: QuantityValue

```
</details>