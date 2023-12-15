# Slot: total particulate carbon (tot_part_carb)


_Total particulate carbon content_



URI: [MIXS:0000747](https://w3id.org/mixs/0000747)




## Inheritance

* [core_field](core_field.md)
    * **tot_part_carb**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* total particulate carbon




## Examples

| Value |
| --- |
| 35 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | microgram per liter, micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: tot_part_carb
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: microgram per liter, micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Total particulate carbon content
title: total particulate carbon
examples:
- value: 35 micromole per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- total particulate carbon
rank: 1000
is_a: core field
slot_uri: MIXS:0000747
multivalued: false
alias: tot_part_carb
domain_of:
- Biosample
range: QuantityValue

```
</details>