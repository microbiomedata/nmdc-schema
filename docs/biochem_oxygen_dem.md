# Slot: biochemical oxygen demand (biochem_oxygen_dem)


_Amount of dissolved oxygen needed by aerobic biological organisms in a body of water to break down organic material present in a given water sample at certain temperature over a specific time period_



URI: [MIXS:0000653](https://w3id.org/mixs/0000653)




## Inheritance

* [core_field](core_field.md)
    * **biochem_oxygen_dem**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* biochemical oxygen demand




## Examples

| Value |
| --- |
|  |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: biochem_oxygen_dem
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter
  occurrence:
    tag: occurrence
    value: '1'
description: Amount of dissolved oxygen needed by aerobic biological organisms in
  a body of water to break down organic material present in a given water sample at
  certain temperature over a specific time period
title: biochemical oxygen demand
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- biochemical oxygen demand
rank: 1000
is_a: core field
slot_uri: MIXS:0000653
multivalued: false
alias: biochem_oxygen_dem
domain_of:
- Biosample
range: QuantityValue

```
</details>