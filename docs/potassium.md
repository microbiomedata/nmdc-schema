# Slot: potassium (potassium)


_Concentration of potassium in the sample_



URI: [MIXS:0000430](https://w3id.org/mixs/0000430)




## Inheritance

* [core_field](core_field.md)
    * **potassium**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* potassium




## Examples

| Value |
| --- |
| 463 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| expected_value | measurement value || preferred_unit | milligram per liter, parts per million || occurrence | 1 |



### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: potassium
annotations:
  expected_value:
    tag: expected_value
    value: measurement value
  preferred_unit:
    tag: preferred_unit
    value: milligram per liter, parts per million
  occurrence:
    tag: occurrence
    value: '1'
description: Concentration of potassium in the sample
title: potassium
examples:
- value: 463 milligram per liter
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- potassium
rank: 1000
is_a: core field
slot_uri: MIXS:0000430
multivalued: false
alias: potassium
domain_of:
- Biosample
range: QuantityValue

```
</details>