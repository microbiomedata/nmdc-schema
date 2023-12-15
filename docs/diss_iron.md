# Slot: dissolved iron (diss_iron)


_Concentration of dissolved iron in the sample_



URI: [MIXS:0000139](https://w3id.org/mixs/0000139)




## Inheritance

* [core_field](core_field.md)
    * **diss_iron**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Biosample](Biosample.md) | Biological source material which can be characterized by an experiment |  no  |







## Properties

* Range: [QuantityValue](QuantityValue.md)



## Aliases


* dissolved iron




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
name: diss_iron
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
description: Concentration of dissolved iron in the sample
title: dissolved iron
examples:
- value: ''
from_schema: https://w3id.org/nmdc/nmdc
aliases:
- dissolved iron
rank: 1000
is_a: core field
slot_uri: MIXS:0000139
multivalued: false
alias: diss_iron
domain_of:
- Biosample
range: QuantityValue

```
</details>