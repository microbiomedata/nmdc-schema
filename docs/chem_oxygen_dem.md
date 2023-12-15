# Slot: chemical oxygen demand (chem_oxygen_dem)


_A measure of the capacity of water to consume oxygen during the decomposition of organic matter and the oxidation of inorganic chemicals such as ammonia and nitrite_



URI: [MIXS:0000656](https://w3id.org/mixs/0000656)




## Inheritance

* [core_field](core_field.md)
    * **chem_oxygen_dem**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* chemical oxygen demand




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
name: chem_oxygen_dem
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
description: A measure of the capacity of water to consume oxygen during the decomposition
  of organic matter and the oxidation of inorganic chemicals such as ammonia and nitrite
title: chemical oxygen demand
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- chemical oxygen demand
rank: 1000
is_a: core field
slot_uri: MIXS:0000656
multivalued: false
alias: chem_oxygen_dem
domain_of:
- Biosample
range: QuantityValue

```
</details>