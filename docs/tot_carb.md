# Slot: total carbon (tot_carb)


_Total carbon content_



URI: [MIXS:0000525](https://w3id.org/mixs/0000525)




## Inheritance

* [core_field](core_field.md)
    * **tot_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  yes  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total carbon




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Total carbon content
title: total carbon
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000525
multivalued: false
alias: tot_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>