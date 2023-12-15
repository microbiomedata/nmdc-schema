# Slot: exposed ductwork (exp_duct)


_The amount of exposed ductwork in the room_



URI: [MIXS:0000144](https://w3id.org/mixs/0000144)




## Inheritance

* [core_field](core_field.md)
    * **exp_duct**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* exposed ductwork




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | square meter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: exp_duct
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: square meter
  occurrence:
    tag: occurrence
    value: '1'
description: The amount of exposed ductwork in the room
title: exposed ductwork
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- exposed ductwork
rank: 1000
is_a: core field
slot_uri: MIXS:0000144
multivalued: false
alias: exp_duct
domain_of:
- Biosample
range: QuantityValue

```
</details>