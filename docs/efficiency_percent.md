# Slot: efficiency percent (efficiency_percent)


_Percentage of volatile solids removed from the anaerobic digestor_



URI: [MIXS:0000657](https://w3id.org/mixs/0000657)




## Inheritance

* [core_field](core_field.md)
    * **efficiency_percent**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* efficiency percent




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | micromole per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: efficiency_percent
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: micromole per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Percentage of volatile solids removed from the anaerobic digestor
title: efficiency percent
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- efficiency percent
rank: 1000
is_a: core field
slot_uri: MIXS:0000657
multivalued: false
alias: efficiency_percent
domain_of:
- Biosample
range: QuantityValue

```
</details>