# Slot: bacterial carbon production (bacteria_carb_prod)


_Measurement of bacterial carbon production_



URI: [MIXS:0000173](https://w3id.org/mixs/0000173)




## Inheritance

* [core_field](core_field.md)
    * **bacteria_carb_prod**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* bacterial carbon production




## Examples

| Value |
| --- |
| 2.53 microgram per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | nanogram per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: bacteria_carb_prod
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: nanogram per hour
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of bacterial carbon production
title: bacterial carbon production
examples:
- value: 2.53 microgram per liter per hour
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- bacterial carbon production
rank: 1000
is_a: core field
slot_uri: MIXS:0000173
multivalued: false
alias: bacteria_carb_prod
domain_of:
- Biosample
range: QuantityValue

```
</details>