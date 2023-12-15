# Slot: aminopeptidase activity (aminopept_act)


_Measurement of aminopeptidase activity_



URI: [MIXS:0000172](https://w3id.org/mixs/0000172)




## Inheritance

* [core_field](core_field.md)
    * **aminopept_act**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* aminopeptidase activity




## Examples

| Value |
| --- |
| 0.269 mole per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | mole per liter per hour || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: aminopept_act
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: mole per liter per hour
  occurrence:
    tag: occurrence
    value: '1'
description: Measurement of aminopeptidase activity
title: aminopeptidase activity
examples:
- value: 0.269 mole per liter per hour
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- aminopeptidase activity
rank: 1000
is_a: core field
slot_uri: MIXS:0000172
multivalued: false
alias: aminopept_act
domain_of:
- Biosample
range: QuantityValue

```
</details>